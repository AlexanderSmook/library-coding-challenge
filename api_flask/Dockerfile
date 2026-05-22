FROM python:3

ENV PYTHONUNBUFFERED=1
ENV USER python

ENV FLASK_DEBUG 1
ENV FLASK_APP ./app.py
ENV FLASK_ENV development

RUN useradd -m $USER && echo $USER:$USER | chpasswd && adduser $USER sudo
RUN chown $USER:$USER $HOME

WORKDIR /api

RUN apt-get update -y


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER $USER

RUN export FLASK_DEBUG=1
RUN export FLASK_APP=./app.py
RUN export FLASK_ENV=development

EXPOSE 4000

CMD [ "python3", "-m" , "flask", "run", "--debug", "--host=0.0.0.0", "--port=4000" ]