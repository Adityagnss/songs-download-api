import jiosavan
import os
import song_detail
import threading 
import asyncio

download_path = 'D:\\practice\\Music\\music'

def song_id_down(song_id, download_path):
    song_data = jiosavan.get_song(str(song_id))
    song_detail.download_details(song_data, download_path)

def main():
    query = input("Enter the song,movie,playlist,artist name:\n")

    data_from_search = jiosavan.search_for_query(query)

    print(f"Songs for the query: {query}")
    for count, song in enumerate(data_from_search['songs'], 1):
        print(f"{count} {song['title']}\n     {song['description']}")

    if data_from_search['albums']:
        print(f"Albums for the query: {query}")
        for count, song in enumerate(data_from_search['albums'], 1):
            print(f"{count} {song['title']}\n     {song['description']}\n     Lang: {song['more_info']['language']}")

    if data_from_search['artists']:
        print(f"Artists for the query: {query}")
        for count, song in enumerate(data_from_search['artists'], 1):
            print(f"{count} {song['title']}\n     {song['description']}")

    if data_from_search['playlists']:
        print(f"Playlists for the query: {query}")
        for count, song in enumerate(data_from_search['playlists'], 1):
            print(f"{count} {song['title']}\n     {song['description']}\n     Lang: {song['language']}")

    selection = input("Type a,b,c song numbers using ,, ").strip().split(',')
    selection_input = selection[0]
    select_int = [int(x) for x in selection[1:] if x.isdigit()]

    

    if selection_input[0] == 'a':
        threads = []
        for song_num in select_int[0:]:
            song_id = data_from_search['songs'][int(song_num-1)]['id']
            print(data_from_search['songs'][int(song_num-1)]['title'])
            t = threading.Thread(target=song_id_down, args=(song_id, download_path))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()


    
    elif selection_input == 'b':
        threads = []
        for album_num in select_int[0:]:
            album_id = data_from_search['albums'][int(album_num-1)]['id']
            print(data_from_search['albums'][int(album_num-1)]['title'])
            album_data = jiosavan.search_albums(album_id)
            for song_id_ in album_data:
                t = threading.Thread(target=song_id_down, args=(song_id_, download_path))
                threads.append(t)
                t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()


    elif selection_input == 'c':
        for playlist_num in select_int:
            playlist_id = data_from_search['playlists'][playlist_num-1]['id']
            print(data_from_search['playlists'][playlist_num-1]['title'])
            playlist_data = jiosavan.search_playlists(playlist_id)
            [song_id_down(song_id_, download_path) for song_id_ in playlist_data]
            print("Playlist Downloaded")

    elif selection_input == 'd':
        for artist_num in select_int:
            artist_id = data_from_search['artists'][artist_num-1]['id']
            print(data_from_search['artists'][artist_num-1]['title'])
            
main()