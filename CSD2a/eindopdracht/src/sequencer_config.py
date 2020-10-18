# Locate json sequencer data and loads it
json_loc = str(f'{proj_folder}\config\sequencerdata.json')
json_file = open(json_loc, 'r')
json_pure = str(json_file.read(1000))
seq_data = json.loads(json_pure)

# Arrays and functions to check if the notes are legal
def drum_legality(beatsort, counter, inputtext):
    drum_legal = ['k', 's', 'h', 'x', '<-', '']
    if inputtext in drum_legal:
        return
    else:
        screen_clear()
        print('Illegale drum input')
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
                seq_builder(beatsort, counter)
        else:
            screen_clear()
            print('Illegale synth input')
            seq_builder(beatsort, counter)

# Script to build sequence
def seq_builder(beatsort, counter):
    screen_clear()
    print(seq_data[str(beatsort)])
    if counter < len(seq_data[str(beatsort)]):
        if beatsort.endswith('s'):
            note = input(f'Voer de noot in van stap nummer {counter + 1}, format = Noot-Kruis-Octaaf, bijvoorbeeld G#5, b2, f8. X betekent een rust. Of type <- om terug te gaan \n')
            synth_legality(beatsort, counter, note)
        else:
            note = input(f'Voer de waarde in van noot nummer {counter + 1} kies uit (k(ick), s(nare), h(i-hat) of x (leeg), of type <- om terug te gaan \n')
            drum_legality(beatsort, counter, note)
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


# Script user input and initialisation
def beat_edit_init():
    screen_clear()
    beatsort = input('Welke maatsoort wil je veranderen? Kies uit 3, 4 of 5 vierde \n')
    counter = 0
    if beatsort.isdigit():
        if beatsort == '3' or beatsort == '4' or beatsort == '5':
            screen_clear()
            sound_type = input('Wil je drums aanpassen of de synth noten? Kies uit drums of synth \n')
            if sound_type.isalpha():
                if sound_type.lower() == 'drums' or sound_type.lower() == 'synth':
                    if sound_type.lower() == 'synth':
                        beatsort = f'{beatsort}s'
                    screen_clear()
                    generator = input('Wil je de noten met een euclidisch algoritme genereren of handmatig aanpassen? Kies uit genereren of handmatig \n')
                    if generator.isalpha():
                        if generator == 'handmatig':
                            seq_builder(beatsort, counter)
                        elif generator == 'genereren':
                            seq_builder(beatsort, counter)
                        else:
                            screen_clear()
                            print('Verkeerde input methode \n')
                            beat_edit_init()
                else:
                    screen_clear()
                    print('Verkeerd instrument \n')
                    beat_edit_init()
            else:
                screen_clear()
                print('Verkeerde input, geen tekst \n')
                beat_edit_init()
    else:
        screen_clear()
        print('Verkeerde maatsoort')
        beat_edit_init()

beat_edit_init()