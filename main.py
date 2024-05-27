#This code is a short typing test to determine typing speed.
#This code uses Wonderwords to create a random sentence.

import tkinter
import customtkinter
import time
from wonderwords import RandomSentence

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=app,
                               width=400,
                               height=500,
                               corner_radius=10)
frame.pack(padx=10, pady=10)

# Give random sentences for testing the speed of user
s = RandomSentence()
# Get a random sentence with a subject, predicate, direct object, and adjective
sentence = s.sentence()
#print(sentence) #Test to see if a sentence appears in the command line

# Defining the values for the test
text_var_s = tkinter.StringVar(value=sentence)
text_var_e = tkinter.StringVar(value="")
text_var_wpm = tkinter.StringVar(value="0")
text_var_acc = tkinter.StringVar(value="0")
start_time = tkinter.IntVar(value=0)
end_time = tkinter.IntVar(value=0)
elapsed_time = tkinter.IntVar(value=0)

def start_timer():
    global start_time
    start_time = int(time.time()) #Start the timer
    #print(f"Start time: {start_time}") #Test the start time
  
def stop_button_event():
    
    #Check WPM
    wpm = 0  
    global sentence
    global start_time
    global end_time
    global elapsed_time
# #Start time is when the person starts typing and 
# the end time is when the person hits the stop button

    end_time = int(time.time())
    #print(f"End time: {end_time}") #Test the end time
    elapsed_time = int(end_time - start_time)
    #print(f"Elapsed time = {elapsed_time}") #Test the elapsed time
    #wpm(word per minute); elapses time is in seconds
    wpm = (int(len(sentence) / elapsed_time)) * 60
    print(wpm)
    wpm_textbox.insert("0.0", text=wpm)
    wpm_textbox.configure(state="normal")
        
    # Check accuracy
    global text_var_acc
    text_var_e = tkinter.StringVar(value=entry.get())
    acc = 0
    correct_answer = 0
    if entry.get() == sentence:
        for word in sentence:
            if word in sentence:
                correct_answer +=1
                acc = ((correct_answer / len(sentence)) * 100)
        #print(f"Accuracy: {acc}%") Test the accuracy
        accuracy_textbox.insert("0.0", text=f"{acc}%")
        accuracy_textbox.configure(state="normal")
    
                               
label_random_sentence = customtkinter.CTkLabel(master=frame,
                                 textvariable=text_var_s,
                                 width=200,
                                 height=50,
                                 text_color="white",
                                 font=("Arial", 16),
                                 fg_color=("red", "black"),
                                 corner_radius=8)
label_random_sentence.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

start_button = customtkinter.CTkButton(master=frame,
                                 text="START TIMER",
                                 command=start_timer)
start_button.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

#This is the entry box for the typing test
entry = customtkinter.CTkEntry(master=frame,
                               #text="Please type in a sentence.",
                               textvariable=text_var_e,
                               width=320,
                               height=75,
                               text_color="white",
                               font=("Arial", 16),
                               fg_color=("black", "black"),
                               corner_radius=8
                              )
entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

#Button that stops test and gives results
stop_button = customtkinter.CTkButton(master=frame,
                                 text="STOP",
                                 command=stop_button_event)
stop_button.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

wpm_textbox = customtkinter.CTkTextbox(master=frame,
                                 width=70,
                                 height=50,
                                 text_color="white",
                                 font=("Arial", 16),
                                 fg_color=("black", "black"),
                                 corner_radius=8)
wpm_textbox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

accuracy_textbox = customtkinter.CTkTextbox(master=frame,
                                 width=100,
                                 height=50,
                                 text_color="white",
                                 font=("Arial", 16),
                                 fg_color=("black", "black"),
                                 corner_radius=8)
accuracy_textbox.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

app.mainloop()