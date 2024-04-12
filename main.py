#-------------------------------------------------------------------
# Before running this script make sure to run before: pip3 install youtube-search-python
#-------------------------------------------------------------------
from youtubesearchpython import VideosSearch, Video, ResultMode, Transcript
from datetime import datetime
import time

def scrape_youtube_videos(q,region = 'US', language = 'en', max_videos = 20,min_videos = 5,min_duration = None, max_duration = None, min_date = None, max_date = None ):
    '''
    q : Query @required
    region : target country (default 'US') 
    language : video's language (default 'en')
    max_videos : maximum number of videos, by default 20 or just put infinity to get everything.
    min_videos : minimum number of videos, by default 5
    min_duration : get videos with minimum duration (default 10 seconds)
    max_duration : get videos with maximu duration (default 120 seconds)
    min_date : minimum upload date (String format %Y-%m-%d) 
    max_date : maximum upload date (String format %Y-%m-%d) 
    '''
    all_videos = []
    min_date = datetime.strptime(min_date, "%Y-%m-%d") if min_date is not None else None
    max_date = datetime.strptime(max_date, "%Y-%m-%d") if max_date is not None else None
    start_time = time.time()

    search = VideosSearch(q, limit=min_videos, language=language, region=region)
    quota = search.result()['result']

    while (len(quota) != 0) and (len(all_videos) <= max_videos):
        for video in quota:
            videoInfo = Video.getInfo(video['id'], mode=ResultMode.json)
            video['descriptionSnippet'] = videoInfo['description']
            video['category'] = videoInfo['category']
            video['keywords'] = videoInfo['keywords']
            video['publishedTime'] = videoInfo['publishDate']
            video['uploadDate'] = videoInfo['uploadDate']
            video['allowRatings'] = videoInfo['allowRatings']
            video['averageRating'] = videoInfo['averageRating']
            video['isLiveContent'] = videoInfo['isLiveContent']
            video['isFamilySafe'] = videoInfo['isFamilySafe']
            video['viewCount'] = videoInfo["viewCount"]
            
            # Filter by upload date
            duration = int(videoInfo['duration']['secondsText'])
            upload_date = datetime.strptime(video['uploadDate'].split('T')[0], "%Y-%m-%d")
            if (min_date is None or upload_date >= min_date) and (max_date is None or upload_date <= max_date):
                # Filter by duration
                if (min_duration is None) or (duration >= min_duration):
                    if (max_duration is None) or (duration <= max_duration):
                        # Fetch transcript keep it last because it is expensive task
                        try:
                            srt = Transcript.get(video['id'])['segments']
                            concatenated_text = ' '.join(item['text'] for item in srt)
                            video['transcript'] = concatenated_text
                        except:
                            video['transcript'] = 'Not available'
                        all_videos.append(video)
        search.next()
        quota = search.result()['result']

    print('scraped', len(all_videos), 'video successfully in', round(time.time() - start_time,2), 'seconds')
    return all_videos



if __name__ == "__main__":
    # Example usage of the scrape_youtube_videos function
    videos = scrape_youtube_videos('european election 2024',    
            region = 'US',
            language = 'en',
            max_videos = 20,
            min_videos = 5,
            min_date = '2024-04-01',  
            max_date = None,  
            min_duration = None,
            max_duration = None
          )
    print(videos)
