#Setup for windows compatability
import pathlib
import os
import json
import time
proj_folder = pathlib.Path(f'{os.getcwd()}\{__file__}').parent.parent

#Script to clear screen
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#Locate json sequencer data and loads it
json_loc = str(f'{proj_folder}\config\sequencerdata.json')
json_file = open(json_loc, 'r')
json_pure = str(json_file.read(500))
seq_data = json.loads(json_pure)

#Script to build sequence
def seq_builder(beatsort, counter):
    screen_clear()
    print (seq_data[str(beatsort)])
    if counter < len(seq_data[str(beatsort)]):
        inputtext = f'Voer de waarde in van noot nummer {counter + 1} kies uit (k(ick), s(nare), h(i-hat) of x (leeg), of type <- om terug te gaan'
        note = input(inputtext)
        if note != '<-':
            if note != '':
                seq_data[str(beatsort)][counter] = note
                counter += 1
                seq_builder(beatsort, counter)
            else:
                seq_data[str(beatsort)][counter] = seq_data[str(beatsort)][counter]
                counter += 1
                seq_builder(beatsort, counter)
        else:
            counter -= 1
            seq_builder(beatsort, counter)
    else:
        with open(json_loc, 'w') as f:
            json.dump(seq_data, f)

beatsort = input('Welke maatsoort wil je veranderen? Kies uit 3, 4, 5 ')
counter = 0
if beatsort == '3' or beatsort == '4' or beatsort == '5':
    amt = 4 * int(beatsort)
    seq_builder(beatsort, counter)
