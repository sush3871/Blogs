from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request,):
    return render(request, 'myapp/index.html')

# Blog List
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'myapp/blog_list.html', {'blogs': blogs})

# Blog Create
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'myapp/blog_create.html', {'form': form})

# Blog Update
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'myapp/blog_edit.html', {'form': form})
    
# Blog Delete
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'myapp/blog_delete.html', {'blog': blog})

# Blog Detail
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'myapp/blog_detail.html', {'blog': blog})
