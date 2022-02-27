from django.urls import path

from .views import index, auth, callback

urlpatterns = [
    path("main", index),
    path("auth", auth),
    path("callback", callback),
]
