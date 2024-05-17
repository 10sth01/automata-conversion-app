import os

try: 
     from tkinter import *
     from tkinter import Tk, Button, PhotoImage, Label, Toplevel
     from tkinter import ttk
     from tkinter.font import Font
     from PIL import Image, ImageTk
     from urllib import request
     import io
except ImportError:
     os.system('python -m pip install tkinter')
     os.system('python -m pip install Pillow')
     os.system('python -m pip install urllib')
     os.system('python -m pip install io')
     os.system('python -m pip install ttk')

screen = Tk()
screen.title("Automata Project")
screen.geometry("1000x1000")

# Create a background frame and set its color
background_frame = Frame(screen, bg="light gray")
background_frame.pack(side='top', fill='both', expand=True)

# Create a notebook
notebook = ttk.Notebook(background_frame, width=900, height=1000)
notebook.pack(side='top', pady=10, expand=True)



# create frames
frame1 = ttk.Frame(notebook,  style="Frame.TFrame")
frame2 = ttk.Frame(notebook,  style="Frame.TFrame")
frame3 = ttk.Frame(notebook,  style="Frame.TFrame")



frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

notebook.add(frame1, text='Starting Page')
notebook.add(frame2, text='Regex1')
notebook.add(frame3, text='Regex2')

# Set frame style
style = ttk.Style()
# style.configure("Frame.TFrame", background="white")

bfont = Font(family = "Helvetica",
             size = "30",
             weight="bold",
             slant = "roman",
             underline=0,
             overstrike=0)

mfont = Font(family = "Helvetica",
             size = "18",
             weight="bold",
             slant = "roman",
             underline=0,
             overstrike=0)

sfont = Font(family = "Helvetica",
             size = "12",
             weight="bold",
             slant = "roman",
             underline=0,
             overstrike=0)


# Frame 1 
Label(frame1, text = "Welcome!",   width = 50, height = 3, font = bfont).pack()

Label(frame1, text = "This application will convert the given Regular expressions to Deterministic ",   width = 100, height = 1, font = sfont).pack()
Label(frame1, text = "finite Automata (DFA), Context-Free Grammars (CFG), and Pushdown Automata (PDA).",   width = 100, height = 1, font = sfont).pack()

Label(frame1, text = "1. Usage Guidelines",   width = 50, height = 3, font = bfont, anchor= "w").pack(padx=20)

Label(frame1, text = "1.1. Selecting a Regular Expression:",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=50)
Label(frame1, text = "• From the tabs above, click on the desired regular expression to begin the conversion process.",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)
Label(frame1, text = "• Alternatively, you can use the buttons below to directly navigate to the desired regex tab.",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)
Label(frame1, text = "",   width = 100, height = 1, font = sfont, anchor= "w" ).pack()

Label(frame1, text = "1.2. Validating a String:",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=50)
Label(frame1, text = "• Enter a string in the provided input field.",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)
Label(frame1, text = "• Click the 'Validate' button to check if the entered string is valid.",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)
Label(frame1, text = "• The program will verify the validity of the string by traversing through each state.",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)

Label(frame1, text = "2. Regular Expression",   width = 50, height = 3, font = bfont, anchor= "w").pack(padx=20)

Label(frame1, text = "2.1. Regular Expression Examples:",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=50)
Label(frame1, text = "• (bab+bbb) a* b* (a*+b*) (ba) + (aba) (bab+aba) + bb(a+b)* (bab+aba) (a+b)*",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)
Label(frame1, text = "• (1+0)* 1* 0* (101+01+000) (1+0)* (101+00)* (111+00+101) (1+0)*",   width = 100, height = 1, font = sfont, anchor= "w" ).pack(padx=60)

Label(frame1, text = "",   width = 100, height = 1, font = sfont, anchor= "w" ).pack()
Label(frame1, text = "",   width = 100, height = 1, font = sfont, anchor= "w" ).pack()
Label(frame1, text = "Please use the buttons below to navigate to the respective regular",   width = 100, height = 1, font = sfont).pack()
Label(frame1, text = "expression page and convert it into DFA, CFG, and PDA.",   width = 100, height = 1, font = sfont).pack()



# Frame 2
# Variable Declaration
alphabets = {'a', 'b'}
final_states = {'q15'}
current_state = 'q0'
out = ""


# States
def q0(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q1'
     elif i == 'b' or i == 'B': 
          current_state='q2'

def q1(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q1'
     elif i == 'b' or i == 'B': 
          current_state='q1'
          
def q2(i): 
     global current_state
     if i == 'a' or i == 'A':
          current_state='q3'
     elif i == 'b' or i == 'B': 
          current_state='q3'

def q3(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q1'
     elif i == 'b' or i == 'B': 
          current_state='q4'
          
def q4(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q6'
     elif i == 'b' or i == 'B': 
          current_state='q5'

def q5(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q6'
     elif i == 'b' or i == 'B': 
          current_state='q5'

def q6(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q6'
     elif i == 'b' or i == 'B': 
          current_state='q7'
          
def q7(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q8'
     elif i == 'b' or i == 'B': 
          current_state='q5'

def q8(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q8'
     elif i == 'b' or i == 'B': 
          current_state='q9'

def q9(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q8'
     elif i == 'b' or i == 'B': 
          current_state='q10'

def q10(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q11'
     elif i == 'b' or i == 'B': 
          current_state='q12'

def q11(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q11'
     elif i == 'b' or i == 'B': 
          current_state='q13'

def q12(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q14'
     elif i == 'b' or i == 'B': 
          current_state='q12'

def q13(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q15'
     elif i == 'b' or i == 'B': 
          current_state='q12'
     
def q14(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q11'
     elif i == 'b' or i == 'B': 
          current_state='q15'

def q15(i):
     global current_state
     if i == 'a' or i == 'A':
          current_state='q15'
     elif i == 'b' or i == 'B': 
          current_state='q15'   

# Dito maglalagay ng function reset   
def handle_input_change(event):
    input_text = input_storage.get()
    if not input_text:
        out_text.config(text="")
        dfa_container.itemconfig(q0_circle, fill="white")
        dfa_container.itemconfig(q1_circle, fill="white")
        dfa_container.itemconfig(q2_circle, fill="white")
        dfa_container.itemconfig(q3_circle, fill="white")
        dfa_container.itemconfig(q4_circle, fill="white")
        dfa_container.itemconfig(q5_circle, fill="white")
        dfa_container.itemconfig(q6_circle, fill="white")
        dfa_container.itemconfig(q7_circle, fill="white")
        dfa_container.itemconfig(q8_circle, fill="white")
        dfa_container.itemconfig(q9_circle, fill="white")
        dfa_container.itemconfig(q10_circle, fill="white")
        dfa_container.itemconfig(q11_circle, fill="white")
        dfa_container.itemconfig(q12_circle, fill="white")
        dfa_container.itemconfig(q13_circle, fill="white")
        dfa_container.itemconfig(q14_circle, fill="white")
        dfa_container.itemconfig(q15_circle, fill="white")

def run():
     global name_storagem, current_state, final_states, out_text, dfa_container
     input = input_storage.get()

     out_text.config(text="")
     
     for circle in state_mapping.values():
          dfa_container.itemconfig(circle, fill="white")
          
     for i in input:
          if i not in alphabets:
               out_text.config(text = "String Rejected")
               return
          
          if current_state == 'q0':
               dfa_container.itemconfig(q0_circle, fill="orange")
               screen.update()
               q0(i)
          elif current_state == 'q1':
               dfa_container.itemconfig(q1_circle, fill="orange")
               screen.update()
               q1(i)
          elif current_state == 'q2':
               dfa_container.itemconfig(q2_circle, fill="orange")
               screen.update()
               q2(i)
          elif current_state == 'q3':
               dfa_container.itemconfig(q3_circle, fill="orange")
               screen.update()
               q3(i)
          elif current_state == 'q4':
               dfa_container.itemconfig(q4_circle, fill="orange")
               screen.update()
               q4(i)
          elif current_state == 'q5':
               dfa_container.itemconfig(q5_circle, fill="orange")
               screen.update()
               q5(i)
          elif current_state == 'q6':
               dfa_container.itemconfig(q6_circle, fill="orange")
               screen.update()
               q6(i)
          elif current_state == 'q7':
               dfa_container.itemconfig(q7_circle, fill="orange")
               screen.update()
               q7(i)
          elif current_state == 'q8':
               dfa_container.itemconfig(q8_circle, fill="orange")
               screen.update()
               q8(i)
          elif current_state == 'q9':
               dfa_container.itemconfig(q9_circle, fill="orange")
               screen.update()
               q9(i)
          elif current_state == 'q10':
               dfa_container.itemconfig(q10_circle, fill="orange")
               screen.update()
               q10(i)
          elif current_state == 'q11':
               dfa_container.itemconfig(q11_circle, fill="orange")
               screen.update()
               q11(i)
          elif current_state == 'q12':
               dfa_container.itemconfig(q12_circle, fill="orange")
               screen.update()
               q12(i)
          elif current_state == 'q13':
               dfa_container.itemconfig(q13_circle, fill="orange")
               screen.update()
               q13(i)
          elif current_state == 'q14':
               dfa_container.itemconfig(q14_circle, fill="orange")
               screen.update()
               q14(i)
          elif current_state == 'q15':
               dfa_container.itemconfig(q15_circle, fill="orange")
               screen.update()
               q15(i)
               
          screen.after(500)
          
     if current_state in final_states:
          out_text.config(text = "Valid String!", fg="DarkGreen")
          dfa_container.itemconfig(q15_circle, fill="DarkOliveGreen1")
     elif input_storage.get().strip() == "":
          out_text.config(text="Please Enter Valid String.")
     else:
          dfa_container.itemconfig(state_mapping[current_state], fill="red")
          out_text.config(text = "Invalid String!", fg="red")
          
     current_state = 'q0'

# Show PDA Image
def show_pda_image():
    # Create a new window for displaying the image
     popup = Toplevel(screen)
     popup.title("PDA Image")

    # Load and display the image
     image_url = "https://i.ibb.co/CPj4JrZ/pda1.png"
     response = request.urlopen(image_url)
     image_data = response.read()

     image = Image.open(io.BytesIO(image_data))
     resized_image = image.resize((600, 800))  # Resize the image to desired dimensions
     photo_image = ImageTk.PhotoImage(resized_image)

     # Display the resized image
     image_label = Label(popup, image=photo_image)
     image_label.image = photo_image  # Store a reference to prevent the image from being garbage collected
     image_label.pack()

# Show CFG Image
def show_cfg_image():
    # Create a new window for displaying the image
     popup = Toplevel(screen)
     popup.title("CFG Image")

    # Load and display the image
     image_url = "https://i.ibb.co/WxddMK8/cfg1.png"
     response = request.urlopen(image_url)
     image_data = response.read()

     image = Image.open(io.BytesIO(image_data))
     resized_image = image.resize((300, 300))  # Resize the image to desired dimensions
     photo_image = ImageTk.PhotoImage(resized_image)

     # Display the resized image
     image_label = Label(popup, image=photo_image)
     image_label.image = photo_image  # Store a reference to prevent the image from being garbage collected
     image_label.pack()

# DFA
dfa_container = Canvas(frame2, width=850, height=630, bg="white")
# Draw states
q0_circle = dfa_container.create_oval(150, 70, 180, 100, fill="white")
q1_circle = dfa_container.create_oval(150, 150, 180, 180, fill="white")
q2_circle = dfa_container.create_oval(230, 70, 260, 100, fill="white")
q3_circle = dfa_container.create_oval(295, 70, 325, 100, fill="white")
q4_circle = dfa_container.create_oval(380, 70, 410, 100, fill="white")
q5_circle = dfa_container.create_oval(380, 150, 410, 180, fill="white")
q6_circle = dfa_container.create_oval(460, 150, 490, 180, fill="white")
q7_circle = dfa_container.create_oval(540, 150, 570, 180, fill="white")
q8_circle = dfa_container.create_oval(620, 150, 650, 180, fill="white")
q9_circle = dfa_container.create_oval(620, 230, 650, 260, fill="white")
q10_circle = dfa_container.create_oval(620, 310, 650, 340, fill="white")
q11_circle = dfa_container.create_oval(570, 390, 600, 420, fill="white")
q12_circle = dfa_container.create_oval(670, 390, 700, 420, fill="white")
q13_circle = dfa_container.create_oval(570, 470, 600, 500, fill="white")
q14_circle = dfa_container.create_oval(670, 470, 700, 500, fill="white")
q15_circle = dfa_container.create_oval(620, 550, 650, 580, fill="white")

state_mapping = {
     'q0': q0_circle,
     'q1': q1_circle,
     'q2': q2_circle,
     'q3': q3_circle,
     'q4': q4_circle,
     'q5': q5_circle,
     'q6': q6_circle,
     'q7': q7_circle,
     'q8': q8_circle,
     'q9': q9_circle,
     'q10': q10_circle,
     'q11': q11_circle,
     'q12': q12_circle,
     'q13': q13_circle,
     'q14': q14_circle,
     'q15': q15_circle,
}

# Draw transitions
q0_q1 = dfa_container.create_line(165, 100, 165, 150, arrow=LAST)
q1_q1 = dfa_container.create_line(180, 171, 189, 174, 198, 214, 151, 229, 130, 190, 150,170, arrow=LAST, smooth=1)
q0_q2 = dfa_container.create_line(180, 85, 230, 85, arrow=LAST)
q2_q3 = dfa_container.create_line(260, 85, 295, 85, arrow=LAST)
q3_q1 = dfa_container.create_line(310, 100, 180, 165, arrow=LAST)
q3_q4 = dfa_container.create_line(325, 85, 380, 85, arrow=LAST)
q4_q5 = dfa_container.create_line(395, 100, 395, 150, arrow=LAST)
q4_q6 = dfa_container.create_line(410, 90, 470, 150, arrow=LAST)
q5_q5 = dfa_container.create_line(390, 180, 370, 200, 380, 160, arrow=LAST, smooth=1)
q5_q6 = dfa_container.create_line(410, 165, 460, 165, arrow=LAST)
q6_q6 = dfa_container.create_line(480, 150, 490, 130, 500, 160, 490, 160, arrow=LAST, smooth=1)
q6_q7 = dfa_container.create_line(490, 165, 540, 165, arrow=LAST)
q7_q8 = dfa_container.create_line(570, 165, 620, 165, arrow=LAST)
q7_q5 = dfa_container.create_line(550, 180, 480, 230, 400, 180, arrow=LAST, smooth=1)
q8_q8 = dfa_container.create_line(630, 150, 660, 130, 650, 170, arrow=LAST, smooth=1)
q8_q9 = dfa_container.create_line(635, 180, 635, 230, arrow=LAST)
q9_q10 = dfa_container.create_line(635, 260, 635, 310, arrow=LAST) 
q9_q8 = dfa_container.create_line(650, 240, 670, 210, 650, 170, arrow=LAST, smooth =1)
q10_q11 = dfa_container.create_line(625, 335, 585, 390, arrow=LAST)
q10_q12 = dfa_container.create_line(645, 335, 675, 390, arrow=LAST)
q11_q11 = dfa_container.create_line(570, 410, 550, 380, 580, 395, arrow=LAST, smooth=1)
q11_q13 = dfa_container.create_line(585, 420, 585, 470, arrow=LAST)
q12_q14 = dfa_container.create_line(685, 420, 685, 470, arrow=LAST)
q12_q12 = dfa_container.create_line(680, 390, 700, 360, 700, 400, arrow=LAST, smooth=1)
q13_q15 = dfa_container.create_line(585, 500, 625, 555, arrow=LAST)
q14_q15 = dfa_container.create_line(685, 500, 645, 555, arrow=LAST)
q13_q12 = dfa_container.create_line(590, 470, 670, 410, arrow=LAST)
q14_q11 = dfa_container.create_line(680, 470, 600, 410, arrow=LAST)
q15_q15 = dfa_container.create_line(620, 560, 640, 530, 640, 555, arrow=LAST, smooth=1)

# States labels
q0_label = dfa_container.create_text(165, 85, text="-")
q1_label = dfa_container.create_text(165, 165, text="T")
q2_label = dfa_container.create_text(245, 85, text="q2")
q3_label = dfa_container.create_text(310, 85, text="q3")
q4_label = dfa_container.create_text(395, 85, text="q4")
q5_label = dfa_container.create_text(395, 165, text="q5")
q6_label = dfa_container.create_text(475, 165, text="q6")  
q7_label = dfa_container.create_text(555, 165, text="q7")
q8_label = dfa_container.create_text(635, 165, text="q8") 
q9_label = dfa_container.create_text(635, 245, text="q9")
q10_label = dfa_container.create_text(635, 325, text="q10")
q11_label = dfa_container.create_text(585, 405, text="q11")
q12_label = dfa_container.create_text(685, 405, text="q12")
q13_label = dfa_container.create_text(585, 485, text="q13")
q14_label = dfa_container.create_text(685, 485, text="q14")
q15_label = dfa_container.create_text(635, 565, text="+")

# Transitions labels
q0_q1_label = dfa_container.create_text(155, 120, text="a")
q0_q2_label = dfa_container.create_text(200, 75, text="b")
q1_q1_label = dfa_container.create_text(155, 200, text="a, b")
q2_q3_label = dfa_container.create_text(275, 75, text="a, b")
q3_q1_label = dfa_container.create_text(235, 125, text="a")
q3_q4_label = dfa_container.create_text(350, 75, text="b")
q4_q5_label = dfa_container.create_text(385, 120, text="b")
q4_q6_label = dfa_container.create_text(445, 110, text="a")
q5_q5_label = dfa_container.create_text(390, 200, text="b")
q5_q6_label = dfa_container.create_text(435, 155, text="a")
q6_q7_label = dfa_container.create_text(510, 155, text="b")
q7_q5_label = dfa_container.create_text(480, 220, text= "b")
q7_q8_label = dfa_container.create_text(590, 155, text="a")
q8_q8_label = dfa_container.create_text(650, 130, text= "a")
q8_q9_label = dfa_container.create_text(645, 200, text="b")
q9_q10_label = dfa_container.create_text(645, 280, text="b")
q9_q8_label = dfa_container.create_text(670, 200, text="a")
q10_q11_label = dfa_container.create_text(595, 355, text="a")
q10_q12_label = dfa_container.create_text(675, 355, text="b")
q11_q11_label = dfa_container.create_text(550, 400, text="a")
q11_q13_label = dfa_container.create_text(575, 440, text="b")
q12_q12_label = dfa_container.create_text(710, 380, text="b")
q12_q14_label = dfa_container.create_text(695, 440, text="a")
q13_q12_label = dfa_container.create_text(610, 465, text="b")
q14_q11_label = dfa_container.create_text(660, 465, text="a")
q13_q15_label = dfa_container.create_text(590, 525, text="a")
q14_q15_label = dfa_container.create_text(680, 525, text="b")
q15_q15_label = dfa_container.create_text(640, 530, text="a, b")

# Create widgets
dfatext = Label(frame2, text="DFA SIMULATOR", font=("Helvetica", 30), fg="#2d3748")
top_container = Frame(frame2)
left_container = Frame(top_container)
right_container = Frame(top_container)
prompt_text = Label(left_container, text="Enter String:", font=("Helvetica", 16))
input_storage = StringVar()
input = Entry(left_container, textvariable=input_storage, font=("Helvetica", 12))
button_frame = Frame(left_container)
run_button = Button(button_frame, text="Validate", command=run, width=10, font=("Helvetica", 12), bg='SkyBlue3', relief='flat')
regEx_label = Label(right_container, text="Regular Expression:", font=("Helvetica", 16))
regEx_text = Label(right_container, text="(bab+bbb) a*b* (a*+b*) (ba)* (aba) (bab + aba)* bb(a+b)* (bab+aba) (a+b)*", font=("Helvetica", 9))
regEx_sample = Label(left_container, text="Sample String: bbbababbbab", font=("Helvetica", 9), fg="grey")
show_pda_button = Button(right_container, text="Show PDA", width=12, font=("Helvetica", 12), command=show_pda_image, bg='SkyBlue3', relief='flat')
show_cfg_button = Button(right_container, text="Show CFG", width=12, font=("Helvetica", 12), command=show_cfg_image, bg='SkyBlue3', relief='flat')
out_text = Label(frame2, text="", font=("Helvetica", 12), fg="red")

# Configure the input field to make it bigger
input.configure(width=30)

# Place widgets using pack layout manager
dfatext.pack(anchor='nw', padx=20, pady=(25, 0))
top_container.pack(side="top", padx=20, pady=0)
left_container.pack(side="left", padx=20, pady=10)
right_container.pack(side="left", padx=20, pady=10)
prompt_text.pack(side='top', anchor='w', padx=20, pady=(10, 10))
input.pack(side='top', anchor='w', padx=25)
button_frame.pack(side='bottom', anchor='w', padx=25, pady=(0, 20))
run_button.pack(side='left')
regEx_label.pack(anchor='nw', padx=20)
regEx_text.pack(anchor='e', padx=22, pady=10)
regEx_sample.pack(anchor='w', padx=20, pady=(0,10))
show_pda_button.pack(side="right", padx=10, pady=(0, 10))
show_cfg_button.pack(side="right", padx=10, pady=(0, 10))
input.bind("<KeyRelease>", handle_input_change)
out_text.pack()
dfa_container.pack()





#Frame 3
#Regex 2 ===============================================================================================================================================================


# Variable Declaration
alphabets2 = {'0', '1'}
final_states2 = {'qq9'}
current_state2 = 'qq0'
out2 = ""

# States
def qq0(i):
     global current_state2
     if i == '1':
          current_state2='qq1'
     elif i == '0':
          current_state2='qq2'

def qq1(i):
     global current_state2
     if i == '1':
          current_state2='qq1'
     elif i == '0':
          current_state2='qq2'

def qq2(i):
     global current_state2
     if i == '1':
          current_state2='qq4'
     elif i == '0':
          current_state2='qq3'
          
def qq3(i):
     global current_state2
     if i == '1':
          current_state2='qq4'
     elif i == '0':
          current_state2='qq4'
          
def qq4(i):
     global current_state2
     if i == '1':
          current_state2='qq6'
     elif i == '0':
          current_state2='qq5'
          
def qq5(i):
     global current_state2
     if i == '1':
          current_state2='qq6'
     elif i == '0':
          current_state2='qq9'

def qq6(i):
     global current_state2
     if i == '1':
          current_state2='qq8'
     elif i == '0':
          current_state2='qq7'
          
def qq7(i):
     global current_state2
     if i == '1':
          current_state2='qq9'
     elif i == '0':
          current_state2='qq9'
          
def qq8(i):
     global current_state2
     if i == '1':
          current_state2='qq9'
     elif i == '0':
          current_state2='qq7'
          
def qq9(i):
     global current_state2
     if i == '1':
          current_state2='qq9'
     elif i == '0':
          current_state2='qq9'

def handle_input2_change(event):
    input2_text = input2_storage2.get()
    if not input2_text:
        out2_text2.config(text="")
        dfa_container2.itemconfig(qq0_circle, fill="white")
        dfa_container2.itemconfig(qq1_circle, fill="white")
        dfa_container2.itemconfig(qq2_circle, fill="white")
        dfa_container2.itemconfig(qq3_circle, fill="white")
        dfa_container2.itemconfig(qq4_circle, fill="white")
        dfa_container2.itemconfig(qq5_circle, fill="white")
        dfa_container2.itemconfig(qq6_circle, fill="white")
        dfa_container2.itemconfig(qq7_circle, fill="white")
        dfa_container2.itemconfig(qq8_circle, fill="white")
        dfa_container2.itemconfig(qq9_circle, fill="white")
   
# Main    

def run2():
     global name_storagem, current_state2, final_states2, out2_text2, dfa_container2
     input2 = input2_storage2.get()
     
     out2_text2.config(text="")

     for circle in state_mapping2.values():
          dfa_container2.itemconfig(circle, fill="white")
          
     for i in input2:
          if i not in alphabets2:
               out2_text2.config(text = "String Rejected", fill='red')
               return
          
          if current_state2 == 'qq0':
               dfa_container2.itemconfig(qq0_circle, fill="orange")
               screen.update()
               qq0(i)
          elif current_state2 == 'qq1':
               dfa_container2.itemconfig(qq1_circle, fill="orange")
               screen.update()
               qq1(i)
          elif current_state2 == 'qq2':
               dfa_container2.itemconfig(qq2_circle, fill="orange")
               screen.update()
               qq2(i)
          elif current_state2 == 'qq3':
               dfa_container2.itemconfig(qq3_circle, fill="orange")
               screen.update()
               qq3(i)
          elif current_state2 == 'qq4':
               dfa_container2.itemconfig(qq4_circle, fill="orange")
               screen.update()
               qq4(i)
          elif current_state2 == 'qq5':
               dfa_container2.itemconfig(qq5_circle, fill="orange")
               screen.update()
               qq5(i)
          elif current_state2 == 'qq6':
               dfa_container2.itemconfig(qq6_circle, fill="orange")
               screen.update()
               qq6(i)
          elif current_state2 == 'qq7':
               dfa_container2.itemconfig(qq7_circle, fill="orange")
               screen.update()
               qq7(i)
          elif current_state2 == 'qq8':
               dfa_container2.itemconfig(qq8_circle, fill="orange")
               screen.update()
               qq8(i)
          elif current_state2 == 'qq9':
               dfa_container2.itemconfig(qq9_circle, fill="DarkOliveGreen1")
               screen.update()
               qq9(i)
          
          screen.update()
          screen.after(500)
          
     if current_state2 in final_states2:
          dfa_container2.itemconfig(qq9_circle, fill="DarkOliveGreen1")
          out2_text2.config(text = "Valid String!", fg="DarkGreen")
     elif input2_storage2.get().strip() == "":
          out2_text2.config(text="Please Enter Valid String.")
     else:
          dfa_container2.itemconfig(state_mapping2[current_state2], fill="red")
          out2_text2.config(text = "Invalid String!", fg="red")
          
     current_state2 = 'qq0'


# Show PDA Image
def show_pda_image2():
    # Create a new window for displaying the image
     popup = Toplevel(screen)
     popup.title("PDA Image")

    # Load and display the image
     image_url = "https://i.ibb.co/g9TPggr/pda2.png"
     response = request.urlopen(image_url)
     image_data = response.read()

     image = Image.open(io.BytesIO(image_data))
     resized_image = image.resize((800, 700))  # Resize the image to desired dimensions
     photo_image = ImageTk.PhotoImage(resized_image)

     # Display the resized image
     image_label = Label(popup, image=photo_image)
     image_label.image = photo_image  # Store a reference to prevent the image from being garbage collected
     image_label.pack()

# Show CFG Image
def show_cfg_image2():
    # Create a new window for displaying the image
     popup = Toplevel(screen)
     popup.title("CFG Image")

    # Load and display the image
     image_url = "https://i.ibb.co/RQ9ZhcP/cfg2.png"
     response = request.urlopen(image_url)
     image_data = response.read()

     image = Image.open(io.BytesIO(image_data))
     resized_image = image.resize((300, 300))  # Resize the image to desired dimensions
     photo_image = ImageTk.PhotoImage(resized_image)

     # Display the resized image
     image_label = Label(popup, image=photo_image)
     image_label.image = photo_image  # Store a reference to prevent the image from being garbage collected
     image_label.pack()


# DFA
dfa_container2 = Canvas(frame3, width=850, height=630, bg="white")

# Draw states
qq0_circle = dfa_container2.create_oval(140, 220, 170, 250, fill="white")
qq1_circle = dfa_container2.create_oval(220, 220, 250, 250, fill="white")
qq2_circle = dfa_container2.create_oval(220, 310, 250, 340, fill="white")
qq3_circle = dfa_container2.create_oval(300, 310, 330, 340, fill="white")
qq4_circle = dfa_container2.create_oval(380, 310, 410, 340, fill="white")
qq5_circle = dfa_container2.create_oval(460, 220, 490, 250, fill="white")
qq6_circle = dfa_container2.create_oval(460, 310, 490, 340, fill="white")
qq7_circle = dfa_container2.create_oval(500, 390, 530, 420, fill="white")
qq8_circle = dfa_container2.create_oval(540, 310, 570, 340, fill="white")
qq9_circle = dfa_container2.create_oval(620, 310, 650, 340, fill="white")

state_mapping2 = {
     'qq0': qq0_circle,
     'qq1': qq1_circle,
     'qq2': qq2_circle,
     'qq3': qq3_circle,
     'qq4': qq4_circle,
     'qq5': qq5_circle,
     'qq6': qq6_circle,
     'qq7': qq7_circle,
     'qq8': qq8_circle,
     'qq9': qq9_circle
}

# Draw transitions
qq0_qq1 = dfa_container2.create_line(170, 235, 220, 235, arrow=LAST)
qq0_qq2 = dfa_container2.create_line(170, 235, 220, 325, arrow=LAST)
qq1_qq2 = dfa_container2.create_line(235, 250, 235, 310, arrow=LAST)
qq2_qq2 = dfa_container2.create_line(230, 220, 270, 180, 250, 230, arrow=LAST, smooth = 1)
qq2_qq3 = dfa_container2.create_line(250, 325, 300, 325, arrow=LAST)
qq2_qq4 = dfa_container2.create_line(240,310, 310,250, 390,310, arrow=LAST, smooth=1)
qq3_qq4 = dfa_container2.create_line(330, 325, 380, 325, arrow=LAST)
qq4_qq5 = dfa_container2.create_line(400, 310, 460, 240, arrow=LAST)
qq4_qq6 = dfa_container2.create_line(410, 325, 460, 325, arrow=LAST)
qq5_qq6 = dfa_container2.create_line(475, 250, 475, 310, arrow=LAST)
qq6_qq7 = dfa_container2.create_line(485, 340, 505, 395, arrow=LAST)
qq6_qq8 = dfa_container2.create_line(490, 325, 540, 325, arrow=LAST)
qq7_qq9 = dfa_container2.create_line(530, 400, 625, 330, arrow=LAST)
qq8_qq7 = dfa_container2.create_line(555, 340, 525, 395, arrow=LAST)
qq8_qq9 = dfa_container2.create_line(570, 325, 620, 325, arrow=LAST)
qq5_qq9 = dfa_container2.create_line(490, 235, 620, 320, arrow=LAST)
qq9_qq9 = dfa_container2.create_line(640,310, 670,300, 690,340, 660,360, 640,340, arrow=LAST, smooth=1)

# States labels
qq0_label = dfa_container2.create_text(155, 235, text="-")
qq1_label = dfa_container2.create_text(235, 235, text="q1")
qq2_label = dfa_container2.create_text(235, 325, text="q2")
qq3_label = dfa_container2.create_text(315, 325, text="q3")
qq4_label = dfa_container2.create_text(395, 325, text="q4")
qq5_label = dfa_container2.create_text(475, 235, text="q5")
qq6_label = dfa_container2.create_text(475, 325, text="q6")  
qq7_label = dfa_container2.create_text(515, 405, text="q7")
qq8_label = dfa_container2.create_text(555, 325, text="q8")
qq9_label = dfa_container2.create_text(635, 325, text="+")

# Transitions labels
qq0_qq1_label = dfa_container2.create_text(195, 225, text="1")
qq0_qq2_label = dfa_container2.create_text(180, 275, text="0")
qq1_qq2_label = dfa_container2.create_text(245, 280, text="0")
qq2_qq2_label = dfa_container2.create_text(250, 190, text="1")
qq2_qq3_label = dfa_container2.create_text(275, 335, text="0")
qq2_qq4_label = dfa_container2.create_text(310, 270, text="1")
qq3_qq4_label = dfa_container2.create_text(355, 335, text="0, 1")
qq4_qq5_label = dfa_container2.create_text(420, 270, text="0")
qq4_qq6_label = dfa_container2.create_text(435, 335, text="1")
qq5_qq6_label = dfa_container2.create_text(485, 280, text="1")
qq5_qq9_label = dfa_container2.create_text(555, 265, text="0")
qq6_qq8_label = dfa_container2.create_text(510, 315, text="1")
qq6_qq7_label = dfa_container2.create_text(500, 360, text="0")
qq7_qq9_label = dfa_container2.create_text(590, 370, text="0, 1")
qq8_qq7_label = dfa_container2.create_text(550, 365, text="0")
qq8_qq9_label = dfa_container2.create_text(585, 315, text="1")
qq9_qq9_label = dfa_container2.create_text(700, 330, text="0, 1")


# Create widgets
dfatext2 = Label(frame3, text="DFA SIMULATOR", font=("Helvetica", 30), fg="#2d3748")
top_container2 = Frame(frame3)
left_container2 = Frame(top_container2)
right_container2 = Frame(top_container2)
prompt_text2 = Label(left_container2, text="Enter String:", font=("Helvetica", 16))
input2_storage2 = StringVar()
input2 = Entry(left_container2, textvariable=input2_storage2, font=("Helvetica", 12))
button_frame2 = Frame(left_container2)
run_button2 = Button(button_frame2, text="Validate", command=run2, width=10, font=("Helvetica", 12), bg='SkyBlue3', relief='flat')
regEx_label2 = Label(right_container2, text="Regular Expression:", font=("Helvetica", 16))
regEx_text2 = Label(right_container2, text="(1+0)*1*0*(101+01+000)(1+0)*(101+00)*(111+00+101)(1+0)*", font=("Helvetica", 9))
regEx_sample2 = Label(left_container2, text="Sample String: 10100", font=("Helvetica", 9), fg="grey")
show_pda_button2 = Button(right_container2, text="Show PDA", command=show_pda_image2, width=12, font=("Helvetica", 12), bg='SkyBlue3', relief='flat')
show_cfg_button2 = Button(right_container2, text="Show CFG", command=show_cfg_image2, width=12, font=("Helvetica", 12), bg='SkyBlue3', relief='flat')

out2_text2 = Label(frame3, text="", font=("Helvetica", 12), fg="red")

# Configure the input field to make it bigger
input2.configure(width=30)

# Place widgets using pack layout manager
dfatext2.pack(anchor='nw', padx=20, pady=(25, 0))
top_container2.pack(side="top", padx=20, pady=0)
left_container2.pack(side="left", padx=20, pady=10)
right_container2.pack(side="left", padx=20, pady=10)
prompt_text2.pack(side='top', anchor='w', padx=20, pady=(10, 10))
input2.pack(side='top', anchor='w', padx=25)
button_frame2.pack(side='bottom', anchor='w', padx=25, pady=(0, 20))
run_button2.pack(side='left')
regEx_label2.pack(anchor='nw', padx=20)
regEx_text2.pack(anchor='e', padx=22, pady=10)
regEx_sample2.pack(anchor='w', padx=20, pady=(0,10))
show_pda_button2.pack(side="right", padx=10, pady=(0, 10))
show_cfg_button2.pack(side="right", padx=10, pady=(0, 10))

input2.bind("<KeyRelease>", handle_input2_change)
out2_text2.pack()
dfa_container2.pack()

def proceed_to_frame1():
    notebook.select(frame1)

def proceed_to_frame2():
    notebook.select(frame2)

def proceed_to_frame3():
    notebook.select(frame3)

button_container1 = Frame(frame1)
button_container1.pack(side="bottom", padx=5, pady=5)
# button_container1.configure(bg="white")


# Button in frame 1
button_frame1To2 = Button(button_container1, text="Switch to RegEx1", command=proceed_to_frame2, bg='SkyBlue3', relief='flat', fg='white')
button_frame1To2.pack(side="left", padx = 5, pady = 5)
button_frame1To3 = Button(button_container1, text="Switch to RegEx2", command=proceed_to_frame3, bg='SkyBlue3', relief='flat', fg='white')
button_frame1To3.pack(side="right", padx = 5, pady = 5)

# Button in frame 2
button_frame2To3 = Button(frame2, text="Switch to RegEx2", command=proceed_to_frame3, bg='SkyBlue3', relief='flat', fg='white')
button_frame2To3.pack(side="right", padx=(0, 25), pady=5)
button_frame2To1 = Button(frame2, text="Go to Starting Page", command=proceed_to_frame1, bg='SkyBlue3', relief='flat', fg='white')
button_frame2To1.pack(side="right", padx=5, pady=5)

# Button in frame 3
button_frame3To2 = Button(frame3, text="Switch to RegEx1", command=proceed_to_frame2, bg='SkyBlue3', relief='flat', fg='white')
button_frame3To2.pack(side="right", padx=(0, 25), pady=5)
button_frame3To1 = Button(frame3, text="Go to Starting Page", command=proceed_to_frame1, bg='SkyBlue3', relief='flat', fg='white')
button_frame3To1.pack(side="right", padx=5, pady=5)


  
screen.mainloop()
