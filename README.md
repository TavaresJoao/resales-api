# resales-api

REST API for Imobiliarias and Imoveis Registry

## Requirements
- docker

or

- django
- djangorestframework
- postgresql
- psycopg2

## Run the API

### Setup
- ensure that postgres is running - if you don't use docker
- makemigrations - with and without docker: `docker-compose run resalespoc python manage.py makemigrations`; `python manage.py makemigrations`.
- migrate - with and without docker: `docker-compose run resalespoc python manage.py migrate`; `python manage.py migrate`.

### Run Server
If docker is installed:

```bash
docker-compose up
```

, otherwise:

```bash
python manage.py runserver
```

## HOW TO

### List

Imobiliaria:

```bash
curl http://localhost:8080/api/imobiliaria/
```

Imovel:

```bash
curl http://localhost:8080/api/imovel/
```

### Add

Imobiliaria:

```bash
curl -XPOST http://localhost:8080/api/imobiliaria/ --data '{"name": "Antares", "email": "antares@email.com", "phone": "+55 11 1234-5678", "other_information": "colocar algo aqui"}' --header "Content-Type: application/json"
```

Imovel:

```bash
curl -XPOST http://localhost:8080/api/imovel/ --data '{"address": "Av Djalama Batista, N 803, Adrianópolis, Manaus - AM 69080-97", "description": "colocar algo aqui", "value": "350000", "sold": false, "imobiliaria": 1}' --header "Content-Type: application/json"
```

### Edit

Imobiliaria:

```bash
curl -XPUT http://localhost:8080/api/imobiliaria/1/ --data '{"name": "Antares", "email": "antares@email.com", "phone": "+55 11 1234-5679", "other_information": "update"}' --header "Content-Type: application/json"
```

Imovel:

```bash
curl -XPUT http://localhost:8080/api/imovel/1/ --data '{"address": "Av Djalama Batista, N 803, Adrianópolis, Manaus - AM 69080-97", "description": "update - vendida", "value": "350000", "sold": true, "imobiliaria": 1}' --header "Content-Type: application/json"
```

### Remove

Imobiliaria:

```bash
curl -XDELETE http://localhost:8080/api/imobiliaria/1/
```

Imovel:

```bash
curl -XDELETE http://localhost:8080/api/imovel/1/
```
