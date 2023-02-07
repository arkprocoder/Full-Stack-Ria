from django.urls import path
from riaapp import views

urlpatterns = [
   path('',views.index,name="index"),
   path('signin',views.handleSignin,name="handleSignin"), 
   path('login',views.handleLogin,name="handleLogin"), 
   path('logout',views.handleLogout,name="handleLogout"), 
   path('enroll',views.enroll,name="enroll"),
   path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
   path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
   path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]
