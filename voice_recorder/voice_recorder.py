# -*- coding: utf-8 -*-
import logging
import threading
from pymedia.audio import acodec
import pymedia.audio.sound as sound
import time


#Ref: http://pymedia.org/tut/src/voice_recorder.py.html
class VoiceRecorder(threading.Thread):
    def __init__(self, full_path, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(VoiceRecorder, self).__init__(group, target, name, args, kwargs, verbose)
        self.full_path = full_path
        self.encoder = None
        self.__is_recording = False
        self.is_stopped = False
        self.opened_file = None
        self.record_lock = None
        #self.record_semaphore = None
        self.__init_encoder()

    def is_recording(self):
        return self.__is_recording

    def start_record(self):
        if (self.record_lock is None) and (not self.is_stopped):
            self.record_lock = threading.Lock()
            #self.record_lock.acquire()
            #self.record_semaphore = threading.Semaphore(1)
            self.__is_recording = True
            self.opened_file = open(self.full_path, 'wb')
            self.start()
        else:
            raise "Already recording, or already stopped %s %s" % (str(self.record_lock), str(self.is_stopped))

    def pause(self):
        if self.__is_recording:
            #self.record_semaphore.aquire()
            self.record_lock.acquire()
            self.__is_recording = False
        else:
            raise "Not started yet"

    def resume(self):
        if (self.record_lock is None) and (not self.__is_recording):
            self.__is_recording = True
            self.record_lock.release()
        else:
            raise "Not recording or not started %s %s" % (str(self.record_lock), str(self.__is_recording))

    def stop(self):
        if self.record_lock is None:
            raise "Not started"
        else:
            self.is_stopped = True
            self.pause()

    def is_started(self):
        return not (self.record_lock is None)

    def __init_encoder(self):
        # Minimum set of parameters we need to create Encoder
        encode_parameters = {'id': acodec.getCodecID('mp3'),
                             'bitrate': 128000,
                             'sample_rate': 44100,
                             'channels': 2}
        self.encoder = acodec.Encoder(encode_parameters)

    def __record(self):
        snd = sound.Input(44100, 2, sound.AFMT_S16_LE)
        snd.start()
        while self.__is_recording:
            s = snd.getData()
            if s and len(s):
                for fr in self.encoder.encode(s):
                    # We definitely should use mux first, but for
                    # simplicity reasons this way it'll work also
                    self.opened_file.write(fr)
            else:
                time.sleep(.003)
        # Stop listening the incoming sound from the microphone or line in
        snd.stop()

    def run(self):
        while not self.is_stopped:
            #self.record_lock.acquire()
            self.__record()
            self.record_lock.acquire()
        self.opened_file.close()
        logging.debug("Recording thread quit")
