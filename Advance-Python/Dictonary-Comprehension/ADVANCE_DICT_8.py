# Problem 6: Create a Dictionary of User Permissions Based on Roles
# Problem: You are given a list of users and their roles. 
# Create a dictionary that assigns permissions based on the user's role.
users_roles = [('john_doe', 'admin'), ('alice_smith', 'editor'), ('bob_jones', 'viewer')]

# Mapping roles to permissions
role_permissions = {
    'admin': ['read', 'write', 'delete'],
    'editor': ['read', 'write'],
    'viewer': ['read']
}

filter_query = {
    user:list(filter(lambda rol:rol[0]==role,role_permissions.items())) for (user,role) in users_roles
}
print(filter_query)