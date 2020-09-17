# Setup for windows compatability
import simpleaudio as sa
import pathlib, os, json, sys, threading
import synthesizer as syn
import time as tijd
from midiutil import MIDIFile

proj_folder = pathlib.Path(__file__).parent.parent

# Define variable
wait_time = 0
measures = 0
beats = 4
notelist = []
drum_ready = 0
synth_ready = 0
notes = ['a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis']
hertz = 0

# Define midi variables
degrees = []  # MIDI note number
track = 0
channel = 0
time = [0]  # In beats
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
    'a': 69,
    'ais': 70,
    'b': 71,
    'c': 72,
    'cis': 73,
    'd': 74,
    'dis': 75,
    'e': 76,
    'f': 77,
    'fis': 78,
    'g': 79,
    'gis': 80
}

# Add class for threading
exitFlag = 0

class drumThread(threading.Thread):
    def __init__(self, threadID, seqloc, counter, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.seqloc = seqloc

    def run(self):
        dsequencer(self.seqloc, self.counter, self.name)

class synThread(threading.Thread):
    def __init__(self, threadID, seqloc, counter, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.seqloc = seqloc

    def run(self):
        nsequencer(self.seqloc, self.counter, self.name)

# Function to convert midi to hz
def mtoh(x):
    global hertz
    a = 440
    hertz = (a / 32) * (2 ^ ((x - 9) / 12))

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
            beat_converter(beats, measures, bpm)
        else:
            print('Wrong BPM amount')
            beatinput()
    else:
        print('Wrong beat amount')
        beatinput()


# Builds a sequencer location array, convert bpm to milliseconds
def beat_converter(beats, measures, bpm):
    global wait_time
    wait_time = (60000 / bpm / 8) * 0.001
    counter = 0
    seqloc = [1, 1, 1]
    screen_clear()
    # Create new threads
    thread1 = drumThread(1, seqloc, counter, 'drumthread')
    thread2 = synThread(2, seqloc, counter, 'synthread')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


# Plays drum samples according to given input
def dsequencer(seqloc, counter, threadName):
    global measures, beats, wait_time, notelist, drum_ready, synth_ready
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
            # Adds to the notelist for later midi export
            notelist.append(note.lower())
            # Plays the given note from a dictionary
            play_obj = sampledict[note.lower()].play()
            # Waits the desired amount of time
            tijd.sleep(wait_time)
            drum_ready = 1
            while drum_ready == 0 or synth_ready == 0:
                tijd.sleep(0.1)
                counter_update(seqloc, counter)
        else:
            print('\n Error, invalid note')
    drum_ready = 1
    if drum_ready == 1 and synth_ready == 1:
        save_to_midi()


# Plays sequencer according to given input
def nsequencer(seqloc, counter, threadName):
    global measures, beats, wait_time, notelist, drum_ready, synth_ready, hertz
    # Checks if the given amount of measures has been played already, if not then executes the script
    player = syn.Player()
    player.open_stream()
    synth = syn(osc1_waveform=Waveform.sine, osc1_volume=0.8, use_osc2=False)
    print('so far so good')
    while seqloc[0] <= measures:
        # Necessary for multi threading, so it can switch to the other thread
        if exitFlag:
            threadName.exit()
        # Gets the note that needs to be played
        note = seq_data[str(f'{beats}s')][counter]
        print(note)
        if note.lower() in notes:
            mtoh(midi_conv.get(notelist[note.lower()]))
            print(hertz)
            player.play_wave(synth.generate_constant_wave(hertz, 3.0))
            tijd.sleep(wait_time)
            synth_ready = 1
            while drum_ready == 0 or synth_ready == 0:
                tijd.sleep(0.1)
        else:
            print('Invalid note!!!')
    drum_ready = 1
    if drum_ready == 1 and synth_ready == 1:
        save_to_midi()



# Updates the counter
def counter_update(seqloc, counter):
    global drum_ready, synth_ready
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
    global degrees, track, channel, time, duration, tempo, volume
    for i in range(len(notelist)):
        # Adds an extra duration to the end of the previous note to make a rest
        if notelist[i] == 'x':
            time[-1] += 1
        else:
            midinum = midi_conv.get(notelist[i])
            degrees.append(midinum)
            time.append(0)
    # Midi export starts here
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, 0, tempo)
    tim = -1
    for i, pitch in enumerate(degrees):
        tim += time[i] + 1
        print(tijd)
        MyMIDI.addNote(track, channel, pitch, tim, duration, volume)

    with open("Sequence.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    print('\n Have a nice day, your midi file has been saved :)')



# Initiate script
screen_clear()
beatinput()
