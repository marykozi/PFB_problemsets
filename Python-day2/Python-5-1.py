#!/usr/bin/env python3

#Write a script in which you construct a dictionary of your favorite things.
#Some of my favorites:
#Type	Favorite
#book	Jitterbug Perfume
#song	Tom Petty - I Won't Back Down
#tree	Cedar


fav_dict = { "book" : "Jitterbug Perfume", "song" : "Tom Petty - I Won't Back Down", "tree" : "Cedar"}

print(fav_dict['book'])  #Print out your favorite book.

fav_thing = 'book'
print(fav_dict[fav_thing])  #Print out your favorite book but use a variable in the key.

fav_thing = 'tree'
print(fav_dict[fav_thing])   #Now print your favorite tree.

fav_dict.update({"organism" : "bacteria"})  #Add your favorite 'organism' to the dictionary. Make organism the new value of fav_thing

fav_thing = 'organism'
print(fav_dict[fav_thing])

#Take a value from the command line for fav_thing and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from. Check out input(). Here is a link.

for fav_key in fav_dict:
	print("Select one favorite thing", fav_key)

user_input = input("Type a favorite thing:")
fav_thing = user_input
user_input = input("Type a favorite type of thing:")
fav_type = user_input

print(fav_thing, fav_type)

#Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.
fav_dict.update({fav_thing : fav_type})

#Use a for loop to print out each key and value of the dictionary.
for fav_key in fav_dict:
	print("Favorite things", fav_key, '\t', fav_dict[fav_key])













