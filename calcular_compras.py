print('=======  MINHA LISTA DE COMPRAS   =======')
carteira = float(input('Digite o valor que você tem para comprar: R$'))
totpreco = 0
resp = 's'
extrato = ''
restante = 0
while 's' in resp or carteira <= 0:
    print('='*30)
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('Valor do produto: R$'))
    quat = int(input('Digite a quantidade: '))
    resp = str(input('Quer continhuar? ')).strip().lower()
    totpreco += preco * quat
    restante = carteira - totpreco
    extrato = (f'Você colocou no carrinho total R$ {totpreco:.2f}\n'
               f'Seu saldo atual é de {restante:.2f}')
    print('='*20)
    print(extrato)

    if restante <= 0:
        break

if restante <= 0:
     print('Você não tem dinheiro suficiente para compras todos os itens adicionado')
     print('Por favor. Tire alguns itens do carrinho.')
     
else:
    print('Finalize a compra no caixa')
