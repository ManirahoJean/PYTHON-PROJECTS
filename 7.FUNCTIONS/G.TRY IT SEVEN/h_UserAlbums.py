# 7.8 User Album

"""
7-7. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.

"""


def make_album(artist_name, album_title):
    """Return a dictionary containing information"""
    artist = {'name': artist_name, 'title': album_title}
    return artist


while True:
    print("\nTell me artist and and album's title")
    print("enter 'q' any time to quit")

    name_artist = input("enter name of the artist: ")
    if name_artist == 'q':
        break
    title_album = input("enter title of the album: ")
    if title_album == 'q':
        break

    my_album = make_album(name_artist, title_album)
    print(f"{my_album}, is a good singer!")
