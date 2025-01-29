from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['artwork', 'user', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }
