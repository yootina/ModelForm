from django import forms
from .models import Article

# forms폴더안에서 ModelForm 상속
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'