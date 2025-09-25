import os,sys,shutil
from pathlib import * 
import base64
import random

base_path = "."


maze_structure = {
    "maze-entrance" : {
        "left" : {
            "east" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "west" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "north" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "south" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            }
        },
        "right" : {
            "east" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "west" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "north" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "south" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            }
        },
        "up" : {
            "east" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "west" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "north" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "south" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            }
        },
        "down" : {
            "east" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "west" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "north" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            },
            "south" : {
                "up":{},
                "down":{},
                "forward":{},
                "back":{}
            }
        }

    }
    
}

def pick_random_path(structure):

    next_step = random.choice(list(structure.keys()))
    
    if structure[next_step]:
        return [next_step] + pick_random_path(structure[next_step])
    else:
        return [next_step]


def create_directories(base_path, structure):
    for dir_name, sub_dirs in structure.items():
        # Create the directory
        new_path = os.path.join(base_path, dir_name)
        os.makedirs(new_path, exist_ok=True)

       
        with open(os.path.join(new_path, "exit.txt"), "a") as f:
            f.write("DEAD END.........")
            

        create_directories(new_path, sub_dirs)


def hide_file(structure):
    root_path =  Path(__file__).parent.resolve()
    random_exit = pick_random_path(structure["maze-entrance"])
    full_path = root_path / "maze-entrance" / os.path.join(*random_exit)
    treasure_map = pick_random_path(structure["maze-entrance"])

    while(treasure_map == random_exit):
        treasure_map = pick_random_path(structure["maze-entrance"])

    treasure_map = root_path / "maze-entrance" / os.path.join(*treasure_map)

    try:
        if(os.path.exists(full_path)):
            file_path = full_path / "exit.txt"
            with open(file_path, "w") as file:
                if os.name == "posix":
                    file.write("YOU FOUND THE EXIT!!!\nType 'cd ~/Desktop' to return to the entrance.")
                elif os.name == "nt":
                    file.write("YOU FOUND THE EXIT!!!\nType\npowershell> 'cd ~\\Desktop' to return to the entrance.\ncmd prompt> 'cd %USERPROFILE%\\Desktop' to return to the entrance.")
                print(f"File hidden successfully at: {base64.b64encode(str(file_path).encode('utf-8')).decode('utf-8')}")
                print(f"Treasure map hidden successfully at:{base64.b64encode(str(treasure_map).encode('utf-8')).decode('utf-8')} ")

            with open(treasure_map / "exit.txt", "w") as f:
                f.write(f"The exit lies on this path: {file_path}")

            
        
        else:
            raise FileNotFoundError

    except FileNotFoundError as e:
        print(f"The file path could not be found, check your path.\n{e}")


def handle_arguments():
    if len(sys.argv) > 1:
        if sys.argv[1] == "clear":
            path = Path.home() / "Desktop"
            if(os.path.exists(path / "maze-entrance")):
                shutil.rmtree(path / "maze-entrance")
                print(f"Directory {path / 'maze-entrance'} and all its contents have been removed.")
                exit()
            else:
                print("Directory does not exist.\nExiting...")
                exit()
        else:
            print(f"Command Not Recognized.\nExiting...")
            exit()
    else:
        return

if __name__ == "__main__":
    handle_arguments()
    create_directories(base_path, maze_structure)
    print("Maze directory structure created successfully!")
    hide_file(maze_structure)




