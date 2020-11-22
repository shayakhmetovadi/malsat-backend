from django.urls import path, include
from django.contrib import admin
from posts import views
from django.conf.urls.static import static
from django.conf import settings
from posts.views import *

urlpatterns = [
    path('regions/', views.RegionViews.as_view()),
    path('regions/<int:pk>', views.RegionDetailViews.as_view()),
    path('', views.index, name="index"),

    path('auth/signup', views.CreateUserView.as_view()),
    path('items/', views.ItemViews.as_view()),
    path('items/<int:pk>', views.ItemDetailViews.as_view()),
    path('categories/', views.CategoryViews.as_view()),
    path('categories/<int:pk>', views.CategoryDetailViews.as_view()),
    path('subcategories/', views.SubcategoryViews.as_view()),
    path('subcategories/<int:pk>', views.SubcategoryDetailViews.as_view()),
    path('comments/<int:item_id>', views.CommentListView.as_view()),
	path('comments/', views.CommentCreateView.as_view()),
    path('bookmark/', views.BookmarkView.as_view()),
    path('bookmark/<int:pk>', views.BookmarkDeleteView.as_view()),
    path('items/itemName=<str:key>/', views.ItemSearchView.as_view()),

]