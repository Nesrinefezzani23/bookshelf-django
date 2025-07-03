from rest_framework import serializers
from .models import Book, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Comment
        fields = ['id', 'book', 'user', 'content', 'rating', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True, required=False
    )
    is_favorite = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {'comments': {'read_only': True}, 'average_rating': {'read_only': True}, 'is_favorite': {'read_only': True}}

    def get_average_rating(self, obj):
        comments = obj.comments.all()
        if comments:
            return round(sum([c.rating for c in comments]) / len(comments), 2)
        return None

    def get_is_favorite(self, obj):
        user = self.context.get('request').user
        if user and user.is_authenticated:
            return obj in user.favorites.all()
        return False

    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        book = Book.objects.create(**validated_data)
        book.categories.set(category_ids)
        return book

    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if category_ids is not None:
            instance.categories.set(category_ids)
        return instance 