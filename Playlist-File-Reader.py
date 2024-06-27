# Python program to read and sort spotify playlists from json files
# Specifically spotify playlist files requested from Spotify
# Results exported to csv file
# Made by Dominic Salamone 6/25/24

import json
import csv

#user input for file path
#fileName = input("Enter Spotify JSON file path: ")

fileName1 = r"C:\Users\domsa\OneDrive\Documents\Spotify\my_spotify_data\Spotify Account Data\Playlist1.json"
fileName2 = r"C:\Users\domsa\OneDrive\Documents\Spotify\my_spotify_data\Spotify Account Data\Playlist2.json"

#open files with proper encoding type
with open(fileName1, 'r', encoding="utf8") as f:
	data1 = json.load(f)

with open(fileName2, 'r', encoding="utf8") as f:
	data2 = json.load(f)	
	
#create output csv file, forces encoding type to match file source
with open('Spotify.csv', 'w', newline='', encoding='utf8') as csvfile:
	
	#creates headers for csv file
	fieldnames = ['playlist', 'trackName', 'artistName', 'albumName', 'trackUri']
	
	#creates csv writer, includes ignore for track parameters not being searched for
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')

	writer.writeheader()

	#iterate through each playlist in list
	for playlist in data1['playlists']:
		playlistName = playlist['name']

		#iterates through each song in each playlist and retrieves song info
		for song in playlist['items']:
			if song['track'] is not None:
				trackName = song['track']['trackName']
				artistName = song['track']['artistName']
				albumName = song['track']['albumName']
				trackUri = song['track']['trackUri']

				#writes song info to csv file
				writer.writerow({'playlist': playlistName, 'trackName': trackName, 'artistName': artistName, 'albumName': albumName, 'trackUri': trackUri})

	#iterate through each playlist in list
	for playlist in data2['playlists']:
		playlistName = playlist['name']

		#iterates through each song in each playlist and retrieves song info
		for song in playlist['items']:
			if song['track'] is not None:
				trackName = song['track']['trackName']
				artistName = song['track']['artistName']
				albumName = song['track']['albumName']
				trackUri = song['track']['trackUri']

				#writes song info to csv file
				writer.writerow({'playlist': playlistName, 'trackName': trackName, 'artistName': artistName, 'albumName': albumName, 'trackUri': trackUri})
	

	
