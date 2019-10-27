# 72636d70
# roguelike
# steal a painting
# dont die
prompt = '> '

def foyer():
	print """
	You enter the foyer.
	To the west is the green room. 
	To the north is the sun room. 
	To the east is the gold room.
	Which room do you enter?
	"""

def gold_room():
	print """
	You enter the gold room. The walls are lined with ornate decorations.
	What do you do?
	"""
	action = raw_input(prompt)
	if action == 'look' or 'look around':
		print """
		You take a glance around the room. The walls are lined with ornate decorations.
		On the north wall, there is a large painting of the owner. There are sconces on each side.
		On the east wall, there is a large table covered in gold artifacts. Chalices, candlesticks and the like.
		On the west wall, there is a number of small portraits. Many of them are of the owners family.
		"""
		looked_around = True
	elif action == 'leave' or 'exit'
		foyer()

def sun_room()

def green_room()

# story
print "Your name is Mr. May. You are a thief. You are casing a home to burgle a painting."
print "The home is small, only 4 rooms. But each room is rather large."
