import tkinter as tk
from tkinter import ttk
from datetime import date
import requests
from frames.message_window import MessageWindow
from PIL import Image, ImageTk

messages = [{
    "message": "Welcome to http://httpbin.org/get \n Please give what you would like to know:\n url ,text or status_code? \n for sending information press SEND Button \n for Recieving the information press RECIEVE Button" , 
    }]
message_labels = []


class Chat(ttk.Frame):

    '''
    Handels all the related functions for sending/recieving the messages.

    Functions:
    - change avatar
    - send messages
    - get messages
    
    '''
    def __init__(self, container,background, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.message_window = MessageWindow(self,background=background)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        input_frame = ttk.Frame(self,style="Controls.TFrame",padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        self.message_input = tk.Text(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))


        self.message_submit = ttk.Button(
            input_frame,
            text="Send",
            style="SendButton.TButton",
            width= 15,
            command=lambda: [self.post_message(), self.change_avatar()]
            )
        
        self.message_submit.pack()

        message_recieve = ttk.Button(
            input_frame,
            text="Recieve",
            style="RecieveButton.TButton",
            width= 15,
            command=self.get_messages,
        )
        
        message_recieve.pack()

        message_Quit = ttk.Button(
            input_frame,
            text="Quit",
            style="QuitButton.TButton",
            width= 15,
            command=quit,
        )
        message_Quit.pack()
        self.message_window.update_message_widgets(messages, message_labels)


    def change_avatar(self):
        '''
        Change the avatar for different Buttons.
        '''
        if self.message_submit["text"]=="Send":
            self.new_img = ImageTk.PhotoImage(Image.open('./assets/rat.jpg'))           
        else:
            self.new_img = ImageTk.PhotoImage(Image.open('./assets/fox.jpg'))
         
        self.message_window.avatar_label.configure(image=self.new_img)
        self.message_window.avatar_label.image = self.new_img
            
    
    def post_message(self):
        '''
        Return the messages from user.
        '''
        self.body = self.message_input.get("1.0", "end").strip()
        messages[0]["message"] = str(self.body)
        self.message_window.update_message_widgets(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0))
        self.message_input.delete('1.0', "end")
        

    def get_messages(self):
        '''
        Get the messages from server.
        '''
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