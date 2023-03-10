from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostLV.as_view(), name="list"),

    path("<slug:slug>/", views.PostDV.as_view(), name="detail"),
]