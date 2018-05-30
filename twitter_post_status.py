from twitter import *
import twitter_config as tc

twitter = Twitter(auth = OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret))

new_status = "Everything begins with an idea"
results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status