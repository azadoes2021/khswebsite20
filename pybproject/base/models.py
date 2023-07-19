from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # learn django - the easyway [youtube]
    


    
    SUBJECT_CHOICES = (
        ('세무기장 서비스','세무기장 서비스'),
        ('경리 아웃소싱','경리 아웃소싱'),
        ('재산세신고','재산세신고'),
        ('세무자문 서비스','세무자문 서비스'),
        ('경정청구 서비스','경정청구 서비스'),
        ('기타','기타'),
        
    )
    
    STATUS_CHOICES = (
        ('신규','신규'),
        ('완료','완료'),
        ('진행중','진행중'),
        ('보류','보류'),
    )

    

    
    # [중요 title 없앨것입니다]
    # title = models.CharField(max_length=100, verbose_name='제목', default='') 

    name = models.CharField(max_length=50 ,null=True, verbose_name='이름(상호)')
    number = models.CharField(max_length=50 ,null=True, verbose_name='전화번호')
    # email = models.EmailField(max_length=50 ,null=True, verbose_name='이메일')

    # [중요 필드생성 필요함]
    # input == text : 전화번호
    # input = selectboxes : 세무기장, 법인세금 신고 기타 등등
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='', verbose_name='문의종류')

    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField(verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='신규')
    # input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지
    terms_confirmed = models.BooleanField(max_length=10, null=True, verbose_name="개인정보 수집 동의")
    code = models.CharField(max_length=10, default='as01') # code 문의하기, as01로 코드두어서 나중에 디비 join시킬때 사용
    dbcode = models.CharField(max_length=10, default='db01')# input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지
    

    

    # object~~ 대신에 제목, 작성자 title name 로 나오도록
    def __str__(self):
        return self.title + ' | ' + str(self.name)
    # 설명 : class AddPostView(CreateView) 로 만든 포스트 등록 폼 저장 후에 이동할 주소
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk':self.id})
        return reverse('home')
    # admin에서 쉽게 사용하기 위해 meta를 사용 => 1.테이블명, 2.어드민에서 사용될 이름
    class Meta:
        # db_table = 'py_user'
        verbose_name = '포스트'
        # verbose_name_plural = '사용자'
        ordering = ['-created']



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    content = models.TextField(max_length=160)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Comment by {}'.format(self.user)
    
    # def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))


    class Meta:
        # db_table = 'py_user'
        verbose_name = '댓글'
        # verbose_name_plural = '사용자'
        # ordering = ['-created']

# 101010





