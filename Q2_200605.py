import cv2
import numpy as np
import librosa


def solution(audio_path):
   
    ############################
    ############################

    ############################
    ############################
  audio, sr = librosa.load(audio_path)
  dir = np.abs(librosa.stft(audio))
  k=np.max
  cann = librosa.amplitude_to_db(dir, ref=k)
  a=100
  b=200
  corner = cv2.Canny(cann.astype(np.uint8), a, b)
  total = np.sum(corner)
  if total > 500000:
    class_name='metal'
  else:
    class_name='cardboard'
  return class_name

