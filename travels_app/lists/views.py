from .models import Lists, Items
from .forms import ManageItems, ManageLists
from my_travels.models import Places
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

@login_required
def add_list(request, **kwargs):
    if request.method == "POST":
        form = ManageLists(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            if 'place_id' in kwargs:
                new_list.place_id = get_object_or_404(Places, pk=kwargs['place_id'])
            new_list.save()
            return redirect("list_edit", pk=new_list.pk)
    else:
        form = ManageLists()
    return render(request, 'lists/list_new.html', {'form': form})

@login_required
def add_items(request, pk, **kwargs):
    list_to_edit = get_object_or_404(Lists, pk=pk)
    list_items = Items.objects.filter(list_id=list_to_edit)
    if 'item_to_edit' in kwargs:
        item_to_edit = get_object_or_404(Items, pk=kwargs['item_to_edit'])
        if request.method == "POST": 
            form_edit = ManageItems(request.POST, instance=item_to_edit)
            if form_edit.is_valid():
                item_to_edit = form_edit.save(commit=False)
                item_to_edit.save()
                return redirect("list_edit", pk=pk)

            form = ManageItems(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.list_id = list_to_edit
                item.save()
                return redirect("list_edit", pk=pk)
        else:
            form_edit = ManageItems(instance=item_to_edit)
            form = ManageItems()
        return render(request, 'lists/list_edit.html', {'list': list_to_edit, 'form': form, 'items': list_items, 'form_edit': form_edit, 'edit_item': item_to_edit})

    if request.method == "POST":
        form = ManageItems(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.list_id = list_to_edit
            item.save()
            return redirect("list_edit", pk=pk)
    else:
        form = ManageItems()
    return render(request, 'lists/list_edit.html', {'list': list_to_edit, 'form': form, 'items': list_items})

@login_required
def lists_all(request):
    lists_all = Lists.objects.filter(user=request.user)
    if len(lists_all) == 0:
        lists_all = False
    return render(request, 'lists/lists_all.html', {'lists': lists_all})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    list_pk = item.list_id.pk
    if request.method == 'GET':
        return render(request, 'lists/confirm_delete.html', {'elem_to_delete': item, 'pk': list_pk})
    elif request.method == "POST": 
        item.delete()
        return redirect("list_edit", pk=list_pk)

@login_required
def delete_list(request, pk):
    list_to_edit = get_object_or_404(Lists, pk=pk)
    if request.method == 'GET':
        return render(request, 'lists/confirm_delete.html', {'elem_to_delete': list_to_edit, 'pk': pk})
    elif request.method == "POST": 
        list_to_edit.delete()
        return redirect("lists_all")

def edit_list_name(request, pk):
    list_to_edit = get_object_or_404(Lists, pk=pk)
    if request.method == "POST":
        form = ManageLists(request.POST, instance=list_to_edit)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect("list_edit", pk=pk)
    else:
        form = ManageLists(instance=list_to_edit)
    return render(request, 'lists/list_new.html', {'form': form})