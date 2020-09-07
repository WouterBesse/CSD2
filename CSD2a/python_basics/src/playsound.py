import simpleaudio as sa
import pathlib
import os

def samplespeler(hoeveelheid, sample):
    if hoeveelheid > 0:
            proj_folder = pathlib.Path(f'{os.getcwd()}\{__file__}').parent.parent
            filetype = ".wav"
            samplefile = f'{sample}{filetype}'
            file_to_open = str(proj_folder / 'media' / samplefile)
            wave_obj = sa.WaveObject.from_wave_file(file_to_open)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            hoeveelheid -= 1
            samplespeler(hoeveelheid, sample)
    else:
        print('Hopelijk heeft U genoten')

sample = input('Welke sample wilt u spelen? (Kies uit WAP, RAP en FAP)')
hoeveelheid = int(input('Hoe vaak wilt u deze sample afspelen?'))
samplespeler(hoeveelheid, sample)
