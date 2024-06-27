# Python program to read spotify library from json files
# Specifically spotify playlist files requested from Spotify
# Results exported to csv file
# Made by Dominic Salamone 6/26/24

import json
import csv

#user input for file path
fileName = input("Enter Spotify JSON file path: ")

#open files with proper encoding type
with open(fileName, 'r', encoding="utf8") as f:
	data = json.load(f)
	
#create output csv file, forces encoding type to match file source
with open('Spotify_My_Library.csv', 'w', newline='', encoding='utf8') as csvfile:
	
	#creates headers for csv file
	fieldnames = ['artist', 'album', 'track', 'uri']
	
	#creates csv writer, includes ignore for track parameters not being searched for
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()

	#iterate through each track in list and retrieve track info
	for song in data['tracks']:

		if song is not None:
			artist = song['artist']
			album = song['album']
			track = song['track']
			uri = song['uri']

			#writes song info to csv file
			writer.writerow({'artist': artist, 'album': album, 'track': track, 'uri': uri})
