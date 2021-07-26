import time
# ======================= FUNÇÃO DE TEMPORIZADOR =======================
def timer(numero, frase):
    time.sleep(numero)
    print(frase)

# ======================= APRESENTAÇÃO =================================

print('===========')
print('Adivinhação')
print('===========')

# ======================= INSTRUÇÃO ====================================

timer(2, 'O objetivo desse programa é adivinhar o número que VOCÊ pensar, dentro do limite dado:')
timer(2, ' - O número que você pensar deve ser ACIMA ou IGUAL à 1 (um)')
timer(2, ' - O número que você pensar deve ser ABAIXO ou IGUAL ao número que você determinar:')

# -------- Intervalo de números possíveis que o usuario pensará --------
min = 1
max = int(input('\n  * Digite um número que determinará o limite máximo --> '))

timer(2, '\nPense em um número de 1 a {}'.format(max))
timer(2, '- Você tem 5 segundos...')

timer(5, '- Já pensou?')
timer(2, '- Ótimo, vamos lá!')
timer(2, '\nVocê vai responder apenas se: ')

print('===================================================================')
print(' Meu chute está CERTO\n Meu chute está ALTO \n Meu chute está BAIXO')


# -------- FEEDBACK DO USUÁRIO --------
chute_alto  = 'A'
chute_baixo = 'B'
correto = 'C'

#-------- CONDIÇÕES --------
acertou = False
tentativa = 1

# ================================== LÓGICA ==========================================
while acertou == False:

    print('===================================================================')
    timer(5, ' "A" para CHUTE ALTO \n "B" para CHUTE BAIXO \n "C" para CHUTE CERTO \n \n EM CAPS LOCK!')

    palpite = round((max + min) / 2)
    print('\n TENTATIVA {}'.format(tentativa))
    feedback = input('Seu número é {}? --> '.format(palpite))

    if feedback == correto:
        print('Eba! Acertei em {} tentativas'.format(tentativa))
        acertou = True
    else:
        if feedback == chute_baixo:
            min = palpite + 1
        elif feedback == chute_alto:
            max = palpite - 1

        tentativa = tentativa + 1
