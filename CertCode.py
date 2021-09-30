"""  This highly exciting code asks if you want a Chuck Noris Joke, and then goes
     to an API call website, pulls a random joke, and displays it.
     Depends on :  Requests for the API call
                   json to read the data
                   crayons to make it pretty                                    """


##  Import the needed libraries to do the work

import requests
import json
import crayons

##  Make a variable so that I don't have to type the API over and over

ChuckAPI = "https://api.chucknorris.io/jokes/random"


def main():
     ## Find out if the user even knows who Chuck Norris is
     Answer = input("Do you know who Chuck Norris is? ")
     ## Validate 2 reasonable responses to Yes/No
     if Answer.lower() == "yes" or Answer.lower() == "y":
         ## They know who Chuck is... Huzzah!  Now get a joke
         resp = requests.get(ChuckAPI)
         ## Now print the joke
         print(resp.json().get("value"))
     else:
         ## They don't know who Chuck is.  Print out the response, in color
         print(crayons.red("Then... I have no words... none"))

##  Best Practice main call
if __name__ == "__main__":
    main()
