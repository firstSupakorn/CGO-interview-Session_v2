# Base Image
FROM python:3.6

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/
COPY requirements.txt /
RUN pip install -U pip \
    && pip install -r /requirements.txt

EXPOSE 9999
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:9999" ]
