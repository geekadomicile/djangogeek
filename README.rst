Used command-line
-----------------
    ::

        $ mkdir djangogeek
        $ cd djangogeek
        $ python3 -m venv myvenv
        $ cd myvenv
        $ . bin/activate
        $ pip install --upgrade pip
        $ pip install Django
        $ django-admin startproject mysite
        $ cd mysite
        $ vim mysite/settings.py
        # amend LANGUAGE_CODE = 'fr-fr'
        # amend TIME_ZONE = 'Europe/Paris'
        # amend STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        # amend ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
        $ python manage.py migrate
        $ python manage.py startapp purchases
        $ vim mysite/settings.py
        # amend INSTALLED_APPS = [..., purchases,]
        $ vim purchases/models.py
        $ python manage.py makemigrations purchases
        $ python manage.py migrate purchases
        $ vim purchases/admin.py
        $ python manage.py createsuperuser
        $ vim purchases/views.py
        $ cd ../..
        $ git init
        $ git config --global user.name "Yevgueny KASSINE"
        $ git config --global user.email ykassine@geekadomicile.com
        $ vim .gitignore
        # amend with :
        #    *.pyc
        #    *~
        #    __pycache__
        #    myvenv
        #    db.sqlite3
        #    /static
        #    .DS_Store
        $ git add --all
        $ git status
        $ git remote add origin https://github.com/geekadomicile/djangogeek.git
        $ git commit -am "Init"
        $ git push -u origin master
        $ cd myvenv/mysite/
        $ vim mysite/urls.py
        # amend 
        #    from django.conf.urls import include
        #    urlpatterns = [..., url(r'', include('purchases.urls')),]
        $ vim purchases/urls.py

