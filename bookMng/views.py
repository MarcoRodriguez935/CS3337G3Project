from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import MainMenu
from .models import Book

from .forms import BookForm
from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Post, MainMenu
from .forms import PostForm



def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():

            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')

    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


def displaybooks(request):

    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  })

def mybooks(request):

    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                  })

def book_detail(request, book_id):

    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]

    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                  })



def book_delete(request, book_id):

    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


class Register(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


#messageboard
def index(request):
    return render(request,
                  'board/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def postlist(request):
    posts = Post.objects.all()  # Query all Post objects

    return render(request,
                  'board/postlist.html',
                  {
                      'posts': posts,
                      'item_list': MainMenu.objects.all(),
                  })

    # return render(request, 'postlist.html', {'posts': posts})


def postdetail(request, post_id):
    posts = Post.objects.all()

    return render(request,
                  'board/postdetail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'posts': posts,
                  })

    #post = get_object_or_404(Post, id=post_id)
    #return render(request, 'board/postdetail.html', {'post': post})


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postlist')
    else:
        form = PostForm()
    return render(request, 'board/postcreate.html', {'form': form})

