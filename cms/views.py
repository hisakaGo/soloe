from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import List
from cms.forms import ListForm


def list_list(request):
    """そろえの一覧"""
    lists = List.objects.all().order_by('id')
    return render(request,
                  'cms/list_list.html',
                  {'lists': lists})

def list_edit(request, list_id=None):
    """そろえの編集"""
    if list_id:
        list = get_object_or_404(List, pk=list_id)
    else:
        list = List()

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
            return redirect('cms:list_list')
    else:
        form = ListForm(instance=list)
    
    return render(request, 'cms/list_edit.html', dict(form=form, list_id=list_id))

def list_del(request, list_id):
    """そろえの削除"""
    list = get_object_or_404(List, pk=list_id)
    list.delete()
    return redirect('cms:list_list')
