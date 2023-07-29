# cris
GUI code for helping blind people in ticket system .




        

import tkinter as tk
from datetime import datetime

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ main code to convert text to braille ------------------------------------------------------------------
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', ' ': ' ',
    '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊'
}

def text_to_braille(find):
    braille_text = ''
    for char in find.lower():
        braille_char = braille_dict.get(char, '')
        braille_text += braille_char
    return braille_text

def translate_text():
    find = entry1.get()
    braille = text_to_braille(find)
    output_label.config(text=f" ⠥⠞⠎ ⠝⠕     {braille}")

#---------------------------------------------------------------------------------------------lable 
window = tk.Tk()
window.title("UTS blind help")
window.geometry("583x591+468+158")
window.configure(width=1500, height=1800, background="#dbd8d7")
window.resizable(False, False)

#---------------------------------------------------------------------------------------------backgtound
bg = tk.PhotoImage(file="D:\\cris\\back.png")
my_label = tk.Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------------------------------------------------------------------------------------logo
Label1 = tk.Label(window)
_img1 = tk.PhotoImage(file="D:\\cris\\1234.png")
Label1.configure(image=_img1)
Label1.pack()

#--------------------------------------------------------------------------------------------input  message - label 
label1 = tk.Label(window, text="UTS NO :")
label1.pack(padx=105, pady=20, side=tk.LEFT)

#---------------------------------------------------------------------------------------------input box - input box
entry1 = tk.Entry(window)
entry1.pack(padx=110, pady=20, side=tk.LEFT)

#---------------------------------------------------------------------------------------------output button
Button1 = tk.Button(window, text="Translate", command=translate_text)
Button1.place(x=300, y=450)

#------------------------------------------------------------------------------------------..OUTPUT  message (Braille) - label 
label2 = tk.Label(window, text="Braille:")
label2.place(x=105, y=500)

#----------------------------------------------------------------------------------------- output 
output_label = tk.Label(window, text="=>")
output_label.place(x=380, y=500)




#--------------------------------------------------------------------------------------------- timer
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

time_label = tk.Label(window, font=("Arial", 24))
time_label.place(x=0, y=0)

# Update the time initially
update_time()    


#---------------------------------------------------------------- from - lable 

from_label = tk.Label(window, text="From :")
from_label.place(x=100, y=250)
#---------------------------------------------------------------- from - entery 
entry3 = tk.Entry(window)
entry3.place(x=150,y=250)


#---------------------------------------------------------------- to - lable

to_label = tk.Label(window, text="To :")
to_label.place(x=300, y=250)

#------------------------------------------------------------------ to - entery 
entry2 = tk.Entry(window)
entry2.place(x=330,y=250)

#---------------------------------------------------------------------------------------------maker  name
output_labe2= tk.Label(window, text="made by vedant singh")
output_labe2.place(x=450, y=550)

window.mainloop()
        
