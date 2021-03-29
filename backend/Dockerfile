FROM python:3.9

WORKDIR /backend

# disable writing pyc to disc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1



# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend