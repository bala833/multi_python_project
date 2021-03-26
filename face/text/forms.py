
from django import forms
from text.models import ImageToText
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder, Submit,Button, Div
from django.forms import CharField, Form, PasswordInput
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
 
# class VideoForm(forms.ModelForm):
#     class Meta:
#         model= Videos
#         fields= ["title", "video"]



class ImageToTextForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super(ImageToTextForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.helper = FormHelper()
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #   self.fields['countrycode'].widget.attrs['readonly'] = True
        self.helper.from_tag = False
        self.helper.disable_csrf = True
        self.helper.layout =Layout(
            Div(
                Div(Field('image'), css_class="col-md-6"),
                Div(Field('text'), css_class="col-md-6"),
                css_class='row'
            ),
        )
    class Meta:
        model = ImageToText
        fields =('image','text')
     


class LoginForm(forms.Form):
    user_name = forms.CharField(label="Enter Email/Number")
    password =  forms.CharField(widget=PasswordInput())

    def __init__(self,*args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)



    def clean(self):
        user_name = self.cleaned_data['user_name']
        password = self.cleaned_data['password']
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            print(user)
            if user:
                print('login')
            else:
                raise ValidationError("enter right credential")
        return user_name    

# class ContactForm(forms.Form):
#     postcode = forms.CharField(max_length=10)
    
#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)

#     def clean(self):
#         import requests
#         postcode = self.cleaned_data.get('postcode')
#         if settings.ECOMM_COUNTRY == 'UK':
#             if not postcode:
#                 self.add_error('postcode','This field is required')
#             r = requests.get('https://api.postcodes.io/postcodes/%s/validate' % (postcode,))
#             print(r.json())
#             is_valid = r.json().get('result')
#             if not is_valid:
#                 raise forms.ValidationError("Invalid Postcode")
#         return postcode