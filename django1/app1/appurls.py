from django.urls import path
from .import views
urlpatterns = [
    path('',views.home),
    path('sqfct',views.sqfct),
    path('facts',views.listfactorials),
    path('perm',views.permutations)
]