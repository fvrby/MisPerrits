from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Perris/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Perris/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Perris/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Perris/post_edit.html', {'form': form})

def inicio(request):
    titulo= "Buenas!"
    if request.user.is_authenticated():
        titulo = "Bienvenido % " %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
                "titulo": titulo,
                "el_form": form,
              }
    if form.is.valid():
        instance = form.save(commit=false)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
                    "titulo": "Gracias %s !" %(nombre)
                }
        if not nombre:
                context = {
                    "titulo": "Gracias %s !" %(email)
                }
        print instance
        print instance.timestamp

return render(request, "Inicio.html",context)



