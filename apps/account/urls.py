from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:slug>/', SignupView.as_view(), name='signup')
    path('profile/<slug:slug>/', views.UpdateUserView.as_view(), name='update_user'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('signup/', views.CustomSIgnUpView.as_view(), name='account_signup')
]