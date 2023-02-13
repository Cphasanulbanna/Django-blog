from django import forms
from posts.models import Posts


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={"class":"input"}), label="Tags (Comma seperated)")

    class Meta:
        model = Posts
        exclude = ("author","published_date","is_deleted","categories")

        widgets = {
            "time_to_read" : forms.TextInput(attrs={"class":"input"}),
            "title" : forms.TextInput(attrs={"class":"input"}),
            "short_description" : forms.Textarea(attrs={"class":"input"}),
        }

        error_messages = {
            "time_to_read" : {
                "required" : "Time to read field is required"
            },
            "title" : {
                "required" : "title field is required"
            },
            "description" : {
                "required" : "description field is required"
            },
            "short_description" : {
                "required" : "short description field is required"
            },
            "featured_image" : {
                "required" : "featured image field is required"
            },
            "is_draft" : {
                "required" : "is draft field is required"
            },    
        }