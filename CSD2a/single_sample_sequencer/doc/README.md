### **Here is my simple sequencer.**

It will play synthesizer notes and drums sequences according to the data in sequencerdata.json. <br>
_~~The program also saves the played sequence as a midi file~~_ **this is currently broken**

If you just want to test out the sequencer, just commence single_sample_sequencer.py

You can also modify the sequence data that the sequencer plays.
You can just open my simple sequencer_config.py script (it needs some new guiding text atm but works just fine)
<br><br><br>

#### **Installing the pyaudio libraries**

To get the synth to work I use the synthesizer libraries, which rely on the pyaudio library. I had a lot of trouble installing this, so here is a small guide on how I got this working.

`pip3 install pyaudio` did not work for me, but I found another version on https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio which works in the current python version.

Version `PyAudio-0.2.11-cp38-cp38-win_amd64` worked for my 64 bit windows system with python version 3.8

Once you've downloaded this you can just do `pip3 install PyAudio-0.2.11-cp38-cp38-win_amd64` in the folder where you downloaded the file.

After this you you should just be able to install the rest of the used libraries without any problem with the `pip3 install` command.

<br><br>
#### **Used libraries**

json <br>
os <br>
pathlib <br>
sys <br>
threading <br>
time <br>
simpleaudio <br>
midiutil <br>
pyaudio <br>
synthesizer <br>
