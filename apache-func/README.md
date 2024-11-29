Criar imagem:
docker build -t python-apache-flask . 

Criar container:
docker run -p 8080:80 python-apache-flask

Para ver:
http://127.0.0.1:8080/