import easygui

easygui.msgbox('Welcom to buy lunch ticket!\n(Lunch : 11:00 - 15:00)')
cho='start'
fee=0
while cho != 'Exit':
    cho=easygui.buttonbox('Choose lunch menu to buy',choices=['Korean dish','Western dish','Chinese\'s style','Japanese','Exit'])
    if cho == 'Korean dish':
        many = easygui.integerbox('%s is 2500 won.\nHow many tickets do you want to buy?'%cho)
        fee += many*2500
    elif cho == 'Western dish':
        many = easygui.integerbox('%s is 3000 won.\nHow many tickets do you want to buy?'%cho)
        fee += many*3000
    elif cho =='Chinese\'s style':
        many = easygui.integerbox('%s is 2000 won.\nHow many tickets do you want to buy?'%cho)
        fee += many*2000
    elif cho == 'Japanese':
        many = easygui.integerbox('%s is 3500 won.\nHow many tickets do you want to buy?'%cho)
        fee += many*3500
    elif cho== 'Exit':
        easygui.msgbox('Total amount to pay : %d\nThanks for using!'%fee)
    
