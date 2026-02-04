from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    distance = models.FloatField(null=True, blank=True)  # in km
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user_name} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.team} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
