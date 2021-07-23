from django import forms


class ChatTextForm(forms.Form):
    text = forms.CharField(required=True)
    sk = forms.CharField(required=False)
