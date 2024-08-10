import tqdm
import requests
import os
import os.path
from mutagen.mp4 import MP4, MP4Cover

def download_song(song_dwn_url, song_title, download_path):
    with requests.get(song_dwn_url, stream=True) as r, open(os.path.join(download_path, song_title)+".m4a", "wb") as f:
        file_size = int(r.headers['Content-Length'])
        for chunk in tqdm.tqdm(
        r.iter_content(chunk_size=1024),
        total= int(file_size / 1024),
        unit = 'KB',
        desc = "Downloading {}".format(song_title),
        leave = True,
        ):
            f.write(chunk)


def download_image(image_url, img_path):
    response = requests.get(image_url)
    with open(img_path, 'wb') as f:
        f.write(response.content)

def delete_img(image_path):
    if os.path.isfile(image_path):
        os.unlink(image_path)
        print("Image Removed  "+image_path+"\n")

    else:
        print(image_path+"  not removed")

def save_metadata(audio_path, song_name, artist_name, featured_artist, img_path, album, year, genre):
    audio = MP4(audio_path)
    audio['\xa9nam'] = song_name
    audio['\xa9alb'] = album
    audio['aART'] = artist_name
    if featured_artist != '':
        audio['\xa9ART'] = artist_name + ", " + featured_artist
    else:
        audio['\xa9ART'] = artist_name
    audio['\xa9day'] = year
    audio['\xa9gen'] = genre
    with open(img_path, "rb") as f:
        audio["covr"] = [
            MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
        ]
    audio.save()
    delete_img(img_path)

def download_details(song_data,download_path):

    song_name = song_data['song'].replace('?', '').replace(':','').strip()
    song_title = song_name

    audio_path = os.path.join(download_path, song_title)+".m4a"
    img_path = os.path.join(download_path, song_title) + ".jpg"

    song_dwn_url =  song_data['media_url']
    album = song_data['album']
    year = song_data['year']
    lang = song_data['language']
    lang = lang[0].upper() + lang[1:]
    image_url = song_data['image']
    artist_name = song_data['primary_artists']
    featured_artist = song_data['featured_artists']

    download_song(song_dwn_url = song_data['media_url'], song_title = song_title, download_path=os.path.abspath(os.getcwd()))
    download_image(image_url, img_path)
    save_metadata(audio_path, song_name, artist_name, featured_artist, img_path, album, year, genre=lang)
    
    print("Done with downloading :{}.................\n".format(song_title))
