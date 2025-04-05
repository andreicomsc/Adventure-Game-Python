from gameparser import *

# ITEMS
item_example = {
    "id": "example",

    "name": "example item",

    "mass": 100,

    "description":
    """Easter egg? Did the developers leave this in by mistake? No, we didn't.... :)""",

    "Carriable": False
}

item_Portal_Gun = {
    "id": "portalgun",

    "name": "Portal Gun",

    "mass": 100,

    "description":
    """I can use this to Fast Travel around the tower.""",
    
    "Carriable": True
}


item_Stickynote = {
    "id": "stickynote",

    "name": "Sticky Note",

    "mass": 100,

    "description":
    """On the sticky note you see the password: 'kill-stud3ntS'. You shiver as you wounder who's password this is""",
    
    "Carriable": False
}

item_Old_Book = {
    "id": "oldbook",

    "name": "Old Book",

    "mass": 50,

    "description":
    """Titled 'Computer Poetry' by Kiril S!*%~ (Name seems to cut of there)""",

    "Carriable": True
}

item_lighter = {

    "id": "lighter",

    "name": "lighter",

    "mass": 15,

    "description": 
    """This is a gas lighter, perhaps could be used to light some candles or smoke your last cigarette...""",

    "Carriable": True

}

item_file = {
    "id": "file",

    "name": "a File",

    "mass": 25,

    "description":
    """This file contains the details of the secret experiment on students by a professor named K. Sidorov.""",

    "Carriable": True
}

item_dynamite = {
    "id": "dynamite",

    "name": "Dynamite",

    "mass": 190,

    "description":
    """I could use this to clear myself a path.""",

    "Carriable": True
}

item_mineKey = {
    "id": "goldkey",

    "name": "Gold Key",

    "mass": 50,

    "description":
    """I wonder what it opens.""",

    "Carriable": True
}

item_toy = {
    "id": "toy",

    "name": "Toy",

    "mass": 75,

    "description":
    """Its the lego minifigure Emmit from the movie.""",

    "Carriable": True
}

item_cigarettes = {
    "id": "cigarettes",

    "name": "Cigarettes",

    "mass": 12,

    "description":
    """A half empty pack of Marlboro Cigarettes.""",

    "Carriable": True
}

item_usb_dirve = {
    "id": "usbdrive",

    "name": "USB Drive",

    "mass": 30,

    "description":
    """A 16Gb SanDisk usb Drive.""",

    "Carriable": True
}

item_laptop = {
    "id":"laptop",

    "description": "It's a laptop that seems to already be running some program, 'portal.exe'",

    "name": "laptop",

    "Carriable": False,

    "mass": 50
}

item_ring = {
    "id": "ring",

    "name": "Ring",

    "mass": 60,

    "description":
    """A plain silver ring.""",

    "Carriable": True
}

item_lantern = {
    "id": "lantern",

    "name": "Lantern",

    "mass": 120,

    "description":
    """An old candle lit lantern, perhaps could be lit using a lighter.""",

    "Carriable": True
}

item_surgical_scalpel = {
    "id": "surgicalscalpel",

    "name": "Surgical scalpel",

    "mass": 25,

    "description":
    """Very sharp surgical Scalpel, appears to be previously used.""",

    "Carriable": True
}

item_binoculars = {
    "id": "binoculars",

    "name": "Binoculars",

    "mass": 650,

    "description":
    """A pair of medium range Binoculars.""",

    "Carriable": True
}

item_pickaxe = {
    "id": "pickaxe",

    "name": "Pickaxe",

    "mass": 800,

    "description":
    """An old-school, rusted, pickaxe.""",

    "Carriable": True
}

item_window = {
    "id": "window",

    "name": "Window",

    "mass": 0,

    "description":
    """You take a look out of the window and notice a garden and tree house in the forest that you didnt notice before. Maybe you should go check it out.""",

    "Carriable": False
}

item_keypad = {
    "id": "keypad",

    "name": "Keypad",

    "mass": 0,

    "description":
    """It is asking for a 4 digit code""",

    "Carriable": False
}

item_whiteboard = {
    "id": "whiteboard",

    "name": "Whiteboard",

    "mass": 120,

    "description":
    """In Red pen are the digits 0011""",

    "Carriable": False
}

item_notebook = {
    "id": "notebook",

    "name": "Notebook",

    "mass": 120,

    "description":
    """On the first page of the notebook are the digits 0010, the rest of the book is blank""",

    "Carriable": True
}

item_graffiti = {
    "id": "wallgraffiti",

    "name": "Wall Graffiti",

    "mass": 0,

    "description":
    """The digits 0011 are spray painted onto the wall""",

    "Carriable": False
}

item_scratch = {
    "id": "wallengraving",

    "name": "Wall Engraving",

    "mass": 0,

    "description":
    """on the wall next to the keypad the digits 1001 are scratched into the stone""",

    "Carriable": False
}

# ======================================================================================================================
# FLOOR 1
f1room_reception = {
    "name": "Reception",

    "description":
    """This is the reception. You can't see much around here, other than a ring on the desk. 
You don’t know what you’ll need. To the east is a long hall, with other rooms. 
Perhaps down there you can find more.""",

    "cleared": False,

    "exits": {"east": "Hall"},

    "items": [item_ring],

    "visible": True
}

f1room_hall = {
    "name": "Hall",

    "description":
    """A hall stretches in front of you. 
To the north is a tutor office, south is a lab and at the end, in the east, is a lecture hall,
as well as reception in the west. Your surroundings seem sparse, 
but there may be more to find in the rooms around you.""",

    "cleared": False,

    "exits": {"north": "Your Tutors Office","east": "Lecture Hall", 
              "west": "Reception", "south": "Computer Lab"},

    "items": [],

    "visible": True
}

f1room_lecture = {
    "name": "Lecture Hall",

    "description":
    """This room is huge, lined with hundreds of chairs. 
It's eerily quiet. Looking around, a small box catches you eye. 
Peering closer, you see it's a book: "Computer Poetry", by Kirill S!*%@#. 
(The surname seems to been scratched off).
You don't know if it's about poems or coding. Either way, seems like an interesting book.""",

    "cleared": False,

    "exits": {"west": "Hall"},

    "items": [item_Old_Book, item_whiteboard],

    "visible": True
}

f1room_complab = {
    "name": "Computer Lab",

    "description":
    """The lights on the ceiling are flickering. Chairs are scattered around, some fallen over. 
A tutor's ID card lies on the floor.  Dozens of computers litter the room, all black except for one. 
In the corner a laptop left on displays enter password. North is the way back to the hall.""",

    "cleared": False,

    "exits": {"north": "Hall"},

    "items": [item_usb_dirve, item_laptop],

    "visible": True
}

f1room_tutor = {
    "name": "Your Tutors Office",

    "description":
    """The tutors' chair sits vacant; their desk is a mess and covered with papers and some cigarettes.
Looking closely, you notice one of these papers has what seems to be a password. 
On the other side of the room is a bookshelf, almost full with space for one more book.""",

    "cleared": False,

    "exits": {"south": "Hall"},

    "items": [item_Stickynote, item_cigarettes],

    "visible": True
}

f1room_abacws_portal = {
    "name": "Abacws Portal Room",

    "description":
    """This room seems mysterios, it has some sort of portal frame in the middle. 
Maybe if the portal is active, you could step through and take a look. 
Strange? Why would a computer science school have worked on portal technology.""",

    "cleared": False,

    "exits": {"west":"Your Tutors Office"},

    "items": [],

    "visible": True
}

#FLOOR 2
f2room_woods_tree = {
    "name": "Large Tree Clearing",

    "description":
    """Tall thin trees tower over you and there is moss and shrubbery all around. 
It may be easy to get lost. You are in the woods. 
A laminated, worn-down poster reads “Warning: mysterious creature spotted nerby”.  """,

    "cleared": False,

    "exits": {"south": "Garden","east":"Wooden Shack"},

    "items": [],

    "visible": True
}

f2room_garden = {
    "name": "Garden",

    "description":
    """You take a look around and see a garden. This garden sticks out, it doesnt fit the eerieness of the forest.""",

    "cleared": False,

    "exits": {"north":"Large Tree Clearing", "up": "Treehouse"},

    "items": [item_example],

    "visible": False
}

f2room_treehouse = {
    "name": "Treehouse",

    "description":
    """This treehouse seems to have been home to a young child.""",

    "cleared": False,

    "exits": {"down": "Garden"},

    "items": [item_toy],

    "visible": True
}



f2wooden_shack = {
    "name": "Wooden Shack",

    "description":
    """You enter a worned down shed. In this shack, the wood is rotting and the air smells stagnant.
Everything inside is ragged and broken. Dangling from the ceiling is a dusty lantern.""",

    "cleared": False,

    "exits": {"east":"Middle of the Woods", "west": "Large Tree Clearing"},

    "items": [item_lighter, item_lantern],

    "visible": True
}

f2room_woods_lost = {
    "name": "Middle of the Woods",

    "description":
    """Another wooded and leafy clearing surrounds you, the ground in shadow from the trees above. 
This place is strange, rocks inscribed with green writing. You see an creepy altar in the distance.""",

    "cleared": False,

    "exits": {"east":"Altar", "south": "Rock Circle Clearing", 
              "north": "Rock Circle Clearing", "west": "Wooden Shack"},

    "items": [item_mineKey],

    "visible": True
}

f2room_woods_rock = {
    "name": "Rock Circle Clearing",

    "description":
    """You go further into the woods, you seem lost, try retracing your steps maybe. 
All you see is a large circle of rocks, incircling a campfire that looks to have not been lit in a while.
You see blood spread accross the rocks.""",

    "cleared": False,

    "exits": {"north": "Middle of the Woods", "south": "Middle of the Woods"},

    "items": [item_notebook],

    "visible": True
}

f2room_altar = {
    "name": "Altar",

    "description":
    """You have entered what appears to be an altar room. 
The altar is covered with dirt and weeds, but its surface is still visible,
marked by strange patterns. This altar is surrounded by 5 small candles.  """,

    "cleared": False,

    "exits": {"west": "Middle of the Woods"},

    "items": [],

    "visible": True,

    "candles_lit": False
}

#FLOOR 3
f3room_morgue = {
    "name": "Morgue",

    "description":
    """You notice one of the other body bags is now empty where has the body gone.""",

    "description1":
    """Your head hurts in confusion.
Are you dead already? But since you can read this, you are probably not.
You cannot see anything, why is it so dark?
It is because you are in a body bag. So you unzip it and realise you're in a morgue!
""",
    
    "description2":
    """This is the morgue, there is your empty body bag and another body zipped up. I woundn't go near it if I where you.""",

    "cleared": False,

    "exits": {"west": "Observation Room", "north": "Surgery"},

    "items": [item_window],

    "visible": True
}

f3room_surgery = {
    "name": "Surgery",

    "description":
    """Tools litter the desks, among them is a surgical scalpel.
A blood-stained table lies in the centre. The lights are dim, the air stagnant.""",

    "cleared": False,

    "exits": {"south": "Morgue"},

    "items": [item_surgical_scalpel],

    "visible": True
}

f3room_Observation = {
    "name": "Observation Room",

    "description":
    """Wide, grime covered windows look down on the morgue.
Ripped notes scatter the desks, along with dust covered binoculars.""",

    "cleared": False,

    "exits": {"south": "Morgue", "west": "Archives"},

    "items": [item_binoculars, item_graffiti],

    "visible": True
}

f3room_archives = {
    "name": "Archives",

    "description":
    """Filing cabinets line the walls, some half open. Most contain various pieces of paperwork but one, 
a post-mortem, catches your eye. To get back to the observation room, go east.""",

    "cleared": False,

    "exits": {"east": "Observation Room"},

    "items": [item_file],

    "visible": True
}

# FLOOR 4

f4room_mine_entrance = {
    "name": "Mine Entrance",

    "description":
    """Through the darkness, you see that rock surrounds you, held up by wooden beams.
This place is a mine. In the east is rocky rubble, blocking your way. """,

    "cleared": False,

    "exits": {"east": "Mineshaft Tunnel"},

    "items": [item_dynamite],

    "visible": True
}

f4room_rubble = {
    "name": "Mineshaft Tunnel",

    "description":
    """Stones are piled all the way to the ceiling. At the moment, there’s no way through.
There are no other passages except the mineshaft entrance east and the other side of the rubble east,
so you’ll need something to clear the way. """,

    "description_cleared":
    """The rubble no longer blocks your path, The mine entrance is to the east.""",

    "cleared": False,

    "exits": {"west": "Mine Entrance", "east": "Mineshaft Gate"},

    "items": [item_pickaxe, item_Portal_Gun],

    "visible": True
}

f4room_gate = {
    "name": "Mineshaft Gate",

    "description":
    """You have reached the rusty gate of the mine, light shining in from the outside.
This gate is locked, and requires a key. On the gate theirs a sign that reads KEEP OUT OR ELSE """,

    "description_cleared":
    """You have reached the rusty gate of the mine, light shining in from the outside. 
    The gate is unlocked. On the gate theirs a sign that reads KEEP OUT OR ELSE """,

    "cleared": False,

    "exits": {"west": "Mineshaft Tunnel", "east": "Haunted Mineshaft"},

    "items": [],

    "visible": False
}

f4room_ghost = {
    "name": "Haunted Mineshaft",

    "description":
    """Ghosts surround you like a pale mist, clouding your vision but you can see an iron door at the end of the mine. 
    There is one ghost staring at you, maybe you should interact with them, he could help you, or they could kill you.... """,

    "description_cleared":
    """A ghost quietly plays with a toy in the corner of the room.""",

    "cleared": False,

    "exits": {"west": "Mineshaft Gate", "east": "Iron Door"},

    "items": [],

    "visible": False
}

f4room_keypad = {
    "name": "Iron Door",

    "description":
    """Its a big iron door with a keypad next to it.""",

    "cleared": False,

    "exits": {"east": "Haunted Mineshaft"},

    "items": [item_scratch, item_keypad],

    "visible": False
}

rooms = {
    #FLOOR 1
    "Reception": f1room_reception,
    "Hall": f1room_hall,
    "Computer Lab": f1room_complab,
    "Lecture Hall": f1room_lecture,
    "Your Tutors Office": f1room_tutor,
    "Abacws Portal Room": f1room_abacws_portal,
    #FLOOR 2
    "Large Tree Clearing": f2room_woods_tree,
    "Garden": f2room_garden,
    "Treehouse": f2room_treehouse,
    "Wooden Shack": f2wooden_shack,
    "Middle of the Woods": f2room_woods_lost,
    "Rock Circle Clearing": f2room_woods_rock,
    "Altar": f2room_altar,
    #FLOOR 3
    "Morgue": f3room_morgue,
    "Surgery": f3room_surgery,
    "Observation Room": f3room_Observation,
    "Archives": f3room_archives,
    #FLOOR 4
    "Mine Entrance": f4room_mine_entrance,
    "Mineshaft Tunnel": f4room_rubble,
    "Mineshaft Gate": f4room_gate,
    "Haunted Mineshaft": f4room_ghost,
    "Iron Door":f4room_keypad
}

floor2 = ["Large Tree Clearing", "Wooden Shack", "Middle of the Woods", "Rock Circle Clearing"]

