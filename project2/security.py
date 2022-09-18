
from hmac import compare_digest
from user import User

users = [
    User(1, 'biswa1', 'asdf'),
    User(2, 'biswa2', 'asdf'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

# users = [
#     {
#         'id': 1,
#         'user': 'biswa',
#         'password': 'asdf'
#     }
# ]

# username_mapping = {
#     'biswa': {
#         'id': 1,
#         'user': 'biswa',
#         'password': 'asdf'
#     }
# }

# userid_mapping = {
#     1: {
#         'id': 1,
#         'user': 'biswa',
#         'password': 'asdf'
#     }
# }

# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     if user and safe_str_cmp(user.password, password):
#         return user
    

# def identity(payload):
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)
        