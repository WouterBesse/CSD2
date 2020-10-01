# Setup for windows compatability
import json
import os
import pathlib
import sys
import threading
import time as tijd

import simpleaudio as sa
from midiutil import MIDIFile
from synthesizer import Player, Synthesizer, Waveform

proj_folder = pathlib.Path(__file__).parent.parent

# Define variable
wait_time = 0
measures = 0
beats = 4
drumlist = []
notelist = []
counter = 0
seqloc = [1, 1, 1]
drum_ready = 0
synth_ready = 0
notes = ['a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis']
hertz = 0


# Initialise synth
player = Player()
player.open_stream()
synth = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=0.2, osc2_freq_transpose=0.48, use_osc2=True, osc2_waveform=Waveform.triangle, osc2_volume=0.1)

# Define midi variables
degrees = []  # MIDI note number for drums
degreesn = [] #MIDI note number for notes
track = 0
channel = 0
time = [0]  # In beats
timen = [0]
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

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
json_pure = str(json_file.read(1000))
seq_data = json.loads(json_pure)

# Load in samples and add these to a simple to acces dictionary
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

# Translation table to convert my data structure to midi notes
midi_conv = {
    'k': 36,
    's': 38,
    'h': 42,
    'a': 45,
    'a#': 46,
    'b': 47,
    'c': 48,
    'c#': 49,
    'd': 50,
    'd#': 51,
    'e': 52,
    'f': 53,
    'f#': 54,
    'g': 55,
    'g#': 56
}

# Add class for threading
exitFlag = 0

class Drumthread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        global seqloc, counter
        self.threadID = thread_id
        self.name = name
        self.counter = counter
        self.seqloc = seqloc

    def run(self):
        dsequencer(self.name)

class synThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        global seqloc, counter
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.seqloc = seqloc

    def run(self):
        nsequencer(self.name)

# Function to convert midi to hz
def mtoh(x):
    global hertz
    a = 440
    #hertz = (a / 32) * (2 ^ ((x - 9) / 12))
    hertz = (a / 32) * pow(2, ((x - 9) / 12))

# Get all information from the user
def beatinput():
    global measures, beats, wait_time, tempo
    beats = int(input('How many beats are there in a measure? (choose from 3, 4 or 5) \n'))
    if beats == 3 or beats == 4 or beats == 5:
        screen_clear()
        measures = int(input('How many measures do you want to play? \n'))
        screen_clear()
        bpm = int(input('What will your BPM be? (maximum is 250BPM) \n'))
        tempo = bpm
        if bpm <= 250 or bpm > 0:
            beat_converter(bpm)
        else:
            print('Wrong BPM amount')
            beatinput()
    else:
        print('Wrong beat amount')
        beatinput()


# Builds a sequencer location array, convert bpm to milliseconds
def beat_converter(bpm):
    global wait_time, beats, measures
    wait_time = (60000 / bpm / 8) * 0.001
    screen_clear()
    # Create new threads
    thread1 = Drumthread(1, 'drumthread')
    thread2 = synThread(2, 'synthread')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


# Plays drum samples according to given input
def dsequencer(threadName):
    global measures, beats, wait_time, drumlist, drum_ready, synth_ready, counter, seqloc
    # Checks if the given amount of measures has been played already, if not then executes the script
    while seqloc[0] <= measures:
        # Necessary for multi threading, so it can switch to the other thread
        if exitFlag:
            threadName.exit()
        # Writes out the current transport location without adding an extra line
        sys.stdout.write("\r " + str(seqloc))
        sys.stdout.flush()
        # Gets the note that needs to be played
        note = seq_data[str(beats)][counter]
        # Checks if it's a legal note
        if note.lower() == 'k' or note.lower() == 's' or note.lower() == 'h' or note.lower() == 'x':
            # Adds to the drumlist for later midi export
            drumlist.append(note.lower())
            # Plays the given note from a dictionary
            play_obj = sampledict[note.lower()].play()
            # Waits the desired amount of time
            tijd.sleep(wait_time)
            drum_ready = 1
            while drum_ready == 0 or synth_ready == 0:
                tijd.sleep(0.001)
            counter_update(seqloc)
        else:
            print('\n Error, invalid note')
    drum_ready = 1


# Plays sequencer according to given input
def nsequencer(threadName):
    global measures, beats, wait_time, drumlist, drum_ready, synth_ready, hertz, synth_ready, counter, seqloc
    # Checks if the given amount of measures has been played already, if not then executes the script
    while seqloc[0] <= measures:
        # Necessary for multi threading, so it can switch to the other thread
        if exitFlag:
            threadName.exit()
        # Gets the note that needs to be played
        note = seq_data[str(f'{beats}s')][counter]
        if note != 'x':
            player.play_wave(synth.generate_constant_wave(str(note.capitalize()), wait_time))
            midinoteraw = midi_conv.get(note[:-1].lower())
            print(note[:-1])
            print(midinoteraw)
            tijd.sleep(wait_time)
            if note[:-1].isdigit():
                midinote = int(midinoteraw) + (note[-1] * 12)
                notelist.append(midinote)
            else:
                notelist.append(int(midinoteraw))
        else:
            play_obj = sampledict[note.lower()].play()
            notelist.append(note.lower())
            tijd.sleep(wait_time)
        synth_ready = 1
        print(drum_ready)
        while drum_ready == 0 or synth_ready == 0:
            tijd.sleep(0.001)
    synth_ready = 1
    print(notelist)
    if drum_ready == 1 and synth_ready == 1:
        save_to_midi()



# Updates the counter
def counter_update(seqloc):
    global drum_ready, synth_ready, beats, counter
    if seqloc[2] == 4:
        if seqloc[1] == beats:
            seqloc[0] += 1
            seqloc[1] = 1
            seqloc[2] = 1
            counter = 0
            drum_ready = 0
            synth_ready = 0
        else:
            seqloc[1] += 1
            seqloc[2] = 1
            counter += 1
    else:
        seqloc[2] += 1
        counter += 1

# Script which converts all the played notes to midi data and saves this as a .mid file
def save_to_midi():
    global degrees, track, channel, time, duration, tempo, volume, degreesn, timen
    for i in range(len(drumlist)):
        # Adds an extra duration to the end of the previous note to make a rest
        if drumlist[i] == 'x':
            time[-1] += 1
        else:
            midinum = midi_conv.get(drumlist[i])
            degrees.append(midinum)
            time.append(0)

    for i in range(len(notelist)):
        # Adds an extra duration to the end of the previous note to make a rest
        if notelist[i] == 'x':
            timen[-1] += 1
        else:
            degreesn.append(notelist[i])
            timen.append(0)

    # Midi export starts here
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(1, 0, tempo)
    tim = -1
    timn = -1
    for i, pitch in enumerate(degrees):
        tim += time[i] + 1
        print(pitch)
        MyMIDI.addNote(1, channel, pitch, tim, duration, volume)

    for i, pitch in enumerate(degreesn):
        timn += timen[i] + 1
        MyMIDI.addNote(2, channel, pitch, timn, duration, volume)

    with open("Sequence.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    print('\n Have a nice day, your midi file has been saved :)')



# Initiate script
screen_clear()
beatinput()
# python3 csd2a/single_sample_sequencer/src/single_sample_sequencer.py