from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fighting for fitness!'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League members committed to peak performance!'
        )

        self.stdout.write('Creating users...')
        
        # Create Marvel superhero users
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com'},
        ]
        
        # Create DC superhero users
        dc_heroes = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel'
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team DC'
            )
            dc_users.append(user)

        all_users = marvel_users + dc_users

        self.stdout.write('Creating activities...')
        
        # Activity types
        activity_types = [
            {'type': 'Running', 'calories_per_min': 10, 'has_distance': True},
            {'type': 'Cycling', 'calories_per_min': 8, 'has_distance': True},
            {'type': 'Swimming', 'calories_per_min': 11, 'has_distance': True},
            {'type': 'Weight Training', 'calories_per_min': 6, 'has_distance': False},
            {'type': 'Yoga', 'calories_per_min': 3, 'has_distance': False},
            {'type': 'Boxing', 'calories_per_min': 9, 'has_distance': False},
            {'type': 'HIIT', 'calories_per_min': 12, 'has_distance': False},
        ]
        
        # Create activities for the last 30 days
        for user in all_users:
            num_activities = random.randint(15, 30)
            for _ in range(num_activities):
                activity = random.choice(activity_types)
                duration = random.randint(20, 90)
                calories = duration * activity['calories_per_min']
                days_ago = random.randint(0, 29)
                activity_date = datetime.now() - timedelta(days=days_ago)
                
                activity_data = {
                    'user_id': str(user._id),
                    'user_name': user.name,
                    'activity_type': activity['type'],
                    'duration': duration,
                    'calories_burned': calories,
                    'date': activity_date,
                }
                
                if activity['has_distance']:
                    activity_data['distance'] = round(random.uniform(2.0, 15.0), 2)
                
                Activity.objects.create(**activity_data)

        self.stdout.write('Calculating leaderboard...')
        
        # Calculate team statistics for leaderboard
        marvel_activities = Activity.objects.filter(user_name__in=[u.name for u in marvel_users])
        dc_activities = Activity.objects.filter(user_name__in=[u.name for u in dc_users])
        
        marvel_total_calories = sum(a.calories_burned for a in marvel_activities)
        dc_total_calories = sum(a.calories_burned for a in dc_activities)
        
        marvel_total_activities = marvel_activities.count()
        dc_total_activities = dc_activities.count()
        
        # Points = total calories / 10
        marvel_points = marvel_total_calories // 10
        dc_points = dc_total_calories // 10
        
        # Determine ranks
        if marvel_points > dc_points:
            marvel_rank, dc_rank = 1, 2
        else:
            marvel_rank, dc_rank = 2, 1
        
        Leaderboard.objects.create(
            team='Team Marvel',
            total_points=marvel_points,
            total_activities=marvel_total_activities,
            total_calories=marvel_total_calories,
            rank=marvel_rank
        )
        
        Leaderboard.objects.create(
            team='Team DC',
            total_points=dc_points,
            total_activities=dc_total_activities,
            total_calories=dc_total_calories,
            rank=dc_rank
        )

        self.stdout.write('Creating workouts...')
        
        # Create sample workouts
        workouts_data = [
            {
                'title': 'Super Soldier Strength Training',
                'description': 'Build strength like Captain America with this intense workout combining weightlifting and bodyweight exercises.',
                'category': 'Strength',
                'difficulty': 'Advanced',
                'duration': 45,
                'calories_estimate': 350,
            },
            {
                'title': 'Web-Slinger Cardio',
                'description': 'Improve your agility and endurance with this high-intensity cardio workout inspired by Spider-Man.',
                'category': 'Cardio',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories_estimate': 300,
            },
            {
                'title': 'Amazonian Warrior HIIT',
                'description': 'Channel your inner Wonder Woman with this powerful HIIT workout for total body conditioning.',
                'category': 'HIIT',
                'difficulty': 'Advanced',
                'duration': 25,
                'calories_estimate': 280,
            },
            {
                'title': 'Flash Speed Training',
                'description': 'Boost your speed and explosive power with sprint intervals and plyometric exercises.',
                'category': 'Speed',
                'difficulty': 'Intermediate',
                'duration': 35,
                'calories_estimate': 320,
            },
            {
                'title': 'Zen Master Recovery Yoga',
                'description': 'Recover like Doctor Strange with this relaxing yoga session focused on flexibility and mental clarity.',
                'category': 'Flexibility',
                'difficulty': 'Beginner',
                'duration': 40,
                'calories_estimate': 120,
            },
            {
                'title': 'Dark Knight Combat Training',
                'description': 'Master combat skills with this Batman-inspired boxing and martial arts workout.',
                'category': 'Combat',
                'difficulty': 'Advanced',
                'duration': 50,
                'calories_estimate': 450,
            },
            {
                'title': 'Atlantean Swimming Circuit',
                'description': 'Build endurance in the water with this Aquaman-inspired swimming workout.',
                'category': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_estimate': 400,
            },
            {
                'title': 'Iron Legion Full Body',
                'description': 'A comprehensive full-body workout using the latest fitness tech, Tony Stark approved.',
                'category': 'Full Body',
                'difficulty': 'Intermediate',
                'duration': 40,
                'calories_estimate': 320,
            },
            {
                'title': 'Asgardian Power Lifting',
                'description': 'Lift like Thor with this heavy compound lifting routine for maximum strength gains.',
                'category': 'Strength',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 400,
            },
            {
                'title': 'Speedster Core Blast',
                'description': 'Strengthen your core with this fast-paced workout designed for heroes on the move.',
                'category': 'Core',
                'difficulty': 'Beginner',
                'duration': 20,
                'calories_estimate': 150,
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created:')
        self.stdout.write(f'  - {Team.objects.count()} teams')
        self.stdout.write(f'  - {User.objects.count()} users')
        self.stdout.write(f'  - {Activity.objects.count()} activities')
        self.stdout.write(f'  - {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'  - {Workout.objects.count()} workouts')
