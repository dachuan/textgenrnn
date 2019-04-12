from wxpy import *
import random
from textgenrnn import textgenrnn


bot = Bot(cache_path=True)
#my_friend = ensure_one(bot.search(u'罗余'))
#print(my_friend)

textgen = textgenrnn(weights_path='peom_weights.hdf5',
                     vocab_path='peom_vocab.json',
                     config_path='peom_config.json')

def gen_poem():
	poem = []
	for i in range(5):
		temp = random.uniform(0.5,0.9)
		p = textgen.generate(n=1, temperature=temp,return_as_list=True)
		poem.append(p[0])
	return poem

#l = gen_poem()
#print(l)
#s = "\n".join(l)
#print(s)


def sayhello():
	return 'hello'

# to specific one 
#@bot.register(my_friend,run_async=True)
#def reply_my_friend(msg):
#	#return 'hi'
#	if msg.text == "写诗":
#		print('got it!')
#		#s = sayhello()
#		#print(s)
#		l = gen_poem()
#	#print(l)
#		s = "\n".join(l)
#	#print(s)
#		return s

# to myself
@bot.register(bot.self, except_self=False)
def reply_self(msg):
	return sayhello()

# to everyone
@bot.register(run_async=True)
def reply_my_friend(msg):
	if msg.text == "写诗":
		print('got it!')
		l = gen_poem()
		s = "\n".join(l)
		return s

gen_poem()

embed()
