import os
 
def upload_photo(photo):
    # Specify where the image will be saved
    upload_folder = 'static/images'
 
    # Create the folder if it does not exist
    os.makedirs(upload_folder, exist_ok=True)
 
    # Get the image file name
    filename = photo.filename
 
    # Create the image path
    photo_path = os.path.join(upload_folder, filename)
 
    # Save the image
    photo.save(photo_path)
 
    # Return the image file name
    return filename