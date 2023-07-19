from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('name','content',)
        fields = ('content',)        


        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'input-field'}),
        #     'title_tag': forms.TextInput(attrs={'class':'input-field'}),            
        #     'author': forms.Select(attrs={'class':'input-field'}), 
        #     'body': forms.TextInput(attrs={'class':'input-field'}),                       
        # }


          
# class AskForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         # fields = ('name','content',)  ['name', 'number', 'subject', 'body']
#         fields = ('name', 'number', 'subject', 'body', 'terms_confirmed','dbcode',)        


#         widgets = {
#             'name': forms.TextInput(attrs={'class':'input-field'}),
#             'number': forms.TextInput(attrs={'class':'input-field'}),            
#             'subject': forms.Select(attrs={'class':'input-field'}), 
#             'body': forms.TextInput(attrs={'class':'input-field'}), 
#             'terms_confirme': forms.CheckboxInput,                  
#             'dbcode': forms.HiddenInput(attrs={'value':'db01'}),
#         }         
          
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'input-field'}),
#             'title_tag': forms.TextInput(attrs={'class':'input-field'}),            
#             'author': forms.Select(attrs={'class':'input-field'}), 
#             'body': forms.TextInput(attrs={'class':'input-field'}),                       
#         }         

class AskForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '이름 또는 상호를 입력해주세요.'
        },
        max_length=64, label='이름(상호)'
    )
    number = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        },
        max_length=64, label='전화번호'
    )
    subject = forms.CharField(
        error_messages={
            'required': '문의종류를 입력해주세요.'
        },
        max_length=64, label='문의종류'
    )
    
    
    body = forms.CharField(
        error_messages={
            'required': '문의내용을 입력해주세요.'
        },
        max_length=64, label='문의내용'
    )
    terms_confirmed = forms.BooleanField(
        error_messages={
            'required': '동의여부를 체크해주세요.'
        },        
        label='개인정보 수집 및 이용 동의'
    )    
    

    def clean(self):        
        cleaned_data = super().clean()
        name = cleaned_data.get('name')        
        number = cleaned_data.get('number')
        subject = cleaned_data.get('subject')
        body = cleaned_data.get('body')
        terms_confirmed = cleaned_data.get('terms_confirmed')  
        if name and number and subject and body and terms_confirmed:

            post = Post(
                name = name,
                number = number,
                subject = subject,
                body = body,
                terms_confirmed = terms_confirmed
            )
            post.save()