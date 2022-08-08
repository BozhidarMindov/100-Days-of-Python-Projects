from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def place_watermark():
    wat_text = watermark_entry.get()
    file = filedialog.askopenfilename(title="Select your image")

    img = Image.open(file)
    img_width = img.size[0]
    img_height = img.size[1]
    draw = ImageDraw.Draw(img)

    font_size = int(img_width/10)

    font = ImageFont.truetype("arial.ttf", font_size)
    x = int(img_width/2)
    y = int(img_height/2)

    draw.text(
        xy=(x, y),
        text=wat_text,
        align="center",
        font=font,
        fill = "lightgrey",
        stroke_width=2,
        stroke_fill= "black",
        anchor = "ms"
              )

    img.show()

#Window
window = Tk()
window.title("Watermarking App")
window.geometry("500x150")
window.config(padx = 50, pady = 50)

#Label
watermark_label = Label(text= "Watermark text:", font = "Arial")
watermark_label.grid(row=0, column=0)

#Entry
watermark_entry = Entry(width = 20, font = "Arial")
watermark_entry.grid(row=0, column=1, padx=10, pady=10)

#storing the user's input
watermark_text = watermark_entry.get()

#when the button is clicked, the user will be allowed to choose an image
show_button = Button(text = "Choose an Image", command = place_watermark)
show_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()