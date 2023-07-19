from .forms import *
from django.db.models import Q
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .utils import searchposts, paginatePosts


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.views.generic.edit import FormView
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
#     ordering = ['-created']
class BaseDbBoardDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'basedbboard_details.html'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        # slug = self.kwargs["slug"]

        form = CommentForm()
        # post = get_object_or_404(Post, pk=pk, slug=slug)
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            
            content = form.cleaned_data['content']

            
            comment = Comment.objects.create(
                user=request.user, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)    

# AddPostView(CreateView)는 widget_tweaks 사용하여 템플릿을 만들었음. [How to] Django로 블로그 만들어보기 [widget tweaks] https://www.youtube.com/watch?v=jS4fLseF_cs
# [중요] 보완할것 포스팅할때 author 선택하지 않고 로그인한 사용자로 정해지도록 할 것. view 수정이 필요할 듯!!!   
# CreateView에 다른 model 가져와서 한 페이지에 나오도록 함
class AddBaseDbView(FormView):
    # model = Post     
    template_name = 'home.html'
    form_class = AskForm

    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    success_url = 'success'    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        context ['blog'] = Blog.objects.all()
        
        return context
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     blog = get_object_or_404(Post, pk=self.kwargs.get('pk'))
    #     context["blog"] = blog
    #     return context

#참고a .objects.all()
# def get_context_data(self. **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["objects"] = self.model.objects.all()
#         return context
#참고b
# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         movie = get_object_or_404(Movies, pk=self.kwargs.get('pk'))
#         context["movie"] = movie
class UpdateBaseDbView(UpdateView):
    model = Post     
    template_name = 'update_basedb.html'
    fields = ['status']
    success_url = reverse_lazy('basedbboard') 


class DeleteBaseDbView(DeleteView):
    model = Post
    template_name = 'delete_basedb.html'    
    success_url = reverse_lazy('basedbboard') 

@login_required(login_url="customlogin")
def basedb(request):
# def posts(request):    
    posts, search_query = searchposts(request)

    # paginatePosts(request, posts, 숫자) 숫자 넣어도 변화없음. utils의 result에 숫자를 넣어야 적용됨. 동영상과 조금 다른점임. 
    custom_range, posts = paginatePosts(request, posts, 5)

    
    context = {'posts': posts, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'basedbboard.html', context)

def success(request):
    return render(request, 'success.html', {})

# def comment_delete_question(request, comment_id):
    
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.question.id)

# 1.본인 2.로그인 하면 사용 가능하도록 @login required . 그리고 if랑 else문 넣어주고, 
# Comment 모델에서 name을 로그인한 user 로 등록되도록 바꿀 것. 
def comment_delete(request, comment_id):
    
    # comment = Comment.objects.get(id=comment_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    
    
    
    # return redirect('pybo:detail', question_id=comment.question.id)
    return redirect('basedbboard-detail', pk=comment.post.id)



def error_500(request):
    return render(request, '500.html')
def error_404(request, exception):
    return render(request, '404.html')








# 로그인 된 경우 사용할 수 있도록 @login required 달아줘야 함.

# def create(request, id):
#     if request.method == "POST":
#         commentForm = CommentForm(request.POST)        
#         if commentForm.is_valid():
#             #a  입력한 값이 유효하다면
#             #a  => save(commit=False)하면 되는데,
#             comment = commentForm.save(commit=False)
#             #b  comment를 저장할 때,
#             #b  comment의 작성자는 로그인한 사용자(user)로
#             comment.user = request.user


#             #d  post는 아래와 같이 post 라는 모델객체를 생성을 하여서 
#             post = Post()
#             #d  post의 id가 우리가 전달받은 'id'를 할당해주고.(넣어 주고.) 그것을  => e
#             post.id = id
            
#             #c  comment의 게시글은 몇번 글인지를 써줘야하는데, comment.post 처럼 관계 맺어준 변수는 해당 객체를 넣어줘야한다. => d
#             #e  comment.post = post 와 같이  comment.post에 저장되게 하고 
#             comment.post = post
#             #f  comment를 save해준다.
#             comment.save()


#     return redirect('article/'+str(id))



# def delete(request,) :











