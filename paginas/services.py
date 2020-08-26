import json
import requests


def get_item():
    response = requests.get("http://localhost:8000/api/item")
    comments = json.loads(response.content)
    lista = {'product': comments}
    return lista


def get_user():
    response = requests.get("http://localhost:8000/api/user")
    comments = json.loads(response.content)
    lista = {'user': comments}
    return lista


def get_note():
    response = requests.post("http://localhost:8000/api/note")
    comments = json.loads(response.content)
    lista = {'note': comments}
    return lista


def insert_cliente(name, document):
    dados = {"name": name, "document": document}
    response = requests.post("http://localhost:8000/api/user", json=dados)
    return response.status_code


def insert_produto(product, description, cost):
    dados = {"product": product, "description": description, "cost": cost}
    response = requests.post("http://localhost:8000/api/item", json=dados)
    return response.status_code



def insert_note(user, date):
    dados = {"user": user, "total_cost": 0.0, "date": date}
    response = requests.post("http://localhost:8000/api/note", json=dados)
    comments = json.loads(response.content)
    lista = {'note': comments}
    return lista['note']

def insert_noteitem(note, item, cost, amount):
    dados = {"note": note, "item": item, "cost": cost, "amount": amount}
    response = requests.post("http://localhost:8000/api/rota", json=dados)
    return response.status_code


def update_note(id, user, total_cost, date):
    dados = {"user": user, "total_cost": total_cost, "date": date}
    response = requests.put(f'http://localhost:8000/api/update/{int(id)}')
    return response.status_code

def list(id):
    response = requests.get(f'http://localhost:8000/api/list/{int(id)}')
    comments = json.loads(response.content)
    lista = {'note': comments}
    return lista

