from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from posts import serializers
from posts.models import *
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.db.models import Prefetch, Q
from rest_framework import filters
from django.http import HttpResponse
# Create your views here.

class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(IsAdminUserOrReadOnly, self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class RegionViews(APIView):
    serializers_class = serializers.RegionSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get(self, request, format=None):
        regions = Region.objects.all()
        serializer = self.serializers_class(regions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=400)


class RegionDetailViews(APIView):
    serializers_class = serializers.RegionSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_queryset(self, pk):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return False
        return region

    def put(self, request, pk, format=None):
        region = self.get_queryset(pk)

        if not region:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(region, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        region = self.get_queryset(pk)
        if not region:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(region)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        region = self.get_queryset(pk)

        if not region:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        region.delete()
        return Response({'msg': 'NO Content'}, status=status.HTTP_204_NO_CONTENT)


class CategoryViews(APIView):
    serializers_class = serializers.CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = self.serializers_class(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=400)


class CategoryDetailViews(APIView):
    serializers_class = serializers.CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_queryset(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return False
        return category

    def put(self, request, pk, format=None):
        category = self.get_queryset(pk)

        if not category:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        category = self.get_queryset(pk)
        if not category:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(category)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        category = self.get_queryset(pk)

        if not category:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'msg': 'NO Content'}, status=status.HTTP_204_NO_CONTENT)


class SubcategoryViews(APIView):
    serializers_class = serializers.SubcategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get(self, request, format=None):
        subcategories = Subcategory.objects.all()
        serializer = self.serializers_class(subcategories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=400)


class SubcategoryDetailViews(APIView):
    serializers_class = serializers.SubcategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_queryset(self, pk):
        try:
            subcategory = Subcategory.objects.get(pk=pk)
        except Subcategory.DoesNotExist:
            return False
        return subcategory

    def put(self, request, pk, format=None):
        subcategory = self.get_queryset(pk)

        if not subcategory:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(subcategory, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        subcategory = self.get_queryset(pk)
        if not subcategory:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(subcategory)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        subcategory = self.get_queryset(pk)

        if not subcategory:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        subcategory.delete()
        return Response({'msg': 'NO Content'}, status=status.HTTP_204_NO_CONTENT)


class ItemViews(APIView):
    serializers_class = serializers.ItemSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get(self, request, format=None):
        items = Item.objects.all()
            # select_related('regionID')
        serializer = self.serializers_class(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=400)


class ItemDetailViews(APIView):
    serializers_class = serializers.ItemSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def get_queryset(self, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return False
        return item

    def put(self, request, pk, format=None):
        item = self.get_queryset(pk)

        if not item:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):

        item = self.get_queryset(pk)
        if not item:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)

        serializer = self.serializers_class(item)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        item = self.get_queryset(pk)

        if not item:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'msg': 'NO Content'}, status=status.HTTP_204_NO_CONTENT)


class CommentListView(APIView):
    serializers_class = serializers.CommentSerializer

    def get(self, request, university_id, format=None):
        comments = Comment.objects.select_related('user').filter(university=university_id)
        serializer = self.serializers_class(comments, many=True)
        return Response(serializer.data)


class CommentCreateView(APIView):
    serializers_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookmarkView(APIView):
    serializers_class = serializers.BookmarkSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        bookmark_item = Bookmark.objects.select_related('item').filter(user=request.user)
        serializer = self.serializers_class(bookmark_item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            try:
                bookmark_item = Bookmark.objects.get(user=request.user,
                                                     item=serializer.validated_data.get('item'))
                bookmark_item.save()
                return Response(self.serializers_class(bookmark_item).data)
            except Bookmark.DoesNotExist:
                serializer.save(user=request.user, item=Item.objects.get(pk=request.data["item"]))
                return Response(serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookmarkDeleteView(APIView):
    serializers_class = serializers.BookmarkSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk, format=None):
        try:
            bookmark_item = Bookmark.objects.get(pk=pk)
            bookmark_item.delete()
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=200)
        except Bookmark.DoesNotExist:
            return Response(content, status.HTTP_404_NOT_FOUND)


class ItemSearchView(APIView):
    serializers_class = serializers.ItemSerializer

    def get(self, request, key, cat_id, format=None):
        if cat_id == 0:
            items = Item.objects.filter(Q(itemName__icontains=key) | Q(region__name__icontains=key))
        else:
            items = Item.objects.filter(Q(region__id=cat_id),
                                                    Q(itemName__icontains=key) | Q(region__name__icontains=key))
        serializer = self.serializers_class(items, many=True)
        return Response(serializer.data)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny
    ]
    serializer_class = UserSerializer


def index(request):
    if request.method == 'POST':
        images = request.FILES.getlist("images")

        for f in images:
            itemInfo = Item(images=f)
            itemInfo.save()
        return HttpResponse("Images added successfully")
    return render(request, "Images/index.html")
