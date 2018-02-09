from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    # そろえ
    path('list/', views.list_list, name='list_list'),   # 一覧
    path('list/add/', views.list_edit, name='list_add'),    #登録
    path('list/mod/<int:list_id>/', views.list_edit, name='list_mod'),  #修正
    path('list/del/<int:list_id>/', views.list_del, name='list_del'),   #削除
]
