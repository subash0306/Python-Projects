from tkinter import Tk, Button, Label, filedialog, StringVar, OptionMenu, Entry, messagebox
from PIL import Image
import os

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter - Arttifai Tech")

        self.files = []

        # Widgets
        self.label = Label(master, text="Select images to convert")
        self.label.pack()

        self.select_button = Button(master, text="Select Images", command=self.select_files)
        self.select_button.pack()

        self.format_var = StringVar(master)
        self.format_var.set("PNG")  # default

        self.format_menu = OptionMenu(master, self.format_var, "PNG", "JPG", "BMP", "GIF")
        self.format_menu.pack()

        Label(master, text="Width (optional)").pack()
        self.width_entry = Entry(master)
        self.width_entry.pack()

        Label(master, text="Height (optional)").pack()
        self.height_entry = Entry(master)
        self.height_entry.pack()

        Label(master, text="JPEG Quality (1-100, optional)").pack()
        self.quality_entry = Entry(master)
        self.quality_entry.pack()

        self.convert_button = Button(master, text="Convert", command=self.convert_images)
        self.convert_button.pack()

    def select_files(self):
        self.files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.png *.bmp *.gif *.jpeg")])
        if self.files:
            self.label.config(text=f"{len(self.files)} files selected.")

    def convert_images(self):
        if not self.files:
            messagebox.showerror("Error", "No files selected!")
            return

        output_format = self.format_var.get().lower()
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

        width = self.width_entry.get()
        height = self.height_entry.get()
        quality = self.quality_entry.get()

        try:
            width = int(width) if width else None
            height = int(height) if height else None
            quality = int(quality) if quality else 85  # default quality for JPEG
        except ValueError:
            messagebox.showerror("Error", "Width, Height, and Quality must be numbers!")
            return

        success_count = 0
        for filepath in self.files:
            try:
                img = Image.open(filepath)
                if width and height:
                    img = img.resize((width, height))

                filename = os.path.splitext(os.path.basename(filepath))[0]
                out_path = os.path.join(output_dir, f"{filename}.{output_format}")

                if output_format == "jpg" or output_format == "jpeg":
                    img = img.convert("RGB")  # To ensure no transparency issues
                    img.save(out_path, output_format.upper(), quality=quality)
                else:
                    img.save(out_path, output_format.upper())

                success_count += 1
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")

        messagebox.showinfo("Done", f"Conversion complete: {success_count} / {len(self.files)} files converted.")

if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()
