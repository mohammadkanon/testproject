from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.models import Entry
from blog.forms import EntryForm
from blog.decorators import user_is_entry_author


@login_required
def index(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request, 'blog/index.html', {'entries': entries})

@login_required
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save(request.user)

            messages.success(request, 'Entry was successfully added!')
            return redirect('blog:index')

        else:
            errors = []
            for field in form:
                for error in field.errors:
                    errors.append(field.label+" "+error)

            for error in form.non_field_errors():
                errors.append(field.label+" "+error)

            print(errors)

    else:
        form = EntryForm()

    context = {
        'form': form
    }

    return render(request, 'blog/entry.html', context)


@login_required
@user_is_entry_author
def edit(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry was successfully edited!')
            return redirect('index')
    else:
        form = EntryForm(instance=entry)

    context = {
        'form': form
    }

    return render(request, 'blog/entry.html', context)


@login_required
@user_is_entry_author
def remove(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.delete()
    messages.success(request, 'Entry was successfully removed!')
    return redirect('index')

@login_required
@user_is_entry_author
def transfer(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    transfer_to = request.POST.get('transfer_to')
    new_owner = User.objects.get(pk=transfer_to)
    entry.created_by = new_owner
    entry.save()
    messages.success(request, 'Entry was successfully transferred!')
    return redirect('index')
