from django import forms
from .models import Event
from datetime import date
from django.conf import settings

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
        self.fields['event_type'].empty_label = "Select the type of event"
        self.fields['title'].required = False
        self.fields['description'].required = False
        self.fields['event_type'].required = False
        self.fields['location'].required = False
        # self.fields['organizer_description'].required = False
        
        self.fields['title'].widget.attrs['placeholder'] = 'Give a short distinct name'
        self.fields['description'].widget.attrs['placeholder'] = 'Your event description goes in here'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter your event Location'

        # self.fields['title'].label_suffix = ''

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        title = cleaned_data.get('title')
        location = cleaned_data.get('location')
        description = cleaned_data.get('description')
        # if not title and not location and not description:
        #     raise forms.ValidationError('You have to write something!')
        if title == "title":
            raise forms.ValidationError('Correct Guy!')