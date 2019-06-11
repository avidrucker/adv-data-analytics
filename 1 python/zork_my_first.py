room_names = ["foyer","front room","library","kitchen","dining room","vault","parlor","secret room"]
room_texts = ["a foyer","the front room of an old house","a library","a dusty kitchen","a lonely dining room","a vault","an elaborate parlor","a secret room"]
room_contents = ["a dead scorpion","a piano","spiders","bats","dust, empty box","3 walking skeletons","treasure chest","piles of gold"]
exits = [["n2"],["s1","w3","e4"],["e2","n5"],["w2","n7"],["s3"],["e7","e8"],["w6","s4"],["w6"]]

def char_to_dir(c):
	if c == "n": return "north"
	elif c == "s": return "south"
	elif c == "e": return "east"
	else: return "west" 

# takes a list of exits as letter number combos, returns a string describing the possible exists
def get_exits(x_list):
	temp_list = [] # prepare temp list
	for x in range(len(x_list)):
		temp_list.append(f"({x+1}) exit to the {char_to_dir(x_list[x][0])}")
	return ', '.join(temp_list)
	
playing, current_room = True, 0
while playing:
	print("="*60)
	print(f"You are standing in {room_texts[current_room]}")
	print(f"You see {room_contents[current_room]}")
	print(f"You can {get_exits(exits[current_room])}. Press (Q) to quit:")
	choice = input("What do you do?")
	
	if str.lower(choice) == "q":
		playing = False
	elif choice.isdigit() and (int(choice)-1) < len(exits[current_room]):
		print(f"-- changing room to room #{int(exits[current_room][int(choice)-1][1])} --")
		current_room = int(exits[current_room][int(choice)-1][1])-1
	else:
		print("See you!")
print("Thanks for playing!")
# todo: define win condition, congratulate user & end on win