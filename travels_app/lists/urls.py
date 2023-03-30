from django.urls import path

from . import views

urlpatterns = [
    path('lists', views.lists_all, name='lists_all'),
    path('list/new', views.add_list, name='list_new'),
    path('list/<int:pk>', views.add_items, name='list_edit'),
]