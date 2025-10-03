# Image Resizer Tool

This repository contains the solution for **Task 7: Image Resizer Tool**, developed as part of the Python Developer Internship.

---

## Objective
The primary objective of this tool is to provide a **Python-based image resizer and format converter**.  
It allows users to interactively choose an image, resize it to custom dimensions, and optionally convert its format.

---

## Key Features
- **Single File Selection**  
  Uses `tkinter.filedialog` to let users pick an image file interactively.

- **Dynamic Input**  
  Prompts for **width**, **height**, and **desired output format** via the console.

- **Image Resizing**  
  Utilizes `PIL.Image.resize()` to scale images precisely.

- **Format Conversion**  
  Supports conversion between formats (e.g., **PNG → JPEG**) during save.

- **Error Handling**  
  Built-in checks for invalid inputs, missing files, and image processing errors.

- **Clean-up**  
  Temporary files created for input are automatically removed after processing.

---

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**
- **Pillow** library for image processing
- **Tkinter** (comes pre-installed with most Python distributions)

Install Pillow with:
```bash
pip install Pillow
```

## How to run the tool
### 1. Setup Directories
- Create a folder named **`output`** in the same directory as the script.  
- The script will automatically create a temporary input folder if required.

---

### 2. Execute the Script
Run the script from your terminal/command line (avoid IDE integrated terminals as they sometimes hide the file dialog):
```bash
python resize_images.py
```
#### NOTE
The resized image will be saved in the ```bash /.output ``` directory.
