from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import mixins
from .models import Book, Comment, Category
from .serializers import BookSerializer, CommentSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'], url_path='favorite', permission_classes=[permissions.IsAuthenticated])
    def favorite(self, request, pk=None):
        book = self.get_object()
        user = request.user
        if book in user.favorites.all():
            user.favorites.remove(book)
            return Response({'status': 'removed from favorites'})
        else:
            user.favorites.add(book)
            return Response({'status': 'added to favorites'})

    @action(detail=False, methods=['get'], url_path='favorites', permission_classes=[permissions.IsAuthenticated])
    def favorites(self, request):
        user = request.user
        books = user.favorites.all()
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
