# Custom Message Box library

![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/Status-Beta-orange)
![PyPI version](https://img.shields.io/pypi/v/custom_message_box.svg)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-blueviolet)



## 📝 Description

Custom Message Boxis simple and modern library to create custom dialog boxes with **CustomTkinter**. It allows you to easily retrieve user responses (inputs, confirmations, multiple choices) without having to deal with complex classes.

## 🖼️ Screenshoots

![Screenshoot](https://raw.githubusercontent.com/xibuoya/Custom-Message-Box-python-library/refs/heads/main/Custom_Message_Box.png).

## 📦 Features

- **Information & Error**: Simple notification boxes.
- **Yes/No**: Confirmation dialog boxes.
- **Entry**: Dialog boxes with text input.
- **Custom**: Dialog boxes with 2 customized buttons.

## 🛠️ Installation

Make sure you have CustomTkinter installed:

```bash
pip install customtkinter
```
Install the library:

```Bash
pip install custom_message_box
```
(Not available at the moment)

Or download the script.

## 🚀 Usage

Quick start guide:

- Information Message
```Python
custom_message_box.ctkinfo("Title", "Operation successful!")
```

- Error Message
```Python
custom_message_box.ctkerror("Warning", "Connection lost.")
```

- Confirmation Window
Returns 1 for Yes and 0 for No.
```Python
response = custom_message_box.ctk_msg_yesno("Exit", "Do you really want to leave?")
```

- Text Input
Returns the entered string.
```Python
username = custom_message_box.ctk_msg_entry("Username", "Enter your name:", "e.g., John")
```

- Custom Buttons
Returns the text of the clicked button.
```Python
choice = custom_message_box.ctk_msg_custom("Menu", "Choose an option:","Play", "Options", "Exit")
```

##  💻 Full Integration Example
```Python
from custom_message_box import * as cmb

# 1. Test Entry
entry_response = cmb.ctk_msg_entry("Title", "Enter something:", "Placeholder")
print(entry_response)

# 2. Test YesNo
yesno_response = cmb.ctk_msg_yesno("Confirm", "Are you sure?")
print(yesno_response)

# 3. Test Custom (Title, Message, Text1, Text2)
custom_response = cmb.ctk_msg_custom("Choice", "Select one:", "Option 1", "Option 2")
print(custom_response)

# 4. Test Info
cmb.ctkinfo("Info", "Everything is OK!")

# 5. Test Error
cmb.ctkerror("Danger", "Something went wrong!")
```

##
Good programing !
