from django.urls import path
from .views import ProductListView, CategotyListView
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', CategotyListView.as_view(), name='category'),
    path('produtos/<slug:slug>/', views.product, name='product'),
]