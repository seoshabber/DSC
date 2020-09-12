class cafe_de_link:
    def __init__(self, charge=0, calorie=0, count=0):
        self.__count=count
        self.__charge=charge
        self.__calorie=calorie
    def sell(self):
        if self.__count > 0:
            self.__count = self.__count - 1
            print('남은 수량은 {0}개 입니다.'.format(self.__count))
        else:
            self.__count = 0
            print('선택하신 음료의 잔여 수량이 0입니다. 선택하신 음료를 판매할 수 없습니다.')

    def getcount(self):
        return self.__count
    def getcharge(self):
        return self.__charge
    def getcalorie(self):
        return self.__calorie



mocha=cafe_de_link(5000, 330, 5)

latte=cafe_de_link(4000, 165, 7)

caramel_macchiato=cafe_de_link(5000,430,8)

user='in'
print('챗봇> 환영합니다. 여기는 cafe_de_link입니다.')
while user == 'in':
    print('◆'*30)
    print('★'*10+' cafe_de_link 메뉴판 '+'★'*10)
    print('1. 라떼 {0}원/{1}칼로리/잔여수량 : {2}' .format (latte.getcharge(), latte.getcalorie(),latte.getcount()))
    print('2. 모카 {0}원/{1}칼로리/잔여수량 : {2}' .format (mocha.getcharge(), mocha.getcalorie(), mocha.getcount()))
    print('3. 카라멜 마끼야토 {0}원/{1}칼로리/잔여수량 : {2}' .format (caramel_macchiato.getcharge(), caramel_macchiato.getcalorie(), caramel_macchiato.getcount()))
    print('4. 나가기\n'+'◆'*30)
    choice = int(input('챗봇> 원하시는 메뉴는? : '))
    if choice == 1:
        print('라떼를 주문하셨습니다.')
        latte.sell()
    elif choice == 2:
        print('모카를 주문하셨습니다.')
        mocha.sell()
    elif choice == 3:
        print('카라멜 마끼야토를 주문하셨습니다.')
        caramel_macchiato.sell()
    elif choice == 4:
        user='out'
        print('이용해주셔서 감사합니다.')