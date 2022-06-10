import tkinter as tk
from PIL import ImageTk, Image
from pult import TVController


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)


def changes_for_controller(channel):
    controller.turn_channel(channel)
    change_image()


def first():
    controller.first_channel()
    change_image()


def last():
    controller.last_channel()
    change_image()


def current():
    print(controller.current_channel())


def next_cnl():
    controller.next_channel()
    change_image()


def prev_cnl():
    controller.previous_channel()
    change_image()


def change_image():
    lbl_tv_3["text"] = controller.current_channel()
    channel_img = (Image.open(f"{controller.current_channel()}.png"))
    resized_image = channel_img.resize((210, 190), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    lbl_tv_2.configure(image=new_image)
    lbl_tv_2.image = new_image



#Mainscreen
root = tk.Tk()
root.geometry("+1000+200")
root.resizable(0, 0)
root.title("Pult")


#Pult
pult_img = ImageTk.PhotoImage(Image.open("pult2.png"))
lbl1 = tk.Label(root, image=pult_img)
lbl1.pack()


#Pult_buttons
btn1 = tk.Button(root, text="1", height=1, width=5, font=25, bg="grey", command=lambda: changes_for_controller(1))
btn2 = tk.Button(root, text="2", height=1, width=5, font=25, bg="grey", command=lambda: changes_for_controller(2))
btn3 = tk.Button(root, text="3", height=1, width=5, font=25, bg="grey", command=lambda: changes_for_controller(3))
btn1.place(x=123, y=128)
btn2.place(x=190, y=128)
btn3.place(x=257, y=128)

btn_first = tk.Button(root, text="First", height=1, width=5, font=25, bg="grey", command=first)
btn_last = tk.Button(root, text="Last", height=1, width=5, font=25, bg="grey", command=last)
btn_first.place(x=123, y=275)
btn_last.place(x=257, y=275)

btn_current = tk.Button(root, text="Current", height=2, width=4, font=25, bg="grey", command=current)
btn_current.place(x=194, y=400)

btn_next = tk.Button(root, text="Next", height=1, width=5, font=25, bg="grey", command=next_cnl)
btn_prev = tk.Button(root, text="Prev", height=1, width=5, font=25, bg="grey", command=prev_cnl)
btn_next.place(x=257, y=343)
btn_prev.place(x=257, y=421)

#TV
telescreen = tk.Toplevel()
telescreen.geometry("+1500+200")
telescreen.title("TV")
telescreen.resizable(0, 0)
frame_tv = tk.Frame(telescreen)
frame_tv.place(anchor="center", relx=0.5, rely=0.5)
tv_img1 = ImageTk.PhotoImage(Image.open("tv.jpg"))
lbl_tv_1 = tk.Label(telescreen, image=tv_img1)
lbl_tv_1.pack()


#TV_screen
screen_frame = tk.Frame(telescreen)
screen_frame.place(x=108, y=170, height=160, width=210)
lbl_tv_2 = tk.Label(screen_frame)
lbl_tv_3 = tk.Label(telescreen, text="---", font=("", 30))
lbl_tv_2.pack()
lbl_tv_3.place(x=30, y=30)

telescreen.mainloop()
root.mainloop()

