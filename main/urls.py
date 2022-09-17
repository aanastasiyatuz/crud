from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import categories_list, create_category, delete_category, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('api/v1/category/list/', categories_list),
    path('api/v1/category/create/', create_category),
    path('api/v1/category/delete/<int:id>/', delete_category),
    path('api/v1/', include(router.urls)),
]
