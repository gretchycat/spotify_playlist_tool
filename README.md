# Spotify Playlist Tool

A command-line tool for exporting, filtering, and managing Spotify playlists. Supports metadata and audio feature filtering, randomization, sorting, and more.

## Installation

```bash
pip install .
```

## Usage

```bash
spotify-tool --source liked --dest "My Mood Boost" --random --min_valence 0.6 --min_energy 0.5 --nodup
```

## Features

- Export to or import from JSON files
- Filter by artist, release date, tempo, energy, valence, and danceability
- Avoid duplicates with `--nodup`
- Automatically resolves playlist names
- Supports sorting and random shuffling
- Prevents accidental overwrites without `--force`