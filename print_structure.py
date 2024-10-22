import os

def print_directory_structure(start_path, indent=''):
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        if os.path.isdir(item_path):
            print(f"{indent}├── {item}/")
            print_directory_structure(item_path, indent + '│   ')
        else:
            print(f"{indent}├── {item}")

if __name__ == "__main__":
    project_path = '.'  # Adjust the path if you want to target a different folder
    print("Project Directory Structure:")
    print_directory_structure(project_path)
