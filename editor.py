import tkinter as tk
from tkinter import ttk, simpledialog

class AddressCommandEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Address and Command Editor")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create address tab
        self.address_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.address_tab, text='Addresses')

        # Address Listbox
        self.address_listbox = tk.Listbox(self.address_tab, selectmode=tk.SINGLE)
        self.address_listbox.pack(fill=tk.BOTH, expand=True)
        self.address_listbox.bind('<<ListboxSelect>>', self.on_address_select)

        # Add Address Button
        self.add_address_button = ttk.Button(self.address_tab, text="Add Address", command=self.add_address)
        self.add_address_button.pack(pady=5)

        # Delete Address Button
        self.delete_address_button = ttk.Button(self.address_tab, text="Delete Address", command=self.delete_address)
        self.delete_address_button.pack(pady=5)

        # Create command tab
        self.command_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.command_tab, text='Commands')

        # Command Listbox
        self.command_listbox = tk.Listbox(self.command_tab, selectmode=tk.SINGLE)
        self.command_listbox.pack(fill=tk.BOTH, expand=True)
        self.command_listbox.bind('<<ListboxSelect>>', self.on_command_select)

        # Add Command Button
        self.add_command_button = ttk.Button(self.command_tab, text="Add Command", command=self.add_command)
        self.add_command_button.pack(pady=5)

        # Delete Command Button
        self.delete_command_button = ttk.Button(self.command_tab, text="Delete Command", command=self.delete_command)
        self.delete_command_button.pack(pady=5)

        # Create associations tab
        self.associations_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.associations_tab, text='Associations')

        # Associations Text
        self.associations_text = tk.Text(self.associations_tab, wrap=tk.WORD)
        self.associations_text.pack(fill=tk.BOTH, expand=True)

        # Create templates tab
        self.templates_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.templates_tab, text='Templates')

        # Templates Listbox
        self.templates_listbox = tk.Listbox(self.templates_tab, selectmode=tk.SINGLE)
        self.templates_listbox.pack(fill=tk.BOTH, expand=True)
        self.templates_listbox.bind('<<ListboxSelect>>', self.on_template_select)

        # Add Template Button
        self.add_template_button = ttk.Button(self.templates_tab, text="Add Template", command=self.add_template)
        self.add_template_button.pack(pady=5)

        # Delete Template Button
        self.delete_template_button = ttk.Button(self.templates_tab, text="Delete Template", command=self.delete_template)
        self.delete_template_button.pack(pady=5)

        # Common Templates
        self.common_templates = {
            "Read Register": {"command": "READ", "address": "REGISTER"},
            "Write Register": {"command": "WRITE", "address": "REGISTER", "value": "DATA"}
        }
        for template_name in self.common_templates:
            self.templates_listbox.insert(tk.END, template_name)

    def add_address(self):
        address_name = simpledialog.askstring("Add Address", "Enter Address Name:")
        if address_name:
            self.address_listbox.insert(tk.END, address_name)

    def delete_address(self):
        selection = self.address_listbox.curselection()
        if selection:
            self.address_listbox.delete(selection)

    def on_address_select(self, event):
        pass  # Placeholder for future functionality

    def add_command(self):
        command_name = simpledialog.askstring("Add Command", "Enter Command Name:")
        if command_name:
            self.command_listbox.insert(tk.END, command_name)

    def delete_command(self):
        selection = self.command_listbox.curselection()
        if selection:
            self.command_listbox.delete(selection)

    def on_command_select(self, event):
        pass  # Placeholder for future functionality

    def add_template(self):
        template_name = simpledialog.askstring("Add Template", "Enter Template Name:")
        if template_name:
            self.templates_listbox.insert(tk.END, template_name)
            self.common_templates[template_name] = {}

    def delete_template(self):
        selection = self.templates_listbox.curselection()
        if selection:
            template_name = self.templates_listbox.get(selection[0])
            self.templates_listbox.delete(selection)
            del self.common_templates[template_name]

    def on_template_select(self, event):
        selection = self.templates_listbox.curselection()
        if selection:
            template_name = self.templates_listbox.get(selection[0])
            template_data = self.common_templates.get(template_name, {})
            self.associations_text.delete('1.0', tk.END)
            for key, value in template_data.items():
                self.associations_text.insert(tk.END, f"{key}: {value}\n")
