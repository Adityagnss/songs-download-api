# download_songs_api_

#### API written in Python 
This is a command tool 
one can easily download high quality songs, playlist ,albums etc
 ---
###### **NOTE:** You don't need to have JioSaavn link of the song in order to fetch the song details, you can directly search songs by their name. Fetching Songs/Albums/Playlists from URL is also supported in this API.  

 ---

### **Features**:
##### Currently the API can get the following details for a specific song in JSON format:
- **Song Name**
- **Singer Name**
- **Album Name**
- **Album URL**
- **Duration of Song**
- **Song Thumbnail URL (Max Resolution)**
- **Song Language**
- **Download Link**
- **Release Year**
- **Album Art Link (Max Resolution)**
- **Lyrics**
- .... and much more!

```json
{
            "id": "Z2qLihQs",
            "title": "Back To You",
            "image": "https://c.saavncdn.com/825/Back-To-You-English-2022-20221205160107-50x50.jpg",
            "album": "Back To You",
            "url": "https://www.jiosaavn.com/song/back-to-you/KloafR1YZkA",
            "type": "song",
            "description": "Lost Frequencies, Elley Duhe, X Ambassadors · Back To You",
            "ctr": 0,
            "position": 1,
            "more_info": {
               "primary_artists": "Lost Frequencies, Elley Duhe, X Ambassadors",
               "singers": "Lost Frequencies, Elley Duhe, X Ambassadors, Lost Frequencies, Elley Duhé, X Ambassadors",
               "video_available": null,
               "triller_available": false,
               "language": "english",
               "is_ringtone_available": false
    }
}
```
Clone this repository using
```sh
$ git clone https://github.com/reddy0852/download_songs_api_
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 main.py
```        
       
     
