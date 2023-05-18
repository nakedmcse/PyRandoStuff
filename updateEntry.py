import tkinter as tk

def update_entry_text():
    entry.delete(0, tk.END)  # Clear the current text
    entry.insert(0, "New Text")  # Insert new text
    #window.update()  # Update the window to redraw the entry widget

# Create a Tkinter window
window = tk.Tk()

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger the update
button = tk.Button(window, text="Update", command=update_entry_text)
button.pack()

# Start the Tkinter event loop
window.mainloop()
