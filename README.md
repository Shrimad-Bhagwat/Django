<div align="center" >

<h1> Django Guide</h1>

<p float="left">
  

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

</p>

### [Django Documentation](https://docs.djangoproject.com/en/3.2/topics/)

</div>

### Contents
- [Django Setup](#1-django-setup)
- [First App](#2-first-app)
- [Django Template Language](#3-django-template-language)

---
## 1. [Django Setup](#1-django-setup)
Python installation required.
### Install Virtual Environment
  ```
  pip install virtualenv
  ```
  
### Activate Virtual Environment
  ```
  ./env/Scripts/activate
  ```

### Install django using pip
  ```
  pip install django
  ```

### Confirm django installation
  ```
  django-admin --version
  ```

### Creating Project
```
django-admin startproject djangoproject
```

`cd djangoproject`

```
djangoproject
  |__ djangoproject
  |     |__ init.py
  |     |__ asgi.py
  |     |__ settings.py
  |     |__ urls.py
  |     |__ wsgi.py
  |__ manage.py
```

### Starting the Development Server
```
python manage.py runserver
```

**Result :**

```
Django version 3.2.6, using settings 'djangoproject.settings'
Starting development server at http://127.0.0.1:8000/        
Quit the server with CTRL-BREAK.
```

> The development server is live at 
**http://127.0.0.1:8000/**

To Stop the Server
 **CTRL + C** 

![Django Successful](./images/django-successful.png)

---
## 2. [First App](#2-first-app)

### Create a New App
```
python manage.py startapp myapp
```
It will create a new app in the Project Directory named `myapp`

```
djangoproject
  |__ djangoproject
  |__ myapp
  |     |__ init.py
  |     |__ admin.py
  |     |__ apps.py
  |     |__ models.py
  |     |__ tests.py
  |     |__ views.py
  |__ manage.py
```
After creating a new app we have to create a new file in it called `urls.py`. It will store all the urls of this app.

### Adding urls
We have to include this file's urls in the project's urls file.

> djangoproject / **djangoproject / urls.py**
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('myapp.urls'),
]
```

Now we need to add new urls in the `urls.py` file of `myapp`.

> djangoproject / **myapp / urls.py**
```
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'), 
] 
```

In this file we have imported views.
And created a path for Home page.

### Creating views

**Now we have to create view for this path in the `views.py`**

> djangoproject / **myapp / views.py**
```
from django.shortcuts import render
rom django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1>")> 
```

Save all the files and open **http://127.0.0.1:8000/**

![First-App](images/first-app.png)

## **Congratulations! You have created your first Django App**

---

### **How do we get this ?**
Django will first search for `home` or `''` url in the urls.py of the project folder i.e. djangoproject.
`path('', include('myapp.urls'),`

It says to search for the url in `myapp/urls.py`
`path('', views.home, name='home'),`

which tells that the `''` url should goto `views.home` i.e. it should look for a function named `home` in the `myapp/views.py` 

```
def home(request):
    return HttpResponse("<h1>Hello World!</h1>")> 
```
This is the home function which returns a HttpResponse to the url `''` for `Hello World`.

---
## 3. [Django Template Language](#3-django-template-language)

### Creating templates folder
```
mkdir templates
```

```
djangoproject
  |__ djangoproject
  |__ myapp
  |__ templates
  |__ manage.py
```

### Adding templates

Create a file `Home.html`
And add the following 

```

<h1>Hello World. This is Home.html</h1>
```
In the `djangoproject/djangoproject/settings.py` add the templates folder in the `DIRS`.

```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
    },
]
```

Now modify your `djangoproject/myapp/views.py`

```
def home(request):
    return render(request, 'Home.html')
```
It will now render a template named `Home.html` from `templates` folder at the Home or `''` url.

Save all the files and open **http://127.0.0.1:8000/**

![Home-Template](images/home-tempate.png)

### Dynamic Content

Now instead of this static content we want to pass values to Home.html dynamically. 

In the `djangoproject/myapp/views.py` pass values using `{}` a Dictionary as follows.

```
def home(request):
    return render(request, 'Home.html',{'name' : "Shrimad"})
```

And in the `templates/Home.html`
```
<h1>Hello {{name}}</h1>
```
add `{{name}}` to show the passed value here.

Save all the files and open **http://127.0.0.1:8000/**

![Dynamic-Name](images/dynamic-name.png)

In this way we can fetch data from the database and pass it in the html file.

### Adding Base Template

In the `templates` folder create a file named `base.html` and add the following html code.

```
<html lang="en">
<head>
    <title>{% block title %}  {% endblock title %}</title>
</head>
<body bgcolor='lightblue'>
    {% block content %}
    
    {% endblock content %}
</body>
</html>
```

In this file the `{% block ___ %}` and `{% endblock ___ %}` are used to insert the data from another html file inside these blocks.

Example : 

Let the background color of the base template be `bgcolor='lightblue'`.

Now in the `home.html` add 
```
{% extends 'base.html' %}

{% block title %}
Django Home
{% endblock title %}

{% block content %}
<h1>Hello {{name}}</h1>
{% endblock content %}
```

The `{% extends 'base.html' %}` will extend the base file.

The data inside  `{% block title %}` will be sent to the block title of the `base.html`.

Similarly the data inside `{% block content %}` will be sent to the block content of the `base.html`.

Save all the files and open **http://127.0.0.1:8000/**

![Base Template](images/base-template.png)

The `base.html` file with blue background and the content from `home.html`.