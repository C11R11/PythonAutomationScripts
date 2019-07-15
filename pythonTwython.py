 #pip install twython
 #https://stackabuse.com/accessing-the-twitter-api-with-python/
 #https://developer.twitter.com/

 # Import the Twython class
from twython import Twython
import pandas as pd
import json

# Load credentials from json file
#with open("twitter_credentials.json", "r") as file:
#    creds = json.load(file)

credentials = {}
credentials['CONSUMER_KEY'] = 'fRobVetPQ5YzyTxG4F5I2gyin'
credentials['CONSUMER_SECRET'] = '5yHZkyVp5Reb4ij0F11FyohAI15f7fWKwNEqV28hTbiz6trmJ9'
credentials['ACCESS_TOKEN'] = '177595853-ns4ERG1gMl2XZbPlIlJIeJlnLUQxaD8CNKmQKfok'
credentials['ACCESS_SECRET'] = 'hneLll9K87YegVJXf52qHkvNtnaUnzEopfeDjKYvVtP0b'

# Instantiate an object
python_tweets = Twython(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])

# Create our query
query = {'q': 'Chadwick',
        'result_type': 'recent',
        #'count': 100,
        'lang': 'es',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(100))
