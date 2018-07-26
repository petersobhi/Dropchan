from django import forms


class ThreadForm(forms.Form):
    title = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'title'})
    )

    description = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description'})
    )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'id': 'image'})
    )


class CommentForm(forms.Form):
    body = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'body', 'rows': "6"})
    )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'id': 'image'})
    )
