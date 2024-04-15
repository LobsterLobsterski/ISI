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