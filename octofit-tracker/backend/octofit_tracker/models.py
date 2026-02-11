
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	member_usernames = models.JSONField(default=list)  # Store usernames as a list
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Activity(models.Model):
	ACTIVITY_TYPES = [
		('run', 'Run'),
		('walk', 'Walk'),
		('cycle', 'Cycle'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	activity_type = models.CharField(max_length=10, choices=ACTIVITY_TYPES)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	date = models.DateTimeField()

	def __str__(self):
		return f"{self.user.username} - {self.activity_type} ({self.duration} min)"

class Workout(models.Model):
	WORKOUT_TYPES = [
		('pushup', 'Pushup'),
		('situp', 'Situp'),
		('squat', 'Squat'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
	workout_type = models.CharField(max_length=10, choices=WORKOUT_TYPES)
	reps = models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.workout_type} ({self.reps} reps)"

class LeaderboardEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	score = models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.score}"
