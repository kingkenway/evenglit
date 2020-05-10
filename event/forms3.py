from django import forms
from .models import Event
from django.forms import SplitDateTimeField, SplitDateTimeWidget

def add_classes(attrs, classes):
    if 'class' in attrs:
        attrs['class'] += f' {classes}'
    else:
        attrs['class'] = classes

class DateTimePicker(SplitDateTimeWidget):
    datepicker_classes = 'datepicker'
    timepicker_classes = 'timepicker'

    def __init__(self, attrs=None, date_format=None, time_format=None, date_attrs=None, time_attrs=None):
        date_attrs, time_attrs = date_attrs or {}, time_attrs or {}
        add_classes(date_attrs, self.datepicker_classes)
        add_classes(time_attrs, self.timepicker_classes)
        super().__init__(attrs, date_format, time_format, date_attrs, time_attrs)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class EventForm(forms.ModelForm):
    # start_time=forms.SplitDateTimeField(input_time_formats=['%I:%M %p'])
    # end_time =forms.SplitDateTimeField(input_time_formats=['%I:%M %p'])

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
            'description': 'Event Description'
        }
        widgets = {
            'start_time': DateTimePicker(),
            'end_time': DateTimePicker(),
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



# class EventForm(forms.Form):
#     title = forms.CharField(max_length=30, label_suffix='')
#     location = forms.CharField(max_length=254)
#     description = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     start_time = forms.DateField(label_suffix='',)
#     end_time = forms.DateField(label_suffix='',)
#     ticket_type = forms.CharField(max_length=30, label_suffix='')

    
#     # source = forms.CharField(       # A hidden input for internal use
#     #     max_length=50,              # tell from which page the user sent the message
#     #     widget=forms.HiddenInput()
#     # )

#     def clean(self):
#         cleaned_data = super(EventForm, self).clean()
#         title = cleaned_data.get('title')
#         location = cleaned_data.get('location')
#         description = cleaned_data.get('description')
#         if not title and not location and not description:
#             raise forms.ValidationError('You have to write something!')