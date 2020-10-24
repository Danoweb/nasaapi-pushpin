FROM python:3
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development
ENV FLASK_APP=index.py

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/

RUN pip install -r requirements.txt
COPY . /src  
CMD ["python", "/src/index.py"]