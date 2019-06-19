# Playlists
This is a repository containing all of my playlists, along with the history of every single change that I've made to my playlists.

## FAQ
1. Why did I create this repository?<br>
I created this repository to show how the WPL format is superior to using iTunes, where all of the playlists are internally managed. iTunes [playlists cannot be versioned](https://discussions.apple.com/thread/7020749), and [neither can Spotify playlists](https://community.spotify.com/t5/Content-Questions/View-previous-versions-of-playlists/td-p/4400750). It's true that the cid and tid fields can cause diffs to fail, but it's better than having no diffs at all.

2. Should you create a repository for your playlists?<br>
Absolutely! I fully expect that there are people just as passionate about their music out there, and I'm hoping this repository emulates that Git repositories cannot just be used for code, but playlists too!

## Tips and Tutorials
1. Before editing a playlist, move the top song down and then back up to the top and save the playlist again. This will detect any changes to the cid or tid fields. Commit these changes before making changes of your own.

2. If you want to update the cid and tid fields while maintaining the last date modified for all your playlists, robocopy the entire Playlists directory to another location, save each of the playlist files, and the run this command to restore the timestamps: ROBOCOPY <backup> <cwd> /COPY:T /XD .git