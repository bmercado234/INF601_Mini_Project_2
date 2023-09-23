# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.

#(5/5 points) Proper import of packages used.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the
# pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.




#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package,
#generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data
# is labeled tabular data.
spotify = pd.read_csv("spotify-2023.csv", encoding='latin1', index_col='track_name')


spotify['streams'] = pd.to_numeric(spotify['streams'], errors='coerce')
top_10_streams = spotify.sort_values(by='streams', ascending=False).head(10)
spotify_streams = top_10_streams['streams']
track_names = top_10_streams.index
fig, ax = plt.subplots(figsize=(10,6))
x_positions = np.arange(len(track_names))
ax.bar(x_positions, spotify_streams)
ax.set_xticks(x_positions)
ax.set_xticklabels(track_names, rotation=45, fontsize=10, ha='right')
ax.set_xlabel('Track Name', fontsize=12)
ax.set_ylabel('Amount of Streams', fontsize=12)
ax.set_title('Top 10 Streamed Tracks on Spotify', fontsize=14)
ax.grid(True)
plt.tight_layout()
plt.show()

#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data.
# Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
top_10_playlists = spotify.sort_values(by='in_spotify_playlists', ascending=False).head(10)
spotify_playlists = top_10_playlists['in_spotify_playlists']
track_names = top_10_playlists.index

fig, ax1 = plt.subplots(figsize=(10,6))
x_positions = np.arange(len(track_names))
ax1.bar(x_positions, spotify_playlists)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(track_names, rotation=45, fontsize=10, ha='right')
ax1.set_xlabel('Track Name', fontsize=12)
ax1.set_ylabel('Amount in Spotify Playlists', fontsize=12)
ax1.set_title('Top 10 Tracks in Spotify Playlists', fontsize=14)
ax1.grid(True)
plt.tight_layout()
plt.show()

current_year = datetime.datetime.now().year
past_20_years = spotify[(spotify['released_year'] >= current_year - 20) & (spotify['released_year'] <= current_year)]
songs_per_year = past_20_years['released_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
songs_per_year.plot(kind='bar')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Tracks', fontsize=12)
plt.title('Number of Top Tracks Past 20 Years', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()