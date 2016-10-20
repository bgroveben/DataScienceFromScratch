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
