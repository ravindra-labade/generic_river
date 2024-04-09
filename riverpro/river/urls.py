from django.urls import path
from .views import Add_river, List_river, Detail_river, Update_river, Delete_river

urlpatterns = [
    path('add/', Add_river.as_view()),
    path('list/', List_river.as_view()),
    path('detail/<int:pk>/', Detail_river.as_view()),
    path('update/<int:pk>/', Update_river.as_view()),
    path('delete/<int:pk>/', Delete_river.as_view()),
]
