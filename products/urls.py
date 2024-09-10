from django.urls import path, include
from . import views
from django.urls import path

app_name="products"
urlpatterns = [
    path('', views.ProductListView.as_view(), name="products"),
    path('<int:productId>/', views.ProductListView.as_view(), name="products"),
    ]