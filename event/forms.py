from django import forms
from .models import Event
# from datetime import date
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.utils import timezone

# def date_time_real(val):
#     if val


class EventForm(forms.ModelForm):

    start_time = forms.DateTimeField(
        input_formats=settings.DATE_TIME_INPUT_FORMATS,
        widget=forms.widgets.DateTimeInput(attrs={'class': 'datepicker'})
    )
    end_time = forms.DateTimeField(
        input_formats=settings.DATE_TIME_INPUT_FORMATS,
        widget=forms.widgets.DateTimeInput(attrs={'class': 'datepicker'})
    )


    class Meta:
        model = Event
        # fields = '__all__'
        fields = (
            'title',
            'description',
            'location',
            'ticket_type',
            'start_time',
            'end_time',
            'image',
            'event_type',
            'organizer_name',
            'organizer_description',
            )
        labels = {
            'title': 'Event Title',
            'description': 'Event Description',
            'image': "Event Image",
        }


    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # for bound_field in self:
        #     if hasattr(bound_field, "field") and bound_field.field.required:
        #         bound_field.field.widget.attrs["required"] = "required"
                
        self.fields['event_type'].empty_label = "Select the type of event"
        self.fields['title'].required = True
        self.fields['description'].required = True
        self.fields['event_type'].required = True
        self.fields['location'].required = True
        # self.fields['image'].required = True
        # self.fields['organizer_description'].required = False
        
        self.fields['title'].widget.attrs['placeholder'] = 'Give a short distinct name'
        self.fields['description'].widget.attrs['placeholder'] = 'Your event description goes in here'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter your event Location'

        # self.fields['title'].label_suffix = ''

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        location = cleaned_data.get('location')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        # DateTime Sorting Validation
        current_date_time = timezone.localtime(timezone.now()).replace(microsecond=0) 
        time_diff = start_time - current_date_time

        if time_diff.total_seconds() < 7200:
            raise forms.ValidationError('The minimum event time is 2 hours after system time')

        elif start_time > end_time:
            raise forms.ValidationError('Start time cannot be greater than End Time')
        
        elif start_time == end_time:
            raise forms.ValidationError('Start time cannot be equal to End Time')
        elif title == "a":
            raise forms.ValidationError('Title error')
            
        # if not title and not location and not description:
        #     raise forms.ValidationError('You have to write something!')