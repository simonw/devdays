from django.db import models

class Event(models.Model):
    location = models.CharField(max_length = 50)
    slug = models.SlugField()
    date = models.DateField()
    sold_out = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.location

class Speaker(models.Model):
    name = models.CharField(max_length = 50)
    affiliation = models.CharField(max_length = 50, blank = True)
    bio = models.TextField(blank = True)
    image_url = models.URLField(verify_exists=False, blank=True)
    
    def __unicode__(self):
        return self.name

class Session(models.Model):
    topic = models.CharField(max_length = 50)
    speakers = models.ManyToManyField(Speaker, blank=True)
    start = models.TimeField()
    end = models.TimeField()
    event = models.ForeignKey(Event)
    
    class Meta:
        ordering = ('start',)
    
    def __unicode__(self):
        return u'%s: %s' % (self.event, self.topic)
