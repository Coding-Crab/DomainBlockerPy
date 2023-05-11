import tkinter as tk
import subprocess
import json
from tkinter import filedialog

def block_domain():
    domain = domain_input.get()
    if domain in history_list.get(0, tk.END):
        status_label.config(text=f"{domain} is already blocked")
    else:
        command = f"sudo sh -c \"echo '0.0.0.0   {domain}' >> /etc/hosts\""
        subprocess.call(command, shell=True)
        status_label.config(text=f"{domain} has been blocked")
        history_list.insert(tk.END, domain)
        save_history()

def delete_domain():
    selected = history_list.curselection()
    if selected:
        domain = history_list.get(selected)
        history_list.delete(selected)
        command = f"sudo sed -i '/0\.0\.0\.0.*{domain}/d' /etc/hosts"
        subprocess.call(command, shell=True)
        status_label.config(text=f"{domain} has been unblocked")
        save_history()
    else:
        status_label.config(text="Please select a domain to delete")

def reset_domains():
    command = "sudo sed -i '/0\.0\.0\.0/d' /etc/hosts"
    subprocess.call(command, shell=True)
    status_label.config(text="All domains have been unblocked")
    history_list.delete(0, tk.END)
    save_history()

def export_domains():
    domains = history_list.get(0, tk.END)
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, "w") as f:
            f.write("\n".join(domains))

def save_history():
    history = history_list.get(0, tk.END)
    with open("history.json", "w") as f:
        json.dump(history, f)

def load_history():
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        history = []
    for domain in history:
        history_list.insert(tk.END, domain)

root = tk.Tk()
root.title("Domain Blocker")

domain_label = tk.Label(root, text="Enter domain to block:")
domain_label.pack()

domain_input = tk.Entry(root)
domain_input.pack()

block_button = tk.Button(root, text="Block Domain", command=block_domain)
block_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_domains)
reset_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_domain)
delete_button.pack()

export_button = tk.Button(root, text="Export", command=export_domains)
export_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

history_label = tk.Label(root, text="Blocked domains:")
history_label.pack()

history_list = tk.Listbox(root)
history_list.pack()

load_history()

root.mainloop()
