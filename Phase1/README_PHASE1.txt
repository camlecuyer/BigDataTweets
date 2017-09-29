Team members: Cameron L’Ecuyer, Fahad Alsubaie, Faiz Alotaiby

Tweets were gathered using the twitter_stream.py file, and parsed using parseTweet.py.

Fahad used similar methods to gather the data, in the Fahad Tweets folder.

I ran both Fahad’s set and my set (tweet_info.txt, parsedTweet_2.txt respectively) through hadoop wordcount and spark wordcount. The output from Fahad’s data are the files with small in the name, my files are the hadoop/spark_wordcount.txt files. My tweets do not have the hashtag in front of the name as I pulled them out of the son file not the text.

The hadoop log files were taken after running hadoop wordcounts, the spark logs were taken after running spark wordcounts.

My full file from the twitter_stream.py is over 1 GB so I cannot upload it, and it violates Githubs 100mb limit even when compressed, so I cannot display it, all other files will also be uploaded to my github as well

https://github.com/camlecuyer/BigDataTweets