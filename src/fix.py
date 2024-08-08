import os

path = os.getcwd()
path = path[:-5]
os.chdir(path + "/Playlists")

l = "'\",./\\|~#%^*+=_<>@&$!?:;-()[]{} "

for d in os.listdir():
	os.chdir(d)
	with open("songs.txt", "r") as f:
		songs = f.read()
	f.close()
	songs = songs.split("\n")
	for i, song in enumerate(songs):
		song = song[:-4]
		for char in l:
			for e in range(song.count(char)):
				song = list(song)
				song.remove(char)
				song = "".join(song)
		songs[i] = song + ".mp4"
	with open ("songs.txt", "w") as f:
		f.write("\n".join(songs))
	f.close()
	os.chdir(path + '/Playlists')
	
os.chdir(path + '/Songs')

for d in os.listdir():
	song = d
	song = song[:-4]
	for char in l:
		for e in range(song.count(char)):
			song = list(song)
			song.remove(char)
			song = "".join(song)
	os.rename(d, song + ".mp4")

print("fixed")
os.system("deactivate")
os.system("open shortcuts://")
