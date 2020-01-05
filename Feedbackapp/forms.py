from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name..'
            }
        )
    )
    ratings = forms.IntegerField(
       label="Enter Ratings:",
       widget=forms.NumberInput(
           attrs={
               'class':'form-control',
               'placeholder':'Ratings..'
           }
       )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback:",
        widget= forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback..'
            }
        )
    )

