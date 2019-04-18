# Django project template

[![Join the chat at https://gitter.im/django-project-template/community](https://badges.gitter.im/django-project-template/community.svg)](https://gitter.im/django-project-template/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

###### python, django 

Whether it be an API Development project or Web development or a hybrid this template can help you get kick-started in seconds.

All settings are configured in such a way that changing a single variable IS_TESTING will shift your project to production mode

## Assumptions
1. You use MySQL in production and PostgreSQL in local testing
2. Static files are served by server in production and by django in testing

### Point 1
Clone it and change the django_project_template -> your_project_name

### Point 2
master app has basic models to save and retrieve keys dynamically
If you would like to keep it makemigrations and migrate as follows
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Point 3
helper app views has a class Helper which contains all staticmethods which are repeatedly used all over the project

### Point 4
fcm_notification.py has code to send firebase notifications

### Point 5
sms has code to send messages via msg91 api

# Scope
There are many things that can be improved here.

1. Code Style
2. Alternate or better structure for a django project
3. Down the line this base setup must to be usable for any type of django project. Maybe a script that does that?

PR's are most welcome \ (•◡•) /

