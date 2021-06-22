from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json
	
access_token = ""
access_token_secret= ""
consumer_key = ""
consumer_secret= ""
	
class StdOutListener(StreamListener):
	    def on_data(self, data):
	       producer.send_messages('homeoffice', data.encode('utf-8'))
	       print data
	       return True
	    def on_error(self, status):
	       print status
	
if __name__ == '__main__':
	   kafka = KafkaClient('192.168.2.118:9092')
	   producer = SimpleProducer(kafka)
	   I = StdOutListener()
	   auth = OAuthHandler(consumer_key, consumer_secret)
	   auth.set_access_token(access_token, access_token_secret)
	   stream = Stream(auth, I)
	   stream.filter(track='EM2020')
