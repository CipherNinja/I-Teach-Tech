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