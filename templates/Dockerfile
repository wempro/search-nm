FROM python:3.11.3
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install net-tools
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install -U setuptools
RUN pip install -r requirements.txt
COPY ./ /code/
RUN ls -la /code/*
RUN touch /code/env.txt
RUN printenv > /code/env.txt
#RUN python manage.py
ENTRYPOINT ["python", "manage.py", "runserver", "127.0.0.1:56872"]
