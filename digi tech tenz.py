import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import random

class ExpiationNotice:
    def __init__(self, officer, offender, offense_type, offense_desc, fine_amt, loc, date):
        self.officer = officer
        self.offender = offender
        self.offense_type = offense_type
        self.offense_desc = offense_desc
        self.fine_amt = fine_amt
        self.loc = loc
        self.date = date

    def to_string(self):
        return f"{self.officer}|{self.offender}|{self.offense_type}|{self.offense_desc}|{self.fine_amt}|{self.loc}|{self.date}"

def save_to_file(notice):
    with open("expiation_notices.txt", "a") as file:
        file.write(notice.to_string() + '\n')

def submit():
    officer = officer_entry.get()
    offender = offender_entry.get()
    offense = offense_entry.get()
    desc = desc_entry.get()
    
    try:
        amt = float(amt_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid fine amount.")
        return

    loc = loc_entry.get()
    date = datetime.now().strftime("%Y-%m-%d")

    notice = ExpiationNotice(officer, offender, offense, desc, amt, loc, date)
    save_to_file(notice)
    add_notice_to_listbox(notice)

    messagebox.showinfo("Success", "Expiation notice logged.")

def add_notice_to_listbox(notice):
    listbox.insert(tk.END, f"{notice.offender} - {notice.offense_type}")

class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        officer_label = tk.Label(self, text="Officer name:")
        officer_entry = tk.Entry(self)
        offender_label = tk.Label(self, text="Offender name:")
        offender_entry = tk.Entry(self)
        offense_label = tk.Label(self, text="Offense type:")
        offense_entry = tk.Entry(self)
        desc_label = tk.Label(self, text="Offense description:")
        desc_entry = tk.Entry(self)
        amt_label = tk.Label(self, text="Fine amount:")
        amt_entry = tk.Entry(self)
        loc_label = tk.Label(self, text="Location:")
        loc_entry = tk.Entry(self)

        submit_btn = tk.Button(self, text="Submit", command=submit)
        switch_btn = tk.Button(self, text="Go to Other Page", command=lambda: master.switch_frame(OtherPage))

        listbox_frame = ttk.Frame(self)
        global listbox
        listbox = tk.Listbox(listbox_frame, height=10, width=50)
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)

        officer_label.grid(row=0, column=0)
        officer_entry.grid(row=0, column=1)
        offender_label.grid(row=1, column=0)
        offender_entry.grid(row=1, column=1)
        offense_label.grid(row=2, column=0)
        offense_entry.grid(row=2, column=1)
        desc_label.grid(row=3, column=0)
        desc_entry.grid(row=3, column=1)
        amt_label.grid(row=4, column=0)
        amt_entry.grid(row=4, column=1)
        loc_label.grid(row=5, column=0)
        loc_entry.grid(row=5, column=1)
        submit_btn.grid(row=6, columnspan=2)
        switch_btn.grid(row=7, columnspan=2)
        listbox_frame.grid(row=8, columnspan=2)
        listbox.pack(side=tk.LEFT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

class OtherPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="This is the Other Page")
        switch_btn = tk.Button(self, text="Go back to Home Page", command=lambda: master.switch_frame(HomePage))

        listbox_frame = ttk.Frame(self)
        listbox = tk.Listbox(listbox_frame, height=10, width=50)
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)

        def generate_fake_data():
            officer_names = ["John Doe", "Jane Smith", "Bob Johnson", "Emily Davis", "Michael Lee"]
            australian_cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle", "Canberra"]

            fake_data = []
            for i in range(50):
                officer = random.choice(officer_names)
                offender = f"Offender {i+1}"
                offense_type = "Traffic Violation"
                offense_desc = "Description of Traffic Violation"
                fine_amt = random.randint(50, 500)
                loc = random.choice(australian_cities)
                date = f"2022-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
                
                notice = ExpiationNotice(officer, offender, offense_type, offense_desc, fine_amt, loc, date)
                fake_data.append(notice)

            return fake_data

        fake_data = generate_fake_data()
        for notice in fake_data:
            listbox.insert(tk.END, f"{notice.offender} - {notice.offense_type}")

        label.pack()
        switch_btn.pack()
        listbox_frame.pack()
        listbox.pack(side=tk.LEFT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Expiation Notice Logger")
        self.geometry("400x300")
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()