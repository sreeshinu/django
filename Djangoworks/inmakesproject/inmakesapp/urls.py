from  .import views
from django.urls import path

urlpatterns = [

    path('',views.contact,name='contact'),
    path('add/',views.addition,name='addition'),
    path('res/',views.result,name='result')
]