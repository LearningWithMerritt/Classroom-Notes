import os

# Define the maze structure as a nested dictionary
maze_structure = {
    "maze": {
        "left": {
            "east": {
                "north": {},
                "south": {
                    "up": {},
                    "down": {
                        "straight": {},
                        "turn-around": {
                            "straight": {}
                        }
                    }
                }
            },
            "west": {
                "north": {},
                "south": {
                    "up": {},
                    "down": {
                        "straight": {
                            "east": {
                                "north": {},
                                "south": {
                                    "up": {},
                                    "down": {
                                        "straight": {},
                                        "turn-around": {}
                                    }
                                }
                            },
                            "west": {
                                "north": {},
                                "south": {
                                    "up": {},
                                    "down": {
                                        "straight": {},
                                        "turn-around": {}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "right": {
            "east": {
                "down": {
                    "north": {},
                    "south": {
                        "up": {},
                        "down": {
                            "straight": {},
                            "turn-around": {}
                        }
                    }

                }
            },
            "west": {
                "north": {},
                "south": {}
            }
        }
    }
}


def create_directories(base_path, structure):
    for dir_name, sub_dirs in structure.items():
        # Create the directory
        new_path = os.path.join(base_path, dir_name)
        os.makedirs(new_path, exist_ok=True)
        
        # Recursively create sub-directories
        create_directories(new_path, sub_dirs)

# Set the base path where the maze structure will be created
base_path = "."

# Create the maze directory structure
create_directories(base_path, maze_structure)

print("Maze directory structure created successfully!")