# Exercises 8.6 to 8.8


def describe_city(city_name, city_country="Ecuador"):
    """ Returns City - Country Pair info in requested format """
    build_description = '"' + city_name + ', ' + city_country + '"'
    return build_description

get_city_formatted = describe_city("Quito")
print(get_city_formatted)
get_city_formatted = describe_city("Guayaquil")
print(get_city_formatted)
get_city_formatted = describe_city(city_name="Bogota", city_country="Colombia")
print(get_city_formatted)
get_city_formatted = describe_city("Lima", "Peru")
print(get_city_formatted)


def make_album(album_artist, album_title, album_songs=""):
    """ Return Album Info as a Dictionary """
    album_info = {"artist": album_artist, "title": album_title}
    if album_songs:
        album_info["songs"] = album_songs
    return album_info

music_album = make_album(album_artist="Nirvana", album_title="Unplugged")
print(music_album)
music_album = make_album(album_artist="U2", album_title="Estes o no Estes", album_songs="11")
print(music_album)
music_album = make_album(album_artist="CNCO", album_title="Reggeaton Lento", album_songs="3")
print(music_album)

# Exercise 8.8
while True:
    print('Input "q" any time to exit')
    artist = input("Enter Album's Artist: ")
    if artist == "q":
        break
    title = input("Enter Album's Title: ")
    if title == "q":
        break
    album_songs = input("Number of song in this album: ")
    if album_songs == "q":
        break
    music_album = make_album(album_artist=artist, album_title=title, album_songs=album_songs)
    print(music_album)
