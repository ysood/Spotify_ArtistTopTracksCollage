from PIL import Image
from dotenv import load_dotenv
import os
import base64
import requests
from requests import post,get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url,headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1" #limit ensures its most popular artist

    query_url = url + query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist found")
        quit()
        return None
    
    return json_result[0]

def get_songs(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_artworks(url,name):
    response = requests.get(url)
    with open(f"{name}.jpg", "wb") as f:
        f.write(response.content)

def create_collage():
    images = [Image.open(f"{i}.jpg") for i in range(1,5)]  # Replace ".jpg" with your actual image extension

    # Resize images to 540x540 (half of 1080) before pasting to create the collage
    resized_images = [img.resize((540, 540)) for img in images]

    # Create a blank image for the collage
    collage = Image.new('RGB', (1080, 1080))

    # Paste resized images onto the collage
    collage.paste(resized_images[0], (0, 0))
    collage.paste(resized_images[1], (540, 0))
    collage.paste(resized_images[2], (0, 540))
    collage.paste(resized_images[3], (540, 540))

    # Save or display the collage
    collage.save("collage.jpg")  # Save the collage as an image file
    collage.show()  # Display the collage

def main():
    token = get_token()
    query = input("Enter Artist Name: ")
    result = search_artist(token,query)
    artist_id = result["id"]

    songs = get_songs(token,artist_id)


    for x in range(1,5):
        images = songs[x]['album']['images']
        image_url = images[0]['url']
        get_artworks(image_url,str(x))
    
    create_collage()

if __name__ == "__main__":
    main()







