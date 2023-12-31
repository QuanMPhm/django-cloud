# Builds basic django app with Mozilla OpenID enabled

FROM python:3.11-alpine

COPY django_requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY ./django_src /django_src

EXPOSE 8000

CMD ["python",  "./django_src/manage.py", "runserver", "0.0.0.0:8000"]