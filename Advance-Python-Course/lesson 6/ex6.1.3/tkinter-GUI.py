import tkinter as tk
from tkinter import PhotoImage


def show_image():  # function that links the desired image to the empty label after the button was pressed
    # the main reason the image is set up in this function is because it takes up space even if it is not shown.
    photo = PhotoImage(file="sigit.png")
    image_label.configure(image=photo)
    image_label.image = photo
    button.pack_forget() # removes the button


# sets up the root scene
root = tk.Tk()

# configures the question text into the root
question_label = tk.Label(root, text="What is my favorite course?", font=("Arial", 24))
question_label.pack()  # shows the text

# configures the button into the root, and sets show image as its action+
button = tk.Button(root, text="Show Image", command=show_image, font=("Arial", 16))
button.pack()  # shows the button

# configures an empty label, this will hold the image when the button is pressed
image_label = tk.Label(root)
image_label.pack()

# starts the program
root.mainloop()
