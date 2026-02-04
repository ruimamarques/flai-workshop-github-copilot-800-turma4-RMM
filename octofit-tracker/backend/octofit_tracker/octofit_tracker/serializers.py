from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'created_at']
        read_only_fields = ['_id', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']
        read_only_fields = ['_id', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'user_name', 'activity_type', 'duration', 
                  'calories_burned', 'distance', 'date', 'created_at']
        read_only_fields = ['_id', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'total_points', 'total_activities', 
                  'total_calories', 'rank', 'updated_at']
        read_only_fields = ['_id', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'title', 'description', 'category', 'difficulty', 
                  'duration', 'calories_estimate', 'created_at']
        read_only_fields = ['_id', 'created_at']
