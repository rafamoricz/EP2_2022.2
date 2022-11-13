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

opcoes = ["A",'a',"B",'b',"C",'c',"D",'d',"ajuda","pular","parar"]
pulos = [2,1,0]
ajudas = [1,2]

premio = ['1000','5000','10000','30000','50000','100000','300000','500000','1000000']

qt_quest = [1,2,3,4,5,6,7,8,9]

print('-'*60,'\nO jogo está para começar! E aqui está a primeira questão!\n\nVamos começar com questoes do nivel \033[32m{0}\033[m!'.format(nivel[0]))
continuar = input('Aperte \033[32mENTER\033[m para continuar...')

def transforma_base(questoes):
    niveis = {}
    for questao in questoes:
        nivel = questao['nivel']
        if nivel not in niveis:
            niveis[nivel] = []
        niveis[nivel].append(questao)
    return niveis
    
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
def valida_questao(questao):
    # Inicializa o dicionário de retorno
    retorno = {}
    # Verifica se as chaves titulo, nivel, opcoes e correta estão na questão
    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao:
        retorno['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao:
        retorno['opcoes'] = 'nao_encontrado'
    if 'correta' not in questao:
        retorno['correta'] = 'nao_encontrado'
    # Verifica se a questão (dicionário principal) tem exatamente quatro chaves
    if len(questao) != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    # Verifica se a chave titulo existe e se o titulo está vazio ou contém apenas espaços / caracteres em branco
    if 'titulo' in questao and questao['titulo'].strip() == '':
        retorno['titulo'] = 'vazio'
    # Verifica se a chave nivel existe e se o nivel contém um dos valores facil, medio ou dificil
    if 'nivel' in questao and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        retorno['nivel'] = 'valor_errado'
    # Verifica se a chave opcoes existe e se todas as opções A, B, C e D existem (e nada além disso)
    if 'opcoes' in questao and set(questao['opcoes'].keys()) != {'A', 'B', 'C', 'D'}:
        retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
    # Verifica se a chave opcoes existe e se o valor da chave opcoes tem exatamente quatro chaves
    if 'opcoes' in questao and len(questao['opcoes']) != 4:
        retorno['opcoes'] = 'tamanho_invalido'
    # Verifica se a chave correta existe e se o valor da chave correta é uma das opções A, B, C ou D
    if 'opcoes' in questao and len(questao['opcoes']) == 4 and set(questao['opcoes'].keys()) == {'A', 'B', 'C', 'D'}:
        for opcao in questao['opcoes']:
            if questao['opcoes'][opcao].strip() == '':
                if 'opcoes' not in retorno:
                    retorno['opcoes'] = {}
                retorno['opcoes'][opcao] = 'vazia'
    # Verifica se a chave correta existe e se o valor da chave correta é uma das opções A, B, C ou D
    if 'correta' in questao and questao['correta'] not in ['A', 'B', 'C', 'D']:
        retorno['correta'] = 'valor_errado'
    return retorno
def sorteia_questao(lista_questoes,nivel):
    repetida = []
    for q in lista_questoes:
        if q.upper() == nivel[0]:
            lista = lista_questoes[q]
            pergunta = random.choice(lista)
            if pergunta not in repetida:
                repetida.append(pergunta)
        elif q.upper() == nivel[1]:
            lista = lista_questoes[q]
            pergunta = random.choice(lista)
            if pergunta not in repetida:
                repetida.append(pergunta)
        else:
            lista = lista_questoes[q]
            pergunta = random.choice(lista)
            if pergunta not in repetida:
                repetida.append(pergunta)
    return pergunta

#print(sorteia_questao(lista_questoes,nivel))

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

for j in range(0, len(qt_quest)):
    pergunta = sorteia_questao(lista_questoes,nivel[0])
    print(questao_para_texto(pergunta,qt_quest[j]))

    resposta = input('Qual a sua resposta? ')
    while resposta not in opcoes:
        print('\033[30mOops! Resposta inválida! Tente de novo\033[m')
        print('\033[34mAs opções de resposta são "A","B","C","D","ajuda","pular" e "parar"\033[m\n')
        resposta = input('Qual a sua resposta? ')
    
    for i in pergunta:
        if i == 'correta':
            if resposta.upper() == pergunta[i]:
                print('\033[32mPARABENS!, Você possui agora R${0}!\033[m\n'.format(premio[j]))
                if premio[j] == '1000000':
                    print('\033[32mMEUS PARABENS! Você se tornou o novo milionário!\033[m')
            elif resposta == 'pular':
                pulos = 2
                while pulos != 0:
                    print('OK, você só tem mais {0} pulos!'.format(pulos))
                    pulos-=1
                    continuar = input('Aperte \033[32mENTER\033[m para continuar...')
                if pulos == 0:
                    print('Voce nao tem mais pulos!')
                    pergunta = sorteia_questao(lista_questoes,nivel)
                    print(questao_para_texto(pergunta,qt_quest[j]))

                pergunta = sorteia_questao(lista_questoes,nivel)
                print(questao_para_texto(pergunta,qt_quest[j]))
            else:
                print('\033[33mAh não! Você errou a resposta, infelizmente terá que sair sem nunhum prêmio! :(\033[m\n')
                quit()

    continuar = input('Aperte \033[32mENTER\033[m para continuar...')
<<<<<<< HEAD
=======

def transforma_base():
    questoes = []

def valida_questao():
    chaves = {}

def valida_questoes():
    lista = []

def sorteia_questao_inedita():
    q = {}

def questao_para_texto():
    representacao = {}
    i = 0

