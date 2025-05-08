import tkinter as tk
from tkinter import messagebox
import re

error_log = []  # List to store error messages

def log_error(message):
    error_log.append(message)

def convert_measurement(event=None):
    input_value = entry.get().strip()
    # Pattern: feet (with ' or f), or just inches (with optional mixed fraction using - or space)
    pattern = r"""^\s*
        (?:(?P<feet>\d+)\s*['f]\s*)?      # Optional feet, must have ' or f
        (?:
            (?P<mixed>\d+[-\s]\d+/\d+)    # Mixed inches, e.g. 6-1/2 or 6 1/2
            |(?P<frac>\d+/\d+)            # Fractional inches, e.g. 1/2
            |(?P<inch>\d+)                # Whole inches, e.g. 6
        )?
        \s*(?:["i]|in)?\s*$
    """
    match = re.match(pattern, input_value, re.IGNORECASE | re.VERBOSE)
    if not match:
        output_var.set("")
        log_error(f"Invalid input: {input_value}")
        messagebox.showerror(
            "Input Error",
            "Invalid input. Examples:\n1' 6, 1' 6-1/2, 6-1/2\", 1', 6\", 1/2\", 6in"
        )
        return
    try:
        feet = int(match.group("feet")) if match.group("feet") else 0
        inches = 0.0
        if match.group("mixed"):
            whole, frac = re.split(r"[-\s]", match.group("mixed"))
            num, den = frac.split('/')
            inches = float(whole) + float(num) / float(den)
        elif match.group("frac"):
            num, den = match.group("frac").split('/')
            inches = float(num) / float(den)
        elif match.group("inch"):
            inches = float(match.group("inch"))
        decimal_value = feet + inches / 12.0
        output_var.set(str(round(decimal_value, 3)))
    except Exception as e:
        output_var.set("")
        log_error(f"Error during conversion: {e}")
        messagebox.showerror("Conversion Error", f"An error occurred while processing the input:\n{e}")

def copy_output():
    output = output_var.get()
    if output:
        root.clipboard_clear()
        root.clipboard_append(output)
    else:
        messagebox.showinfo("Copy Output", "There is no output to copy.")

def view_error_log():
    log_window = tk.Toplevel(root)
    log_window.title("Error Log")
    text_frame = tk.Frame(log_window)
    text_frame.pack(fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget = tk.Text(text_frame, height=10, width=50, yscrollcommand=scrollbar.set)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)
    if not error_log:
        text_widget.insert(tk.END, "No errors logged.")
    else:
        for err in error_log:
            text_widget.insert(tk.END, err + "\n")
    text_widget.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Imperial to Decimal Converter")

# Input field with label
input_label = tk.Label(
    root,
    text="Enter a measurement (e.g. 1' 6, 1' 6 1/2, 6 1/2, 1', 6, 1/2, 6 1/2\", 6in):"
)
input_label.pack(pady=(10, 0))
entry = tk.Entry(root, width=40)
entry.pack(pady=(0, 10))
entry.focus_set()
entry.bind('<Return>', convert_measurement)  # Allow Enter key to trigger conversion

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_measurement)
convert_button.pack(pady=(0, 10))

# Output field with label
output_label = tk.Label(root, text="Decimal Value:")
output_label.pack()
output_var = tk.StringVar()
output_display = tk.Label(root, textvariable=output_var, width=20, relief="sunken", bg="#f0f0f0")
output_display.pack(pady=(0, 10))

# Copy button
copy_button = tk.Button(root, text="Copy", command=copy_output)
copy_button.pack(pady=(0, 10))

# Error log viewer button
error_button = tk.Button(root, text="View Error Log", command=view_error_log)
error_button.pack(pady=(0, 10))

root.mainloop()