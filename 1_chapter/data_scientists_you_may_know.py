# This exercise begins on page 25 with the section titled "Finding Key Connectors".

# The data dump: a list of users.
# Each user is represented by a dict containing the user's id and name. The name rhymes with the id.
users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"}
]

# Now for the "friendship" data, represented as a list of tuples which are pairs of user ids.
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Quick recap:
# users is a list of dicts -- http://openbookproject.net/thinkcs/python/english3e/dictionaries.html
# friendships is a list of tuples -- http://openbookproject.net/thinkcs/python/english3e/tuples.html.


# Now, let's do something with our data.


# Add a list of friends to each user:
# First we set each user's friends property to an empty list.
for user in users:
    user["friends"] = []
# Then we populate the lists using data from friendships.
for i, j in friendships:
    # This works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])  # add j as a friend of i


# Once each user dict contains a list of friends, we can start asking questions.


# What is the average number of connections?
# First, let's find the total number of connections by summing all of the lengths of all of the friends lists.
def number_of_friends(user):
    """ (dict) -> int

    How many friends does _user_ have?
    Return the length of friend_ids list.

    >>> number_of_friends(users[1])
    3
    >>> number_of_friends(users[9])
    1
    """
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
print("There are " + str(total_connections) + " total connections among the users.")

# Then we divide by the number of users (using floating point division) to get our result.
num_users = len(users)
avg_connections = total_connections / num_users
print("The average number of users is " + str(avg_connections) + ".")
print('')


# Who are the most and least connected people?
# Since there aren't many users, we can sort them all based on the number of friends.
# Let's start by creating a list. The result will be (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print("In this list, the user id will be followed by the number of friends:\n" + str(num_friends_by_id))
print('')
print("Now the list will be sorted by number of friends, most to least:")
print(sorted(num_friends_by_id,
             key=lambda pair: pair[1],  # http://www.diveintopython.net/power_of_introspection/lambda_functions.html
             reverse=True))

# What we have just computed is the network metric called degree centrality (https://en.wikipedia.org/wiki/Centrality#Degree_centrality).
# Not a bad start, huh?

###### Data Scientists You May Know ######
print('')

# The VP of Fraternization wants you to encourage more connections among your members by designing a "Data Scientists YOu May Know" suggester/recommender.

# Let's start with friend of a friend ('foaf').
# For each of a user's friends, iterate over that person's friends, and collect all of the results.

def friends_of_friend_ids_bad(user):
    """ (dict) -> list
    For each friend of the user, get each of their friends.

    >>> friends_of_friend_ids_bad(users[0])
    [0, 2, 3, 0, 1, 3]
    """
    return [foaf["id"]
            # for each of user's friends
            for friend in user["friends"]
            # get each of _their_ friends
            for foaf in friend["friends"]]

print("Below are the friends for users 0, 1, and 2:")
print([friend["id"] for friend in users[0]["friends"]])
print([friend["id"] for friend in users[1]["friends"]])
print([friend["id"] for friend in users[2]["friends"]])
print('')

# Knowing that people are friends-of-friends in multiple ways seems like interesting information.
# Let's go a bit further and produce a count of mutual friends.
# Let's also include a helper function to exclude people already known to the user.
from collections import Counter
# https://docs.python.org/3/library/collections.html#collections.Counter

def not_the_same(user, other_user):
    """ (int, int) -> boolean
    Two users are not the same if they have different ids
    """
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """ (int, int) -> boolean
    other_user is not a friend if not in user["friends"]
    """
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    """ (dict) -> dict
    Return a dict with key: user["id"] and value: number of friends
    >>> friends_of_friend_ids(users[3])
    Counter({0: 2, 5: 1})

    Chi has 2 mutual friends with Hero and one mutual friend with Clive.
    """
    return Counter(foaf["id"]
                   # for each of my friends
                   for friend in user["friends"]
                   # count *their* friends
                   for foaf in friend["friends"]
                   # who aren't me
                   if not_the_same(user, foaf)
                   # and aren't my friends
                   and not_friends(user, foaf)
    )
print("The Counter represents the user id followed by the number of mutual friends:")
print(friends_of_friend_ids(users[3]))
print('')


# These users have different areas of expertise.
# The following dataset is a list of interests paired by (user_id, interest).
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
# This can be another way to connect users by interests instead of by friendships.
# For example, Thor has no friends in common with Devin, but they share an interest in machine learning.

# What follows is a function that uses brute force to find users with a certain interest:
def data_scientists_who_like(target_interest):
    """ (str) -> list
    Return a list containing the ids of users whose interests include the target_interest.

    >>> data_scientists_who_like("Python")
    [2, 3, 5]
    """
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest
            ]

print("Here are the ids of users who like Python:")
print(data_scientists_who_like("Python"))
print('')

# That works, but the function examines the whole list of interests for every search.
# If we have lots of users and interests, or if we are going to do a lot of searches,
# we are better off building an index (or two)

from collections import defaultdict
# https://docs.python.org/3/library/collections.html#collections.defaultdict

# Here is an index from interests to users.
# Keys are interests, values are lists of user_ids with that interest.
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
print("Here is a defaultdict that assigns user_ids to each interest:")
print(user_ids_by_interest)
print('')

# Here is an index from users to interests.
# Keys are user_ids, values are lists of interests for that user_id.
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
print("Here is a defaultdict that assigns interests to each user_id:")
print(interests_by_user_id)
print('')

# Now we can continue by finding who has the most interests in common with a given user:
def most_common_interests_with(user):
    """ (dict) -> dict
    1. Iterate over the user's interests.
    2. For each interest, iterate over the other users with that interest.
    3. Keep count of how many times we see each other user.

    >>> most_common_interests_with(users[3])
    Counter({5: 2, 6: 2, 2: 1, 4: 1})
    """
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"]
                   )
print("The dictionary below shows that Sue has 1 interest (each) in common with Chi, Clive, and Devin:")
print(most_common_interests_with(users[2]))
print('')
