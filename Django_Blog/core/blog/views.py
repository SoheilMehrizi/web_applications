# Import Essential Libraries
from django.shortcuts import render
from django.views.generic import (
                                 TemplateView,
                                 ListView,
                                 CreateView, DetailView)
from .forms import PostForm
from .models import Post
def index_fbView(request):
    return render(request, 'blog/index.html', context = {"message": "Hello"})


class IndexView(TemplateView):
    """
        Serve's index.html Template and passes extra arguments to it
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Soheil"
        return context



class PostListView(ListView):
    """
    Lists All Posts that paginated by 2 post per page
    """
    model = Post
    paginate_by = 2
    context_object_name = 'Posts'
    template_name='postlist.html'
    ordering = '-id'
    def get_queryset(self):
        queryset = Post.objects.filter()
        return super().get_queryset()

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = ""
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = "PostDetailView.html"
    context_object_name = "Post"


