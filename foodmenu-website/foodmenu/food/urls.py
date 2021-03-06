from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food/
    #path('', views.index, name='index'),  Path for function index view
    path("", views.IndexClassView.as_view(), name="index"),
    path('item/', views.item, name='item'),
     #/food/1
    #path('<int:item_id>', views.detail, name='detail'), Path for function detail view
    path('<int:pk>', views.FoodDetail.as_view(), name='detail'),
    # add items
    #path('add', views.create_item, name='create_item'), Path for function create view
    path('add', views.CreateItem.as_view(), name='create_item'),
    # edit items
    path('update/<int:id>', views.update_item, name='update_item'),
    # delete items
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]
