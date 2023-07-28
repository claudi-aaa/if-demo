from django import forms
from django.forms import TextInput, EmailInput


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Last', 'style': 'width: 100%'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'yourname@email.com', 'style': 'width: 100%'}))
    subject = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Just wanted to say hello', 'style': 'width: 100%'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message here...', 'style': 'width: 100%'}))