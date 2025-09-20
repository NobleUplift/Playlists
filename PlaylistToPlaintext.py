import xml.etree.ElementTree as ET
import os
import time

def parse_wpl(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    # WPL playlists typically use a namespace, but here yours doesn’t
    media_elements = root.findall(".//media")

    results = []
    for media in media_elements:
        artist = media.get("trackArtist")
        title = media.get("trackTitle")

        if not artist or not title:
            # fallback to parsing path
            src = media.get("src")
            if src:
                parts = src.split("\\")  # Windows-style paths
                if len(parts) >= 3:
                    artist = parts[-3]
                    title = os.path.splitext(parts[-1])[0].split(" ", 1)[-1]
                else:
                    artist = "Unknown"
                    title = os.path.splitext(parts[-1])[0]
            else:
                artist, title = "Unknown", "Unknown"

        results.append(f"{artist} - {title}")

    return results


if __name__ == "__main__":
    playlist_file = "Singles.wpl"  # change this to your WPL file
    songs = parse_wpl(playlist_file)
    for song in songs:
        print(song)
    time.sleep(600)
