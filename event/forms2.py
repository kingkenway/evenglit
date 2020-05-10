from django import forms
from .models import Event

class EventForm(forms.Form):

    title = forms.CharField(
        max_length=30, required=False
    )
    location = forms.CharField(
        max_length=254, required=False, label='xxx', label_suffix=''
    )
    event_type = forms.TypedChoiceField(
        required=False, label='Event Type', label_suffix=''
    )
    start_time = forms.DateTimeField(
        required=False, label='Start Time', label_suffix=''
    )
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your descr.!',
        required=False,
    )
    
    # class Meta:
    #     model = Event
    #     fields = '__all__'
    #     # fields = ('title', 'description', 'location', 'ticket_type', 'start_time',
    #     #             'end_time', 'image', 'event_type'
    #     #         )
    #     labels = {
    #         'title': 'Event Title',
    #         'description': 'Event Description',
    #         'start_time': 'Starts',
    #         'end_time': 'Ends',
    #         'image': 'Event Image',
    #     }

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['event_type'].empty_label = "Select Event"

    #     def clean(self):
    #         cleaned_data = super(EventForm, self).clean()
    #         title = cleaned_data.get('title')
    #         description = cleaned_data.get('description')
    #         location = cleaned_data.get('location')
    #         if not title and not description and not location:
    #             raise forms.ValidationError('You have to write something!')


    #     self.fields['title'].required = False
    #     self.fields['description'].required = False
    #     self.fields['location'].required = False
    #     self.fields['image'].required = False
    #     self.fields['organiser'].required = False
    #     self.fields['event_type'].required = False
        