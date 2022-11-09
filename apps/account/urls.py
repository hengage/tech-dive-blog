from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:slug>/', SignupView.as_view(), name='signup')
    path('<slug:slug>/', views.UpdateUserView.as_view(), name='update_user')
]