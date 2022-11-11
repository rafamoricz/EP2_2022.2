import random

print('='*70)
print('\033[35mOlá, você está no Fortuna DesSoft, onde poderá se tornar um milionario!\033[m')
print('='*70,'\n')

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
    repetida = []
    for q in lista_questoes:
        if q.upper() == nivel[0]:
            lista = lista_questoes[q]
            pergunta = random.choice(lista)
        if pergunta not in repetida:
            repetida.append(pergunta)
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
    print('-'*60,'\n\033[36mQUESTAO {0}\033[m\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}'.format(qt_quest,titulo,a,b,c,d))
    return ''

for j in len(qt_quest):
    print(questao_para_texto(pergunta,qt_quest[j]))

    resposta = input('Qual a sua resposta? ')
    for i in pergunta:
        if i == 'correta':
            if resposta.upper() == pergunta[i]:
                print('\033[32mPARABENS!, Você possui agora R$1000.00!\033[m\n')
            else:
                print('\033[33mAh não! Você errou a resposta, infelizmente terá que sair sem nunhum prêmio! :(\033[m\n')
                quit()

    continuar = input('Aperte \033[32mENTER\033[m para continuar...')

def transforma_base():
    questoes = []

def valida_questao():
    chaves = {}