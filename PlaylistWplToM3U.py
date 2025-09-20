import os
import glob
import xml.etree.ElementTree as ET

# Folder containing your WPL files
wpl_folder = "."
# Folder where M3U files will be saved
m3u_folder = os.path.join(wpl_folder, "m3u")
os.makedirs(m3u_folder, exist_ok=True)

# Find all WPL files
wpl_files = glob.glob(os.path.join(wpl_folder, "*.wpl"))

for wpl_file in wpl_files:
    # Determine output M3U filename
    base_name = os.path.basename(wpl_file)
    m3u_file = os.path.join(m3u_folder, base_name.replace(".wpl", ".m3u"))
    
    # Parse WPL XML
    tree = ET.parse(wpl_file)
    root = tree.getroot()
    
    # Extract all <media src="..."/> paths
    media_files = []
    for media in root.findall(".//media"):
        src = media.get("src")
        if src:
            # Convert Windows-style backslashes to forward slashes (optional for Android)
            src = src.replace("\\", "/")
            media_files.append(src)
    
    # Write M3U file
    with open(m3u_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for media in media_files:
            f.write(f"{media}\n")
    
    print(f"Converted {wpl_file} -> {m3u_file}")
