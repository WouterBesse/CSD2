import simpleaudio as sa

def samplespeler(hoeveelheid, sample):
    if hoeveelheid > 0:
        if sample == 'WAP':
            wave_obj = sa.WaveObject.from_wave_file('../media/WAP.wav')
            play_obj.wait_done()
            hoeveelheid -= 1
            samplespeler(hoeveelheid, sample)
        elif sample == 'RAP':
            wave_obj = sa.WaveObject.from_wave_file('./media/RAP.wav')
            play_obj.wait_done()
            hoeveelheid -= 1
            samplespeler(hoeveelheid, sample)
        elif sample == 'FAP':
            wave_obj = sa.WaveObject.from_wave_file('../media/FAP.wav')
            play_obj.wait_done()
            hoeveelheid -= 1
            samplespeler(hoeveelheid, sample)
        else:
            print('Uw gekozen sample bestaat hier niet')
    else:
        print('Hopelijk heeft U genoten')



print ('Welke sample wilt u spelen? (Kies uit WAP, RAP en FAP)')
sample = input()
print ('Hoe vaak wilt u deze sample afspelen?')
hoeveelheid = int(input())
samplespeler(hoeveelheid, sample)
