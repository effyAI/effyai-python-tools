import speech_recognition as sr
import os
from tqdm import tqdm
from threading import Thread

def audio_to_text(audio_path, language):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        # print(text, audio_path)
        return text, audio_path
    except:
        return False, audio_path

txt_f = '' # output txt folder path
base_p = '' # base wav folder path
lang_use = 'hi-IN' # language code


if not os.path.exists(txt_f):
    os.makedirs(txt_f)

i = 0
lst = os.listdir(base_p)

class ThreadWithReturnValue(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def pre_process_meta(metafile):
    lst = []
    with open(metafile, 'r') as f:
        data = f.readlines()
    for i in range(len(data)):
        lst.append(data[i].split('|')[0])
    return lst


rm = []
while i < len(lst):
    thd = []
    # print('h1')

    for _ in range(20):
        if i >= len(lst):
            break
        # print(base_p+'/'+lst[i])
        txt = ThreadWithReturnValue(target=audio_to_text, args=(base_p+'/'+lst[i],lang_use))
        thd.append(txt)
        txt.start()
        i+=1


    for j in thd:
        ret_j = j.join()
        if ret_j[0]:
            txt, path = ret_j
            # print(txt, path)
            txt_file = txt_f+'/'+path.split('/')[-1].split('.')[0]+'.txt' #txt_f+'/'+lst[i].split('.')[0]+'.txt'
            with open (txt_file, 'w') as f:
                # print('Success writing', txt_file)
                f.write(txt)
        else:
            print('Fail', ret_j)
            rm.append(ret_j[1])
print(rm)
