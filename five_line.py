import random
from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path='peom_weights.hdf5',
					vocab_path='peom_vocab.json',
					config_path='peom_config.json')

#poem = textgen.generate(n=5,temperature=0.8,return_as_list=True)

#for i in range(5):
#	temp = random.uniform(0.5,0.9)
#	poem = textgen.generate(n=1,temperature=temp,return_as_list=True)
#	print(poem[0])


def gen_poem():
    poem = []
    for i in range(5):
        temp = random.uniform(0.5,0.9)
        p = textgen.generate(n=1, temperature=temp,return_as_list=True)
        poem.append(p[0])
    return poem

g = gen_poem()

for line in g:
	print(line)
