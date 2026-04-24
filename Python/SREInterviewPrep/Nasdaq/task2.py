services = {
    "WebGateway": "AuthService",
    "AuthService": "UserDB",
    "UserDB": "StorageS3",
    "OrderAPI": "InventoryDB",
    "InventoryDB": "UserDB"
}
def is_dependent(source, target, dependecy_map):
    current = source

    visited = set()

    while current in dependecy_map:
        next_service = dependecy_map[current]

        if next_service == target:
            return True 
        
        if next_service in visited:
            break 

        visited.add(next_service)
        current = next_service
    
    return False

print(f"WebGateway --> StorageS3 : {is_dependent('WebGateway', 'StorageS3', services)}")
