import random
import uuid
from datetime import datetime

def formated(v):
    if type(v) == str:
        return f'\"{v}\"'
    else:
        return str(v)

with open('servidor.txt', 'a') as file:
    file.write('INSERT INTO "sefit_servidor" ("mat","nome","sexo","email") VALUES \n')

name = ["Sr. Davi Sanches Barreto Neto","Sr. Marcos Gustavo Rico","Srta. Cristina Stella Cortês","Sr. Tomás Vinícius Meireles","Dr. Teobaldo Vicente Cordeiro","César de Oliveira Jr.","Sr. Adriano Ávila Sobrinho","Emily Galindo Grego Filho","Sra. Yohanna Faro Neto","Alessandra das Dores Matos Jr.","Dr. Samanta Campos Filho","Sr. Guilherme Andres Abreu Jr.","Paulo Brito Pereira","Matheus Fidalgo Jr.","Wellington Beltrão Neto","Ian Juan Godói Neto","Dr. Lucio Juan Godói","Késia Gusmão Ferraz","Srta. Clarice Lilian Salas","Franco Fabiano Brito","Dr. João Gilberto Valentin","Iasmin Lira Jr.","Srta. Paloma Santana","Aurora Padrão Serna","Ian Galindo Valentin","Sra. Débora Cruz","Sr. Manuel das Neves Sobrinho","Srta. Naiara Rezende Benez","Dr. Paulo Diogo Escobar","Edilson Uchoa Martines Filho","Marina Molina","Dr. Victor de Arruda Rodrigues","Srta. Ohana Clarice Benez","Ícaro Raphael Pereira Jr.","Madalena Tatiane Ferreira","Srta. Olga Benez Carmona Sobrinho","Dr. Luiz Salgado Toledo Filho","Estela Karine Flores Neto","Mariah Teles","Dr. Isis Sueli da Silva","Raphael Franco Filho","Josué Roberto Azevedo","Paulo Lovato","Ítalo Francisco Arruda","Danielle da Cruz","Dr. Renan Aaron Fidalgo","Karine Aragão Ramires","Thiago Leal Soto","Nicolas Leandro Leon","Franco Cervantes","Emilly Tábata Lozano Sobrinho","Vitória Quintana Escobar Filho","Maya Flor Batista Jr.","Valentin Lovato Soto","Nathalia Suzana Galvão Filho","Srta. Hortência Caroline Fidalgo","Sra. Adriele Pedrosa Dias Filho","Lilian Esteves Jimenes","Eunice Guerra Carvalho","Marcelo Théo Flores Sobrinho","Reinaldo Dener Valência Sobrinho","Mirella Gusmão","Dr. Marco Martines","Dr. Heitor Ferreira Neto","Srta. Heloise Betina Saito Filho","Sra. Ariana Suellen Sales","Victor Barros","Dr. Erik de Souza Jr.","Dr. Ivan Aranda","Arthur Lira Jr.","William Espinoza","Srta. Marina Santiago Neto","Sr. Mateus Azevedo Sobrinho","Luiza Casanova Jr.","Srta. Clara Amaral Queirós","Danielle Regiane Brito","Sr. Sebastião Benez Neto","Dr. Tiago Maldonado","Sr. Diego Gustavo Ortiz Jr.","Clarice Camila Soares Sobrinho","Sra. Abgail Montenegro","Taís Pérola Santos Sobrinho","Sr. Igor Fábio Marinho","Srta. Joana Toledo Neto","Felipe Cortês","Alana Maia Filho","Clarice Uchoa Lourenço","Dr. Théo Simão Jimenes","Renato Franco Bonilha","Reinaldo Maldonado Brito","Sr. Allan Flores Colaço","Dr. Franco das Dores Delatorre Neto","Sr. Adriel Furtado Ávila Sobrinho","Melina Serna da Silva Jr.","Sandro Willian Assunção Sobrinho","Srta. Laiane Ortega","Constância Regiane Soares","Sr. Wagner Benedito Leon Jr.","Alonso David Solano Neto","Sra. Pérola Laís Carmona"]

def randomEmail(name):
    name = ''.join(name.split(' '))
    name = name[0:10]
    dom = random.choice(['@gmail.com','@yahoo.com'])
    return f'{name}@{dom}'

for _ in range(100):
    line = [
        uuid.uuid4().int & (1<<20)-1,
        random.choice(name),
        random.choice(['m','f']),
        randomEmail(random.choice(name)),
    ]
    with open('servidor.txt', 'a') as file:
        file.write('(')
        file.write(','.join([formated(l) for l in line]))
        file.write(')')
        file.write(',\n')

with open('servidor.txt', 'a') as file:
    file.write('\n COMMIT;')