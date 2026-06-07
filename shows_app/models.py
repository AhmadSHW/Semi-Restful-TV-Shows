from django.db import models

class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.CharField(max_length=255)
	release_date = models.DateField()
	description = models.TextField()
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	

	