print ('|' + '\u203E' * 40 + '|')
print ('|  Lojinha AÇAIAÇU do Rodrigo Alcantara  |') #Print de boas-vindas
print ('|' + '_' * 40 + '|')
print ('|' + ' ' * 40 + '|')
print ('| TAMANHO |   AÇAÍ (AC)   | CUPUAÇU (CP) |') #Print cardápio
print ('|    P    |   R$ 11,00    |   R$ 09,00   |')
print ('|    M    |   R$ 16,00    |   R$ 14,00   |')
print ('|    G    |   R$ 20,00    |   R$ 18,00   |')
print ('|' + '_' * 40 + '|')
conta = 'sim'
total = 0
while conta == 'sim': #Looping para verificar mais pedidos
    while True: #Looping para escolher apenas açai ou cucuaçu
        sabor = input('Por favor, escolha (AC) para açaí ou (CP) para cuapuaçu:\n') #Escolha de produto
        if (sabor != 'AC') and (sabor != 'CP'): #Verifica se escolheu AC ou CP
            print('Sabor inválido. Tente novamente!')
            continue
        while True: #Looping para escolher apenas P M G
            tamanho = input('Por favor, escolha (P)equeno, (M)édio ou (G)rande:\n') #Escolha de produto
            if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
                break
            else:
                print('Tamanho inválido. Tente novamente!')
        break
#Calculo para AC
    if sabor == 'AC':
        if tamanho == 'P':
            total += 11
        elif tamanho == 'M':
            total += 16
        else:
            total += 20
#Calculo para CP
    elif sabor == 'CP':
        if tamanho == 'P':
            total += 9
        elif tamanho == 'M':
            total += 14
        else:
            total += 18
    print('Deseja pedir mais alguma coisa?')
    print('Digite sim para adicionar mais pedidos ou digite qualquer outra coisa para fechar a conta.') #Verifica se deseja adicionar mais pedidos
    conta = input('')
print (f'Total da sua compra é: R${total:.2f}'.replace('.',',') + '.') #Total acumulado da compra