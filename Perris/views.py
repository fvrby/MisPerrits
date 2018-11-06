from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post, Adoptar, Adoptado
from .forms import PostForm, LoginForm
from .forms import AdoptarForm, AdoptadoForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Perris/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Perris/post_detail.html', {'post': post})

def index(request):
    adoptar = Adoptar.objects.order_by('run')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'Perris/index.html', {'adoptar': adoptar, 'adoptados': adoptados})

def galeria(request):
    PerriDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    PerriRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    PerriAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'Perris/galeria.html',{'PerriDisponibles': PerriDisponibles, 'PerriAdoptados': PerriAdoptados ,'PerriRescatados': PerriRescatados})


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

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message = "Te has identificado correctamente"
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render_to_response('login.html', {'message': message, 'form': form},
                                context_instance=RequestContext(request))

#Log Required

@login_required
def adopta(request):
    if request.method == "POST":
        form = AdoptarForm(request.POST)
        if form.is_valid():
            Adoptar = form.save(commit=False)
            Adoptar.save()
            return redirect('perritos_disponibles')
    else:
        form = AdoptarForm()
    return render(request, 'Perris/adopta.html',{'form': form})


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...

@login_required
def perritos_disponibles(request):
    PerriDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    return render(request, 'Perris/galeriaDisponible.html', {'PerriDisponibles': PerriDisponibles})

def perritos_rescatados(request):
    PerriRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    return render(request, 'Perris/galeriaRescatado.html', {'PerriRescatados': PerriRescatados})

def perritos_adoptados(request):
    PerriAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'Perris/galeriaAdoptado.html', {'PerriAdoptados': PerriAdoptados})

@login_required
def detalle_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    return render(request, 'Perris/detalle_perro.html',{'adoptado': adoptado})

@login_required
def adoptar_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    if request.method == "POST":
        form = AdoptadoForm(request.POST, instance=adoptado)
        if form.is_valid():
            adoptado = form.save(commit=False)
            adoptado.save()
            return redirect('galeria')
    else:
        form = AdoptadoForm(instance=adoptado)
    return render(request, 'Perris/adoptar_perro.html', {'form': form, 'adoptado': adoptado})

