from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Team A"
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, "Team A")
    
    def test_user_str(self):
        """Test the string representation of user"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Team A",
            description="Test team description"
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Team A")
        self.assertEqual(self.team.description, "Test team description")
    
    def test_team_str(self):
        """Test the string representation of team"""
        self.assertEqual(str(self.team), "Team A")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="user123",
            user_name="Test User",
            activity_type="Running",
            duration=30,
            calories_burned=250,
            distance=5.0,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_name, "Test User")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 250)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            team="Team A",
            total_points=1000,
            total_activities=50,
            total_calories=5000,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.leaderboard.team, "Team A")
        self.assertEqual(self.leaderboard.total_points, 1000)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title="Morning Run",
            description="5K morning run",
            category="Cardio",
            difficulty="Medium",
            duration=30,
            calories_estimate=300
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.title, "Morning Run")
        self.assertEqual(self.workout.category, "Cardio")
        self.assertEqual(self.workout.difficulty, "Medium")


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def test_create_user(self):
        """Test creating a user via API"""
        url = reverse('user-list')
        data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'team': 'Team B'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def test_create_team(self):
        """Test creating a team via API"""
        url = reverse('team-list')
        data = {
            'name': 'API Team',
            'description': 'Team created via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def test_create_activity(self):
        """Test creating an activity via API"""
        url = reverse('activity-list')
        data = {
            'user_id': 'user123',
            'user_name': 'Test User',
            'activity_type': 'Swimming',
            'duration': 45,
            'calories_burned': 400,
            'distance': 2.0,
            'date': datetime.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_api_root(self):
        """Test that API root returns all endpoint links"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
