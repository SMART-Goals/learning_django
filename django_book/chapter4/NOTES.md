Inject the web-page into the view generator function, instead of embedding the page in the view.
This way we separate the HTML source from the python source.

- template variables: `{{ a_name }}`
- template tag:
  + `{% if bool_var %}}`...`{% else %}`...`{% endif %}`
  + `{% for item in list_var %}`...`{{ item }}`...`{% endfor %}`
- filter tag:
  + `date` filter, e.g. `{{ ship_date|date:"F j, Y" }}`
  
The Django templates can be used as a python module to templatize any text file.  
Templates cannot be interpreted unless we load the settings.py module, though. Thus, we
need to invoke `python manage.py shell` to start an interactive python session where the
settings.py file has been loaded.

When the template system encounters a dot in a variable name, it tries the following lookups,
in this order:  
- Dictionary lookup (e.g., `foo["bar"]`)
- Attribute lookup (e.g., `foo.bar`)
- Method call (e.g., `foo.bar()`)
- List-index lookup (e.g., `foo[2]`)

There are a myriad of tags and filters, as well as magic variable `forloop`.

If you add `mysite` as one of the apps installed in file _settings.py_, like this:
```python
INSTALLED_APPS = [
    'mysite',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

_and_ place your templates within directory `mysite/templates/`, then function `get_template()` will
find your template files within that directory when setting `'APP_DIRS'` to `True` in the `TEMPLATES`
setting:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```