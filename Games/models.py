from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    Genre = [
        ('fps', 'First-Person Shooter'),  # Wert und lesbare Form
        ('rp', 'Role-Play'),
        ('sg', 'Strategy Game'),
        ('moba', 'Mulitplayer Online Battle Arena'),
        ('ftp', 'Free to Play'),
    ]
    Fsk = [
        ('0', 'FSK 0'),  # Wert und lesbare Form
        ('6', 'FSK 6'),
        ('12', 'FSK 12'),
        ('16', 'FSK 16'),
        ('18', 'FSK 18'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200,
                                   blank=True)
    type = models.CharField(max_length=4,
                            choices=Genre,
                            )
    fsk = models.CharField(max_length=2,
                           choices=Fsk,
                           )
    creator = models.CharField(max_length=50)
    date_published = models.DateTimeField(blank=True,
                                          default=date.today,
                                          )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             # Löscht den User und alle anderen Einträge die der User eingetragen hat
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta:
        ordering = ['title', '-type']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def get_full_title(self):
        return_string = self.title
        if self.description:  # if subtitle is not empty
            return_string = self.title + ': ' + self.description
        return return_string

    def __str__(self):
        return self.title + ' (' + self.creator + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.creator + ' / ' + self.type
