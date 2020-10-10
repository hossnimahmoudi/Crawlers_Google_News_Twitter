import json
import tweepy

consumer_key = "wpjfstyikV9KrXhfmiVZfEc4y"
consumer_secret = "D9nPYlE3u8piuGeToToUU61m3IpMiKPhGZUmvziHJsPHs5Qrjo"
access_token = "1085687624004718592-OFt18RwTk2Fjs8iIkxNQJ7hGCTRc8k"
access_token_secret = "aJbXM453ABM6XYjZdadkDbSVfTuW8W4UlSnyheevlZAIY"
search = "python"


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, query):

    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)

    list = []
    df={}
    for tweet in tweepy.Cursor(api.search, q=query+' -filter:retweets', lang="fr", tweet_mode="extended").items(500):
        try:
            df = {
                     "created_at":str(tweet.created_at),
                      "full_text":tweet.full_text.replace('\n', ' '),
                      "place":str(tweet.place),
                      "username":tweet.user.screen_name.strip('b'),
                      "user_followers": tweet.user.followers_count,
                      "user_id_str":tweet.id_str,
                      "user_location": tweet.user.location,
                      "description": tweet.user.description
                }

        except:
            pass
        list.append(json.dumps(df))
    return list

if __name__ == '__main__':
        search_for_hashtags(consumer_key,consumer_secret,access_token,access_token_secret,query=search)
