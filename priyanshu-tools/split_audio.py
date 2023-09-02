import librosa
import soundfile as sf
import os

out_path = '' # path to save audio files
file_path = '' # path to audio file
min_split_sec = 10 # range min_split_sec - till word complete

if not os.path.exists(out_path):
    os.makedirs(out_path)

y, sr = librosa.load(file_path, mono=True, sr=22050)
duration = librosa.get_duration(y=y, sr=sr)
# y = librosa.to_mono(y)
print(y.shape, sr, duration, len(y)/sr, len(y)/duration)

y_split = librosa.effects.split(y, top_db=30,)

def time_spliter(y_split, y,out_path, sr=22050):
    i = 0
    p1 = 0

    while p1<len(y_split):
        start = y_split[p1][0]
        p1+=1
        if p1 >= len(y_split):
            break
        while (y_split[p1][1] - start) <= sr*min_split_sec:
#             print((y_split[p1][1] - start) / sr , (y_split[p1][1] - start) / sr  <= 8, 8)
            if p1>=len(y_split):
                break
            p1+=1
            
            print(p1,"here")
        print(p1,len(y_split))
        print((y_split[p1][1] - start) / sr , (y_split[p1][1] - start) / sr, "Writing:-","{}.wav".format(i))
        sf.write('{}/{}.wav'.format(out_path,i), y[start:y_split[p1][1]], 22050, 'PCM_24')
        p1+=1
        i+=1

time_spliter(y_split, y, out_path, sr=22050 )
