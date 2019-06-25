from django.urls import path, include
# '.' means, it's in our directory
from . import views

urlpatterns = [
    # path('') to significate it's the index of our website
    # give the road of the website
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('details/', views.news_details, name='details'),
    path('year/<int:year>', views.news_year, name='year'), # the <int:year> call the year in the views and past an int number in the URL
    path('register/', views.register, name='add'),
    path('addUser/', views.addUser, name='addUser'),
    path('modalform/', views.modalformview, name='addmodalform'),
    path('admodalform/', views.addModalForm, name='admodalform'),
    path('upload/', views.upload, name='upload'),
    path('addfile/', views.addFIle, name='addfile'),
    path('detailsdoc/', views.document_details, name ='detailsdoc')

]
