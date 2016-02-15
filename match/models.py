from django.db import models
from django.conf import settings
import trueskill as ts

class Match(models.Model):
    matchTitle = models.CharField(max_length=255)
    isPublic = models.BooleanField(default=False)
    matchDescription = models.TextField()
    matchPrompt = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '[Match: {}]'.format(self.matchTitle)

class Item(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    webPage = models.URLField(max_length=1024)
    itemTitle = models.CharField(max_length=255)
    itemText = models.TextField()
    itemPicture = models.ImageField()
    mu = models.FloatField(default=25.0, editable=False)
    sigma = models.FloatField(default=8.333, editable=False)

    def getRating(self):
        return ts.Rating(self.mu, self.sigma)

    def setRating(self, rating):
        self.mu = rating.mu
        self.sigma = rating.sigma

    rating = property(getRating, setRating)

    def __str__(self):
        mt = self.match.matchTitle[:50]
        it = self.itemTitle
        return '[Match , Item {}]'.format(mt, it)
