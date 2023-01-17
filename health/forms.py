from .models import Comment, Post
from django import forms


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
    class Meta:
        model = Post
        fields = ('category', 'title', 'slug', 'author', 'featured_image', 'excerpt', 'content', 'status')
        prepopulated_fields = {'slug': ('title',)}

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug':  forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a post....'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'featured_image', 'excerpt', 'content')
        prepopulated_fields = {'slug': ('title',)}

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug':  forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'status': forms.Select(attrs={'class': 'form-control'}),
        }
