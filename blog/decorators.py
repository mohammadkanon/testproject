import logging
import time
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden

from blog.models import Entry

def user_is_entry_author(function):
	def wrap(request, *args, **kwargs):
		entry = Entry.objects.get(pk=kwargs['entry_id'])
		if entry.author == request.user:
			return function(request, *args, **kwargs)
		else:
			return PermissionDenied

	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__

	return wrap


def group_required(*group_names):
	""" Requires user memdership in at least one of the groups passed in."""

	def in_groups(u):
		if u.is_authenticated():
			if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
				return True

		return False

	return user_passes_test(in_groups)


def anonymous_required(function=None, redirect_url=None):

	if not redirect_url:
		redirect_url = settings.LOGIN_REDIRECT_URL

	actual_decorator = user_passes_test(
		lambda u: u.is_anonymous(),
		login_url=redirect_url
	)

	if function:
		return actual_decorator(function)

	return actual_decorator



def superuser_only(function):
	"""Limit view to superusers only """

	def _inner(request, *args, **kwargs):
		if not request.user.is_superuser:
			raise PermissionDenied

		return function(request, *args, **kwargs)

	return _inner


def ajex_required(f):
	"""AJAX request required decorator use it in views """
	def wrap(request, *args, **kwargs):
		if not request.is_ajax():
			return HttpResponseBadRequest()

		return f(request, *args, **kwargs)

	wrap.__doc__ = f.__doc__
	wrap.__name__ = f.__name__

	return wrap


def timeit(method):
	"""Use to measure the time to procces the function """

	def timed(*args, **kwargs):
		ts = time.time()
		result = method(*args, **kwargs)
		te = time.time()
		print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kwargs, te - ts))

		return result

	return timed


logger = logging.getLogger(__name__)

def user_can_write_a_review(func):
	"""View decorator that checks a user is allowed to write a review, in negative case the decorator return Forbidden"""
	
	@functools.wrap(func)
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.points < 10:
			logger.warning('The {} user has tried to write a review, but does not have enough points to do so'.format(request.user.pk))
			return HttpResponseForbidden()

		return func(request, *args, **kwargs)

	return wrapper	



user_login_required = user_passes_test(lambda user: user.is_active, login_url='/')

def active_user_required(view_func):
	decorated_view_func = login_required(user_login_required(view_func))

	return decorated_view_func


def is_recruiter(self):
	if str(self.user_type) == 'Recruiter':
		return True

	else:
		return False

rec_login_required = user_passes_test(lambda u: True if u.is_recruiter else False, login_url='/')

def recruiter_login_required(view_func):
	decorated_view_func = login_require(rec_login_required(view_func), login_url='/')

	return decorated_view_func



class Meta:
	permissions = (
		('blog_view', 'can view blog posts and categories'),
		('blog_edit', 'can edit blog category and post'),
		('support_view', 'can view tickets'),
		('support_edit', 'can edit tickets'),
		('activity_view', 'can view recruiters, applicants, data, posts'),
		('activity_edit', 'can edit data'),
	)

def has_perm(self, perm, obj=None):
	try:
		user_perm = self.user_permissions.get(codename=perm)

	except ObjectDoesNotExist:
		user_perm = False

	if user_perm:
		return True

	else:
		return False

def permission_required(*perms):
	return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/')