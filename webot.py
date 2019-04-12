from wxpy import *

bot = Bot()

#def reply_my_friend(msg):
#	return 'received: {} ({})'.format(msg.text, msg.type)

@bot.register()
def auto_reply(msg):
	return 'hi'

embed()
