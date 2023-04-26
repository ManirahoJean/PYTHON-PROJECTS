# 7.7 Album
"""
7-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""


def make_album(artist_name, album_title):
    """Return a dictionary containing information"""
    artist = {'name': artist_name.title(), 'title': album_title.title()}
    return artist


my_album = make_album('mbonyi', 'ibihe')
print(my_album)
my_album = make_album('jay polly', 'rusumbanzika')
print(my_album)
my_album = make_album('kizito', 'inuma')
print(my_album)

print("\n")

# With number of songs included


def make_album(artist_name, album_title, songs=None):
    """Return a dictionary containing information"""
    artist = {'name': artist_name.title(), 'title': album_title.title()}

    if songs:
        artist['songs'] = songs
    return artist


my_album = make_album('alex kagame', "umurunga w'iminsi")
print(my_album)

my_album = make_album('kizito', 'arc en ciel', 200)
print(my_album)

my_album = make_album('bull dog', 'custer care', '50')
print(my_album)
