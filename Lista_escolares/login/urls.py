from django.urls import path
from .views import (logeo,Crear_user,logout_view,paginainicio)
from django.contrib.auth import views as auth_views
#para definr las rutas que van a comportarse en esta aplicacion usamos la variable urlpatterns
urlpatterns = [
    path('',logeo,name=''),
    path('crear-user',Crear_user,name='crear_user'),
    path('logout_view',logout_view,name='logout-view'),
    path('index',paginainicio,name='index'),
    path('reset_password', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_send', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>[0-9A-Za-z]/<token>', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    

]