# Setup for windows compatability
import json
import os
import pathlib
import sys
import threading
import time

import simpleaudio as sa
from midiutil import MIDIFile
from synthesizer import Player, Synthesizer, Waveform


proj_folder = pathlib.Path(__file__).parent.parent


# Define midi variables
degrees = []  # MIDI note number for drums
track = 0
channel = 0
midi_time = [0]  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard


# Define script variables
wait_time = 0
measures = 0
beats = 4
snare_list = []
snare_times = []
snare_degrees = []
kick_list = []
kick_times = []
kick_degrees = []
hat_list = []
hat_times = []
hat_degrees = []
synth_list = []
synth_times = []
synth_degrees = []
counter = 0
seqloc = [1, 1, 1]
drum_ready = 0
synth_ready = 0
notes = ['a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis']
hertz = 0
base_time = 0


# Reset all variables
def sequencer_init():
    global wait_time, measures, beats, snare_list, snare_times, snare_degrees, kick_list, kick_times, kick_degrees, hat_list, hat_times, hat_degrees, counter, seqloc, drum_ready, synth_ready, notes, hertz, base_time, track, channel, duration, volume, synth_list, synth_times, synth_degrees
    wait_time = 0
    measures = 0
    beats = 4
    snare_list = []
    snare_times = []
    snare_degrees = []
    kick_list = []
    kick_times = []
    kick_degrees = []
    hat_list = []
    hat_times = []
    hat_degrees = []
    synth_list = []
    synth_times = []
    synth_degrees = []
    counter = 0
    seqloc = [1, 1, 1]
    drum_ready = 0
    synth_ready = 0
    notes = ['a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis']
    hertz = 0
    base_time = 0
    track = 0
    channel = 0
    duration = 1  # In beats
    volume = 100  # 0-127, as per the MIDI standard
    beat_input()


# Initialise synth
player = Player()
player.open_stream()
synth = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=0.2, osc2_freq_transpose=0.48, use_osc2=True, osc2_waveform=Waveform.triangle, osc2_volume=0.1)


# Midi save script
def save_to_midi():
    global degrees, track, channel, time, duration, tempo, volume
    note_lists = [snare_list, kick_list, hat_list, synth_list]
    time_lists = [snare_times, kick_times, hat_times, synth_times]
    degree_lists = [snare_degrees, kick_degrees, hat_degrees, synth_degrees]
    n = 0
    # Let's build all the degree lists and duration lists shall we!
    while n < 4:
        i = 0
        x = 0
        for i in range(len(note_lists[n])):
            # Adds an extra duration to the end of the previous note to make a rest
            if note_lists[n][i] != 'x':
                if n == 3:
                    degree_lists[n].append(note_lists[n][i])
                else:
                    midinum = midi_conv.get(note_lists[n][i])
                    degree_lists[n].append(midinum)
                time_lists[n].append(x)
                x += 1
            else:
                x += 1
        n += 1
    # Midi export starts here
    MyMIDI = MIDIFile(3)
    MyMIDI.addTempo(1, 0, tempo)
    n = 0
    while n < 4:
        if n == 3:
            track = 1
        for i, pitch in enumerate(degree_lists[n]):
            MyMIDI.addNote(track, channel, int(pitch), time_lists[n][i], duration, volume)
        n += 1

    with open("CSD2a/eindopdracht/media/Sequence.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    print('\n Have a nice day, your midi file has been saved :)')
    input()

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

class seq_thread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
    def run(self):
        play_sound(self.name)

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

# Function to update seqloc counter
def update_seqloc():
    global seqloc, beats
    if seqloc[2] == 4:
        if seqloc[1] == beats:
            seqloc[0] += 1
            seqloc[1] = 1
            seqloc[2] = 1
        else:
            seqloc[1] += 1
            seqloc[2] = 1
    else:
        seqloc[2] += 1

# Function to play the drum sound according to beat number, checks if it's a legal drum note
def play_drum(drum_note):
    global drum_list
    if drum_note.lower() == 'k' or drum_note.lower() == 's' or drum_note.lower() == 'h' or drum_note.lower() == 'x':
        # Plays the given note from a dictionary
        play_obj = sampledict[drum_note.lower()].play()
    else:
        print('PANIEK!')

# Function to play the synth sound according to note name
def play_synth(synth_note):
    global synth_list, wait_time
    # Checks if the note is not a rest (x)
    if synth_note != 'x':
        # Plays the note, no need for conversions to hertz or midi because the synth library already does that
        player.play_wave(synth.generate_constant_wave(str(synth_note.capitalize()), wait_time))
        # Convert the note to midi
        midi_note_raw = midi_conv.get(synth_note[:-1].lower())
        if synth_note[:-1].isdigit():
            midi_note = int(midi_note_raw) + (synth_note[-1] * 12)
            synth_list.append(midi_note)
        else:
            synth_list.append(int(midi_note_raw))
    else:
        play_obj = sampledict[synth_note.lower()].play()
        synth_list.append(synth_note.lower())


# Get all information from the user
def beat_input():
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
            beat_input()
    else:
        print('Wrong beat amount')
        beat_input()


# Builds a sequencer location array, convert bpm to milliseconds, also starts the sequencer and threading
def beat_converter(bpm):
    global wait_time, beats, measures, base_time
    wait_time = (60000 / bpm / 8) * 0.001
    base_time = int(round(time.time() * 1000))
    screen_clear()
    # Create new thread
    thread1 = seq_thread(1, 'seq_thread')
    thread1.start()
    thread1.join()

def play_sound(threadName):
    global beats, counter, seqloc, wait_time, base_time, measures
    # Makes sure it stops when all measures are played
    while seqloc[0] <= measures:
        # Exit flag for the threading to work
        if exitFlag:
            threadName.exit()
        # Writes the time that has elapsed since starting the sequencer
        elapsed_time = int(round(time.time() * 1000)) - base_time
        # Keeps track of the count
        counter = ((seqloc[0] - 1) * 16) + ((seqloc[1] - 1) * 4) + seqloc[2]
        # Which note in the sequence to play
        note_to_play = ((seqloc[1] - 1) * 4) + seqloc[2] - 1
        # Check if a beat needs to be played, multiplies the wait_time by 1000 to make it whole milliseconds
        if elapsed_time / (int(wait_time * 1000)*2) >= counter:
            # Write out beat number
            sys.stdout.write("\r " + str(seqloc))
            sys.stdout.flush()
            # Gets the notes to be played and saves them to their list
            kick_note = seq_data[str(f'{beats}k')][note_to_play]
            kick_list.append(kick_note.lower())
            snare_note = seq_data[str(f'{beats}sn')][note_to_play]
            snare_list.append(snare_note.lower())
            hat_note = seq_data[str(f'{beats}h')][note_to_play]
            hat_list.append(hat_note.lower())
            synth_note = seq_data[str(f'{beats}s')][note_to_play]
            # Plays the sounds
            play_drum(kick_note)
            play_drum(snare_note)
            play_drum(hat_note)
            play_synth(synth_note)
            # Update the sequence counter
            update_seqloc()
        time.sleep(0.001)
    save_to_midi()