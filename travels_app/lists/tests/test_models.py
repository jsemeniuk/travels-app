from django.test import TestCase
from django.contrib.auth.models import User

from lists.models import Lists, Items
from my_travels.models import Places

class ListsModelsTest(TestCase):

    def test_adding_list_for_place(self):
        user = User.objects.create_user(username='MysteryPlaces',
                                        password='MysteryPlaces123')
        new_place = Places()
        new_place.name = 'Loch Ness'
        new_place.location = 'POINT(-4.48 57.27)'
        new_place.visit_date = '1933-04-14'
        new_place.user = user
        new_place.save()

        new_list = Lists()
        new_list.name = 'To-Do in Loch Ness'
        new_list.user =  user
        new_list.place_id = new_place
        new_list.save()

        saved_lists = Lists.objects.all()
        self.assertEqual(len(saved_lists), 1)

        saved_list = saved_lists[0]
        
        self.assertEqual(saved_list.name, 'To-Do in Loch Ness')
        self.assertEqual(saved_list.place_id, new_place)


    def test_adding_item_to_list(self):
        user = User.objects.create_user(username='MysteryPlaces',
                                        password='MysteryPlaces123')

        new_list = Lists()
        new_list.name = 'To-Do in Loch Ness'
        new_list.user =  user
        new_list.save()

        first_item = Items()
        first_item.name = 'Find monster!'
        first_item.list_id = new_list
        first_item.save()

        saved_items = Items.objects.all()
        self.assertEqual(len(saved_items), 1)

        saved_item = saved_items[0]
        
        self.assertEqual(saved_item.name, 'Find monster!')
        self.assertEqual(saved_item.list_id, new_list)
