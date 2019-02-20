from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator # Paginator import
from .forms import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋
    
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)
    
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts, 'range':range(posts.paginator.num_pages) })

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) # 몇 번 객체
    return render(request, 'detail.html', {'details': details})

def new(request): # new.html 띄어주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 데이터베이스에 저장하라는 메소드
    # 객체.delete() 하면 데이터베이스로부터 내용을 지우라는 뜻
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST    
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid:            
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
        # return render(request, 'new.html', {'form':form})

    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

