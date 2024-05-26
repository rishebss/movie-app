from django.urls import path
from . import views
app_name='movie_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('movi/',views.movi,name='movi'),
    path('add/', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('revw/',views.revw,name='revw'),
    # path('reviewpage/',views.reviewpage,name='reviewpage'),
    path('search/', views.search, name='search')


]