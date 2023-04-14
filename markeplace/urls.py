from .middlewares.auth import auth_middleware
from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    LojaHomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    store,
    RequestRefundView,
    Signup,
    Login,
    logout,
)

app_name = 'markeplace'

urlpatterns = [
   path('lojahome', LojaHomeView.as_view(), name='lojahome'),
   path('lojaiTems', store, name='lojaiTems'),
   path('checkout/', CheckoutView.as_view(), name='checkout'),
   path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
   path('product/<slug>/', ItemDetailView.as_view(), name='product'),
   path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
   path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
   path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
   path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
   path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
   path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
   path('signup', Signup.as_view(), name='signup'),
   path('loginStore', Login.as_view(), name='loginStore'),
   path('logout', logout, name='logout'),
]
