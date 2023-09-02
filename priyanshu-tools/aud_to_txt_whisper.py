import whisper
import os, os.path
import glob
import pandas as pd
from tqdm import tqdm
import shutil

from pathlib import Path

wavs = '' # path to wav files
out_txt = '' # path to save txt files


if os.path.exists(out_txt):
	shutil.rmtree(out_txt)

if not os.path.exists(out_txt):
	os.makedirs(out_txt)

model = whisper.load_model("medium.en") #https://github.com/openai/whisper
paths = glob.glob(os.path.join(wavs, '*.wav'))
print(len(paths))
paths = sorted(paths)

all_filenames = []
transcript_text = []
# with open(meta_file, 'w', encoding='utf-8') as outfile:
for filepath in tqdm(paths):
	base = os.path.basename(filepath)
	all_filenames.append(base)

for filepath in tqdm(paths):
	result = model.transcribe(filepath)
	output = result["text"].lstrip()
	output = output.replace("\n","")
	thefile = str(os.path.basename(filepath).lstrip(".")).rsplit(".")[0]
	txt_file = thefile+'.txt'
	with open(out_txt+'/'+txt_file, 'w') as f:
		f.write(output)
	# outfile.write(thefile + '|' + output +'\n')
	# print(thefile + '|' + output + '|' + output + '\n')
