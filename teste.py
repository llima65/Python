month = int(input('Digite um numero entre 1 e 12 para ver o mês: '))

months_dict = {0:'January', 1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11:'December'}
c =0
for c in months_dict:
    c += 1
    if month == 1:
        print(months_dict[0])
        break
    elif month == 2:
        print(months_dict[1])
        break
    elif month == 3:
        print(months_dict[2])
        break
    elif month == 4:
        print(months_dict[3])
        break
    elif month == 5:
        print(months_dict[4])
        break
    elif month == 6:
        print(months_dict[5])
        break
    elif month == 7:
        print(months_dict[6])
        break
    elif month == 8:
        print(months_dict[7])
        break
    elif month == 9:
        print(months_dict[8])
        break
    elif month == 10:
        print(months_dict[9])
        break
    elif month == 11:
        print(months_dict[10])
        break
    elif month == 12:
        print(months_dict[11])
        break
    else:
        print('Opção inválida!')
        break
    