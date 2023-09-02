from pydub import AudioSegment
import os
from tqdm import tqdm

src_f = '' # path to mp3 files
src = os.listdir(src_f)
out_f = '' # path to save wav files

if not os.path.exists(out_f):
    os.makedirs(out_f)

for i in tqdm(src):
    sound = AudioSegment.from_mp3(src_f+'/'+i)
    sound = sound + 20
    f_name = i.split('.')[0]+'.wav'
    sound.export(out_f+'/'+f_name, format='wav')