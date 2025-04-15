from setuptools import setup, find_packages

setup(
    name="spotify_playlist_tool",
    version="0.1.0",
    description="A CLI tool for managing Spotify playlists with filtering, sorting, and deduplication.",
    author="Gretchen Maculo",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "spotify_playlist_tool=spotify_playlist_tool.tool:main",
            "spotify-tool=spotify_playlist_tool.tool:main"
        ],
    },
    install_requires=["spotipy"],
    python_requires=">=3.7",
)