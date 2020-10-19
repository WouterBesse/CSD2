# Setup for windows compatability
import pathlib
import os
import json
import random

proj_folder = pathlib.Path(__file__).parent.parent


# Script to clear screen
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# Locate json sequencer data and loads it
json_loc = str(f'{proj_folder}\config\sequencerdata.json')
json_file = open(json_loc, 'r')
json_pure = str(json_file.read(100000))
seq_data = json.loads(json_pure)

# Arrays and functions to check if the notes are legal
def drum_legality(beatsort, counter, inputtext):
    drum_legal = ['k', 's', 'h', 'xk', 'xh', 'xs', 'x', '<-', '']
    if inputtext in drum_legal:
        if inputtext == 'k':
            beatsort = f'{beatsort}k'
        elif inputtext == 's':
            beatsort = f'{beatsort}sn'
        elif inputtext == 'h':
            beatsort = f'{beatsort}h'
        else:
            return
    else:
        screen_clear()
        print('Illegale drum input')
        input("Press Enter to continue...")
        seq_builder(beatsort, counter)


def synth_legality(beatsort, counter, inputtext):
    synth_legal = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(len(inputtext))
    if inputtext != '<-' and inputtext != 'x' and len(inputtext) != 0:
        if inputtext[0].lower() in synth_legal:
            if len(inputtext) == 2 and inputtext[-1].isdigit():
                return
            elif len(inputtext) == 3 and inputtext[1] == '#' and inputtext[-1].isdigit():
                return
            else:
                screen_clear()
                print('Illegale synth input')
                input("Druk op Enter om door te gaan...")
                seq_builder(beatsort, counter)
        else:
            screen_clear()
            print('Illegale synth input')
            input("Druk op Enter om door te gaan...")
            seq_builder(beatsort, counter)

# Script to build sequence
def seq_builder(beatsort, counter):
    screen_clear()
    pointer_list = []
    n = 0
    while n < (int(beatsort) * 4):
        if n == counter:
            pointer_list.append('^')
        else:
            pointer_list.append(' ')
        n += 1
    print('Synth')
    print(seq_data[f'{beatsort}s'])
    print('Drums')
    print(seq_data[f'{beatsort}h'])
    print(seq_data[f'{beatsort}sn'])
    print(seq_data[f'{beatsort}k'])
    color_blue = '\033[34;1m'
    pointer_list_str = str(pointer_list)
    n = 0
    while n < len(pointer_list_str):
        if pointer_list_str[n] == "'" or pointer_list_str[n] == "[" or pointer_list_str[n] == "]" or pointer_list_str[n] == ",":
            pointer_list_str = pointer_list_str[:n] + ' ' + pointer_list_str[n+1:]
        n += 1
    print(f'{color_blue}{pointer_list_str}')
    note = input(f'\033[0;37mVoer de noot in van stap nummer {counter + 1}, typ help om de mogelijkheden te zien! \n')
    if note == 'help':
        screen_clear()
        print('In deze configurator pas je de tracks aan van de snare, hi-hat, kick en synthesizer. \nHierbij de legenda:\nSnare: s, snare rust = xs\nKick: k, kick rust is xk\nHi-hat: h, hi-hat rust = xh\nSynth noot: (nootnaam)(kruis of géén kruis)(octaaf nummer). Bijvoorbeeld g3, a#5, D2. Mollen zijn hier niet van toepassing. Synth rust = x\nJe kunt zien bij welke stap je bent in de message. \nOm terug te gaan in de sequence kun je "<-" invoeren, om naar de volgende stap te gaan is een enter voldoende, als je klaar bent mag je done typen.\n')
        input("Druk op Enter om door te gaan...")
        seq_builder(beatsort, counter)
    elif note == 'done':
        with open(json_loc, 'w') as f:
            json.dump(seq_data, f)
        return
    else:
        if note != '<-':
            if note != '':
                if note[0] == 'x':
                    if note[-1] == 's':
                        seq_data[str(f'{beatsort}sn')][counter] = 'x'
                        seq_builder(beatsort, counter)
                    elif note[-1] == 'x':
                        seq_data[str(f'{beatsort}s')][counter] = 'x'
                        seq_builder(beatsort, counter)
                    elif note[-1] == 'k':
                        seq_data[str(f'{beatsort}k')][counter] = 'x'
                        seq_builder(beatsort, counter)
                    elif note[-1] == 'h':
                        seq_data[str(f'{beatsort}h')][counter] = 'x'
                        seq_builder(beatsort, counter)
                elif note == 's':
                    drum_legality(beatsort, counter, note)
                    seq_data[str(f'{beatsort}sn')][counter] = note
                    seq_builder(beatsort, counter)
                elif note[-1].isdigit():
                    synth_legality(beatsort, counter, note)
                    seq_data[str(f'{beatsort}s')][counter] = note
                    seq_builder(beatsort, counter)
                else:
                    drum_legality(beatsort, counter, note)
                    seq_data[str(f'{beatsort}{note}')][counter] = note
                    seq_builder(beatsort, counter)
            else:
                if int(counter) + 1 < 4 * int(beatsort):
                    counter += 1
                    seq_builder(beatsort, counter)
                else:
                    counter = 0
                    seq_builder(beatsort, counter)
        else:
            counter -= 1
            seq_builder(beatsort, counter)


def euclidian_generator(beatsort):
    screen_clear()
    generator_list = ['k', 's', 'h']
    for i in generator_list:
        n = 1
        if i == 's':
            i = 'sn'
        euclid_counter = 1
        ran_val = random.randint(1, ((2 * int(beatsort))-1))
        while n <= (int(beatsort) * 4):
            if n == euclid_counter or n == 1:
                seq_data[str(f'{beatsort}{i}')][n-1] = i[0]
                euclid_counter += ran_val
            else:
                seq_data[str(f'{beatsort}{i}')][n-1] = 'x'
            n += 1
    print('Jouw gegenereerde beat:')
    print(seq_data[f'{beatsort}h'])
    print(seq_data[f'{beatsort}sn'])
    print(seq_data[f'{beatsort}k'])
    with open(json_loc, 'w') as f:
        json.dump(seq_data, f)
    input("Druk op Enter om door te gaan...")


# Script user input and initialisation
def beat_edit_init():
    screen_clear()
    beatsort = input('Welke maatsoort wil je veranderen? Kies uit 3, 4 of 5 vierde \n')
    counter = 0
    if beatsort.isdigit():
        if beatsort == '3' or beatsort == '4' or beatsort == '5':
            screen_clear()
            generator = input('Wil je de noten met een euclidisch algoritme genereren of handmatig aanpassen? Kies uit genereren of handmatig \n')
            if generator.isalpha():
                if generator == 'handmatig':
                    seq_builder(beatsort, counter)
                elif generator == 'genereren':
                    euclidian_generator(beatsort)
                else:
                    screen_clear()
                    print('Verkeerde input methode \n')
                    input("Druk op Enter om door te gaan...")
                    beat_edit_init()
            else:
                screen_clear()
                print('Verkeerde input')
                input("Druk op Enter om door te gaan...")
                beat_edit_init()
        else:
            screen_clear()
            print('Verkeerde maatsoort')
            input("Druk op Enter om door te gaan...")
            beat_edit_init()
    else:
        screen_clear()
        print('Verkeerde input')
        input("Druk op Enter om door te gaan...")
        beat_edit_init()