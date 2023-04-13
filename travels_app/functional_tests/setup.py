from django.contrib.auth.models import User
from datetime import datetime
from my_travels.models import Places
from lists.models import Lists, Items

def add_new_user():
    login = f'New User {datetime.today()}'
    password = 'P455w0rd'
    user = User.objects.create_user(username=login,
                                    password=password)
    return login, password, user

def delete_user(user):
    user.delete()

def add_new_place(user):
    new_place = Places()
    new_place.name = 'Test Place'
    new_place.location = 'POINT(17.00 51.00)'
    new_place.visit_date = '2023-01-01'
    new_place.description = 'Test description'
    new_place.user = user
    new_place.save()
    return new_place.pk

def add_new_list(user, list_name):
    new_list = Lists()
    new_list.name = list_name
    new_list.user =  user
    new_list.save()
    return new_list

def add_item_to_list(new_list, item_name):
    new_item = Items()
    new_item.name = item_name
    new_item.list_id = new_list
    new_item.save()