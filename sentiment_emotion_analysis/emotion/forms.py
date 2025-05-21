
from django import forms

# Form to handle input for typed tweet analysis
class Emotion_Typed_Tweet_analyse_form(forms.Form):
    emotion_typed_tweet = forms.CharField(
        max_length=280, 
        initial='nothing', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your tweet here'})
    )

# Form to handle input for imported tweet analysis (by Twitter handle)
class Emotion_Imported_Tweet_analyse_form(forms.Form):
    emotion_imported_tweet = forms.CharField(
        max_length=100, 
        initial='nothing', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Twitter handle (e.g. @username)'})
    )
