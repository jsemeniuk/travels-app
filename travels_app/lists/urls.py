from django.urls import path

from . import views

urlpatterns = [
    path('lists', views.lists_all, name='lists_all'),
    path('list/new', views.add_list, name='list_new'),
    path('list/<int:pk>', views.add_items, name='list_edit'),
    path('list/<int:pk>/edit', views.edit_list_name, name='edit_list_name'),
    path('list/<int:pk>/<int:item_to_edit>', views.add_items, name='list_edit_item'),
    path('<int:place_id>/list/new', views.add_list, name='list_place_new'),
    path('item/delete/<int:pk>', views.delete_item, name='delete_item'),
    path('list/delete/<int:pk>', views.delete_list, name='delete_list'),
]