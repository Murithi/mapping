from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('county/', views.county_datasets, name='county'),
    path('headquarter/', views.headquarter_datasets, name='headquarter'),
    path('regionaloffice/', views.regionaloffice_datasets, name='regionaloffice'),
    path('fieldoffice/', views.fieldoffice_datasets, name='fieldoffice'),
    

    

]