from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
import os

def addToPlaylist():
  
  os.chdir(path + '/Playlists/'+playlistTitle)

  with open("songs.txt", "r") as f:
    text = f.read()
  text = text.split("\n")
  f.close()

  os.chdir(path+'/Songs')

  songs = os.listdir()

  if "playlist" not in url:
    try:
      yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
      t = yt.title
      for char in l:
        for e in range(t.count(char)):
          t = list(t)
          t.remove(char)
          t = "".join(t)
      if t + ".mp4" not in songs:
        yt.streams.get_audio_only().download(filename=f'{t}.mp4')
      if t + ".mp4" not in text:
        text.append(t + ".mp4")
    except VideoUnavailable:
      print("Video is unavailable")
  else:
    pl = Playlist(url) 
    for ur in pl.video_urls:
      try:
        yt = YouTube(ur, use_oauth=True, allow_oauth_cache=True)
        t = yt.title
        for char in l:
          for e in range(t.count(char)):
            t = list(t)
            t.remove(char)
            t = "".join(t)
        if t + ".mp4" not in songs:
          yt.streams.get_audio_only().download(filename=f'{t}.mp4')
        if t + ".mp4" not in text:
          text.append(t + ".mp4")
      except VideoUnavailable:
        continue

  os.chdir(path+'/Playlists/'+playlistTitle)

  for i in range(text.count("")):
    text.remove("")

  with open("songs.txt", "w") as f:
    f.write("\n".join(text))
  f.close()


def createPlaylist():

  pl = Playlist(url)

  os.chdir(path + '/Songs')

  songs = os.listdir()

  text = []

  for u in pl.video_urls:
    try:
      yt = YouTube(u, use_oauth=True, allow_oauth_cache=True)
    except VideoUnavailable:
      continue
    t = yt.title
    for char in l:
      for e in range(t.count(char)):
        t = list(t)
        t.remove(char)
        t = "".join(t)
    
    text.append(t+'.mp4')
    if t+'.mp4' not in songs:
      yt.streams.get_audio_only().download(filename=f'{t}.mp4')

  title = pl.title

  os.chdir(path+'/Playlists')
  os.mkdir(title)

  os.chdir(title)

  finalTxt = "\n".join(text)

  with open("songs.txt", 'w') as f:
    f.write(finalTxt)
  f.close()

l = "'\",./\\|~#%^*+=_<>@&$!?:;-()[]{} "
path = os.getcwd()
path = path[:-5]

with open("tmp.txt", "r") as f:
  u = f.read()
  u = u.strip()
if u.find(" ") != -1:
  w = u.find(" ")
  u = [u[:w], u[w+1:]] #[url, name]
  url = str(u[0])
  playlistTitle = str(u[1])
  addToPlaylist()
else:
  url = u
  createPlaylist()
f.close()

os.chdir(path + "/Code")

with open("tmp.txt", "w") as nf:
  nf.write(" ")

os.system("deactivate")
os.system("open shortcuts://")
