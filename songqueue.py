songs = [] 
def music_queue(song_name):
    songs.append(song_name)
def pop():
    return songs.pop(0)
def rm_queue(position):
    songs.pop(position)
