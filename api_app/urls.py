from django.urls import path
from rest_framework.authtoken import views as auth_view 
from . import views

urlpatterns = [
    path('category/',views.CategoryEndpoint.as_view(),name='category'),
    path('products/',views.ProductEndpoint.as_view(), name='products'),
    path('category/<int:pk>/', views.SingleCategoryEndPoint.as_view(), name="category-up"),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name="category-del"),
    path('products/<int:pk>/', views.SingleProductEndPoint.as_view(), name='products-up'),
    path('products/<int:pk>/delete/', views.ProductDeleteEndpoint.as_view(), name='products-del'),
    path('update/category/<int:pk>/', views.UpdateCategoryEndpoint.as_view(),  name='update-category'),
    path('update/product/<int:pk>/', views.UpdateProductEndpoint.as_view(), name='update-product'),
    path('users/', views.UserResgisterEndpoint.as_view(), name='user-create'),
    path('login/', auth_view.ObtainAuthToken.as_view(), name='login'),
    path('product-list/', views.ProductListEndPoint.as_view(), name='product_id'),
]
