from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class ActivityManager(models.Manager):
    def get_queryset(self):
        return super(ActivityManager,
                    self).get_queryset()\
                    .filter(is_active=1)

class EventType(models.Model):
    title = models.CharField(max_length=50)

    objects = models.Manager() # The default manager.    
    def __str__(self):
        return self.title


class Event(models.Model):
    DISABLED = 0
    ACTIVE = 1
    
    ACTIVITY_TYPE = (
        (DISABLED, 'disabled'),
        (ACTIVE, 'active'),
    )
    TICKET_TYPE = (
        ('free', 'FREE'),
        ('paid', 'PAID'),
    )
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    organiser = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=10,
                                choices=TICKET_TYPE,
                                default='free')
    
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    is_active  = models.IntegerField(default=1, choices=ACTIVITY_TYPE)

    image = models.ImageField(upload_to='event_image', blank=True, null=True)

    organizer_name = models.CharField(max_length=250, blank=True, null=True)
    organizer_description = models.TextField(max_length=250, blank=True, null=True)

    slug = models.SlugField(default='', editable=False,max_length=255,)
   
    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.
    active = ActivityManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('event_detail', kwargs=kwargs)

    def get_slug(self):
        return slugify(self.title)
        
    def get_absolute_url(self):
        url = reverse('event_detail', kwargs={'pk': self.pk, 'slug': self.get_slug()})
        return url

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)