from django.urls import path, views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>', views.detail, name='detail')
]