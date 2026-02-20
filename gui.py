import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time

# Your encryption dictionaries
secr = {'a': "30", 'b': "87", 'c': "67", 'd': "65", 'e': "63", 'f': "58", 'g': "56", 'h': "54", 'i': "52", 
        'j': "50", 'k': "49", 'l': "47", 'm': "45", 'n': "43", 'o': "41", 'p': "38", 'q': "36", 'r': "34", 
        's': "32", 't': "31", 'u': "29", 'v': "27", 'w': "25", 'x': "23", 'y': "21", 'z': "18", ' ': "16", 
        '?': "14", '.': "12", '!': "10", '0': "09", '1': "07", '2': "05", '3': "03", '4': "01", '5': "02", 
        '6': "04", '7': "06", '8': "08", '9': "11"}

decr = {"30": 'a', "87": 'b', "67": 'c', "65": 'd', "63": 'e', "58": 'f', "56": 'g', "54": 'h', "52": 'i', 
        "50": 'j', "49": 'k', "47": 'l', "45": 'm', "43": 'n', "41": 'o', "38": 'p', "36": 'q', "34": 'r', 
        "32": 's', "31": 't', "29": 'u', "27": 'v', "25": 'w', "23": 'x', "21": 'y', "18": 'z', "16": ' ', 
        "14": '?', "12": '.', "10": '!', "09": '0', "07": '1', "05": '2', "03": '3', "01": '4', "02": '5', 
        "04": '6', "06": '7', "08": '8', "11": '9'}

# Your encryption function
def secros(secr, textt):
    text = textt.lower()
    ule = ""
    for i in text:
        if i in secr:
            ule = ule + secr[i]
        elif i not in secr:
            ule = ule + i
    return ule

# Your decryption function
def decros(decr, text):
    ll = 0
    mm = ""
    nn = ""
    
    for i in text:
        ll = ll + 1
        l = ll % 2
        if l == 0:
            nn = nn + i
            try:
                xx = decr[nn]
                mm = mm + xx
                nn = ""  # Reset nn after successful decoding
            except KeyError:
                # If not a valid code, keep the original characters
                mm = mm + nn
                nn = i
        elif l != 0:
            nn = i
    
    # Handle any remaining characters
    if nn and nn in decr:
        mm = mm + decr[nn]
    elif nn:
        mm = mm + nn
        
    return mm

class CodeCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Cipher - Encoder/Decoder")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Set style
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Code Cipher Tool", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Mode selection
        ttk.Label(main_frame, text="Select Mode:", font=('Arial', 11)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.mode_var = tk.StringVar(value="encode")
        mode_frame = ttk.Frame(main_frame)
        mode_frame.grid(row=1, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(mode_frame, text="Encode (Text to Code)", variable=self.mode_var, 
                       value="encode", command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(mode_frame, text="Decode (Code to Text)", variable=self.mode_var, 
                       value="decode", command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Input section
        ttk.Label(main_frame, text="Input:", font=('Arial', 11)).grid(row=2, column=0, sticky=tk.NW, pady=5)
        
        # Input text area with scrollbar
        self.input_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=50, height=8, 
                                                    font=('Courier', 10))
        self.input_text.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Process", command=self.process_text, 
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all, 
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Copy Output", command=self.copy_output, 
                  width=15).pack(side=tk.LEFT, padx=5)
        
        # Output section
        ttk.Label(main_frame, text="Output:", font=('Arial', 11)).grid(row=4, column=0, sticky=tk.NW, pady=5)
        
        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=50, height=8, 
                                                     font=('Courier', 10))
        self.output_text.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, 
                               anchor=tk.W, font=('Arial', 9))
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Character mapping display (optional)
        self.show_mapping = tk.BooleanVar(value=False)
        ttk.Checkbutton(main_frame, text="Show Character Mapping", 
                       variable=self.show_mapping, command=self.toggle_mapping).grid(row=6, column=0, columnspan=3, pady=5)
        
        # Mapping display frame (initially hidden)
        self.mapping_frame = ttk.Frame(main_frame)
        self.mapping_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        self.mapping_frame.grid_remove()
        
        # Create mapping display
        self.create_mapping_display()
        
        # Instructions
        instructions = "Instructions:\n- For encoding: Enter text to convert to code\n- For decoding: Enter code numbers (2 digits each) to convert back to text"
        instr_label = ttk.Label(main_frame, text=instructions, font=('Arial', 9), foreground='gray')
        instr_label.grid(row=8, column=0, columnspan=3, pady=10)
    
    def create_mapping_display(self):
        """Create a frame showing character mappings"""
        # Create notebook for tabs
        notebook = ttk.Notebook(self.mapping_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Letters
        letters_frame = ttk.Frame(notebook)
        notebook.add(letters_frame, text="Letters")
        
        # Create grid of letter mappings
        letters = 'abcdefghijklmnopqrstuvwxyz'
        row, col = 0, 0
        for i, letter in enumerate(letters):
            if letter in secr:
                label = ttk.Label(letters_frame, text=f"{letter} → {secr[letter]}", 
                                 font=('Courier', 9), relief=tk.RIDGE, padding=5)
                label.grid(row=row, column=col, padx=2, pady=2, sticky=tk.W)
                col += 1
                if col > 5:
                    col = 0
                    row += 1
        
        # Tab 2: Numbers & Special
        special_frame = ttk.Frame(notebook)
        notebook.add(special_frame, text="Numbers & Special")
        
        # Numbers and special characters
        special_chars = {'0': '09', '1': '07', '2': '05', '3': '03', '4': '01', 
                        '5': '02', '6': '04', '7': '06', '8': '08', '9': '11',
                        ' ': '16', '?': '14', '.': '12', '!': '10'}
        
        row, col = 0, 0
        for char, code in special_chars.items():
            display_char = 'Space' if char == ' ' else char
            label = ttk.Label(special_frame, text=f"{display_char} → {code}", 
                             font=('Courier', 9), relief=tk.RIDGE, padding=5)
            label.grid(row=row, column=col, padx=2, pady=2, sticky=tk.W)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def toggle_mapping(self):
        """Show or hide the mapping display"""
        if self.show_mapping.get():
            self.mapping_frame.grid()
        else:
            self.mapping_frame.grid_remove()
    
    def clear_fields(self):
        """Clear input and output fields when mode changes"""
        self.input_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Ready")
    
    def clear_all(self):
        """Clear all fields"""
        self.input_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("All fields cleared")
    
    def copy_output(self):
        """Copy output text to clipboard"""
        output = self.output_text.get(1.0, tk.END).strip()
        if output:
            self.root.clipboard_clear()
            self.root.clipboard_append(output)
            self.status_var.set("Output copied to clipboard")
            messagebox.showinfo("Success", "Output copied to clipboard!")
        else:
            self.status_var.set("No output to copy")
            messagebox.showwarning("Warning", "No output to copy!")
    
    def process_text(self):
        """Process the input text based on selected mode"""
        input_data = self.input_text.get(1.0, tk.END).strip()
        
        if not input_data:
            messagebox.showwarning("Warning", "Please enter some text to process!")
            return
        
        try:
            if self.mode_var.get() == "encode":
                # Encode the text
                result = secros(secr, input_data)
                self.status_var.set(f"Encoded successfully! ({len(input_data)} characters → {len(result)} digits)")
            else:
                # Decode the code
                # Remove any spaces or special characters for decoding
                clean_input = ''.join(c for c in input_data if c.isdigit())
                result = decros(decr, clean_input)
                self.status_var.set(f"Decoded successfully! ({len(clean_input)//2} codes → {len(result)} characters)")
            
            # Clear output and insert result
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            
        except KeyError as e:
            self.status_var.set("Error: Invalid code sequence")
            messagebox.showerror("Error", f"Invalid code sequence found!\nMake sure you're using valid codes.\nError: {e}")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def main():
    root = tk.Tk()
    app = CodeCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
