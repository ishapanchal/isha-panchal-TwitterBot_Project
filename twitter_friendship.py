from twitter import *
#from twitter import Twitter, OAuth
import twitter_config as tc
import os, sys
#global str

twitter = Twitter(auth =OAuth(tc.access_key, tc.access_secret, tc.consumer_key, tc.consumer_secret))

source = "IshaPanchal"
target = "aamir_khan"

result=twitter.friendships.show(source_screen_name = source, target_screen_name = target)

following = result["relationship"]["target"]["following"]
follows = result["relationship"]["target"]["followed_by"]

print("%s following %s: %s " %(source,target,follows))
print("%s following %s: %s " % (target,source,following))