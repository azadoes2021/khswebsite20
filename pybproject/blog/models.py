from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    # learn django - the easyway [youtube]
    


    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    # [중요 필드생성 필요함] 01 active, 02 nonactive  models.boolean


    title = models.CharField(max_length=100, verbose_name='제목')    
    # slug = models.SlugField(max_length=120, null=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='글쓴이')    
    # image = models.ImageField(null=True, blank=True, upload_to="images", default="/blog.jpg", verbose_name='이미지')
    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    body = RichTextUploadingField(verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    

    # object~~ 대신에 제목, 작성자 title author 로 나오도록
    def __str__(self):
        return self.title + ' | ' + str(self.author)
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

class Blog(models.Model):
    # learn django - the easyway [youtube]
    


    STATUS_CHOICES = (
        ('yes','Yes'),
        ('no','No'),
    )

    # [중요 필드생성 필요함] 01 active, 02 nonactive  models.boolean


    title = models.CharField(max_length=100, verbose_name='제목')    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='글쓴이')    
    # image = models.ImageField(null=True, blank=True, upload_to="images", verbose_name='이미지')
    image = models.ImageField(null=True, blank=True, upload_to="images", default="/blog.jpg", verbose_name='이미지')
    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    body = RichTextUploadingField(verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='yes', verbose_name="노출여부")
    

    # object~~ 대신에 제목, 작성자 title author 로 나오도록
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    # 설명 : class AddPostView(CreateView) 로 만든 포스트 등록 폼 저장 후에 이동할 주소
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk':self.id})
        return reverse('home')
    # admin에서 쉽게 사용하기 위해 meta를 사용 => 1.테이블명, 2.어드민에서 사용될 이름
    class Meta:
        # db_table = 'py_user'
        verbose_name = '세금뉴스'
        # verbose_name_plural = '사용자'
        ordering = ['-created']























