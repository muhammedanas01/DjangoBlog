from django.urls import path, include
from . import views


urlpatterns = [
     path('',views.home, name='home'),
     path('ckeditor/', include('ckeditor_uploader.urls')),
     path('about/', views.about, name='about'),
     path('contact/',views.contact, name='contact'),
     path('content/<str:id>',views.content, name='content'),
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name="login"),
     path('logout/', views.logout, name='logout'),
     path('createblog/', views.createblog, name= 'createblog'),
     path('comment', views.comments, name='comment'),
     path('replies', views.replies, name='replies'),
     path('search', views.searchcontent, name='search'),
     path('submitblog', views.submitblog, name='submitblog')
    
]
