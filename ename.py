import os

# Set the directory where files are located (change this if needed)
directory = "C:\\Users\\Pranjal\\Desktop\\Projects\\100 days Projects\\shorts\\Html,css and javascript"

# Loop through all files in the directory
for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)
    
    # Skip directories, rename only files
    if os.path.isfile(old_path):
        new_filename = "0" + filename  # Add "0" prefix
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_filename}")

print("All files renamed successfully!")
