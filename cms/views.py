from django.shortcuts import render
from django.http import HttpResponse
from cms.models import List


def list_list(request):
    """そろえの一覧"""
    lists = List.objects.all().order_by('id')
    return render(request,
                  'cms/list_list.html',
                  {'list': lists})

def list_edit(request, list_id=None):
    """そろえの編集"""
    return HttpResponse('[そろえ]の編集')

def list_del(request, list_id):
    """そろえの削除"""
    return HttpResponse('[そろえ]の削除')
