import os

def organize_files(directory):
    # Create folders for each file type
    folders = {
        'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'videos': ['mp4', 'avi', 'mov', 'wmv'],
        'documents': ['doc', 'docx', 'pdf', 'txt'],
        'audio': ['mp3', 'wav', 'ogg']
    }

    for folder, extensions in folders.items():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1][1:].lower()
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(directory, folder)
                    os.rename(file_path, os.path.join(dest_folder, filename))
                    break

# Get directory address from user
directory = input("Enter the directory address: ")

# Organize files
organize_files(directory)


print("Files organized successfully!")