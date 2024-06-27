from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.paginators import HabitPaginator

from habits.models import Habit

from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = HabitSerializer

    # def perform_create(self, serializer):
    #     habit = serializer.save()
    #     habit.user = self.request.user
    #     habit.save()


class HabitListAPIView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    # permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    # permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    # permission_classes = (IsAuthenticated, IsOwner,)
    queryset = Habit.objects.all()
