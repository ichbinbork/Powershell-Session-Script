import os
import shutil

folder_path = input("Enter the log folder path: ") # Enter the path of the your log folder
                                                   # Example: C:\Logs\WindowsPowershelLogs
                                                   # And sure path is correct !!!

directorys = os.listdir(folder_path)
new_log_file_name = input("Enter your new malicious log files name: ")
new_dir_path = os.path.join(folder_path,new_log_file_name)
os.mkdir(new_dir_path)
print("Directory '% s' created" % new_log_file_name)

for sub_directory in directorys:

    for file_names in os.listdir(folder_path + "\\"+sub_directory):
        
        file = os.fsdecode(file_names) 

        if file.endswith(".txt"):

            new_path = os.path.join(folder_path, sub_directory, file)

            size = os.path.getsize(new_path)
            kilobyte_file_size = str(round(size/1024, 2))
            
            if float(kilobyte_file_size) >= 5:
                print("File name: " + file + " File size: " + kilobyte_file_size + " KB","Might be malicious Powershell session log" )

                malicious_files = []
                
                malicious_files += [file]
                shutil.copy(new_path, new_dir_path)

print("Copied to", new_dir_path)                             
print("     Copying of log files completed!!!")             
  