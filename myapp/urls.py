# myapp/urls.py
from django.urls import path
from .views import make_payment, payment_list, user_profile_list

urlpatterns = [
    path('user-profile-list/', user_profile_list, name='user_profile_list'),
    path('make-payment/', make_payment, name='make_payment'),
    path('payment-list/', payment_list, name='payment_list'),
]
