from django import template
from django.template.defaultfilters import stringfilter

from ..models import TestModel

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
	return value.replace(arg, '')

@stringfilter
def lower(value):
	return value.lower()

@register.filter
def number(value, type_of):

	if not type(value) == int:
		try:
			value = int(value)
		except:
			raise ValueError('Value should be interger or should able to converted into interger')

	if value > 90:
		return "90+"
	elif value < 1:
		if type_of == 'str':
			return "zero"
		else:
			return "0"
		return value

	else:
		return value
	return value

# @register.filter
# def user(number):
# 	if number == str(number):
# 		return "zero"
# 	else:
# 		return "0"
# 	return number




# @register.simple_tag
# def any_function():
# 	return TestModel.objects.count()


# @register.inclusion_tag('path_to_your_html_file.html')
# def any_function():
#   variable = YourModel.objects.order_by('-publish')[:5]
#   return {'variable': variable}

# @register.assignment_tag
# def any_function(count=5):
# 	return *some database query*


# custom template tag banaben
# 	1. jeta student ar number dekhabe
# 	2. jodi number 99 ar besi hoy tahole 99+ retunr korbe
	

# 99|dfdl

# 	1. argument niben oi arg ar user bole dibe 'zero' dekhab na na 0 dekhabe. ( 1 ar niche hole)

# 	99|aita:"numb"