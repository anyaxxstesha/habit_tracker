from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
