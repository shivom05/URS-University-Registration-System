from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns= [
     path('',views.loginuser,name="login"),
     path('registermain',views.registermain,name="registermain"),
     path('login',views.loginuser,name="login"),
     path('front/login',views.loginuser,name="login"),
     path('front/logout',views.logout,name="logout"),
     path('logout',views.logout,name="logout"),
     path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
     path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]