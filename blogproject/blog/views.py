from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def postList(request):
    posts = Post.objects.all().order_by('-createdAt')
    return render(request, 'blog/postList.html',{'posts':posts})

def postDetail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/postDetail.html', {'post':post})

def postCreate(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postList')
    else:
        form = PostForm()
    return render(request, 'blog/postForm.html', {'form':form})

def postUpdate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postList')
    else:
        form = PostForm(instance=post)

    # Sempre retorna o render, independentemente do método da requisição
    return render(request, 'blog/postForm.html', {'form': form})


def postDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
       post.delete()
       return redirect('postList')
    return render(request, 'blog/postConfirmDelete.html', {'post':post}) 