from .models import Comment, Post
from django import forms
# from django_summernote.admin import SummernoteModelAdmin


class CommentForm(forms.ModelForm):
    # remove the body label and make the comment box samller
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '4',
            'placeholder': 'Write a comment....'          
        })
    )

    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    # remove the content label and make the post box samller
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '6',
            'placeholder': 'Write a post....'        
        })
    )

    class Meta:
        model = Post
        fields = ('category', 'title', 'content')
        summernote_fields = ('content',)