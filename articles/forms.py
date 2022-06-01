
# django related imports
from django import forms


class ArticleForm(forms.Form):
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