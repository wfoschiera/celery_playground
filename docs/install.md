# Short intro
Stack:
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

TODOS:
  [ ] Fix CI/CD
  [ ] Fix Dockerfile conf
  [ ] Write about basic conf in celery_settings.