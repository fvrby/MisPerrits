from django.contrib import admin
from .models import Post
from .models import Adoptar, Adoptado

admin.site.register(Post)
#adoptar y adoptados
admin.site.register(Adoptar)
admin.site.register(Adoptado)
