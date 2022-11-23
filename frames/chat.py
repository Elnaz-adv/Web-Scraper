import tkinter as tk
from tkinter import ttk
import requests
from frames.message_window import MessageWindow
from PIL import Image, ImageTk

messages = [{
    "message": "Welcome to http://httpbin.org/get \n Please give what you would like to know : url,text or status_code? \n for sending information press SEND Button \n for Recieving the information press RECIEVE Button" , 
    "date": 15498487,
    "answer":"url"}]
message_labels = []


class Chat(ttk.Frame):

    '''
    This Class contains all the related functions related to sending/recieving the messages.
    '''
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.message_window = MessageWindow(self)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        input_frame = ttk.Frame(self, padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        self.message_input = tk.Text(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))


        self.message_submit = ttk.Button(
            input_frame,
            text="Send",
            width= 15,
            command=lambda: [self.post_message(), self.change_avatar()]
            )
        
        self.message_submit.pack()

        message_fetch = ttk.Button(
            input_frame,
            text="Recieve",
            width= 15,
            command=self.get_messages,
        )
        
        message_fetch.pack()

        message_Quit = ttk.Button(
            input_frame,
            text="Quit",
            width= 15,
            command=quit,
        )
        message_Quit.pack()
        self.message_window.update_message_widgets(messages, message_labels)


    def change_avatar(self):
        if self.message_submit["text"]=="Send":
            self.new_img = ImageTk.PhotoImage(Image.open('./assets/rat.jpg'))           
        else:
            self.new_img = ImageTk.PhotoImage(Image.open('./assets/fox.jpg'))
         
        self.message_window.avatar_label.configure(image=self.new_img)
        self.message_window.avatar_label.image = self.new_img
            
    
    def post_message(self):
        self.body = self.message_input.get("1.0", "end").strip()
        print(self.body)
        messages[0]["message"] = str(self.body)
        messages[0]["date"] = 23457687
        self.message_window.update_message_widgets(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0))
        self.message_input.delete('1.0', "end")
        

    def get_messages(self):
        global messages
        myurl= "http://httpbin.org/get"
        if self.body == "url":
            payload = {'message':'firstMessage','data':272675462}
            recieved_msg = requests.get(url=myurl, params=payload)
            messages[0]["message"] = str(recieved_msg.url)
            
        elif self.body == "text":
            payload = {'message':'firstMessage','data':272675462}
            recieved_msg = requests.get(url=myurl, params=payload)
            messages[0]["message"] = str(recieved_msg.text)
        else:
            payload = {'message':'firstMessage','data':272675462}
            recieved_msg = requests.get(url=myurl, params=payload)
            messages[0]["message"] = str(recieved_msg.status_code)

        self.message_window.update_message_widgets(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0))