
from django import forms
from text.models import ImageToText
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder, Submit,Button, Div
 
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
     