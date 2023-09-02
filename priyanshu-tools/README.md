# Tools Description

## aud_to_metadata_whisper.py
This script is used to create transcript in a csv format of a wav file. It uses [whisper]('https://github.com/openai/whisper') to convert audio to text.

## audio_to_txt_sr_lib.py
This script is used to create transcript in a txt format of a wav file and save to a output folder. It uses [SpeechRecognition]('https://pypi.org/project/SpeechRecognition/') to convert audio to text.

## audio_to_txt_whisper.py
This script is used to create transcript in a txt format of a wav file and save to a output folder. It uses [whisper]('https://github.com/openai/whisper') to convert audio to text.

## mp3_to_wav.py
This script is used to convert mp3 files to wav files. It uses [pydub]('https://pypi.org/project/pydub/') to convert mp3 to wav.

## split_audio.py
This script is used to split a wav file into multiple wav files. It uses [librosa]('https://pypi.org/project/librosa/') and arbitrary frame sliding window to split the audio.