from pathlib import Path
from datetime import datetime
import os

screenshotsDirectory = '/Users/derekwebb/Desktop/Screenshots'
archiveDirectory = screenshotsDirectory + '/Archive'
todayISO = datetime.now().strftime('%Y-%m-%d')
todayArchiveDirectory = screenshotsDirectory + "/Archive/" + todayISO

# Create the Screenshots directory if it doesn't exist
Path(screenshotsDirectory).mkdir(parents=True, exist_ok=True)

# Create the Archive directory if it doesn't exist
Path(archiveDirectory).mkdir(parents=True, exist_ok=True)

# Create today's directory if it doesn't exist
Path(todayArchiveDirectory).mkdir(parents=True, exist_ok=True)

# Get a list of all files in the screenshots directory
files = os.listdir(screenshotsDirectory)

# Loop through each file
for file in files:
    # Do not move the archive directory
    if file != 'Archive':
        # Move the file from the screenshots directory into today's archive folder
        os.rename(screenshotsDirectory + '/' + file, todayArchiveDirectory + '/' + file)