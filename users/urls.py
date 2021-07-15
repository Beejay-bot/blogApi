from django.urls import path
from .views import BlackListTokenView, CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlackListTokenView.as_view(), name="blacklist")
]
