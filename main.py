#this is for the 24-25 open day
#base story (credits to Leah):
'''There was a reunion party in the mountains
(It's near a town so the area isn't very secluded) and 
they had a picnic. They were watching the sunset when 
one of them said the trees blocked the view and they 
couldn't take pictures, so they went through the trees 
to a nearby cliff to take pictures. Then, the others 
heard a yelp not long after and they rushed over to see 
what happened. They saw the victim's camera on the ground 
and the victim was plummeting down. The victim was calling 
out, “(someone) pushed me!” But they couldn't hear the name 
because he was already very far down.'''

'''
characters:
ophelia : murderer
laurence : victim
veronica : friend (no role)
katrina : friend (no role)
nathan : friend (no role)
police officer

your role:
detective
'''

'''
picture dimensions
image1 : 780 x 780
image2 : 960 x 640
'''

import tkinter as tk
from PIL import Image, ImageTk

import keypad


def textbox(message):
    root = tk.Tk()
    root.title("message")
    root.geometry("400x200")

    label = tk.Label(root, text = message, bg = "white", fg = "black")

    label.pack()
    root.mainloop()

def image(imagenum, dimensionx, dimensiony):
    root = tk.Tk()
    root.title("testing")

    dimensions = str(dimensionx) + "x" + str(dimensiony)

    root.geometry(dimensions)

    filename = "assets/image" + str(imagenum) + ".png"

    photo = Image.open(filename)
    resized_image = photo.resize((dimensionx, dimensiony), Image.BILINEAR)
    converted_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(root, image = converted_image, bg = "white", fg = "black")

    label.pack()
    root.mainloop()


textbox("hello world")