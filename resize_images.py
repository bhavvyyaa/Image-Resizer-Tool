import os
from PIL import Image
import sys
import tkinter as tk
from tkinter import filedialog
import shutil

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

def resize_image(filename, target_width, target_height, output_format):
    
    input_path = os.path.join(INPUT_DIR, filename)
    target_size = (target_width, target_height)
    
    name_only, _ = os.path.splitext(filename)
    save_format = output_format.upper()
    
    if save_format == 'JPEG':
        new_ext = '.jpg'
    elif save_format == 'PNG':
        new_ext = '.png'
    else:
        new_ext = '.' + save_format.lower()
        
    output_filename = f"{name_only}_resized{new_ext}"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    try:
        with Image.open(input_path) as img:
            print(f"Processing {filename}...")

            resized_img = img.resize(target_size)
            
            save_kwargs = {}
            if save_format == 'JPEG':
                save_kwargs['quality'] = 90
            
            resized_img.save(output_path, format=save_format, **save_kwargs)
            print(f"   --> Saved successfully to {output_path}")

    except Exception as e:
        print(f"   --> Could not process {filename}. Error: {e}")

def get_user_inputs():
    
    while True:
        size_input = input("Enter target size (WIDTH HEIGHT, e.g., 800 600): ").strip()
        try:
            width_str, height_str = size_input.split()
            user_width = int(width_str)
            user_height = int(height_str)
            
            if user_width <= 0 or user_height <= 0:
                 print("Error: Dimensions must be positive numbers. Try again.")
                 continue
                 
            user_format = input("Enter desired output format (e.g., JPEG, PNG): ").strip() or 'JPEG'
            
            return user_width, user_height, user_format
            
        except ValueError:
            print("Error: Invalid input format. Please enter two whole numbers separated by a space.")
        except Exception:
             print("Error: Invalid input. Please enter both WIDTH and HEIGHT.")
             
    sys.exit("Failed to get valid dimensions and format.")


def select_file_for_resize(user_width, user_height, user_format):
    
    root = tk.Tk()
    root.withdraw() 
    
    print("\nPlease select an image file to resize...")
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"), ("All files", "*.*"))
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return

    if not os.path.exists(INPUT_DIR): os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    original_filename = os.path.basename(file_path)
    temp_input_path = os.path.join(INPUT_DIR, original_filename)

    try:
        shutil.copy(file_path, temp_input_path)
        print(f"File selected: {original_filename}")
        
        resize_image(original_filename, user_width, user_height, user_format)

    except Exception as e:
        print(f"An error occurred during file selection or copy: {e}")
        
    finally:
        if os.path.exists(temp_input_path):
            os.remove(temp_input_path)
            print(f"Cleaned up temporary file: {original_filename}")
        root.destroy()

def main():
    
    print("\n--- Single Image Resizer Tool ---")
    
    user_width, user_height, user_format = get_user_inputs()
    
    print("-" * 30)
    print(f"Target Size: {user_width}x{user_height}, Output Format: {user_format.upper()}")
    print("-" * 30)
    
    select_file_for_resize(user_width, user_height, user_format)
    
    print("\n--- Process Complete! ---")

if __name__ == "__main__":
    main()