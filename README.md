# YouTube Video Scraper
This Python script allows you to scrape YouTube videos based on various criteria such as search keywords, duration, upload date, and more. It utilizes the **youtubesearchpython** library to fetch video metadata from YouTube.

## Requirements:
Before running the script, make sure you have the following dependencies installed:
```script
pip install youtube-search-python
```
## Usage : 
```script
python youtube_video_scraper.py
```
## Function Parameters

- **q** : Query (required) - The search query to find relevant YouTube videos.
- **region** : Target country (default: 'US') - The region to filter videos from.
- **language** : Video's language (default: 'en') - The language of the videos.
- **max_videos** : Maximum number of videos (default: 20 or set to infinity).
- **min_videos** : Minimum number of videos (default: 5) - The script will continue searching for videos until it reaches this minimum number.
- **min_duration** : Minimum duration (default: None) - Get videos with a minimum duration (in seconds).
- **max_duration** : Maximum duration (default: None) - Get videos with a maximum duration (in seconds).
- **min_date** : Minimum upload date (default: None) - The minimum upload date of videos (format: YYYY-MM-DD).
- **max_date** : Maximum upload date (default: None) - The maximum upload date of videos (format: YYYY-MM-DD).
