# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.

#(5/5 points) Proper import of packages used.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
spotify_streams = spotify.sort_values(by='streams', ascending=False).head(10)
spotify_streams = spotify_streams['streams']

ax1 = spotify_streams.plot()
plt.xlabel('Track Name')
plt.ylabel('Streams')
plt.title('Top 10 Tracks by Streams')
plt.grid(True)
plt.xticks(range(10), spotify_streams.index, rotation=45, fontsize=6)
plt.tight_layout()
plt.show()

#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data.
# Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
spotify_playlists = spotify.sort_values(by='in_spotify_playlists', ascending=False).head(10)
spotify_playlists = spotify_playlists['in_spotify_playlists']
ax = spotify_playlists.plot()
plt.xlabel('Track Name')
plt.ylabel('Amount in Spotify Playlists')
plt.title('Top 10 Tracks in Spotify Playlists')
plt.grid(True)
plt.xticks(range(10), spotify_playlists.index, rotation=45, fontsize=6)
plt.tight_layout()
plt.show()
