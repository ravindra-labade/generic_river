from django.db import models


class River(models.Model):
    river_name = models.CharField(max_length=20)
    length = models.IntegerField()
    area = models.IntegerField()
    states_covered = models.CharField(max_length=20)
    choice = [('Perrenial', 'PERRENIAL'), ('seasonal', 'SEASONAL')]
    river_mode = models.CharField(max_length=10, choices=choice)
