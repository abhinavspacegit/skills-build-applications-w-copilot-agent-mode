import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Workout, LeaderboardEntry

def create_users():
    users = []
    for i in range(5):
        username = f'user{i+1}'
        email = f'user{i+1}@example.com'
        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        users.append(user)
    print(f"Created {len(users)} users.")
    return users

def create_teams(users):
    teams = []
    for i in range(2):
        team_name = f"Team{i+1}"
        Team.objects.filter(name=team_name).delete()  # Ensure uniqueness
        team_members = random.sample(users, k=3)
        member_usernames = [user.username for user in team_members]
        team = Team.objects.create(name=team_name, member_usernames=member_usernames)
        teams.append(team)
    print(f"Created {len(teams)} teams.")
    return teams

def create_activities(users):
    activities = []
    activity_types = ['run', 'walk', 'cycle']
    for user in users:
        for _ in range(3):
            activity = Activity.objects.create(
                user=user,
                activity_type=random.choice(activity_types),
                duration=random.randint(20, 90),
                date=datetime.now() - timedelta(days=random.randint(0, 10))
            )
            activities.append(activity)
    print(f"Created {len(activities)} activities.")
    return activities

def create_leaderboard(users):
    leaderboard = []
    for user in users:
        entry = LeaderboardEntry.objects.create(user=user, score=random.randint(100, 1000))
        leaderboard.append(entry)
    print(f"Created {len(leaderboard)} leaderboard entries.")
    return leaderboard

def create_workouts(users):
    workouts = []
    workout_types = ['pushup', 'situp', 'squat']
    for user in users:
        for _ in range(2):
            workout = Workout.objects.create(
                user=user,
                workout_type=random.choice(workout_types),
                reps=random.randint(10, 50)
            )
            workouts.append(workout)
    print(f"Created {len(workouts)} workouts.")
    return workouts

def main():
    users = create_users()
    teams = create_teams(users)
    activities = create_activities(users)
    leaderboard = create_leaderboard(users)
    workouts = create_workouts(users)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()
if __name__ == '__main__':
    main()

def create_users():
    users = []
    for i in range(5):
        username = f'user{i+1}'
        email = f'user{i+1}@example.com'
        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        users.append(user)
    print(f"Created {len(users)} users.")
    return users

# Add similar functions for teams, activities, leaderboard, and workouts when models are implemented

def main():
    users = create_users()
    # Call other creation functions here

if __name__ == '__main__':
    main()
