import Tweet
import pickle


def tweet_menu():
    print("Tweet Menu")
    print("------------")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    print("\nWhat would you like to do?")


def main():
    option = "1"
    tweets_storage = []
    while option != '4':
        tweet_menu()
        option = input()
        if option.isalpha():
            print("Please enter a numeric value.")
        elif int(option) < 1 or int(option) > 4:
            print("Please select a valid option")

        if option == "1":
            tweet_author = input("What is your name? ")
            tweet_text = input("What would you like to tweet? ")
            while len(tweet_text) > 140:
                print("Tweets can only be 140 characters!")
                tweet_text = input("What would you like to tweet? ")

            new_tweet = Tweet.Tweet(tweet_author, tweet_text)
            tweets_storage.append(new_tweet)
            print(tweet_author, "Your tweet has been saved.")
            pickle.dump(tweets_storage, open("tweets.dat", "wb"))

        if option == "2":
            print("Recent Tweets")
            print("-------------------")
            count = 0
            tweets_storage = pickle.load(open("tweets.dat", "rb"))
            if len(tweets_storage) == 0:
                print("There are no recent tweets")
            else:
                for i in tweets_storage:
                    print(i.get_author() + "-" + i.get_age())
                    print(i.get_text())
                    print("\n")
                    if count > 5:
                        break
                    else:
                        count += 1
        if option == "3":
            tweets_storage = pickle.load(open("tweets.dat", "rb"))
            search = input("What would you like to search for? ")
            print("Search Results")
            print("----------------")
            if len(tweets_storage) == 0:
                print("There are no tweets to be searched for.")
            else:
                for tweets in tweets_storage:
                    for element in tweets.get_text():
                        if search in tweets.get_text():
                            print(tweets.get_author() + "-" + tweets.get_age())
                            print(tweets.get_text())
                            print("\n")
                            break
        if option == "4":
            pass


main()
