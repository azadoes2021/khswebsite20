from typing import Any, Dict
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import searchposts, paginatePosts


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class BlogHomeView(ListView):
    # model = Blog
    template_name = 'home.html' # [중요] index.html 로 바꿔야 할듯
    ordering = ['-created']  
    # object_list 대신에 product_list라는 이름을 사용하겠다.
    # context_object_name = 'product_list'

class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'article_details.html'
    
# AddPostView(CreateView)는 widget_tweaks 사용하여 템플릿을 만들었음. [How to] Django로 블로그 만들어보기 [widget tweaks] https://www.youtube.com/watch?v=jS4fLseF_cs
class AddPostView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("customlogin")
    success_url = reverse_lazy("posts") 
    model = Blog 
    
    template_name = 'add_post.html'
    fields = ['title', 'image', 'body', 'status']

    # 장고문서활용 - 글쓴이 자동으로 넣는 방법 https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
class UpdatePostView(UpdateView):
    model = Blog      
    template_name = 'update_post.html'
    fields = ['title', 'image', 'body', 'status']


class DeletePostView(DeleteView):
    model = Blog
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts') 


@login_required(login_url="customlogin")
def posts(request):
# def posts(request):    
    posts, search_query = searchposts(request)

    # paginatePosts(request, posts, 숫자) 숫자 넣어도 변화없음. utils의 result에 숫자를 넣어야 적용됨. 동영상과 조금 다른점임. 
    custom_range, posts = paginatePosts(request, posts, 5)

    
    context = {'posts': posts, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'posts.html', context)













