from django import forms
from blog.models import Blog,ContactBlog
class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content"]


#class Contactform(forms.Form):
 #   name = forms.CharField()
 #   email = forms.EmailField()
  #  content = forms.CharField(widget=forms.Textarea)

class ContactBlogModel(forms.ModelForm):
    class Meta:
        model = ContactBlog
        fields = '__all__'

        def clean_name(self):
            name = self.cleaned_data.get("name")
            if 'ashraf' in name:
                return name
            else:
                raise forms.ValidationError("Invalid")