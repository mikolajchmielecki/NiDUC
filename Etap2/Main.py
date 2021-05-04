from komm import *
import numpy as np

# podstawa kodu BCH
m = 4

# zdolność korekcyjna kodu BCH
t = 2

# przysyłana wiadomość - długość  = parametr 'k' w książce Mochnackiego
msg = np.array([1,1,1,0,0,0,1])
print(msg)

code = BCHCode(m,t)
coder_output = code.encode(msg)
print(coder_output)

channel_output = coder_output[:]
channel_output[1] = abs(channel_output[1]-1)
channel_output[2] = abs(channel_output[2]-1)
channel_output[8] = abs(channel_output[8]-1)
print(channel_output)

decoder_output = code.decode(channel_output)
print(decoder_output)


