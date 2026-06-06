from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        # fields = ['name', 'rollno', 'email', 'contact', 'course', 'address']
        exclude = ['trainer']

        labels = {
            'name' : 'Full Name',
            'rollno' : 'Roll Number',
        }

        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Write your name here...'
                }
            ),

            'rollno' : forms.NumberInput(
                attrs = {
                    'placeholder' : 'Write your roll number here...'
                }
            ),

            'email' : forms.EmailInput(
                attrs = {
                    'placeholder' : 'Write your email here...'
                }
            ),

            'contact' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Write your contact here...'
                }
            ),

            'course' : forms.Select(
                attrs = {
                    'style': 'height:35px; width:400px; font-size:25px;'
                }
            ),

            'address' : forms.Textarea(
                attrs={
                    'placeholder' : 'Write your address here...',
                    'style' : 'font-size:25px',
                    'row' : 4,
                    'cols' : 30,
                }
            ),

            'marks' : forms.NumberInput(
                attrs={
                    'placeholder' : 'Write your marks here...'
                }
            )
        }










# class StudentForm(forms.Form):
#     name = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 'placeholder' : 'Write you name here...'
#             }
#         )
#     )

#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     contact = forms.CharField()
#     course = forms.ChoiceField(
#         widget=forms.Select(
#             attrs={

#             }
#         )
#     )
#     address = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'row':6,
#                 'cols':10
#             }
#         )
#     )