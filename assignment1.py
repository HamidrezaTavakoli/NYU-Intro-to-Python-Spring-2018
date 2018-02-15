
# constants
TWEET_MAX_LEN_COUNT = 280

# global variables
finalTweet = ""
orderToPerform = "y"

# helper functions
def getTweet():
    remaining = TWEET_MAX_LEN_COUNT - len(finalTweet)
    tweet = input("type your tweet (characters left " + str(remaining)+ "): ")
    return tweet


def dealWihtEnteredTweet(tweetedValue):
    global finalTweet
    finalTweet = finalTweet + tweetedValue + " "
    decision = input("This is your tweet so far \"" + finalTweet + "\". Would you like to add to it? (y/n):" )
    return decision

# main function
while len(finalTweet) < TWEET_MAX_LEN_COUNT :
    if orderToPerform == "y":
        enteredTweet = getTweet()
        if len(enteredTweet) > TWEET_MAX_LEN_COUNT:
            print("Tweet is too long by " + str(len(enteredTweet) - TWEET_MAX_LEN_COUNT) + " characters. Max characters allowed is " + str(TWEET_MAX_LEN_COUNT) + ".")
            break
        else :
            orderToPerform = dealWihtEnteredTweet(enteredTweet)
    else :
        print("Posting your tweet")
        print(finalTweet)
        break
