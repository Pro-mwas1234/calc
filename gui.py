import tkinter as tk
from tkinter import font

def create_calculator():
    # Create main window
    root = tk.Tk()
    root.title("Graphical Calculator")
    root.resizable(False, False)
    
    # Custom font
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=12)
    
    # Entry field for display
    display_var = tk.StringVar()
    display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), 
                      bd=10, insertwidth=2, width=14, borderwidth=4, 
                      justify='right')
    display.grid(row=0, column=0, columnspan=4)
    
    # Button layout
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]
    
    # Button click handler
    def on_button_click(char):
        if char == 'C':
            display_var.set('')
        elif char == '=':
            try:
                result = str(eval(display_var.get()))
                display_var.set(result)
            except:
                display_var.set("ERROR")
        else:
            display_var.set(display_var.get() + char)
    
    # Create and position buttons
    row = 1
    col = 0
    for button in buttons:
        if button == 'C':
            cmd = lambda x=button: on_button_click(x)
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
                     command=cmd, bg='orange').grid(row=row, column=col, columnspan=4, sticky="nsew")
        else:
            cmd = lambda x=button: on_button_click(x)
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
                     command=cmd).grid(row=row, column=col, sticky="nsew")
        
        col += 1
        if col > 3:
            col = 0
            row += 1
    
    # Configure row/column weights
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    
    root.mainloop()

# Run the calculator
create_calculator()
