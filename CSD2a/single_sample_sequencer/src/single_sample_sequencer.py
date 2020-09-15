# Setup for windows compatability
import simpleaudio as sa
import pathlib, os, json, sys, _thread, threading
import time as tijd
from midiutil import MIDIFile

proj_folder = pathlib.Path(__file__).parent.parent

# Define variable
wait_time = 0
measures = 0
beats = 4
notelist = []

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
json_pure = str(json_file.read(500))
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

midi_conv = {
    'k': 36,
    's': 38,
    'h': 42,
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


# Get all information from the user
screen_clear()


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
    thread1.start()
    thread1.join()


# Plays drum samples according to given input
def dsequencer(seqloc, counter, threadName):
    global measures, beats, wait_time, notelist
    while seqloc[0] <= measures:
        if exitFlag:
            threadName.exit()
        sys.stdout.write("\r " + str(seqloc))
        sys.stdout.flush()
        note = seq_data[str(beats)][counter]
        if note.lower() == 'k' or note.lower() == 's' or note.lower() == 'h' or note.lower() == 'x':
            notelist.append(note.lower())
            play_obj = sampledict[note.lower()].play()
            tijd.sleep(wait_time)
            if seqloc[2] == 4:
                if seqloc[1] == beats:
                    seqloc[0] += 1
                    seqloc[1] = 1
                    seqloc[2] = 1
                    counter = 0
                else:
                    seqloc[1] += 1
                    seqloc[2] = 1
                    counter += 1
            else:
                seqloc[2] += 1
                counter += 1
        else:
            print('\n Have a nice day :)')
            save_to_midi()
    print('\n Have a nice day :)')
    save_to_midi()

def save_to_midi():
    global degrees, track, channel, time, duration, tempo, volume
    for i in range(len(notelist)):
        if notelist[i] == 'x':
            time[-1] += 1
        else:
            midinum = midi_conv.get(notelist[i])
            degrees.append(midinum)
            time.append(0)
    print(time)
    print(degrees)
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
    # automatically)
    MyMIDI.addTempo(track, 0, tempo)
    tim = -1
    for i, pitch in enumerate(degrees):
        tim += time[i] + 1
        print(tijd)
        MyMIDI.addNote(track, channel, pitch, tim, duration, volume)

    with open("major-scale.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)



# Initiate functions
beatinput()
