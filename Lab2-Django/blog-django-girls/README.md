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



