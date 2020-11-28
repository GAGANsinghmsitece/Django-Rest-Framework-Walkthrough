from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import viewset

router=DefaultRouter()
router.register(r'snippets', viewset.SnippetViewSet)
router.register(r'users', viewset.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]