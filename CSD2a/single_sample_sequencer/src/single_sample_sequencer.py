#Setup for windows compatability
import simpleaudio as sa
import pathlib
import os
import json
import time
proj_folder = pathlib.Path(f'{os.getcwd()}\{__file__}').parent.parent

#Locate json sequencer data and loads it
json_loc = str(f'{proj_folder}\config\sequencerdata.json')
json_file = open(json_loc, 'r')
json_pure = str(json_file.read(500))
seq_data = json.loads(json_pure)

#Get all information from the user
def beatinput():
    beats = int(input('How many beats are there in a measure? (choose from 3, 4 or 5) '))
    if beats == 3 or beats == 4 or beats == 5:
        measures = int(input('How many measures do you want to play?'))
        bpm = int(input('What will your BPM be? (maximum is 250BPM) '))
        if bpm <= 250:
            beatconverter(beats, measures, bpm)
        else:
            beatinput()
    else:
        print('Wrong beat amount')
        beatinput()

#Builds a sequencer location array, convert bpm to milliseconds
def beatconverter(beats, measures, bpm):
    waittime = (60000 / bpm / 16) * 0.001
    seqloc = [1, 1, 1]
    sequencer(seqloc, waittime, beats, measures)

def sequencer(seqloc, waittime, beats, measures):
    print(seqloc)
    if seqloc[0] < measures:
        print (seqloc)
        note = seq_data[str(beats)][seqloc[2] - 1]
        print(note)
        if note == 'k' or note == 's' or note == 'h' or note == 'x':
            samplefile = f'{note}.wav'
            file_to_open = str(f'{proj_folder}\media\samplefile')
            #wave_obj = sa.WaveObject.from_wave_file(file_to_open)
            time.sleep(waittime)
            if seqloc[2] == 16:
                if seqloc[1] == beats:
                    seqloc[0] += 1
                    seqloc[1] = 1
                    seqloc[2] = 1
                    sequencer(seqloc, waittime, beats, measures)
                else:
                    seqloc[1] += 1
                    seqloc[2] = 1
                    sequencer(seqloc, waittime, beats, measures)
            else:
                seqloc[2] += 1
                sequencer(seqloc, waittime, beats, measures)
        else:
            print('Have a nice day :)')

print(seq_data['3'][2])
beatinput()
