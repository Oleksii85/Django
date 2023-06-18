from django import forms
from django.contrib.auth.models import User
from .models import Blogpost, Topic, Comment


# class BlogpostForm(forms.Form):
#     title = forms.CharField(max_length=155, required=True)
#     content = forms.CharField(max_length=155, required=True, widget=forms.Textarea)
#     author = forms.ModelChoiceField(queryset=User.objects.all())
#     topic = forms.ModelChoiceField(queryset=Topic.objects.all())


class BlogpostModelForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'content', 'topic']


# class CommentForm(forms.Form):
#     content = forms.CharField(max_length=155, widget=forms.Textarea)
#     author = forms.ModelChoiceField(queryset=User.objects.all())
#     blogpost = forms.ModelChoiceField(queryset=Blogpost.objects.all())


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'blogpost']
