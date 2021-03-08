import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import time
from .plugins import greeting
from .tts import output_command






class Assistant(object):

    def __init__(self , model : str , command_mode_time : int):

        self.model = model
        self.samplerate = int(sd.query_devices(None, 'input')['default_samplerate'])
        self.model = vosk.Model(model)
        self.q = queue.Queue()
        self._cmd_start_t = 0
        self.command_mode_time = command_mode_time
        self.interrupted = False



    def _command_interrupt_check(self):
        its_over = time.time() - self._cmd_start_t > self.command_mode_time
        return its_over or self.interrupted


    def callback(self , indata, frames, time, status):
        """ This is called (from a separate thread) for each audio block. """
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))
   
      
    def commandـhandler(self):
        self._cmd_start_t = time.time()

        try:
            with sd.RawInputStream(samplerate=self.samplerate, blocksize = 8000, device=None, dtype='int16',
                            channels=1, callback=self.callback):

                    rec = vosk.KaldiRecognizer(self.model, self.samplerate)
                    
                    while True: #not self._command_interrupt_check()
                        data = self.q.get()
                        if rec.AcceptWaveform(data):
                            jdata = json.loads(rec.Result())
                            cmd = jdata['text']
                            print("Admin :", cmd, end=f"\n-----{'-'*len(cmd)}\n")
                            print("Jarvis :", greeting.greeting(cmd=cmd), end=f"\n-----{'-'*len(str(greeting.greeting(cmd=cmd)))}\n")
                            self._handel_cmd(cmd)
                            
        except KeyboardInterrupt:
            print('\nDone')
            exit(0)
        except Exception as e:
            exit(type(e).__name__ + ': ' + str(e))


    def _handel_cmd(self , cmd):
        output_command(greeting.greeting(cmd=cmd))
        

        
    def main(self):

        self.commandـhandler()



