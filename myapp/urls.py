from django.urls import path
from .views import register, user_login, user_logout, home, about, user , thankyou

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('user/', user, name ='user'),
    path('thankyou/', thankyou, name="thankyou"), 
    #path('form/',form, name ='form')
] 

