from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Create the main window
root = Tk()
root.title("Image Resizer by File Size")
root.geometry("400x400")

# Global variables
img = None
img_path = ""

def upload_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])
    
    if img_path:
        img = Image.open(img_path)
        img.show()  # Display the image
        display_image_info()

def display_image_info():
    if img:
        width, height = img.size
        size = os.path.getsize(img_path) / 1024  # Size in KB
        size_str = f"{size:.2f} KB"
        info_label.config(text=f"Resolution: {width}x{height}\nFile Size: {size_str}\nFile Name: {os.path.basename(img_path)}")

def resize_image():
    if img:
        try:
            target_size = float(target_size_entry.get())
            unit = unit_var.get()
            if unit == "MB":
                target_size *= 1024  # Convert MB to KB

            # Resize the image iteratively until the target size is reached
            current_size = os.path.getsize(img_path) / 1024  # Size in KB
            new_img = img
            quality = 100

            while current_size > target_size and quality > 10:
                # Save the image to a temporary file to check its size
                temp_path = "temp_image.jpg"
                new_img.save(temp_path, quality=quality)
                current_size = os.path.getsize(temp_path) / 1024  # Size in KB
                quality -= 5  # Decrease quality to reduce size

            if current_size <= target_size:
                # Show the resized image
                new_img.show()
                save_option = messagebox.askyesno("Save Resized Image", "Do you want to save the resized image?")
                if save_option:
                    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", ".jpg;.jpeg")])
                    if save_path:
                        new_img.save(save_path, quality=quality + 5)  # Save with last successful quality
                        messagebox.showinfo("Success", "Resized image saved successfully!")
            else:
                messagebox.showerror("Error", "Could not reduce the image size sufficiently.")
            
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for file size.")
    else:
        messagebox.showerror("No Image", "Please upload an image first.")

# Create GUI elements
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

info_label = Label(root, text="")
info_label.pack(pady=5)

target_size_label = Label(root, text="Target File Size:")
target_size_label.pack(pady=5)
target_size_entry = Entry(root)
target_size_entry.pack(pady=5)

unit_var = StringVar(value="KB")
kb_radio = Radiobutton(root, text="KB", variable=unit_var, value="KB")
kb_radio.pack(anchor=W)
mb_radio = Radiobutton(root, text="MB", variable=unit_var, value="MB")
mb_radio.pack(anchor=W)

resize_button = Button(root, text="Resize Image", command=resize_image)
resize_button.pack(pady=10)

# Run the application
root.mainloop()