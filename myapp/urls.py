from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.list_location, name="list_location"),
    path("form-client/", views.form_client, name="client-create"),
    path("form-immobile/", views.form_immobile, name="immobile-create"),
]
