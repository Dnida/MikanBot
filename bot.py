import config
import utils
import socket
import re
import time, thread
from time import sleep




def main():

	form = "utf-8"
	#netwerking ;)
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode(form))
	s.send("NICK {}\r\n".format(config.NICK).encode(form))
	s.send("JOIN #{}\r\n".format(config.CHAN).encode(form))

	CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
	utils.chat(s, "h-hello senpai ^-^")

	#thread.start_new_thread(utils.threadFillOpList, ())

	while True:
		#PING PONG RESPONSE FOR TWITCH
		response = s.recv(1024).decode(form)
		if response == "PING :tmi.twitch.tv\r\n":
			s.send("PONG :tmi.twitch.tv\r\n".encode(form))
		else:
			#WHO IS SENDING MESSAGES?
			username = re.search(r"\w+", response).group(0)
			message = CHAT_MSG.sub("", response)
			print(response)

			# COMMANDS - ADD HERE


			#Simple Time Command
			if message.strip() == "!time":
				utils.chat(s, "it's currently " + time.strftime("%I:%M %p %Z on %A, %B %d, %Y"))
		sleep(1)



if __name__ == "__main__":
	main()
