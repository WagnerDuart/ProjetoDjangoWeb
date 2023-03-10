# **<p align = center> Trabalho Django WEB**

## **Grupo: Wagner Santos - Stephen Barreto **

---

## <p align = center>Versão da linguagem de programação deste projeto.

Para a criação deste projeto é necessário possuir o **Python 3.9** ou superior instalado no seu computador para instalar [click aqui](https://www.python.org/downloads/).

Também será necessário o editor de código **Visual Studio Code** que pode ser baixado [clicando aqui](https://code.visualstudio.com/).

---

# <p align = center>**Criando um projeto com o Django**

Para utilizar o django no projeto iremos criar uma nova pasta que conterá o projeto e dentro desta pasta máquina virtual `venv` para o python.

---

## **Passo 1:** Criando uma máquina virtual `python` para o projeto.

### **O terminal usado foi o `Windows PowerShell`.**

_Observação: Neste exemplo o nome da pasta que será usado é **ProjetoDjangoWeb**._

Dentro da nova pasta criada abra-a no terminal e execute o comando para criar uma máquina virtual venv.

```powershell
    python -m venv  nomedoambientevirtua
```

**Exemplo no Terminal:**

```powershell
   PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb>   python -m venv DjangoWeb
```

**Saída na Criação do Ambiente Virtual:**

```powershell
    Não conseguir visualizar a saída no terminal
```

Após o comando dentro da pasta haverá criado uma nova pasta chamada **nomedoambientevirtua**.

```bash
    📦ProjetoDjangoWeb
     ┗ 📁DjangoWeb
```

Ativando a máquina virtual:

```powershell
    nomedoambientevirtua\scripts\activate
```

Exemplo no Terminal:

```
    PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb> ..DjangoWeb\scripts\activate
```

_Saída na Ativação do Ambiente Virtual:_

```
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb>
```

---

## **Passo 2:** Instalação do framework Django.

Instalando o Django para o projeto.

No terminal digite:

```powershell
    pip install django
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb>pip install Django

```

**Saída Instalação Django:**

```powershell
   Collecting Django==4.1.7
  Using cached Django-4.1.7-py3-none-any.whl (8.1 MB)
Collecting tzdata
  Using cached tzdata-2022.7-py2.py3-none-any.whl (340 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.3-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.6.0-py3-none-any.whl (23 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-4.1.7 asgiref-3.6.0 sqlparse-0.4.3 tzdata-2022.7

```

---

## **Passo 3:** Criando o Projeto Django.

Para iniciar um projeto Django será necessário digitar no terminal o comando:

```powershell
    django-admin startproject nomedoprojeto
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb>  django-admin startproject projetoBlog
```

**Saída da Criação Projeto Django**

Na pasta **ProjetoDjangoWeb** será criado uma nova pasta com o nome indicado:

```bash
    📦ProjetoDjangoWeb
     ┣ 📁 projetoBlog
     ┗ 📁 DjangoWeb
```

Abra o pasta projetoBlog no Visual studio code:
Exemplo

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb> cd .\projetoBlog\
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> code .
```

Tela que aparecerá ao iniciar o Visual Studio code:

![](images/iniprojeto.png)

---

## **Passo 4:** Configurando o Python no Visual Studio code.

Aperte a tecla F1 do teclado e procure “Selecionar Interpretador” e clique nele.

![](images/interpretador.png)

Selecione o python da pasta DjangoWeb do projeto e ative ele como interpretador.

---

## **Passo 5:** Testando projeto.

No terminal verifique se está na pasta projetoBlog, se sim digite o comando para executar o projeto:

```powershell
   python manage.py runserver
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py runserver
```

No terminal aparecerá o ip no qual está sendo executado exemplo: http://127.0.0.1:8000/
Ao clicar nesta tela será direcionado para a página inicial de um projeto django.

![](images/inidjango.png)

Na saída do terminal apareceu que:

<code style="color:red">
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    March 08, 2023 - 14:56:55
    Django version 4.1.7, using settings 'projetoBlog.settings'
    Starting development server at http://127.0.0.1:8000/
</code>

Para parar a execução CTRL - C ou CTRL-BREAK, ser não tiver o BREAK no seu teclado execute FN-CTRL-B

---

## **Passo 6:** Migrando os apps padrões.

Para efetuar as migrações, no terminal digite o comando:

```powershell
  python manage.py migrate
```

**Exemplo no Terminal:**

```powershell
  (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py migrate
```

**Saída da Migração dos Apps Padrões:**

```powershell
  Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

---

## **Passo 7:** Criando um novo app.

Nesse passo vamos criar um novo app para o projeto chamado blog. Para isso no terminal vamos digitar o comando:

```powershell
   python manage.py startapp nomedoapp
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py startapp blog
```

Na pasta **projetoBlog** será criado uma nova pasta com o nome indicado:

```bash
     📁 projetoBlog
     ┗ 📁 blog
          ┣ 📁 migrations
          ┣ 📜 __init__.py
          ┣ 📜 admin.py
          ┣ 📜 app.py
          ┣ 📜 models.py
          ┣ 📜 tests.py
          ┗ 📜 views.py
```

---

## **Passo 8:** Criação do modelo de tabela para o banco de dados.

No visual studio code abra a pasta blog e abra para editar o arquivo **models.py**
Neste arquivo vamos criar uma classe Post, que definirá os campos da tabela que armazenará os posts no banco de dados.
Digite o seguinte código para a criação desta classe:

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # Titulo do post.
    title = models.CharField(max_length=255)
    # Slug será a Url do post.
    slug = models.SlugField(max_length=255, unique=True, auto_created=title)
    # Autor do post.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Texto do post
    body = models.TextField()
    # Data de criação do post
    created = models.DateTimeField(auto_now_add=True)
    # Data de atualização do post.
    update = models.DateTimeField(auto_now=True)
```

Após ter adicionado essa classe vá na pasta **projetoBlog/projetoBlog** e selecione o arquivo settings.py

```bash
     📁 projetoBlog
     ┣ 📁 blog
     ┗📁 projetoBlog
          ┗ 📜 settings.py
```

Na linha 32 em **INSTALLED_APPS** adicione o blog: ‘blog.apps.BlogConfig’:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig', # Adicione o blog
]
```

Criando o arquivo de migrate, no terminal digite o comando:

```powershell
  python manage.py makemigrations blog
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py makemigrations blog
```

**Saída da Criação do Arquivo Migrate:**

```powershell
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
```

---

## **Passo 9:** Migração do blog para o sql.

No terminal digite o comando para migrar o blog:

```powershell
   python manage.py sqlmigrate blog 0001
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py sqlmigrate blog 0001
```

**Saída da Migração do Blog**

```powershell
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("slug" varchar(255) NOT NULL UNIQUE, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "body" text NOT NULL, "created" datetime NOT NULL, "update" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
```

Aplicando o migrate digite o comando:

```powershell
  python manage.py migrate blog
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py migrate blog
```

**Saída da Aplicação do Migrate**

```powershell
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
```

A tabela foi criada no banco de dados.

## **Passo 10:** Criando um usuário administrador(super admin).

No terminal digite este comando para criar um usuário administrador:

```powershell
  python manage.py createsuperuser
```

**Exemplo no Terminal:**

```powershell
   (DjangoWeb) PS C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog> python manage.py createsuperuser
```

Será pedido o nome de usuário, senha e email, todos os campos devem ser preenchidos:

```powershell
Username (leave blank to use 'wagne'): admin@user.com
Email address: admin@user.com
Password:
Password (again):
Superuser created successfully.
```

Para testar esse usuário inicie o server usando o comando `python manage.py runserver` e acesse o endereço localhost/admin exemplo: http://127.0.0.1:8000/admin

![](images/admin.png)

Após logar verá a tela do administrador:

![](images/confgadmin.png)

Para mudar o idioma da página, na linha 105 do `settings.py` mude o `'en-us'` para `'pt-br'`, as páginas ficaram em portugues do brasil.

Na tela de administrador você poderá criar grupos e adicionar usuários ao banco de dados.

---

## **Passo 11:** Adicionado Post para alteração na tela de admin.

Vá ate o arquivo `blog\admin.py` nele escreva o seguinte código:

```python
from django.contrib import admin

from .models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug":("title",)}
```

Dando F5 na página admin estará com uma nova opção para adicionar Posts:

![](images/confgadminpost.png)

Podendo adicionado novos posts com os campos definidos no **Passo 8**:

![](images/criacaopost.png)

Adicione um método a `class Post` para definir o nome dos post adicionados igual ao título dos mesmos:

```python
def __str__(self):
        return self.title
```

---

## **Passo 12:** Criando as Views.

Abra o arquivo blog\views.py nele vamos importar as classes `DetailView` e `ListView`, abaixo vamos importar nossa classe `Post`.
Então criaremos duas classes que herdam de `DetailView` e `ListView`, como no código abaixo:

```python
from django.views.generic import DetailView, ListView
from .models import Post

class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post
```

Agora só temos que ligar está view a uma urls para isso vamos criar um arquivo `.py` dentro da pasta blog ficando `projetoBlog\blog\urls.py`.
Dentro deste arquivo será escrito o seguinte código:

```python
from django.urls import  path
from . import views

app_name = "blog"

urlpatterns = [
   # Link que será usado na tela inicial do blog.
    path("", views.PostListView.as_view(), name="list"),
   # Link usando os slugs de cada post, para vê-los.
    path("<slug:slug>/", views.PostDV.as_view(), name="detail"),
]
```

Agora vamos alterar o arquivo `urls.py` dentro da pasta `projetoBlog`, então temos que: `projetoBlog\urls.py`, o codigo deste arquivo ficará:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
```

Agora será necessário criar os templates `.html`.

---

## **Passo 13:** Criando os Templates.

Dentro da pasta blog vamos criar uma pasta `template` e dentro desta uma `blog` e dentro da blog `post_list.html` e um base.html, como abaixo:

```bash
  📁 projetoBlog
  ┣ 📁 blog
  +  ┣ 📁 templates
     +  ┗📁 blog
          ┣ 📜 base.html
          ┗ 📜 post_list.html
```

No arquivo `base.html` vamos escrever o código:

```html
<!DOCTYPE html>
<head>
    <title>{% block title%}{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Projeto WEB - Blog</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

O arquivo `post_list.html` herdará a estrutura do `base.html`, com o código abaixo::

```html
{% extends "blog/base.html" %} 

{% block title %}Blog usando Django{% endblock %}

{% block content %} 
    {% for post in post_list %}
        <article class="artigolist">
          <h2>{{ post.title }}</h2>
          <p class="data">Publicado em {{post.created}} por {{ post.author }}</p>
          {{ post.body|linebreaks|truncatewords:9 }}
        </article>
    {% endfor %} 
{% endblock %}
```

Criando o html que estará um post só, na mesma pasta criaremos um arquivo `post_detail.html` com o seguinte conteúdo:

```bash
  📁 projetoBlog
  ┣ 📁 blog
  +  ┣ 📁 templates
     +  ┗📁 blog
          ┣ 📜 base.html
          ┣ 📜 post_detail.html
          ┗ 📜 post_list.html
```

**post_detail.html:**

```html
{% extends "blog/base.html" %}

{% load static %} {% block title %}Blog usando Django - {{ post.title }}{% endblock %} 

{% block content %}
    <article>
        <h2>{{ post.title }}</h2>
        <p class="data">Publicado em {{ post.created }} por {{ post.author }}</p>
        {{ post.body|linebreaks}}
    </article>
{% endblock %}
```

---

## **Passo 14:** Adicionado o link ao clicar em um post.

No arquivo model será alterado a `class Post`, vamos importar a classe reverse e adicionar um método a class, a class ficando assim:

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # Titulo do post.
    title = models.CharField(max_length=255)
    # Slug será a Url do post.
    slug = models.SlugField(max_length=255, unique=True, auto_created=title)
    # Autor do post.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Texto do post
    body = models.TextField()
    # Data de criação do post
    created = models.DateTimeField(auto_now_add=True)
    # Data de atualização do post.
    update = models.DateTimeField(auto_now=True)

    class meta: # Definindo a ordem do último post para o primeiro.
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
```

Agora vamos mudar o arquivo `post_list.html` e adicionar um link para os posts completos:

```html
{% extends "blog/base.html" %} 

{% block title %}Blog em Django{% endblock %} 

{%block content %}
    {% for post in post_list %}
        <article class="artigolist">
            <h2>
              <a href="{{ post.get_absolute_url }}"> 
                  {{ post.title }} 
              </a>
            </h2>
            <p class="data">Publicado em {{post.created}} por {{ post.author }}  
            </p>
            {{ post.body | linebreaks | truncatewords:9 }}
        </article>
    {% endfor %} 
{% endblock %}
```

Com isso só iniciar o server e colocar /blog no link ficando: `http://127.0.0.1:8000/blog` e ao clicar aparecera está tela com os posts adicionados, para adicionar entre na tela de admin e adicione os posts:

![](images/listblogpost.png)

e ao clicar no título é redirecionado ao post:

![](images/blogpost.png)

—

## **Passo 14:** Adicionado o css para as páginas.

No arquivo `base.html` vamos adicionar o link para um arquivo css, então vamos mudar o html para o seguinte:

```html
{% load static %}

<!DOCTYPE html>
<head>
    <title>{% block title%}{% endblock %}</title>
    <link href="{% static 'css/blog.css' %}" rel="stylesheet">
</head>
<body>
    <header>
        <h1>Projeto WEB - Blog</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>

```

Após isso vamos criar uma pasta com o css na pasta `meuBlog/blog`, será criado uma pasta static/css/blog.css

```bash
     📁 projetoBlog
     ┣ 📁 blog
      +  ┣ 📁 templates
         ┣ 📁 static
          + ┗ 📁 css
               ┗ 📜 blog.css
```

No `blog.css` será adicionado este código:

```css
body {
  margin-left: 3vw;
  margin-right: 3vw;
  text-align: center;
}

h1 {
  text-align: center;
}

.artigo {
  margin-top: 2vh;
  background-color: #eff3f0;
  border-radius: 10px;
  margin-bottom: 2vh;
  margin-right: auto;
  min-width: 400px;
  width: auto;
  margin-left: auto;
  max-width: 600px;
  padding: 10px;
  box-shadow: 5px 5px 10px black;
}

h2 {
  font-weight: bold;
}
.date {
  font-style: italic;
  color: #303134;
}

article {
  margin-left: auto;
  margin-right: auto;
  min-width: 400px;
  width: 60%;
  color: #15262e;
}
```

# **Resultado do projeto:**

Para acessar os sites inicie o servidor com o comando

```powershell
    python manage.py runserver
```

**Saída :**

```powershell
Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
?: (staticfiles.W004) The directory 'C:\Users\Wagne\OneDrive\Documentos\ProjetoDjangoWeb\projetoBlog\static\css' in the STATICFILES_DIRS setting does not exist.

System check identified 1 issue (0 silenced).
March 09, 2023 - 23:58:56
Django version 4.1.7, using settings 'projetoBlog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## **No navegador acesse o blog com: http://127.0.0.1:8000/blog**

Nesta página conterá os posts que foram adicionados pelos usuários como por exemplo o `admin`, exemplo com alguns posts adicionados:

![](images/listblogpost.png)

---

E ao clicar no título de um post será redirecionado para a
tela que mostra um post, no qual seu link é automático através do slug:

![](images/blogpost.png)

## Créditos

Vídeo do youtuber School of Net [Clique para acessar](https://youtu.be/eK2sfDWQUXc).

Vídeo do youtuber Leonardo Lourenco [Clique para acessar](https://youtu.be/aadiQA8cBAg).
