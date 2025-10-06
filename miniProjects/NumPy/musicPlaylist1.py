
import numpy as np

songs= np.array([
    "song1", "song2", "song3", "song4", "song5",
    "song6", "song7", "song8", "song9", "song10"
])

print("Original Playlist: ",songs)

shuffled = np.random.permutation(songs)

print("Shuffled Playlist: ",shuffled)
