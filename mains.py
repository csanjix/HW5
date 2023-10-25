from decouple import config
from logic import play_bet

balance = config("MY_MONEY", cast=int)

while True:
    bet = int(input(f'Сколько вы хотите поставить? (баланс: {balance})'))
    lot = int(input(f'Лот на который вы хотите поставить (1-30)'))
    if bet < 1 or bet > balance:
        print('Неправильная сумма ставки')
        continue
    if lot < 1 or lot > 30:
        print('Неправильный лот')
        continue
    balance += play_bet(bet, lot)
    if balance == 0:
        print('Вы бомж')
        break
    answer = input('Вы хотите продолжить? (Y/N)')
    if answer == 'N':
        print('До свадания приходите еще')
        break