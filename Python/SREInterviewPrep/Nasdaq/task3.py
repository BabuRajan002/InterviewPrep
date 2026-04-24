perms = {"Admin": "Editor", "Editor": "Viewer", "Viewer": "Guest"}

def can_perform_action(user_role, required_role, perm):
    if user_role == required_role:
        return True
    
    current_role = user_role

    visited_role = set()

    while current_role in perm:
        target_role = perm[current_role]

        if target_role == required_role:
            return True 
        
        if target_role in visited_role:
            break 

        visited_role.add(target_role)
        current_role = target_role
    return False

print(f"Admin --> Viewer: {can_perform_action('Editor', 'Editor', perms)}")

