from django.test import TestCase
from django.contrib.auth.models import User
import datetime


from my_travels.models import PlacesVisited

class PlacesModelsTest(TestCase):

    def test_adding_places_for_one_user(self):
        user = User.objects.create_user(username='MysteryPlaces',
                                              password='MysteryPlaces123')
        first_place = PlacesVisited()
        first_place.name = 'Trójkąt Bermudzki'
        first_place.location = 'POINT(-71.05 27.051)'
        first_place.visit_date = '1978-11-03'
        first_place.description = '''Według Lawrence’a Davida Kuschego, pracownika biblioteki Uniwersytetu Stanowego Arizony[1], który szczegółowo zbadał źródła, ojcem pojęcia Trójkąt Bermudzki jest Vincent Gaddis, który użył go w artykule The deadly Bermuda Triangle w czasopiśmie „Argosy” w 1964 roku.
        W 1965 roku Gaddis opublikował książkę Invisible horizons, w której zajął się tą legendą. Po nim wielu innych autorów próbowało uzyskać sławę zajmując się tym tematem.
        W zależności od autora, wielkość Trójkąta Bermudzkiego jest różna. Niektórzy rozszerzają ją aż do wybrzeży Irlandii. Zazwyczaj jednak mowa jest o trójkącie między Miami, Puerto Rico i Bermudami, który to teren jest bardzo często uczęszczany przez statki i samoloty.
        Legenda narodziła się wraz z historią zniknięcia eskadry pięciu amerykańskich samolotów torpedowo-bombowych Grumman TBF Avenger 5 grudnia 1945 u wybrzeży Florydy (słynny lot 19). Opisane to zostało w magazynie „American Legion” przez Allena Eckerta w artykule Tajemnica zaginionego patrolu. Eckert nigdy nie potrafił podać źródeł swojego twierdzenia.
        Lawrence David Kusche i Jules Metz dogłębnie zbadali tę historię, analizując 500 stron oficjalnego raportu. Stwierdzają w nim, że był to tragiczny wypadek, jeden z najtragiczniejszych wypadków lotnictwa wojskowego w czasach pokoju, ale spowodowany przyczynami naturalnymi.
        W 1492 roku Krzysztof Kolumb, według swojej relacji, zaobserwował w okolicach Trójkąta „dziwne, tańczące na horyzoncie światła”, oraz nietypowe odczyty kompasu'''
        first_place.photo = ''
        first_place.user = user
        first_place.save()

        second_place = PlacesVisited()
        second_place.name = 'Potwór z Loch Ness'
        second_place.location = 'POINT(-4.48 57.27)'
        second_place.visit_date = '1933-04-14'
        second_place.description = '''Oto w piątek zeszłego tygodnia mieszkający w pobliżu Inverness znany biznesmen jechał wraz z żoną północnym brzegiem jeziora. 
        W pewnej chwili oboje w osłupieniu skonstatowali, że coś przerażającego wyrzuca w górę wodę […] Stworzenie baraszkowało całą minutę. 
        Kształtem przypominało nieco wieloryba. Wzburzona woda pieniła się i przelewała jak we wrzącym kotle […]. 
        Patrzący odnieśli wrażenie, że uczestniczą w niesamowitym wydarzeniu, i uświadomili sobie, że nie był to zwykły mieszkaniec głębiny'''
        second_place.photo = ''
        second_place.user = user
        second_place.save()

        saved_places = PlacesVisited.objects.all()
        self.assertEqual(len(saved_places), 2)

        first_saved_item = saved_places[0]
        self.assertEqual(first_saved_item.name, 'Trójkąt Bermudzki')
        
        second_saved_item = saved_places[1]
        self.assertEqual(second_saved_item.name, 'Potwór z Loch Ness')

    def test_adding_places_for_different_users(self):
        first_user = User.objects.create_user(username='Vincent Gaddis',
                                              password='InvisibleHorizons1965')
        first_place = PlacesVisited()
        first_place.name = 'Trójkąt Bermudzki'
        first_place.location = 'POINT(-71.05 27.051)'
        first_place.visit_date = '1978-11-03'
        first_place.description = '''Według Lawrence’a Davida Kuschego, pracownika biblioteki Uniwersytetu Stanowego Arizony, który szczegółowo zbadał źródła, ojcem pojęcia Trójkąt Bermudzki jest Vincent Gaddis, który użył go w artykule The deadly Bermuda Triangle w czasopiśmie „Argosy” w 1964 roku.
        W 1965 roku Gaddis opublikował książkę Invisible horizons, w której zajął się tą legendą. Po nim wielu innych autorów próbowało uzyskać sławę zajmując się tym tematem.
        W zależności od autora, wielkość Trójkąta Bermudzkiego jest różna. Niektórzy rozszerzają ją aż do wybrzeży Irlandii. Zazwyczaj jednak mowa jest o trójkącie między Miami, Puerto Rico i Bermudami, który to teren jest bardzo często uczęszczany przez statki i samoloty.
        Legenda narodziła się wraz z historią zniknięcia eskadry pięciu amerykańskich samolotów torpedowo-bombowych Grumman TBF Avenger 5 grudnia 1945 u wybrzeży Florydy (słynny lot 19). Opisane to zostało w magazynie „American Legion” przez Allena Eckerta w artykule Tajemnica zaginionego patrolu. Eckert nigdy nie potrafił podać źródeł swojego twierdzenia.
        Lawrence David Kusche i Jules Metz dogłębnie zbadali tę historię, analizując 500 stron oficjalnego raportu. Stwierdzają w nim, że był to tragiczny wypadek, jeden z najtragiczniejszych wypadków lotnictwa wojskowego w czasach pokoju, ale spowodowany przyczynami naturalnymi.
        W 1492 roku Krzysztof Kolumb, według swojej relacji, zaobserwował w okolicach Trójkąta „dziwne, tańczące na horyzoncie światła”, oraz nietypowe odczyty kompasu'''
        first_place.photo = ''
        first_place.user = first_user
        first_place.save()
        
        second_user = User.objects.create_user(username='Robert Wilsona',
                                              password='ZdjęciaChirurga1934')
        second_place = PlacesVisited()
        second_place.name = 'Potwór z Loch Ness'
        second_place.location = 'POINT(-4.48 57.27)'
        second_place.visit_date = '1934-04-01'
        second_place.description = '''W kwietniu 1934 powstała słynna fotografia płk. Roberta Wilsona, lekarza pracującego w Londynie. 
        Zyskała ona szybko przydomek „zdjęcia chirurga”, ze względu na profesję autora, jak i to, że było to pierwsze do tej pory tak ostre i doświetlone zdjęcie potwora, 
        przedstawiające rzekomo szyję zwierzęcia podobnego do plezjozaura, wystającą z wody. 
        Wilson wracał z urlopu w północnej Szkocji, gdzie fotografował pociągi. 
        Jak twierdził, znajdując się 5 km od Invermoriston, wysiadł z samochodu, gdy kręta szosa zbliżyła się na ok. 60 metrów do jeziora. 
        Wówczas to, 250 metrów od brzegu miał mu się ukazać dziwny obiekt. 
        Wilson wykonał cztery zdjęcia, z których dwa okazały się nieudane. 
        Na trzeciej fotografii widnieje obiekt przypominający długą szyję i małą główkę jakiegoś zwierzęcia. 
        Ostatnie zdjęcie przedstawia obiekt o wiele mniejszy, jakby zanurzający się. 
        Uwagę zwracał jednak fakt, że Wilson nigdy nie twierdził, że sfotografował potwora z Loch Ness, tylko „coś w wodzie”.'''
        second_place.photo = ''
        second_place.user = second_user
        second_place.save()

        third_place = PlacesVisited()
        third_place.name = 'Tu też Trójkąt Bermudzki'
        third_place.location = 'POINT(-66.01 30.82)'
        third_place.visit_date = '1978-11-03'
        third_place.user = first_user
        third_place.save()

        saved_places = PlacesVisited.objects.all()
        self.assertEqual(len(saved_places), 3)

        first_users_places = PlacesVisited.objects.filter(user=first_user)
        self.assertEqual(len(first_users_places), 2)

        first_saved_item = saved_places[0]
        self.assertEqual(first_saved_item.name, 'Trójkąt Bermudzki')
        self.assertEqual(first_saved_item.user, first_user)
        self.assertIn('Według Lawrence’a Davida Kuschego, pracownika biblioteki Uniwersytetu Stanowego Arizony', first_saved_item.description)
        self.assertEqual([first_saved_item.location[0], first_saved_item.location[1]], [-71.05, 27.051])
        self.assertEqual(first_saved_item.visit_date, datetime.date(1978, 11, 3))
        
        second_saved_item = saved_places[1]
        self.assertEqual(second_saved_item.name, 'Potwór z Loch Ness')
        self.assertEqual(second_saved_item.user, second_user)
        
        third_place = saved_places[2]
        self.assertEqual(third_place.name, 'Tu też Trójkąt Bermudzki')
        self.assertEqual(third_place.user, first_user)