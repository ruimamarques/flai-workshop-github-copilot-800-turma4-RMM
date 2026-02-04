from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'created_at']
    search_fields = ['name', 'email', 'team']
    list_filter = ['team', 'created_at']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'activity_type', 'duration', 'calories_burned', 'date']
    search_fields = ['user_name', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['team', 'rank', 'total_points', 'total_activities', 'total_calories', 'updated_at']
    search_fields = ['team']
    list_filter = ['rank', 'updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    search_fields = ['title', 'description', 'category']
    list_filter = ['category', 'difficulty', 'created_at']
    ordering = ['-created_at']
