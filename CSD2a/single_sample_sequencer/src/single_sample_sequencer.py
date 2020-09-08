#Setup for windows compatability
import simpleaudio as sa
import pathlib
import os
proj_folder = pathlib.Path(f'{os.getcwd()}\{__file__}').parent.parent

#Get all information from the user
def beatinput():
    beats = int(input('How many beats are there in a measure? (choose from 3, 4 or 5) '))
    if beats == 3 or beats == 4 or beats == 5:
        measures = int(input('How many measures do you want to play?')) -1
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
    waittime = 60000 / bpm
    seqloc = [0, 0, 0]
    sequencer(seqloc, waittime, beats, measures)

def sequencer(seqloc, waittime, beats, measures):

beatinput()
