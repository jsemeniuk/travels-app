from django.contrib.auth.models import User
import datetime
from my_travels.models import PlacesVisited

def add_new_user(login, password):
    user = User.objects.create_user(username=login,
                                    password=password)
    return user

def add_new_place(user):
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
    first_place.user = user
    first_place.save()