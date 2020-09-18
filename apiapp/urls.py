from django.urls import path

from apiapp import views

urlpatterns = [
    path('demo/', views.Demo.as_view()),
    path('book/', views.BookAPIView.as_view()),
]