import requests

# Replace YOUR_ACCESS_TOKEN with a valid access token
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Get the list of users who follow you
followers_response = requests.get(
    "https://api.instagram.com/v1/users/self/followed-by?access_token=%s" % ACCESS_TOKEN
).json()
followers = followers_response["data"]

# Get the list of users that you follow
following_response = requests.get(
    "https://api.instagram.com/v1/users/self/follows?access_token=%s" % ACCESS_TOKEN
).json()
following = following_response["data"]

# Find the users that you follow but do not follow you back
not_following_back = [user for user in following if user not in followers]

# Print the list of users that do not follow you back
print("These users do not follow you back:")
for user in not_following_back:
    print(user["username"])
