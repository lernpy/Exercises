import os
import time

class CommandPrompt:
    def __init__(self, current_directory='.'):
        self.current_directory = current_directory

    def show_prompt(self):
        return f"{self.current_directory}> "

    def list_directories(self):
        return os.listdir(self.current_directory)

    def change_directory(self, new_directory):
        try:
            os.chdir(new_directory)
            self.current_directory = os.getcwd()
        except FileNotFoundError:
            raise Exception(f"Directory not found: {new_directory}")

    def create_directory(self, directory_name):
        os.mkdir(directory_name)

    def delete_directory(self, directory_name):
        os.rmdir(directory_name)

    def rename_directory(self, old_name, new_name):
        os.rename(old_name, new_name)

    def create_file(self, file_name):
        with open(file_name, 'w') as file:
            pass

    def delete_file(self, file_name):
        os.remove(file_name)

    def view_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def execute_time_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper

@CommandPrompt.execute_time_decorator
def main():
    cmd = CommandPrompt()

    while True:
        user_input = input(cmd.show_prompt())
        words = user_input.split()

        try:
            if words[0] == 'ls' or words[0] == 'dir':
                print(cmd.list_directories())
            elif words[0] == 'cd':
                cmd.change_directory(words[1])
            elif words[0] == 'create_dir':
                cmd.create_directory(words[1])
            elif words[0] == 'delete_dir':
                cmd.delete_directory(words[1])
            elif words[0] == 'rename_dir':
                cmd.rename_directory(words[1], words[2])
            elif words[0] == 'create_file':
                cmd.create_file(words[1])
            elif words[0] == 'delete_file':
                cmd.delete_file(words[1])
            elif words[0] == 'view_file':
                print(cmd.view_file(words[1]))
            elif words[0] == 'exit':
                break
            else:
                print("Invalid command. Type 'exit' to end.")
        except Exception as e:
            print(f"Error: {e}")

