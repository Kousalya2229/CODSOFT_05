import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        messagebox.showinfo("Success", "Contact added!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

def view_contacts():
    listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone:")
    if keyword:
        listbox.delete(0, tk.END)
        for i, contact in enumerate(contacts):
            if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
                listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        contact["name"] = entry_name.get()
        contact["phone"] = entry_phone.get()
        contact["email"] = entry_email.get()
        contact["address"] = entry_address.get()
        messagebox.showinfo("Updated", "Contact updated.")
        view_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Error", "Select a contact to update.")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        messagebox.showinfo("Deleted", "Contact deleted.")
        view_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Error", "Select a contact to delete.")

def load_contact_details(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact["name"])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact["email"])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact["address"])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

window = tk.Tk()
window.title("Contact Manager")
window.geometry("500x500")

tk.Label(window, text="Store/Contact Name:").pack()
entry_name = tk.Entry(window, width=50)
entry_name.pack()

tk.Label(window, text="Phone Number:").pack()
entry_phone = tk.Entry(window, width=50)
entry_phone.pack()

tk.Label(window, text="Email:").pack()
entry_email = tk.Entry(window, width=50)
entry_email.pack()

tk.Label(window, text="Address:").pack()
entry_address = tk.Entry(window, width=50)
entry_address.pack()

tk.Button(window, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(window, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(window, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(window, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(window, text="View All Contacts", command=view_contacts).pack(pady=5)

listbox = tk.Listbox(window, width=60, height=10)
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', load_contact_details)

window.mainloop()
