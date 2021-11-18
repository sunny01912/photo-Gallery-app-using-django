from django.urls import path
from django.utils.regex_helper import normalize
from photos import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewphoto,name='photo'),
    path('add/',views.addphoto,name='add'),
    path('login/',views.customLoginView.as_view(),name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',LogoutView.as_view(next_page='/login/'),name='logout'),
    path('delete/<int:pk>',views.delphoto,name='delete'),


]
