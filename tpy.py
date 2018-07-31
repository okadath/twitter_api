import tweepy
import json
import sys
sys.path.append("/home/okadath/Desktop/sc")
import functions as f
import pickle
import time




# Specify the account credentials in the following variables:

def get_timeline_data():

    tweets_list = []
    # construct the dataframe
    for tweet in tweepy.Cursor(api.user_timeline, include_rts=False).items():

        tweets_list.append([str(tweet.id), int(tweet._json['favorite_count']),
                            str(tweet._json['retweet_count']), tweet.created_at])

    #tweets = pd.DataFrame(data=tweets_list,columns=['id', 'like', 'retweet', 'date'])

    return tweets_list

# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)
        print(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


def post_tweet(twitter_api, tweet_text, reply_id=None, media_ids=None):
    '''post a tweet to the timeline, trims tweet if appropriate
    Args:
    twitter_api (:class:`tweepy.API`): the Twitter API instance to use
    tweet_text (string): the status text to tweet
    reply_id (int): optional, nests the tweet as reply to that tweet (use id_str element from a tweet)
    media_ids (list of media_ids): optional, media to attach to the tweet Returns:bool: True if posted successfully, False otherwise
    '''
    try:
        twitter_api.update_status(tweet_text, reply_id, media_ids=media_ids)
        return True
    except tweepy.error.TweepError as e:
        print("post_tweet Error: " + str(e))
        return False 

def ObtenerTweets(palabra="Trump",times=100,leguanje="en"):
    #Se define las listas que capturan la popularidad
    popularidad_list = []
    numeros_list = []
    numero = 1
    for tweet in tweepy.Cursor(api.search, palabra, lang=lenguaje).items(numero_de_Tweets):
        try:
            #Se toma el texto, se hace el analisis de sentimiento
            #y se agrega el resultado a las listas
            print(tweet.text)
            # analisis = TextBlob(tweet.text)
            # analisis = analisis.sentiment
            # popularidad = analisis.polarity
            # popularidad_list.append(popularidad)
            # numeros_list.append(numero)
            # numero = numero + 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    return 0#(numeros_list,popularidad_list,numero)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate

    auth=f.log_twitter()
    # Connect the stream to our listener

    #stream = tweepy.Stream(auth, listener)
    #stream.filter(track=['Python'])
    api = tweepy.API(auth)
    # tweet = api.get_status(1011990507470254080)
    # print("retwits"+str(tweet.retweet_count))
    # print("likes"+str(tweet.favorite_count))
    # a=get_timeline_data()
    # print( "primeros twits del perfil"+str(a))

#===========

    user = api.get_user('OmniKadath')

    pickled_file = open('user_twitter.pickle', 'wb')
    pickle.dump(user, pickled_file)



    print (user.screen_name)
    print (user.followers_count)
    print(user.has_extended_profile)
    print(user.profile_image_url)
    print(user.description)
    print(user.screen_name)
    print(user.name )
    print(user.id)
    #print(user.__dict__)
    print(user.favourites_count)
    print(user.friends_count)
    print(user.profile_banner_url)
    print(user.profile_image_url)
    


    t = api.get_status(id=  1013811811311849475)#obtiene perfil 998399800876978177

                                
    print(t.retweet_count, t.text,t.favorite_count,t.in_reply_to_status_id)
    #in_reply_to_screen_name
    #in_reply_to_status_id
    #in_reply_to_user_id

    #print(t.__dict__)
    ids=[]
    for page in tweepy.Cursor(api.followers_ids, screen_name="OmniKadath").pages():#seguidores de la cuenta
        ids.extend(page)
        #time.sleep(60)

        print (ids)
        #print()
    print('meh')
    # for tweet in tweepy.Cursor(api.search,q="AMLO",geocode="19.4244134,-99.1590249,150km").pages():
    #     print (tweet)#tweet.created_at, tweet.text, tweet.user.id, tweet.geo)




    #post_tweet(api,"test 2")
    print(api.me().name)

    # pickled_file = open('user_twitter.pickle','rb')
    # user = pickle.load(pickled_file)
    # print(user)

    # print (user.screen_name)
    # print (user.followers_count)
    # print(user.has_extended_profile)


    # for friend in user.friends():
    #    print (friend.screen_name)


    # for friend in tweepy.Cursor(api.friends).items():
    # # Process the friend here
    #     print(friend)

    #===================

    # MAX_TWEETS = 5000000000000000000000

    # for tweet in tweepy.Cursor(api.search, q='#python', rpp=100).items(MAX_TWEETS):
    #     # Do something
    #     print(tweet)
    #     pass