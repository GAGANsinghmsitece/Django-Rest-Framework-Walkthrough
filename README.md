# Django Rest Framework Walkthrough
This repository is a good place for learning Django Rest Framework. It introduces you to the fundamental concepts of rest framework and its examples.
## How to run this project?
Since it's a django project. Download this project and in the project folder, run database migrations using

    python manage.py makemigrations
    python manage.py migrate

Now run the server using

    python manage.py runserver

## How to run this project with different url patterns?
This project provides three urls which are in `urls.py`(generics with urlpatterns),`viewset_urls.py`(viewsets with urlpatterns) and `Rest_Router.py`(viewsets with DRF Router).
1) If you wish to run project with `urls.py`, open`tutorial/urls.py` and edit:-


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('snippets.urls')),
    ] 

2) If you wish to run project with `viewset_urls.py`, open`tutorial/urls.py` and edit:-

    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('snippets.viewset_urls')),
    ]

3) If you wish to run project with `Rest_Router.py`, open`tutorial/urls.py` and edit:-

    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('snippets.Rest_Router')),
    ]
## How to read this project?
You should start reading the files in this order:-
1)  `models.py`
2)  `simpleserializer.py`
3)  `modelserializer.py`
4)  `serializers.py`
5)  `views.py`
6)  `urls.py`
7)  `viewset.py`
8)  `viewset_urls.py`
9)  `Rest_Router.py`
10) `tutorial/urls.py`

## Topic-Wise Specific Reference
If you're looking for some quick reference you can follow this guide in following order:-
### Serializers:-
1) `Simpleserializer.py`(topic:- `serializer`)
2) `modelserializer.py`(topic:- `ModelSerializer`)
3) `serializers.py`:-(topic:- `HyperlinkedModelSerializer`)
### Generics:-
1) `Generics.py`(topic:- `generics`)
2) `urls.py`(topic:- url with generics)
### Viewsets:-
1) `viewset.py`(topic:-`ViewSets`)
2) `viewset_url.py`(topic:- Viewsets with django urlpatterns)
3) `Rest_Router.py`(topic:- Viewsets with DRF Router)