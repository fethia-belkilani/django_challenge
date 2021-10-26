# Django REST API

REST API using Django python3

## Installation steps:
- create a virtualenv 

```bash
virtualenv env
```
- clone the GIt repository fron Github into script directory
- activate the virtualenv
```bash
cd env\script\activate
```

- install requirements.txt
```bash
pip install -r requirements.txt
```
- run the server

```bash
python manage.py runserver
``` 



## API endpoints:


- create a new printer ==>  POST: http://localhost:8000/api/v1/printer/create/
- get list of printers ==> GET: http://localhost:8000/api/v1/printer
- update a printer ==>PUT: http://localhost:8000/api/v1/printer/update/id/
- delete a printer ==>DELETE: http://localhost:8000/api/v1/printer/delete/id/



## Author
Fethia belkilani
