#**Wouter's pythonic sample sequencer v2.0**

This is a sequencer that plays notes according to sequencerdata.json<br>


If you just want to test out the sequencer, just commence `src/sample_sequencer_v20.py`

You can also modify the sequence data that the sequencer plays, or generate an Euclidian rhythm<br>

The program also saves the played music as a midi file, which is neat :)
<br><br><br>

## **Installing the pyaudio libraries**

To get the synth to work I use the synthesizer libraries, which rely on the pyaudio library. I had a lot of trouble installing this, so here is a small guide on how I got this working.

`pip3 install pyaudio` did not work for me, but I found another version on https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio which works in the current python version.

Version `PyAudio-0.2.11-cp38-cp38-win_amd64` worked for my 64 bit windows system with python version 3.8

Once you've downloaded this you can just do `pip3 install PyAudio-0.2.11-cp38-cp38-win_amd64` in the folder where you downloaded the file.

After this you you should just be able to install the rest of the used libraries without any problem with the `pip3 install` command.
<br><br><br>
## **Used libraries**

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
