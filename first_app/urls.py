from django.urls import path
from .views import signup, home, signin, profile, signout, changePass, setPass

urlpatterns = [
    path('', home),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', signout, name='logout'),
    path('changePass/', changePass, name='changePass'),
    path('setPass/', setPass, name='setPass'),
]
