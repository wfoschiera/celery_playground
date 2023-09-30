# Short intro
## Stack:
- Poetry
- Taskipy
- Django
- Celery
- RabbitMQ
- Redis

## Basic setup

In this project we use poetry as the default dependency manager. So, to setup your venv and install all dependencies is simple as run:  
```bash
poetry install
```

## Aliases  
We also use Taskipy to avoid repeating long commands in bash and keep track of the most useful commands. To see all commands available:  
```bash
poetry run task --list
```

## Using existing code demonstration  
The best way to test Celery capabilities with django is to use django shell. A better shell for django is provided with the django-extensions package (already included).   
Another tip is to use Ipython instead of native Python compiles. Ipython, another other advantages, offer a build in autocomplete, autoimport for django models and better erros messages.  
Since we are lazy, just run this command:
```python
poetry run task djshell
```
If it all just works, you will see something like this:
```bash
Python 3.11.0 (main, Aug 15 2023, 08:39:45) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.
```
And your prompt will looks like:
```console
In [1]: 
```
Now, you can try to execute some code:
```python
from demo_app.basic_canvas import signature_example

signature_example()

>>> tasks.add(2, 2)
>>> demo_app.tasks.add(2, 2)
>>> demo_app.tasks.add(2, 2)
```

## Real-time tasks monitoring using Flower
[Docs](https://flower.readthedocs.io/en/latest/features.html)
```bash
poetry run task flower
```
### Flower monitoring:  
http://localhost:5555/


### Prometheus /metrics:  
http://localhost:5555/metrics


__TODOS__:  
- [ ] Fix CI/CD  
- [ ] Fix Dockerfile conf  
- [ ] Write about basic conf in celery_settings.  