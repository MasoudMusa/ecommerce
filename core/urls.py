from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import (ItemDetailView, OrderSummaryView, add_to_cart, index,
                    registration_view, remove_from_cart,
                    remove_single_item_from_cart)

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('accounts/register/', registration_view, name='registration'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
