import tkinter as tkinter
from tkinter import ttk
import datetime
import requests
from PIL import Image, ImageTk

class MessageWindow(tk.Canvas):
    def __init__(self, container,*args, **kwargs):
        super.__init__(container,*args,**kwargs, highlighttickness = 0)

        self.message_frame =ttk.Frame(self)
        self.message_frame.columnconfigure(0,weight=1)

        self.scrollable_window = self.create_window((0,0),window = self.message_frame, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))
        
        def configure_window_size(event):
            self.itemconfig(self.scrollable_window,width=self.winfo_width())

        self.bind("<Configure>",configure_window_size)
        self.messages_frame.bind("<Configure>",configure_scroll_region)

        scrollbar =ttk.Scrollbar(container,orient="vertical",command=self.yview)
        scrollbar.grid(row=0 ,column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def get_messages(self):
        global messages
        messages = requests.get("http://167.99.63.70/messages").json()
        self.messages_window.update_message_widgets()
    

    def update_message_widgets(self):
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels
        ]

        for message in messages:
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)
    
    def _create_message_container(self, message_content, message_time, message_labels):
        container = ttk.Frame(self.messages_window)
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        self._create_message_bubble(container, message_content, message_time, message_labels)
    
    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        avatar_image = Image.open("./assets/fox.jpg")
        avatar_photo = ImageTk.PhotoImage(avatar_image)

        avatar_label = tk.Label(
            container,
            image=avatar_photo
        )
        avatar_label.image = avatar_photo
        avatar_label.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="NEW",
            padx=(0, 10),
            pady=(5, 0)
        )

        time_label = ttk.Label(
            container,
            text=message_time,
        )
        time_label.grid(row=0, column=1, sticky="NEW")

        message_label = ttk.Label(
            container,
            text=message_content,
            anchor="w",
            justify="left"
        )
        message_label.grid(row=1, column=1, sticky="NSEW")

        message_labels.append((message_label, time_label))