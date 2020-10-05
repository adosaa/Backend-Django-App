#############################
# Docker project container
# Authored by: Ariel Saavedra
#############################

FROM python:3.8.3-alpine

# File Author / Maintainer
LABEL maintainer="Ariel Saavedra"

# Setting enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV appDir /usr/src/app

WORKDIR ${appDir}

# Create app directory
RUN mkdir -p ${appDir}

# Add an alias to the python manage.py command inside the container
RUN echo 'alias dj="python manage.py"' >> ~/.bashrc

# Update, Install dependencies and install psycopg2
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

## Add and Install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

## Add app
COPY . ./

RUN chmod +x ./entrypoint.sh

EXPOSE 8080

ENTRYPOINT [ "./entrypoint.sh" ]

CMD python manage.py run -h 0.0.0.0
