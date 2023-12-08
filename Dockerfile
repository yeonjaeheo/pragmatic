FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/yeonjaeheo/pinterest.git

WORKDIR /home/pragmatic/

RUN pip3 install -r requirements.txt

RUN echo "SECRET_KEY=3i-#68nv6=groj32ss!x%7ti@1nx+#25usagic0w5ft9u=_h-*" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
