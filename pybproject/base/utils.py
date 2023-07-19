from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatePosts(request, posts, results):
    page = request.GET.get('page')
    # utils의 result에 숫자를 넣어 페이지에 나올 결과 숫자 조절가능
    results = 5
    paginator = Paginator(posts, results)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages

        posts = paginator.page(page)

    leftindex = (int(page) - 4)

    if leftindex < 1 :
        leftindex = 1

    rightindex = (int(page) + 5)

    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1

    custom_range = range(leftindex,rightindex)


    return custom_range, posts


def searchposts(request):    
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query') 
    # Q(author__name : author는 외래키라서 표현을 달리해준 것임.
    # Q(author__username__icontains=search_query) |
    posts = Post.objects.filter(

        Q(name__icontains=search_query) |
        Q(number__icontains=search_query) |
        Q(status__icontains=search_query) |        
        Q(body__icontains=search_query) |
        Q(created__icontains=search_query) 
    )

    return posts, search_query
