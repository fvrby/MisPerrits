from django.contrib import admin
from .models import Post

admin.site.register(Post)
#adoptar y adoptados
admin.site.register(Adoptar)
admin.site.register(Adoptado)
