from django.shortcuts import render
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request,):
    return render(request, 'myapp/index.html')

# Blog List
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'myapp/blog_list.html', {'blogs': blogs})

# Blog Create
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Save the form but don't commit yet
            blog.user = request.user       # Assign the user properly
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'myapp/blog_form.html', {'form': form})

# Blog Update
@login_required
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
        return render(request, 'myapp/blog_form.html', {'form': form})
    
# Blog Delete
@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'myapp/blog_delete.html', {'blog': blog})

# User Registration
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Blog Detail
# def blog_detail(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     return render(request, 'myapp/blog_detail.html', {'blog': blog})
