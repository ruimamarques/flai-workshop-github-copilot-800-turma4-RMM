from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    Provides CRUD operations for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Team model.
    Provides CRUD operations for teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Activity model.
    Provides CRUD operations for activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Leaderboard model.
    Provides CRUD operations for leaderboard entries.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Workout model.
    Provides CRUD operations for workouts.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
