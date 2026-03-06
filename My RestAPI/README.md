# Twitter Favorites REST API

A simple REST API built with Flask that reads a JSON archive of Twitter favorites and lets you query tweet and user data through HTTP requests.

## Requirements

Python 3.7+ and pip.

## Running the Server

    python restapi.py

The server starts at http://localhost:8080. Port 5000 is avoided because macOS can conflict with it.

## Endpoints

GET /
Returns a simple message confirming the server is running.

GET /tweets
Returns all tweets in the archive. Each entry includes the creation time, tweet ID, and text.

GET /links
Returns all external URLs found in tweet text, grouped by tweet ID. Links are extracted using regular expressions.

GET /details/<tweet_id>
Returns the creation time, text, and author screen name for a specific tweet. Replace <tweet_id> with a real ID. Returns 404 if the tweet is not found.

GET /profile/<screen_name>
Returns the location, description, followers count, and friends count for a given Twitter user. Replace <screen_name> with a real username from the archive. Returns 404 if the user is not found.

## Testing with Postman

Make sure the server is running first. Open Postman, create a new GET request, and use http://localhost:8080 as the base URL. You can grab a real tweet ID or screen name from the /tweets response and plug it into /details and /profile.

You can also test through the browser.

My tests:
    Get all Tweets: http://127.0.0.1:8080/tweets
    Get Links: http://127.0.0.1:8080/links
    Get Details: http://127.0.0.1:8080/details/311432631726264320
    Get Profile: http://127.0.0.1:8080/profile/johnmaeda