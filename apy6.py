jatos={
    'marca1':'Tiger II',
    'marca2':'B-2 Spirit',
    'marca3':'F-35 Lightning II'
}

modelo=input()
if modelo in jatos:
    print('há modelos dessa caça disponivel')
else:
    print('não há disponivel')