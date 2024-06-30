from django.urls import path

from habits import views
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path(
        'habit/',
        views.HabitListAPIView.as_view(),
        name='habit-list'
    ),
    path(
        'habit/public/',
        views.HabitPublicListAPIView.as_view(),
        name='habit-public-list'
    ),
    path(
        'habit/create/',
        views.HabitCreateAPIView.as_view(),
        name='habit-create'
    ),
    path('habit/update/<int:pk>/',
         views.HabitUpdateAPIView.as_view(),
         name='habit-update'
         ),
    path(
        'habit/delete/<int:pk>/',
        views.HabitDestroyAPIView.as_view(),
        name='habit-delete'
    ),
]
