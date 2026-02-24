import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

class ClothingPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Clothing Brand POS System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f5f5f5")

        self.cart = []
        self.total = 0

        # ======= Title =======
        title = tk.Label(root, text="CLOTHING BRAND POS SYSTEM",
                         font=("Arial", 20, "bold"),
                         bg="#222", fg="white")
        title.pack(fill="x")

        # ======= Frame =======
        frame = tk.Frame(root, bg="#f5f5f5")
        frame.pack(pady=10)

        # Product Name
        tk.Label(frame, text="Item Name", bg="#f5f5f5").grid(row=0, column=0)
        self.item_entry = tk.Entry(frame)
        self.item_entry.grid(row=0, column=1)

        # Price
        tk.Label(frame, text="Price (Ksh)", bg="#f5f5f5").grid(row=1, column=0)
        self.price_entry = tk.Entry(frame)
        self.price_entry.grid(row=1, column=1)

        # Quantity
        tk.Label(frame, text="Quantity", bg="#f5f5f5").grid(row=2, column=0)
        self.qty_entry = tk.Entry(frame)
        self.qty_entry.grid(row=2, column=1)

        # Add Button
        tk.Button(frame, text="Add to Cart",
                  command=self.add_to_cart,
                  bg="green", fg="white").grid(row=3, columnspan=2, pady=5)

        # ======= Cart Table =======
        self.tree = ttk.Treeview(root, columns=("Item", "Price", "Qty", "Total"),
                                 show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Qty", text="Quantity")
        self.tree.heading("Total", text="Total")
        self.tree.pack(fill="both", expand=True, padx=20)

        # ======= Bottom Frame =======
        bottom_frame = tk.Frame(root, bg="#f5f5f5")
        bottom_frame.pack(pady=10)

        self.total_label = tk.Label(bottom_frame,
                                    text="Total: Ksh 0",
                                    font=("Arial", 14, "bold"),
                                    bg="#f5f5f5")
        self.total_label.grid(row=0, column=0, padx=10)

        tk.Button(bottom_frame, text="Remove Selected",
                  command=self.remove_item,
                  bg="red", fg="white").grid(row=0, column=1, padx=5)

        tk.Button(bottom_frame, text="Generate Receipt",
                  command=self.generate_receipt,
                  bg="blue", fg="white").grid(row=0, column=2, padx=5)

        tk.Button(bottom_frame, text="Clear Cart",
                  command=self.clear_cart,
                  bg="orange", fg="white").grid(row=0, column=3, padx=5)

    # ======= Functions =======

    def add_to_cart(self):
        try:
            item = self.item_entry.get()
            price = float(self.price_entry.get())
            qty = int(self.qty_entry.get())

            total_price = price * qty
            self.cart.append((item, price, qty, total_price))
            self.tree.insert("", "end",
                             values=(item, price, qty, total_price))

            self.total += total_price
            self.total_label.config(text=f"Total: Ksh {self.total}")

            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)

        except:
            messagebox.showerror("Error", "Enter valid values!")

    def remove_item(self):
        selected = self.tree.selection()
        if not selected:
            return

        for item in selected:
            values = self.tree.item(item, "values")
            self.total -= float(values[3])
            self.tree.delete(item)

        self.total_label.config(text=f"Total: Ksh {self.total}")

    def clear_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.cart.clear()
        self.total = 0
        self.total_label.config(text="Total: Ksh 0")

    def generate_receipt(self):
        if not self.cart:
            messagebox.showinfo("Receipt", "Cart is empty!")
            return

        receipt = "====== CLOTHING BRAND RECEIPT ======\n"
        receipt += f"Date: {datetime.datetime.now()}\n"
        receipt += "------------------------------------\n"

        for item in self.cart:
            receipt += f"{item[0]} x{item[2]} - Ksh {item[3]}\n"

        receipt += "------------------------------------\n"
        receipt += f"TOTAL: Ksh {self.total}\n"
        receipt += "Thank you for shopping!\n"

        messagebox.showinfo("Receipt", receipt)


# ======= Run App =======
if __name__ == "__main__":
    root = tk.Tk()
    app = ClothingPOS(root)
    root.mainloop()