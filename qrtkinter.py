import tkinter as tk
import qrcode as qr

# Function to generate QR code and display in tkinter window
def generate_qr_code():
    link = link_entry.get()
    img = qr.make(link)
    img.save("TECHNICAL_ARHAN_MANSOORI_YOUTUBE.png")
    qr_code_img = tk.PhotoImage(file="TECHNICAL_ARHAN_MANSOORI_YOUTUBE.png")
    qr_label.config(image=qr_code_img)
    qr_label.image = qr_code_img

# Create tkinter window
root = tk.Tk()
root.title("QR Code by arhan_mansoori pvt.ltd")

# Label and entry for entering the link
link_label = tk.Label(root, text="Enter the link to convert to QR code:")
link_label.pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack()

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack()

# Run the tkinter main loop
root.mainloop()
