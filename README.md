# Journal
Just a small project to keep up with Django, Docker, and Nginx

# TODO
- Revise Unit Tests
- Clean-up UI
  - base layout
  - forms for add/edit/delete

- Make a production ready branch
  - add in extra configurations to settings.py
  - force settings.py to read sensitive environment variables from os.environ()
  - switch over to nginx, or apache2
  - switch over to postgresql

# TODO - Extras
- add in a docker config
  

# Quick Setup with Venv
1. python3 -m venv venv
2. . venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py test
7. python manage.py runserver 0:8080

