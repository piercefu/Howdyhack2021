# Howdyhack2021
Find music that resonates with you

## Installation

Make sure you have python3 installed.

Download the following libraries:

```
pip install streamlit pandas sklearn PIL 
```

## Run

```
streamlit run MusicRecommendation.py
```

## Features

Resonance is a cluster-based Machine learning web app that recommends music based on musical features such as tempo, energy, danceability, and loudness. The app

asks the user to input a song name and search for that song in our database. If our database does not contain the specific song, it will notify the user and ask for

new input. In the case that the song is found, our algorithm locates the cluster that the song belongs to and fits the recommendation model to it to identify the 

five closest neighbors within the same cluster. It returns these five songs as recommendations to the user.
