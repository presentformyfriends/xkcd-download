# xkcdDownload
My own take on the project from Al Sweigart's book "Automate the Boring Stuff".

Downloads all comics from https://xkcd.com, saves the files by comic number, and prints an error log in the shell. 

Written in Python.

Check out the next repository, chgWinWallpaper, which includes a script I wrote that uses these saved images and displays a different xkcd comic each day as my Windows desktop background!

## :arrow_down: Usage

Decide where you want the images saved and change the path accordingly. Then run the script.

The error log will print in the shell. The following seven files could not be saved, as they are interactive comics: 2198, 2067, 1663, 1608, 1525, 1416, and 1350.

![xkcdDownload.gif](img/xkcdDownload.gif)

## :snake: Dependencies

Written in Python for Windows. This script uses the following Python modules: os, bs4, requests, and the requests exception InvalidURL.
