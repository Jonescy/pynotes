"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path
from apps.ipThrottler import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<int:pk>/', views.BookAPIView.as_view()),
    path('books2/', views.BookGenericAPIView.as_view()),
    path('books2/<int:pk>/', views.BookGenericAPIView.as_view()),
    path('books3/', views.BookView.as_view()),
    path('books4/', views.BookView2.as_view()),

]
