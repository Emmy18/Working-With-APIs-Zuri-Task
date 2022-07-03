from django.urls import path, include
from . import views

app_name = "links"

urlpatterns = [
    path("", views.LinkListApi.as_view(), name="api_list"),
    path("create/", views.LinkCreateApi.as_view(), name="api_create"),
    path("delete/<slug:slug>", views.LinkDeleteApi.as_view(), name="api_delete"),
    path("update/<slug:slug>", views.LinkUpdateApi.as_view(), name="api_update"),
    path("read/<slug:slug>", views.LinkDetailApi.as_view(), name="api_detail"),
    path("links/", include("links.urls", namespace="links"))

]