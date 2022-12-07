from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>', views.product_detail_view, name='product_detail'),
]
