from django.urls import path
from main.views import index, account_search, friends
app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('search/', account_search, name="account_search"),
    path('friends/', friends, name="friends"),
]
