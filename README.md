# Terminal Typing
___
A simple terminal-based typing practice.


### Table of Contents
+ [Introduction](#Introduction)
+ [Status Bar](#status-bar)
+ [Get Start](#get-start)
    - [requirement](#requirement)
    - [installation](#installation)
+ [Example-video](#example-video)
+ [Customization](#customization)
+ [.bashrc Alias](#bashrc-alias)
+ [Licence](#licence)

## Introduction
Terminal Typing is a simple Python-based application.

It features a minimalistic user interface and includes a status bar to track progress. Lightweight and resource-efficient. 

This application is designed to help you practice and improve your typing skills. 😊

## Status-bar
The status bar is created using the Tkinter module. It displays four status indicators:

**Correct** - The count of correctly typed paragraphs.

**Wrong** - The count of incorrectly typed paragraphs (this increases if typing is incomplete).

**Incomplete Type** - Displays incomplete paragraphs, missing lines, or extra words typed.

**Status** - Shows the status of the previously typed paragraph.

## Get-start
### Requirement
+ Python3
+ python3-tk

### Installation
**Debian based distro**

install python tkinter
```
sudo apt update
sudo apt install python3-tk
```
**Copy repository**
```
git clone https://github.com/github-CS-krishna/TerminalTyping
cd TerminalTyping
python3 terminalType.py
```
## Example-video
https://github.com/user-attachments/assets/26e79f05-a01c-418e-809a-d7af31707a0f



## Customization
To customize the paragraph selection, simply edit the `GetPara` variable.

__set paragraph__

Set `PrintPara` to a specific index.  
Example:
```
GetPara = 0
```
__set random paragaph__

Randomly select a paragraph.  
Example:
```
GetPara = random.randint(0,(len(PrintPara)-1))
```
## bashrc-alias

1. First, open the terminal.

2. Manually navigate to the cloned directory.
 
   Example:
   ```
   cd TerminalTyping
   ```

3. After that, run the following command.  
   ```
   echo -e "\n#set terminalTyping alias\nalias terminalType='python3 $(pwd)/terminalType.py'" | tee -a ~/.bashrc && bash
   ```
This command will add an alias to your `.bashrc` file

## Licence
this project is **open-source** and uses the GPL v3 license, supporting open-source development.
