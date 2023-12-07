# Spotify Artist Collage Generator
This Python script utilizes the Spotify API to generate a collage of album artworks for the top tracks of a specified artist. The collage is created by fetching the top tracks of the artist, downloading the corresponding album artworks, and combining them into a single image.

## Prerequisites
Before running the script, make sure you have the following:

1. **Spotify Developer Account:** 
Log into https://developer.spotify.com/dashboard using your Spotify account.
2. **Obtain the `CLIENT_ID` and `CLIENT_SECRET`**: Create an app at the same link and select "Web API" for the question asking which APIs are you planning to use. Once you have created your app, you will have access to the app credentials. These will be required for API authorization to obtain an access token.


   
## Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/ysood/Spotify_ArtistTopTracksCollage.git
cd Spotify_ArtistTopTracksCollage
```
2. Install required dependencies:
```bash
   pip install -r requirements.txt
   ```

3. Setup Environment Variables:
    ```
    open '.env_sample' and rename it to '.env'
    replace CLIENT_ID and CLIENT_SECRET with your own credentials obtained from your developer account. 
    
    
## Usage
Run the script by executing the following command in your terminal or command prompt:

```
python3 spotify_artistTopTrackCollage.py 
```
Enter the name of the artist when prompted.

The script will fetch the top tracks of the artist from Spotify, download the album artworks, and create a 4 picture collage.
The resulting collage image (collage.jpg) will be saved in the project directory.

## Notes
This version creates a collage of the most popular tracks *after* the 1st one. This is in line with my work for Nitrility, wherein we already used the most popular track elsewhere, and so created the post with tracks 2-5.

To change modify this range to the top 4 tracks, change the code in line 91:
```
#before
for x in range(1,5):

#after
for x in range(0,4):
```

The collage is saved as a JPEG image file and displayed for visual inspection.

Feel free to customize and enhance the script according to your needs. For more information about the Spotify API, refer to the Spotify for Developers documentation.