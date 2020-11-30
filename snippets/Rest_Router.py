from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import viewset
"""
When using DRF router, we will create a router using DefaultRouter and then we can register our 
viewset with it.
After registering our viewsets with router we can include urls of router with urlpatterns.
"""
router=DefaultRouter()
router.register(r'snippets', viewset.SnippetViewSet)
router.register(r'users', viewset.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]