#### Blog w Django

I. Dokumentacja - [Django Girls](https://tutorial.djangogirls.org/pl/)

II. Uwagi  
- każdą czynność zrealizowaną wpisujemy do punktu nr III wraz z użytą komendą, np.  
```bash
python manage.py makemigrations
```
- wymagane konto na [Python Anywhere](https://www.pythonanywhere.com/),  
- proszę o utworzenie nazwy użytkownika na Python Anywhere, takiej jak na Discordzie,  

III. Kolejne kroki
- tworzymy folder roboczy dla naszego projektu, np. `blog-django-girls`,  
- utworzenie środowiska wirtualnego, nazwa środowiska powinna zawierać nr albumu lub nick z Discorda:  
```bash
python3 -m venv env_potoczko
```
- aktywacja środowiska wirtualnego:  
```cmd
env_potoczko\Scripts\activate
```
- po aktywacji środowiska wracamy do folderu roboczego, czyli `blog-django-by-girls`
- robimy screenshot z aktywnym środowiskiem wirtualnym i wrzucamy jako obrazek do README, np.  
![venv](venv-screenshot.png)

- dodajemy nazwę śrowiska wirtualnego do pliku `.gitignore`:  
```bash
# .gitignore
env_potoczko/
```
- pip install django

- django-admin.exe startproject mysite .

- python manage.py startapp blog

- add blog to mysite/settings.py installed apps section

- blog/models.py
```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

- python manage.py makemigrations blog

- python manage.py migrate blog

- edit blog/admin.py

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
- python manage.py runserver

- python manage.py createsuperuser

- python manage.py migrate

- log in at  http://127.0.0.1:8000/admin/

- log into PythonAnywhere, make an account and make API token

- create a bash console and ```run pip3.8 install --user pythonanywhere```

- pa_autoconfigure_django.py --python=3.8 https://github.com/LobsterLobsterski/ISI.git (a log in may be necessary)

- wait until it does everything

- something broke, i imagine its the fact that ISI repo is not just Lab2. Can be bothered to fix it, i can't be bothered creating a repo for every lab for this subject -> no deployment

- mysite/urls.py
```python
"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```
-blog/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```
- blog/views.py
```python
from django.shortcuts import render
def post_list(request):
    return render(request, 'blog/post_list.html', {})
```
- create /blog/templates/blog/post_list.html
- blog/templates/blog/post_list.html
```HTML
<!DOCTYPE html>
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <header>
            <h1><a href="/">Django Girls Blog</a></h1>
        </header>

        <article>
            <time>published: 14.06.2014, 12:14</time>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </article>

        <article>
            <time>published: 14.06.2014, 12:14</time>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </article>
    </body>
</html>
```

- if deployment works, git commit, git push and then git pull on the server console

- blog/views.py
```python
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

- replace <article>s with in the template
```html
{% for post in posts %}
    <article>
        <time>published: {{ post.published_date }}</time>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </article>
{% endfor %}
```









