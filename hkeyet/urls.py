from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CommentViewSet, CategoryViewSet, UserRegistrationView
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
] 