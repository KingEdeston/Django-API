from django.urls import path
from . import views
from .views import *


urlpatterns = [
path("", views.index, name="index"),
#path("home/", views.index0, name="index0"),
path("<int:id>", views.index2, name="index2"),
path("<str:name>", views.index3, name="index3"),

path("api/", views.apiOverview, name="api-overview"),

path("item-list/", views.itemList, name="item-list"),
path("item-detail/<str:pk>/", views.itemDetail, name="item-detail"),
path("item-create/", views.itemCreate, name="item-create"),
path("item-update/<str:pk>/", views.itemUpdate, name="item-update"),
path("item-delete/<str:pk>/", views.itemDelete, name="item-delete"),

path('certification/', CertFormView.as_view(), name = 'certification'),
path("cert-list/", views.certList, name="cert-list"),
path("cert-create/", views.certCreate, name="cert-create"),
path("cert-update/<str:pk>/", views.certUpdate, name="cert-update"),

#path("info-create/", views.infoCreate, name="info-create"),

path("data-create/", views.dataCreate, name="data-create"),
path("data-list/", views.dataList, name="data-list"),
path("data-delete/<str:pk>/", views.dataDelete, name="data-delete"),
path("data-delete/", views.dataDelete, name="data-delete"),
path("data-search/", views.dataSearch, name="data-search"),
]
