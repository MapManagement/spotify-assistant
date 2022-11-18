# Spotify-Assistant

A bunch of Python functions and classes to interact with Spotify's web API.

## Commands

### Track Related

```sh
track-features [track URL]
```
returns audio features of the track

```sh
track-genre [track URL]
```
returns the genre of the track

```sh
full-track [track URL]
```
returns detailed information about the track

### Artist Related

```sh
artist-genres [artist URL]
```
returns all genres which are connected to the artist

```sh
full-artist [artist URL]
```
returns detailed information about the artist

### Album Related

```sh
full-album [album URL]
```
returns detailed information about the album

## Features

- implementation of different Spotify API objects
- retrieve access token
- request tracks, albums and artists by ID
