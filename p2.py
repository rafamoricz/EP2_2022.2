import random

print('='*70)
print('\033[35mOlá, você está no Fortuna DesSoft, onde poderá se tornar milionario!\033[m\n')

nome = input('Qual seu nome? ')
print('-'*60,'\nOk \033[36m{0}\033[m, você poderá pular 3 vezes e terá 2 ajudas!\n'.format(nome.upper()))
print('\033[34mAs opções de resposta são "A","B","C","D","ajuda","pular" e "parar"\033[m\n')
continuar = input('Aperte \033[32mENTER\033[m para continuar...')

facil = 'FACIL'
medio = 'MEDIO'
dificil = 'DIFICIL'
nivel = [facil,medio,dificil]

qt_quest = [1,2,3,4,5,6,7,8,9,10]

print('-'*60,'\nO jogo está para começar! E aqui está a primeira questão!\n\nVamos começar com questoes do nivel \033[32m{0}\033[m!'.format(nivel[0]))
continuar = input('Aperte \033[32mENTER\033[m para continuar...')

lista_questoes = {
  "facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
      "nivel": "dificil",
      "opcoes": {
        "A": "Autogamia",
        "B": "Esporulação",
        "C": "Partenogênese",
        "D": "Divisão binária"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}

def sorteia_questao(lista_questoes,nivel):
    for q in lista_questoes:
        if q.upper() == nivel[0]:
            lista = lista_questoes[q]
            pergunta = random.choice(lista)
    return pergunta

#print(sorteia_questao(lista_questoes,nivel))
pergunta = sorteia_questao(lista_questoes,nivel)

def questao_para_texto(pergunta,qt_quest):
    for i in pergunta:
        if i == 'titulo':
            titulo = pergunta[i]
        if i == 'opcoes':
            op = pergunta[i]
            for alt in op:
                if alt == 'A':
                    a = op[alt]
                elif alt == 'B':
                    b = op[alt]
                elif alt == 'C':
                    c = op[alt]
                else:
                    d = op[alt]
    questao = '-'*60,'\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}'.format(qt_quest[0],titulo,a,b,c,d)
    return questao

print(questao_para_texto(pergunta,qt_quest))