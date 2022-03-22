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
tentativa = 1

# ================================== LÓGICA ==========================================
while True:

    print('===================================================================')
    timer(2, ' "A" para CHUTE ALTO \n "B" para CHUTE BAIXO \n "C" para CHUTE CERTO \n ')

    palpite = round((max + min) / 2)
    print(f'\n TENTATIVA {tentativa}')
    feedback = input(f'Seu número é {palpite}? --> ').upper()

    if feedback == correto:
        print(f'Eba! Acertei em {tentativa} tentativas')
        break
    else:
        if feedback == chute_baixo:
            min = palpite + 1
        elif feedback == chute_alto:
            max = palpite - 1

        tentativa += 1
