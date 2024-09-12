import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from movieapp.models import Filme

def populate():
    filmes = [
        {'titulo': 'O Senhor dos Anéis', 'genero': 'Fantasia', 'premiado': True, 'ano_de_lancamento': 2001},
        {'titulo': 'Matrix', 'genero': 'Sci-Fi', 'premiado': False, 'ano_de_lancamento': 1999},
        {'titulo': 'A Espera de um Milagre', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 1999},
        {'titulo': 'A Origem', 'genero': 'Ação', 'premiado': True, 'ano_de_lancamento': 2010},
        {'titulo': 'O Clube da Luta', 'genero': 'Drama', 'premiado': False, 'ano_de_lancamento': 1999},
        {'titulo': 'Pulp Fiction', 'genero': 'Crime', 'premiado': True, 'ano_de_lancamento': 1994},
        {'titulo': 'O Poderoso Chefão', 'genero': 'Crime', 'premiado': True, 'ano_de_lancamento': 1972},
        {'titulo': 'Forrest Gump', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 1994},
        {'titulo': 'Interstellar', 'genero': 'Sci-Fi', 'premiado': True, 'ano_de_lancamento': 2014},
        {'titulo': 'Os Infiltrados', 'genero': 'Crime', 'premiado': True, 'ano_de_lancamento': 2006},
        {'titulo': 'Coringa', 'genero': 'Crime', 'premiado': True, 'ano_de_lancamento': 2019},
        {'titulo': 'O Grande Lebowski', 'genero': 'Comédia', 'premiado': False, 'ano_de_lancamento': 1998},
        {'titulo': 'Gladiador', 'genero': 'Ação', 'premiado': True, 'ano_de_lancamento': 2000},
        {'titulo': 'O Silêncio dos Inocentes', 'genero': 'Terror', 'premiado': True, 'ano_de_lancamento': 1991},
        {'titulo': 'Cidade de Deus', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2002},
        {'titulo': 'Parasita', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2019},
        {'titulo': 'O Labirinto do Fauno', 'genero': 'Fantasia', 'premiado': True, 'ano_de_lancamento': 2006},
        {'titulo': 'O Exorcista', 'genero': 'Terror', 'premiado': False, 'ano_de_lancamento': 1973},
        {'titulo': 'O Pianista', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2002},
        {'titulo': 'A Vida é Bela', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 1997},
        {'titulo': 'O Aviador', 'genero': 'Biografia', 'premiado': True, 'ano_de_lancamento': 2004},
        {'titulo': 'Os Vingadores', 'genero': 'Ação', 'premiado': False, 'ano_de_lancamento': 2012},
        {'titulo': 'A Rede Social', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2010},
        {'titulo': 'O Lobo de Wall Street', 'genero': 'Comédia', 'premiado': False, 'ano_de_lancamento': 2013},
        {'titulo': 'Mad Max: Estrada da Fúria', 'genero': 'Ação', 'premiado': True, 'ano_de_lancamento': 2015},
        {'titulo': 'Django Livre', 'genero': 'Western', 'premiado': True, 'ano_de_lancamento': 2012},
        {'titulo': 'O Grande Hotel Budapeste', 'genero': 'Comédia', 'premiado': True, 'ano_de_lancamento': 2014},
        {'titulo': 'O Artista', 'genero': 'Comédia', 'premiado': True, 'ano_de_lancamento': 2011},
        {'titulo': 'O Fabuloso Destino de Amélie Poulain', 'genero': 'Comédia', 'premiado': False, 'ano_de_lancamento': 2001},
        {'titulo': 'Os Caça-Fantasmas', 'genero': 'Comédia', 'premiado': False, 'ano_de_lancamento': 1984},
        {'titulo': 'Jurassic Park', 'genero': 'Aventura', 'premiado': False, 'ano_de_lancamento': 1993},
        {'titulo': 'O Hobbit', 'genero': 'Fantasia', 'premiado': True, 'ano_de_lancamento': 2012},
        {'titulo': 'Brilho Eterno de uma Mente Sem Lembranças', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2004},
        {'titulo': 'O Segredo de Brokeback Mountain', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2005},
        {'titulo': 'O Homem que Mudou o Jogo', 'genero': 'Drama', 'premiado': False, 'ano_de_lancamento': 2011},
        {'titulo': 'O Leitor', 'genero': 'Drama', 'premiado': True, 'ano_de_lancamento': 2008},
        {'titulo': 'O Menino do Pijama Listrado', 'genero': 'Drama', 'premiado': False, 'ano_de_lancamento': 2008},
        {'titulo': 'O Náufrago', 'genero': 'Drama', 'premiado': False, 'ano_de_lancamento': 2000},
        {'titulo': 'A Culpa é das Estrelas', 'genero': 'Drama', 'premiado': False, 'ano_de_lancamento': 2014},
        {'titulo': 'Her', 'genero': 'Romance', 'premiado': True, 'ano_de_lancamento': 2013},
        {'titulo': 'O Jogo da Imitação', 'genero': 'Biografia', 'premiado': True, 'ano_de_lancamento': 2014},
       
    ]

    for filme in filmes:
        f, created = Filme.objects.get_or_create(**filme)

        if f:
            print(f'Filme "{f.titulo}" ja existe')

if __name__ == '__main__':
    populate()
