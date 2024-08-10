import jiosavan
import os
import song_detail

download_path = 'D:\\practice\\Music\\music'

def song_id_down(song_id,download_path):
  song_data = jiosavan.get_song(str(song_id))
  song_detail.download_details(song_data, download_path)
  

def main():
    query = input("Enter the song name :\n")

    data_from_search = jiosavan.search_for_query(query)
    print('Songs for the query:',query)
    count = 0
    for song in data_from_search['songs']:
      song_name = song['title']
      song_desc = song['description']
      lang = song['more_info']['language']
      count+=1
      print("{} {}\n     {}".format(count,song_name,song_desc))

    if(len(data_from_search['albums']))!=0:
      print('Albums for the query:',query)
      count = 0
      for song in data_from_search['albums']:
        song_name = song['title']
        song_desc = song['description']
        lang = song['more_info']['language']
        count+=1
        print("{} {}\n     {}\n     Lang :{}".format(count,song_name,song_desc,lang))
    
    if(len(data_from_search['artists']))!=0:
      print('Artists for the query:',query)
      count = 0
      for song in data_from_search['artists']:
        song_name = song['title']
        song_desc = song['description']
        count+=1
        print("{} {}\n     {}\n    ".format(count,song_name,song_desc))

    if(len(data_from_search['playlists']))!=0:
      print('Playlists for the query:',query)
      count = 0
      for song in data_from_search['playlists']:
        song_name = song['title']
        song_desc = song['description']
        lang = song['language']
        count+=1
        print("{} {}\n     {}\n     Lang :{}".format(count,song_name,song_desc,lang))

  
    selection = input("Type  a,b,c song numbers using ,, ").strip().split(',')
    selection_input = selection[0]
    select_int = [int(x) for x in selection[1:] if x.isdigit()]

    

    if selection_input[0] == 'a':
      for song_num in select_int[0:]:
        song_id = data_from_search['songs'][int(song_num-1)]['id']
        print(data_from_search['songs'][int(song_num-1)]['title'])

        # song_data = jiosavan.get_song(str(song_id))
        # song_detail.download_details(song_data, download_path)

        song_id_down(song_id,download_path)

    elif selection_input[0] == 'b':
      for album_num in select_int[0:]:
        album_id = data_from_search['albums'][int(album_num-1)]['id']
        print(data_from_search['albums'][int(album_num-1)]['title'])
        album_data = jiosavan.search_albums(album_id)
        [song_id_down(song_id_,download_path) for song_id_ in album_data]
        print("Album Downloaded\n")


    elif selection_input[0] == 'c':
      for playlist_num in select_int[0:]:
        playlist_id = data_from_search['playlists'][playlist_num-1]['id']
        print(data_from_search['playlists'][playlist_num-1]['title'])
        playlist_data = jiosavan.search_playlists(playlist_id)
        [song_id_down(song_id_,download_path) for song_id_ in playlist_data]
        print("Playlist Downloaded")


    elif selection_input[0] == 'd':
      for artist_num in select_int[0:]:
        artist_id = data_from_search['artists'][artist_num-1]['id']
        print(data_from_search['artists'][playlist_num-1]['title'])
        artist_data = jiosavan.search_artist(artist_id)

main()