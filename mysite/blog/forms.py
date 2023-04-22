from django import forms
from .models import Post
class PostCreateForm(forms.ModelForm): # DjangoのModelFormでは強力なValidationを使える
    
    class Meta: 
        model = Post # Postモデルと接続しPostモデルの内容に応じてformを作ってくれる
        fields = ('title', 'text') # 入力するカラムを指定
        