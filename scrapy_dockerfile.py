FROM python:3.11.4
WORKDIR /code

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "scraping/go-spider.py"]