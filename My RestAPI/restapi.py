from flask import Flask, jsonify, request
import requests
import re

app = Flask(__name__)

LINK = 'https://foyzulhassan.github.io/files/favs.json'

def fetch_data(): # Function to fetch data from the provided link
    response = requests.get(LINK)
    return response.json()

DATA = fetch_data() # Fetch the data once when the application starts and store it in a global variable for later use, since it's static data

@app.route("/", methods=["GET"]) # Home route to check if the API is working
def home():
    return jsonify({"message": "Homepage"}), 200


@app.route("/tweets", methods=["GET"]) # Route to get all tweets with only created_at, id, and text fields
def getAllTweets():
    tweets = list()
    for _ in DATA: # Loop through the data and extract only the required fields for each tweet, then append it to the tweets list
        tweet = {"tweet":{"created_at": _["created_at"], "id": _["id"], "text": _["text"]}}
        tweets.append(tweet)
    return jsonify(tweets), 200


@app.route("/links", methods=["GET"]) # Route to get all links from the tweets, with the id of the tweet they were found in, and the links themselves in an array (since there can be multiple links in a single tweet)
def getLinks():
    links = list()
    for _ in DATA: # Loop through the data and extract the id and text fields for each tweet
        tweet = {"id": _["id"], "text": _["text"]}
        urls = re.findall(r'https?://[^\s]+', tweet["text"]) # Regular Expression to find all links in a tweet
        entry = {"id": _["id"], "links": [urls]}
        links.append(entry)
    return jsonify(links), 200


@app.route("/details/<int:id>", methods=["GET"]) # Route to get details of a specific tweet by its ID
def getDetails(id):
    for _ in DATA: # Loop through the data and check if the id of the current tweet matches the id provided in the URL
        if _["id"] == id:
            return jsonify({"created_at": _["created_at"], "text": _["text"], "screen_name": _["user"]["screen_name"]}), 200
    return jsonify({"message": "Tweet not found"}), 404 # Return a 404 error if the tweet is not found in the data


@app.route("/profile/<string:screen_name>", methods=["GET"]) # Route to get profile information of a user by their screen name, including location, description, followers count, and friends count
def getProfile(screen_name):
    for _ in DATA: # Loop through the data and check if the screen name of the current user matches the screen name provided in the URL
        if _["user"]["screen_name"] == screen_name:
            return jsonify({"location": _["user"]["location"], "description": _["user"]["description"], "followers_count": _["user"]["followers_count"], "friends_count": _["user"]["friends_count"]}), 200
    return jsonify({"message": "User not found"}), 404 # Return a 404 error if the user is not found in the data



if __name__ == "__main__":
    app.run(debug=True, port=8080) # Changed to port 8080 bc macOS has some issues with port 5000
