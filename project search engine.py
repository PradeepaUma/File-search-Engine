import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox

def browse_directory():
    # Allow user to select a directory
    directory = filedialog.askdirectory()
    entry_dir.delete(0, tk.END)
    entry_dir.insert(0, directory)

def search_files():
    # Clear previous results
    listbox_results.delete(0, tk.END)

    # Get the directory path and search term from input fields
    directory = entry_dir.get()
    search_term = entry_search.get()

    if not directory or not search_term:
        messagebox.showwarning("Input Error", "Please specify both directory and search term.")
        return

    # Traverse the directory and search for files matching the term
    for root, _, files in os.walk(directory):
        for file in files:
            if search_term.lower() in file.lower():
                # Display the matching file path in the listbox
                listbox_results.insert(tk.END, os.path.join(root, file))

# Initialize the main window
root = tk.Tk()
root.title("File Search Engine")
root.geometry("600x400")

# Directory label and input field
tk.Label(root, text="Directory:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_dir = tk.Entry(root, width=50)
entry_dir.grid(row=0, column=1, padx=10, pady=5)

# Browse button
btn_browse = tk.Button(root, text="Browse", command=browse_directory)
btn_browse.grid(row=0, column=2, padx=10, pady=5)

# Search term label and input field
tk.Label(root, text="Search Term:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_search = tk.Entry(root, width=50)
entry_search.grid(row=1, column=1, padx=10, pady=5)

# Search button
btn_search = tk.Button(root, text="Search", command=search_files)
btn_search.grid(row=1, column=2, padx=10, pady=5)

# Listbox for displaying results
listbox_results = Listbox(root, width=80, height=15)
listbox_results.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()
