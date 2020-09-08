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

#Load in samples and add these to a simple to acces dictionary
snare = str(f'{proj_folder}\media\s.wav')
kick = str(f'{proj_folder}\media\k.wav')
hat = str(f'{proj_folder}\media\h.wav')
empt = str(f'{proj_folder}\media\l.wav')
sampledict = {
    's': sa.WaveObject.from_wave_file(snare),
    'k': sa.WaveObject.from_wave_file(kick),
    'h': sa.WaveObject.from_wave_file(hat),
    'x': sa.WaveObject.from_wave_file(empt)
}


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
    waittime = (60000 / bpm / 8) * 0.001
    seqloc = [1, 1, 1]
    counter = 0
    sequencer(seqloc, waittime, beats, measures, counter)

#Plays samples according to given input
def sequencer(seqloc, waittime, beats, measures, counter):
    if seqloc[0] <= measures:
        print(seqloc)
        note = seq_data[str(beats)][counter]
        if note == 'k' or note == 's' or note == 'h' or note == 'x':
            samplefile = f'{note}.wav'
            play_obj = sampledict[note].play()
            time.sleep(waittime)
            if seqloc[2] == 4:
                if seqloc[1] == beats:
                    seqloc[0] += 1
                    seqloc[1] = 1
                    seqloc[2] = 1
                    counter = 0
                    sequencer(seqloc, waittime, beats, measures, counter)
                else:
                    seqloc[1] += 1
                    seqloc[2] = 1
                    counter += 1
                    sequencer(seqloc, waittime, beats, measures, counter)
            else:
                seqloc[2] += 1
                counter += 1
                sequencer(seqloc, waittime, beats, measures, counter)
        else:
            print('Have a nice day :)')

#Initiate functions
beatinput()
