
from django.urls import path
from checkout.views import CreateCartItemView, CartItemView, CheckoutView, OrderListView, OrderDetailView

app_name = 'checkout'

urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', CreateCartItemView.as_view(), name='create_cartitem'),
    path('carrinho/', CartItemView.as_view(), name='cart_item'),
    path('finallizar/', CheckoutView.as_view(), name='checkout'),
    path('meus-pedidos/', OrderListView.as_view(), name='order_list'),
    path('meus-pedidos/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]