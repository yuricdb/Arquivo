#talvez seja necessário trocar/alterar as duas "contra barras" (isso depende do SO)

import os #necessário apenas para utilizar a função q mostra os diretórios(apesar de varrer manualmente com for).

def inicio(nomeUser):
    vPasta = 0
    endSO = 'C:\\Users\\'+nomeUser+'\\AppData\\Local\\Programs\\Python\\Python37\\'
    cam = os.listdir(endSO)
    for ex in cam:
        if 'tempEx' == ex:
            vPasta += 1
    if vPasta == 0:
        endSO = 'C:\\Users\\'+nomeUser+'\\AppData\\Local\\Programs\\Python\\Python37\\tempEx\\'
        os.mkdir(endSO)
        return endSO
    return endSO+'tempEx\\'

def registro():
    nome = input('Digite o nome do animal: ')
    raca = input('Digite a raça do animal: ')
    lugar = input('Onde o animal foi perdido? ')
    animal = (nome, raca, lugar)
    return animal

def excluir(remove):
    cont = 0
    for i in lista:
        if i[0] == remove:
            del(lista[cont])
        cont += 1

def checaArq(checa):
    
    caminho = acesso
    cam = os.listdir(acesso)
    for i in cam:
        if checa+'.txt' == i:
            sobre = input('Arquivo existente\ndeseja sobrescrever? [s/n]\n')
            if sobre == 'n':
                prox = 0
                z = 1
                while (z>0):
                    z = 0
                    for i in cam:
                        confere = checa+str(prox)+'.txt'
                        if confere == i:
                            z += 1    
                    prox += 1    
                caminho += checa+(str(int(prox-1))+'.txt')
                return caminho
    caminho += checa+'.txt'
    return caminho

def leArq():
    print('Todos os seus dados temporários não salvos serão perdidos!\n')
    tupla = ()
    caminho = acesso 
    cam = os.listdir(acesso)
    for i in cam:
        if 'txt' in i :
            tm = (len(i)-4)
            print('arquivo: ', i[:tm])
    carrega = input('\nDigite o nome do arquivo que deseja carregar\n')
    if carrega == '':
        print('Você não digitou um nome de arquivo válido')
        return ''
    leCaminho = caminho+carrega+'.txt'
    print(leCaminho, '\nArquivo carregado\n')
    arq2= open(leCaminho, 'r')
    lista = []
    for itens in arq2:
        if itens != '\n':
            num = (len(itens)-1)
            tmp = (itens[:num],)
            tupla += tmp
        if itens == '\n':
            lista.append(tupla)
            tupla = ()
            
    arq2.close()
    return lista

print('Para a execução do programa, o python 3.7 deve estar instalado na pasta padrão de instalação padrão\n')
nomeUser = input('\nDigite o nome de usuário do seu PC: #NOME DA PASTA DO USUÁRIO WINDOWS#\n')
acesso = inicio(nomeUser)

lista = []
resp = True
while(resp != 'n'):
    opcao = int(input('\nMenu:\n\n[1]Cadastrar um novo animal\n[2]Excluir um animal existente\n[3]Exibir lista dos animais\n[4]Salvar no banco de dados\n[5]Exibir arquivos salvos\n\n'))
    if opcao == 1:
        reg = registro()
        lista.append(reg)
    elif opcao == 2:
        encontrado = input('Digite o nome do animal encontrado:\n')
        excluir(encontrado)
    elif opcao == 3:
        print(lista)
    elif opcao == 4:
        salva = input('Insira o nome que deseja salvar:\n')
        if salva == '':
            salva = 'unknown'
        temp = checaArq(salva)
        arq = open(temp, 'w')    
        for item in lista:
            for j in item:
                arq.write(j)
                arq.write('\n')
            arq.write('\n')
        arq.close()
        print('Seu arquivo foi salvo como:', temp)
    elif opcao == 5 :
        lista = leArq()
                
    resp = input('Deseja retornar ao menu inicial?\n')







        
