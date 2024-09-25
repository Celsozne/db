# Feito por Celso Augusto Machado Junior

from pymongo import MongoClient
from faker import Faker
import random

client = MongoClient('localhost', 27017)
db = client['loja']
collection = db['coisas']

fake = Faker('pt_BR')

def novo_produto():
    return {
        'nome': fake.word().capitalize() + ' ' + fake.word().capitalize(),
        'preco': fake.text(max_nb_chars=100),
        'estoque': random.randint(1, 100),
        'data': fake.date_time_this_year(),
    }

    coisa= [novo_produto() for _ in range(150)]
    collection.insert_many(coisa)

    print("Produtos inseridos com sucesso")