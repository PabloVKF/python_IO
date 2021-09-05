import csv
import pickle
import json
from contato import Contato
from abc import ABC, abstractmethod


def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for row in leitor:
            id_contato, nome, email = row

            contato = Contato(id_contato, nome, email)
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)


def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_dict)


def _contato_para_dict(contato):
    return contato.__dict__


def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            # '**contato' é iquivalente a 'id=contato['id'], nome=contato['nome'], email=contato['email']'
            c = Contato(**contato)
            contatos.append(c)

    return contatos


'''
Daqui para baixo foi um exemplo de refazer o código seguindo os padores de projeto DAO.
Criando uma classe especifica para cada domínio (ContatoDaoJson, ContatoDaoPickle, ContatoDaoCSV, ContatoDaoSQL...) 
todas erdando a class ContatoDao.
'''

'''
Segundo o professor Yuri: 
    "O DAO é um padrão de projeto muito utilizado por quem busca um meio de acessar seus dados. Popularmente, ele é 
    muito utilizado para acessar o banco de dados e realizar as operações de criação, busca, exclusão e atualização. 
    Além disso, ele pode ser utilizado para salvar e recuperar dados em arquivos[...]"
'''


class ContatoDao(ABC):

    @abstractmethod
    def buscar_todos(self, caminho):
        pass

    @abstractmethod
    def salvar(self, contatos, caminho):
        pass


class ContatoDaoJason(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        contatos = []

        with open(caminho, mode='r') as arquivo:
            contatos_json = json.load(arquivo)

            for contato in contatos_json:
                # '**contato' é iquivalente a 'id=contato['id'], nome=contato['nome'], email=contato['email']'
                c = Contato(**contato)
                contatos.append(c)

        return contatos

    def salvar(self, contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(contatos, arquivo, default=lambda objeto: objeto.__dict__)
