import imp
from django.db import router
from rest_framework.routers import DefaultRouter
from .views import BookItemViewset, BookViewset

router = DefaultRouter()
router.register('books', BookViewset)
router.register('rack', BookItemViewset)

urlpatterns =router.urls

