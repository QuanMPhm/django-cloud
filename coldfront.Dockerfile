# Builds basic coldfront app

FROM python:3.11-alpine

COPY coldfront_requirements.txt /requirements.txt
COPY ./coldfront_src/coldfront_config.py ./coldfront_config.py

RUN pip3 install -r requirements.txt

RUN printf "yes\n" | coldfront initial_setup 

RUN printf "admin\n\nadmin\nadmin" | coldfront createsuperuser

EXPOSE 7000

CMD ["coldfront", "runserver", "0.0.0.0:7000"]
# CMD ["sleep", "9999"]