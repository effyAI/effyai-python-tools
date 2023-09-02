import whisper
import os, os.path
import glob
import pandas as pd
from tqdm import tqdm

from pathlib import Path

wavs = '' # path to wav files
metadata = '' # path to save metadata

model = whisper.load_model("medium.en") # https://github.com/openai/whisper
paths = glob.glob(os.path.join(wavs, '*.wav'))
print(len(paths))
paths = sorted(paths)

all_filenames = []
transcript_text = []
with open(metadata, 'w', encoding='utf-8') as outfile:
	for filepath in tqdm(paths):
		base = os.path.basename(filepath)
		all_filenames.append(base)
	for filepath in tqdm(paths):
		result = model.transcribe(filepath)
		output = result["text"].lstrip()
		output = output.replace("\n","")
		thefile = str(os.path.basename(filepath).lstrip(".")).rsplit(".")[0]
		outfile.write(thefile + '|' + output +'\n')
		# print(thefile + '|' + output + '|' + output + '\n')   