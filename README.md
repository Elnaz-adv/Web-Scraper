# Project Name
> Web Scraper: you can use it to get different information from websites.
> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Libraries Used](#libraries-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)

<!-- * [License](#license) -->


## General Information
- requests get() and post() are used for the communication with the website.
- Which problem is solved? Through a tkinter GUI interface you can make a communication for the user easier


## Libraries Used
- Lib 1 - tkinter 
- Lib 2 - requests



## Features

- message label with time stempel
- avatar for users
- scrollable message field
- send ,recieve and quit buttons for communication
- screen is adjusted to the message length

#### How is the scrollable container made?

 scrollable container is done with tk.Canvas.

 steps to do the Frame:
 1. make a container(our window) 
 2.  make a Canvas and put it on the container
 3.  put a frame inside it.
 4. tell the Canvas ,what size the frame is, so it know how much it can scroll.
 5. put your elements inside the inner frame
 6. use Canvas scrolling to move about the inner frame



## Screenshots
![Example screenshot](/assets/screenshot1.png)
![Example screenshot](/assets/rat.jpg)
![Example screenshot](./assets/rat.jpg)


## Setup
You can find the setting by Pipfile.lock 


## Usage
Here how you can start the program in main file:

```
from Messanger import Messenger


if __name__ == "__main__":
    root = Messenger()
    styler = root.style_container()
    root.mainloop()  
```


## Project Status
Project is:  / _complete_ / 


## Room for Improvement
Room for improvement:
- The website could be given by user
- The website information could be expended
- error handling should be added.


## Acknowledgements




<!-- Optional -->
<!-- ## License -->

