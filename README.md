# Notetaker
<h1> This is a custom note taking app aimed at call center techs </h1>

1. [Current testing and issues](#Issues)
2. [Personal wishlist](#Wishlist)
3. [Installation](#Installation)
4. [App in action](#Action)

I wrote this code after observing several different people's methods while training. I realized I could combine and simplify some of their designs into a singular app that could save notes to a unique file name and allow for previewing any notes taken for easy copy/paste into another case management system.

<a name="Issues"> </a>

<h2> Current testing and issues </h2>

__Currently this has only been tested for Windows 10 devices!__

<li> When clear fields is selected before a file has been saved for the day, the app will crash. Need to setup a safeguard for this. </li>
<li> Case name error has popped up incorrectly under certain circumstances; need to reproduce. </li>
<li> Closing the program does not warn the user if the file has not been saved yet. </li>
<li> When preview window is in focus, it blocks any additional popups from happening from clearing fields or saving the file. </li>

<a name="Wishlist"> </a>

<h2> Personal wishlist </h2>

<li> Add ability to theme change the windows/text; this requires importing code from a separate project and testing </li>
<li> Add ability to include custom fields, if and where desired </li>
<li> Test for different OS deployments </li>

<a name="Installation"> </a>

<h2> Installation </h2>

Either download the code and execute using Python, ensuring to download dependent library (PySimpleGUI) first or download .zip that contains all of the necessary libraries. .zip also contains a shortcut that can be moved to desktop for quick launch.

<a name="Action"> </a>

<h2> App in action </h2>

The window serves as the starting point for taking notes during a call. It has sections for customer name, phone, email, and a case number:

![Notetaker on launch](https://user-images.githubusercontent.com/81875107/172763672-46adb693-d539-4cc1-a1d7-105085e5e533.png)

Clicking the preview button opens a separate window where the text can be copied. __IF ANY EDITS ARE MADE HERE, THE EDITS WILL NOT APPEAR IN THE MAIN WINDOW!__

![Preview window](https://user-images.githubusercontent.com/81875107/172763827-a76b05b4-1a02-4d6e-b087-41e74e7017e1.png)

The save button does what it says. It saves the file. The way it does so is to create a new directory with the year as the top level, the month as the next level, and then the year/month/day as the final level. The file is saved as the case number. If the case number is not exactly 8 digits, the save will fail and the program will display a reason why it failed. A separate warning will pop up if the case number has already been used for that day.

![What the save button creates](https://user-images.githubusercontent.com/81875107/172764061-8cc34b97-03c4-4841-8d31-921b724320ea.png)

After saving, the text file will look like this:

![Text file saved](https://user-images.githubusercontent.com/81875107/172764518-b3f4599d-a02b-4deb-9884-ec9f994298dc.png)

If clear fields is selected before saving, the app will throw a warning. This is to prevent accidental deletion of notes.

![Clear fields warning before saving](https://user-images.githubusercontent.com/81875107/172764587-7c18959b-fb94-4241-9e7a-82acc6eca93b.png)
