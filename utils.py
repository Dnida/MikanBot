import config
import urllib2, json
import time, thread
from time import sleep

def chat(sock, msg):
	sock.send("PRIVMSG #{} : {}\r\n".format(config.CHAN, msg))

def ban(sock, user):
	chat(sock, ".ban {}".format(user))

def mute(sock, user, seconds=600):
	chat(sock, ".timeout {}".format(user, seconds))


# filling op list in a seperate thread
"""
def threadFillOpList():
	while True:
		try:
			url = "http://tmi.twitch.tv/group/user/kaptainkoter/chatters"
			req = urllib2.Request(url, headers={"accept": "*/*"})
			reposnse = urllib2.urlopen(req).read()
			if reposnse.find("502 Bad Gateway") == -1:
				cfg.oplist.clear()
				data = json.loads(reposnse)
				for p in_data["chatters"] ["moderators"]:
					cfg.oplist[p] = "mod"
		except:
			'do nothing'
		sleep(5)
	
	
def isOP(user):
	return user in cfg.oplist
"""