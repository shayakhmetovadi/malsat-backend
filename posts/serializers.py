from rest_framework import serializers
from posts.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phoneNumber=validated_data['phoneNumber'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "phoneNumber", "password")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'regionName')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'categoryName')


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = ('id', 'subcategoryName', 'category')


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Item
        fields = (
        'id', 'itemName', 'itemDescription', 'itemPrice', 'images', 'category', 'subcategory', 'region', 'user', 'itemCreated', 'itemExchange',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ("id", "commentText", "user", "item", 'commentDate')


class BookmarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    class Meta:
        model = Bookmark
        fields = ("id", "user", "item")
