# Setup for windows compatability
import os
import datetime
import sequencer
import sequencer_config

# Script to clear screen
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

dagdeel = ''

tijd = datetime.datetime.now()
if tijd.hour <= 4:
    dagdeel = 'nacht'
elif tijd.hour > 4 and tijd.hour <= 12:
    dagdeel = 'morgen'
elif tijd.hour > 12 and tijd.hour <= 18:
    dagdeel = 'middag'
elif tijd.hour > 18 and tijd.hour <= 23:
    dagdeel = 'navond'
else:
    dagdeel = 'nacht'

def keuze_menu():
    screen_clear()
    keuze_tekst = f'Goede{dagdeel}, welkom bij mijn mooie sequencer.\nOm door te gaan moet je een keuze maken, wil je een nieuwe sequence genereren/schrijven of wil je de huidig opgeslagen sequence afspelen en opslaan? \nKies hier uit "schrijven", "spelen" of "sluiten" om dit programma te sluiten. \n'
    keuze = input(keuze_tekst)
    screen_clear()
    if keuze.isalpha():
        if keuze == 'spelen':
            sequencer.sequencer_init()
            keuze_menu()
        elif keuze == 'schrijven':
            sequencer_config.beat_edit_init()
            keuze_menu()
        elif keuze == "sluiten":
            exit()
        else:
            print('Deze keuze bestaat op het huidige moment helaas nog niet')
            input("Press Enter to continue...")
            keuze_menu()
    else:
        print('Deze keuze bestaat op het huidige moment helaas nog niet')
        input("Press Enter to continue...")
        keuze_menu()


screen_clear()
keuze_menu()