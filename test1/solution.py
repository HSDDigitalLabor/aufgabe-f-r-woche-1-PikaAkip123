print("Hallo, Welt!")


# print (name)

def print_name(name):
    if name == 'Ole' or name == 'ole' :
        print('Schön dich zu sehen',name)
    else:
        print('Hallo', name, 'Du bist neu hier')

while True:
    vorname = input ('Wie ist dein Name?')                      # Wartet auf Benutzereingabe
    if vorname == 'q' or vorname == 'Q' :
        break
    print_name(vorname)