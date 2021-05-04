from django.urls import path
from . import views
from .views import render_pdf_view
from django.conf.urls import url

urlpatterns= [path('',views.index,name="index"),
             path('front/index',views.index,name="index"),
             path('register',views.registeruser,name="register"),
             path('check',views.check,name="check"),
             path('front/front/index',views.index,name="index"),
             path('register',views.registeruser,name="register") ,
             path('payment',views.paymentuser,name="payment"),
             path('student',views.studentUser,name="student"),
             path('index',views.index,name="index"),
             path('pdf/',render_pdf_view,name="pdf_view"),
]

  
