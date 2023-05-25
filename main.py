# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import requests
# from PIL import ImageTk, Image
# import tkinter as tk
# import io
#
# def get_current_track_info(sp):
#     current_track = sp.current_user_playing_track()
#     if current_track is not None and current_track['is_playing']:
#         track_name = current_track['item']['name']
#         artist_name = current_track['item']['artists'][0]['name']
#         album_name = current_track['item']['album']['name']
#         album_cover_url = current_track['item']['album']['images'][0]['url']
#         track_id = current_track['item']['id']
#
#         return track_name, artist_name, album_name, album_cover_url, track_id
#
#     return None
#
# def update_album_cover():
#     global previous_track_id, previous_album_cover
#     current_track_info = get_current_track_info(sp)
#     if current_track_info is not None:
#         track_name, artist_name, album_name, album_cover_url, track_id = current_track_info
#         print(f"Currently playing: {track_name} by {artist_name}")
#         response = requests.get(album_cover_url)
#         image_data = response.content
#
#         # Only update the album cover if the track has changed
#         if track_id != previous_track_id:
#             previous_track_id = track_id
#             previous_album_cover = ImageTk.PhotoImage(Image.open(io.BytesIO(image_data)))
#
#         # Update the label with the stored album cover image
#         album_cover_label.configure(image=previous_album_cover)
#         album_cover_label.image = previous_album_cover
#
#     else:
#         print("No track currently playing.")
#
#     # Schedule the next album cover update
#     window.after(5000, update_album_cover)
#
# # Create the Tkinter window
# window = tk.Tk()
# window.title("Spotify Album Cover Viewer")
#
# # Create a label to display the album cover
# album_cover_label = tk.Label(window)
# album_cover_label.pack()
#
# # Set up Spotify authentication
# scope = "user-read-currently-playing"
# username = "Rohanagni11"
# client_id = "a5f6ed27ca2b416daa27d5e39f5f5877"import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import requests
# from PIL import ImageTk, Image
# import tkinter as tk
# import io
#
# def get_current_track_info(sp):
#     current_track = sp.current_user_playing_track()
#     if current_track is not None and current_track['is_playing']:
#         track_name = current_track['item']['name']
#         artist_name = current_track['item']['artists'][0]['name']
#         album_name = current_track['item']['album']['name']
#         album_cover_url = current_track['item']['album']['images'][0]['url']
#         track_id = current_track['item']['id']
#
#         return track_name, artist_name, album_name, album_cover_url, track_id
#
#     return None
#
# def update_album_cover():
#     global previous_track_id, previous_album_cover
#     current_track_info = get_current_track_info(sp)
#     if current_track_info is not None:
#         track_name, artist_name, album_name, album_cover_url, track_id = current_track_info
#         print(f"Currently playing: {track_name} by {artist_name}")
#         response = requests.get(album_cover_url)
#         image_data = response.content
#
#         # Only update the album cover if the track has changed
#         if track_id != previous_track_id:
#             previous_track_id = track_id
#             previous_album_cover = ImageTk.PhotoImage(Image.open(io.BytesIO(image_data)))
#
#         # Update the label with the stored album cover image
#         album_cover_label.configure(image=previous_album_cover)
#         album_cover_label.image = previous_album_cover
#
#     else:
#         print("No track currently playing.")
#
#     # Schedule the next album cover update
#     window.after(5000, update_album_cover)
#
# # Create the Tkinter window
# window = tk.Tk()
# window.title("Spotify Album Cover Viewer")
#
# # Create a label to display the album cover
# album_cover_label = tk.Label(window)
# album_cover_label.pack()
#
# # Set up Spotify authentication
# scope = "user-read-currently-playing"
# username = "Rohanagni11"
# client_id = "a5f6ed27ca2b416daa27d5e39f5f5877"
# client_secret = "a5ae4fd03e1f4d0ea1120a4d7d0d4c4c"
# redirect_uri = "https://open.spotify.com/?"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
#
# # Global variables to store the previous track details
# previous_track_id = None
# previous_album_cover = None
#
# # Update the album cover initially
# update_album_cover()
#
# # Start the Tkinter event loop
# window.mainloop()
#
# client_secret = "a5ae4fd03e1f4d0ea1120a4d7d0d4c4c"
# redirect_uri = "https://open.spotify.com/?"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
#
# # Global variables to store the previous track details
# previous_track_id = None
# previous_album_cover = None
#
# # Update the album cover initially
# update_album_cover()
#
# # Start the Tkinter event loop
# window.mainloop()
