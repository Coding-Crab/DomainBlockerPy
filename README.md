# DomainBlockerPy
A simple domain blocker application using Tkinter - Unix-based systems

# The concept of the domain blocker app:

The concept of the domain blocker app is to provide a simple graphical user interface (GUI) for blocking and unblocking domains on a Unix-based system (e.g., Linux, macOS).

The app allows the user to:

Block a domain: By entering a domain in the input field and clicking the "Block Domain" button, the app adds an entry to the system's hosts file, redirecting the domain to the IP address 0.0.0.0. This effectively prevents the system from accessing that domain.

Unblock a domain: The app maintains a history of blocked domains in a list. To unblock a domain, the user can select it from the history list and click the "Delete" button. The app removes the corresponding entry from the hosts file, allowing access to the domain again.

Reset all blocked domains: The app provides a "Reset" button that removes all blocked domains from the hosts file and clears the history list. This action effectively unblocks all previously blocked domains.

Export blocked domains: The app allows the user to export the list of blocked domains to a text file. By clicking the "Export" button, a file dialog opens, enabling the user to choose the location and name of the file. The exported file contains a newline-separated list of blocked domains.

The app also includes a status label to provide feedback on the success or failure of blocking/unblocking operations.

The purpose of the app is to provide a user-friendly way to manage blocked domains, allowing users to control their access to specific websites or online resources.


# Here's an overview of how the code works:

Import the necessary modules: tkinter for creating the GUI, subprocess for executing shell commands, json for handling the history data, and filedialog for saving the blocked domains to a file.

Define the functions for various actions:

block_domain(): This function retrieves the domain entered in the input field, checks if it's already blocked, and if not, adds it to the hosts file. It updates the status label and saves the domain to the history.
delete_domain(): This function deletes the selected domain from the history list and removes its entry from the hosts file. It updates the status label and saves the updated history.
reset_domains(): This function removes all blocked domains from the hosts file, clears the history list, updates the status label, and saves the updated history.
export_domains(): This function retrieves all blocked domains from the history list and allows the user to choose a file to save them in a newline-separated format.
save_history(): This function saves the current list of blocked domains to a JSON file.
load_history(): This function loads the previously saved list of blocked domains from the JSON file and populates the history list.
Create the main window and set its title.

Create the GUI elements:

domain_label: A label for the domain input field.
domain_input: An entry field for entering the domain to block.
block_button: A button to initiate blocking the domain.
reset_button: A button to reset all blocked domains.
delete_button: A button to delete a selected domain from the history list.
export_button: A button to export the list of blocked domains to a file.
status_label: A label to display the status of domain blocking operations.
history_label: A label for the history list.
history_list: A listbox to display the blocked domains.
Load the history of blocked domains.

Start the main event loop using root.mainloop() to display the GUI and handle user interactions.

Overall, the code provides a basic interface for blocking and unblocking domains using the hosts file. However, it's worth noting that the code assumes the user has administrative privileges (sudo access) to modify the hosts file, and it works on Unix-based systems (Linux, macOS) where the hosts file is located at /etc/hosts.

# How to run this app ?

To run the domain blocker app, you need a Unix-based system (such as Linux or macOS) that supports the execution of Python scripts and has the necessary dependencies installed. Here are the system requirements:

Unix-based operating system: The app is designed to work on Unix-based systems like Linux or macOS. It may not work on Windows without modifications, as the hosts file path and shell commands may differ.

Python: Make sure you have Python installed on your system. The code you provided is written in Python and requires Python to be available for execution.

Tkinter: Tkinter is the Python standard library for creating GUI applications. It is usually included with Python installations, but you might need to install it separately if it's not already available.

Administrative privileges: The app modifies the hosts file, which typically requires administrative (sudo) access. Make sure you have the necessary privileges to edit system files.

If you meet these requirements, you should be able to run the domain blocker app successfully on your Unix-based system.

![Untitled](https://github.com/Coding-Crab/DomainBlockerPy/assets/121975087/6350f1f9-9bb4-444f-9560-55f5d76e6ff5)
