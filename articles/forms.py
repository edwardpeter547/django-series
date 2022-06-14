
# django related imports
from dataclasses import fields
from django import forms
from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "author", "category", "content"]
        
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        content = data.get("content")
        is_title = Article.objects.all().filter(title__icontains=title)
        if is_title.exists():
            self.add_error("title", f"\"{title}\" is already in use")
        return data
        


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    author = forms.CharField() 
    category = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        
        if "office" in title:  # type: ignore
            self.add_error(field="title", error="Title has been taken")
        if "office" in content:   # type: ignore
            self.add_error(field="content", error="Content has been taken")
        return cleaned_data