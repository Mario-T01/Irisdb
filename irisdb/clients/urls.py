from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('',views.IndexView.as_view(), name='clients-index' ),
    path('',views.home, name='clients-home'),
    #path('detail', views.DetailView.as_view(),name='detail'),

]
