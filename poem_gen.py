import time
import random
from textgenrnn import textgenrnn
#textgen = textgenrnn('./weights/hacker_news.hdf5')
textgen = textgenrnn(weights_path='peom_weights.hdf5',
					vocab_path='peom_vocab.json',
					config_path='peom_config.json')
#poem = textgen.generate_samples(temperatures=[0.2,0.5,1.0])
#poem = textgen.generate(n=5,temperature=0.5,return_as_list=True)
#for line in poem:
#	print(line)

for i in range(5):
	temp = random.random() + 0.5
	if temp >1:
		temp = 1
	poem = textgen.generate(n=1, temperature=0.8, return_as_list=True)
	#poem = textgen.generate(n=1, temperature=temp, return_as_list=True)
	print(poem[0])
	#print(temp)


