from django.db import models


class Movie(models.Model):
	actor=models.CharField(max_length=30)
	actor_movie=models.CharField(max_length=50)
	genre=models.CharField(max_length=20)
	movie_logo=models.CharField(max_length=100)

	def __str__(self):
		return self.actor+'---'+self.actor_movie+'---'+self.genre

class Song(models.Model):
	"""docstring for Sonm\g"""
	movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
	File_type=models.CharField(max_length=50)
	Song_name=models.CharField(max_length=100)

	def __str__(self):
		return self.File_type+'---'+self.Song_name

	
