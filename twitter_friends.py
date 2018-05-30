from twitter import *
#from twitter import Twitter, OAuth
import twitter_config as tc
#global str

twitter = Twitter(auth =OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret))

username = "IshaPanchal4"

query = twitter.friends.ids(screen_name = username)
print("Found %d friends" %(len(query["ids"])))

for n in range(0,len(query["ids"]),100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
			print(" [%s] %s - %s" %("*" if user["verified"] else " ", user["screen_name"], user["location"]))

