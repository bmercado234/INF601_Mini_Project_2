# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.

#(5/5 points) Proper import of packages used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import shutil, os
from pathlib import Path

# check to see if charts folder exists, create one if not
if not os.path.exists('charts'):
    os.makedirs('charts')

#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package,
#generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data
# is labeled tabular data.

# read the spotify csv and store the data
spotify = pd.read_csv("spotify-2023.csv", encoding='latin1', index_col='track_name')


#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data.
# Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

# ***********Top Streamed Songs Spotify Graph************

# for some reason the program doesn't read the data values in streams as numbers, so they have to be converted
spotify['streams'] = pd.to_numeric(spotify['streams'], errors='coerce')
# sort the values gathered from spotify streams into highest to lowest and gather only the top ten
top_10_streams = spotify.sort_values(by='streams', ascending=False).head(10)

# gather only the data value part
spotify_streams = top_10_streams['streams']

# gather the indexes (which is the track names) for the most streamed spotify tracks
track_names = top_10_streams.index

# make the graph with specified width and height
fig, ax = plt.subplots(figsize=(10,6))

# create array of x-positions for bars on the graph based on amount of track_names
x_positions = np.arange(len(track_names))

# utilize x_positions as x coordinates and spotify_streams as the height for bar graph
ax.bar(x_positions, spotify_streams)

# was having trouble with alignment of song names, this aligns them
ax.set_xticks(x_positions)

# make the x axis ticks look more readable
ax.set_xticklabels(track_names, rotation=45, fontsize=10, ha='right')

# editing the labels
ax.set_xlabel('Track Name', fontsize=12)
ax.set_ylabel('Amount of Streams', fontsize=12)
ax.set_title('Top 10 Streamed Tracks on Spotify', fontsize=14)

# grid on
ax.grid(True)

# have all labels and text fit
plt.tight_layout()

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.

# save the graph as a png and move it to the charts folder
plt.savefig('spotify_top_streams_2023')
shutil.move('spotify_top_streams_2023.png', 'charts')

# ***********Top Songs in Playlists Spotify Graph************

# sort in_spotify_playlists data by descending order and get the top 10 values
top_10_playlists = spotify.sort_values(by='in_spotify_playlists', ascending=False).head(10)

# contains the number values
spotify_playlists = top_10_playlists['in_spotify_playlists']

# contains the index of the numbers which in this case is the track names
track_names = top_10_playlists.index

# define width and height for graph
fig, ax1 = plt.subplots(figsize=(10,6))

# create array of x-positions for bars on the graph based on amount of track_names
x_positions = np.arange(len(track_names))

# utilize x_positions as x coordinates and spotify_playlists as the height for bar graph
ax1.bar(x_positions, spotify_playlists)

# was having trouble with alignment of song names, this aligns them
ax1.set_xticks(x_positions)

# make the x axis ticks look more readable
ax1.set_xticklabels(track_names, rotation=45, fontsize=10, ha='right')

# editing labels
ax1.set_xlabel('Track Name', fontsize=12)
ax1.set_ylabel('Amount in Spotify Playlists', fontsize=12)
ax1.set_title('Top 10 Tracks in Spotify Playlists', fontsize=14)

# grid on
ax1.grid(True)

# all labels and text fit
plt.tight_layout()

# save graph as png and move to charts folder
plt.savefig('spotify_top_songs_in_playlists_2023')
shutil.move('spotify_top_songs_in_playlists_2023.png', 'charts')


# ***********Amount of Top Songs Organized by Year the Past 20 Years Spotify Graph************

# gather current year
current_year = datetime.datetime.now().year

# have data limited to collect only the past 20 years
past_20_years = spotify[(spotify['released_year'] >= current_year - 20) & (spotify['released_year'] <= current_year)]

# organize the collected data
songs_per_year = past_20_years['released_year'].value_counts().sort_index()

# define graph width and height
plt.figure(figsize=(12, 6))

# define graph as bar graph
songs_per_year.plot(kind='bar')

# editing labels
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Tracks', fontsize=12)
plt.title('Number of Top Tracks Past 20 Years', fontsize=14)

# grid on
plt.grid(True)

# all text and labels fit on graph
plt.tight_layout()

# save graph as png and move to charts folder
plt.savefig('spotify_top_songs_by_year_2023')
shutil.move('spotify_top_songs_by_year_2023.png', 'charts')

#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!