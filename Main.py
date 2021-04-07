from Etap1 import *

generator = Generator.Generator(15)
generator.generate_signal()
print("Wygenerowany sygnał:")
print(generator.signal)

coder = Coder.Coder()
coder_output = coder.code(generator.signal)
print("Zakodowany sygnał:")
print(coder_output)

channel = Channel.Channel(0.3)
channel_output = channel.get_output(coder_output)
print("Sygnał po przejściu przez kanał transmisyjny:")
print(channel_output)

decoder = Decoder.Decoder()
decoder_output = decoder.decode(channel_output)
print("Zdekodowany sygnał:")
print(decoder_output)





