from tkinter.ttk import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, Menu
from tkcalendar import Calendar


# Main window
root = tk.Tk()
root.title("Login / Register")
root.geometry("400x500")

# Function to open the signup window
def open_register_window():
    register_window = tk.Toplevel()
    register_window.title("Register")
    
    Label(register_window, text="Get Started Now", font=("Arial", 24)).pack(pady=20)

    Label(register_window, text="Name").pack()
    name_entry = Entry(register_window)
    name_entry.pack(pady=5)

    Label(register_window, text="Email address").pack()
    email_entry = Entry(register_window)
    email_entry.pack(pady=5)

    Label(register_window, text="Password").pack()
    password_entry = Entry(register_window, show='*')
    password_entry.pack(pady=5)

    
    Button(register_window, text="Register", command=lambda: messagebox.showinfo("Info", "Sign up successful!")).pack(pady=20)

    Button(register_window, text="Log in", command=register_window.destroy).pack()

# Function to open the login window
def open_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")
    
    Label(login_window, text="Welcome back!", font=("Arial", 24)).pack(pady=20)

    Label(login_window, text="Email address").pack()
    email_entry = Entry(login_window)
    email_entry.pack(pady=5)

    Label(login_window, text="Password").pack()
    password_entry = Entry(login_window, show='*')
    password_entry.pack(pady=5)
    password=password_entry.get()
    email=email_entry.get()



    Button(login_window, text="Login", command=lambda: messagebox.showinfo("Info", "Login successful!")).pack(pady=20)

    Button(login_window, text="Forgot Password?", command=lambda: messagebox.showinfo("Info", "Password recovery options")).pack(pady=5)

    Button(login_window, text="Register", command=login_window.destroy).pack()

# Main Buttons
Button(root, text="Register", command=open_register_window).pack(pady=20)
Button(root, text="Log In", command=open_login_window).pack(pady=20)






#Menu bar
# Importing only those functions which are needed  
root.title('Menu Demonstration')
holidays_window=0

def open_holidays_window():
    holidays_window = tk.Toplevel()
    holidays_window.title("Holidays & Packages")

    # Function to handle search button click
    def search():
        from_city = from_city_combobox.get()
        to_city = to_city_combobox.get()
        departure_date = departure_date_entry.get()
        guests = guests_entry.get()
        print(f"Searched from {from_city} to {to_city} on {departure_date} for {guests}.")

    # Function to select a date from the calendar
    def select_date():
        def get_selected_date():
            departure_date_entry.delete(0, tk.END)
            departure_date_entry.insert(0, cal.get_date())
            top.destroy()

        # Create a new top-level window for the calendar
        top = tk.Toplevel(holidays_window)
        top.title("Select Departure Date")

        cal = Calendar(top, selectmode='day', year=2025, month=3, day=19)
        cal.grid(row=0, column=0, padx=20, pady=20)

        select_btn = tk.Button(top, text="Select Date", command=get_selected_date)
        select_btn.grid(row=1, column=0, pady=10)

    # Predefined options for From City
    cities = ["New Delhi", "Goa", "Mumbai", "Bengaluru", "Kolkata", "Chennai", "Kerala", "Kashmir", "Rajasthan", "Agra", "Jaipur", "Mysuru", "Varanasi", "Udaipur"]

    # Dropdown for From City
    tk.Label(holidays_window, text="From City").grid(row=0, column=0, padx=10, pady=10)
    from_city_combobox = ttk.Combobox(holidays_window, values=cities, width=30)
    from_city_combobox.set("Select a city")  # Default text
    from_city_combobox.grid(row=0, column=1) 

    # To City Dropdown
    tk.Label(holidays_window, text="To City/Country/Category").grid(row=0, column=2, padx=10, pady=10)
    to_city_combobox = ttk.Combobox(holidays_window, values=cities, width=30)
    to_city_combobox.set("Select a city")
    to_city_combobox.grid(row=0, column=3)

    # Departure Date Selection
    tk.Label(holidays_window, text="Departure Date").grid(row=1, column=0, padx=10, pady=10)
    departure_date_entry = tk.Entry(holidays_window)
    departure_date_entry.grid(row=1, column=2)
    date_button = tk.Button(holidays_window, text="Select Date", command=select_date)
    date_button.grid(row=1, column=1, padx=10, pady=10)

    # Guests Entry
    tk.Label(holidays_window, text="Rooms & Guests").grid(row=1, column=3, padx=10, pady=10)
    guests_entry = tk.Entry(holidays_window)
    guests_entry.grid(row=1, column=4)

    # Search Button
    search_button = tk.Button(holidays_window, text="SEARCH", command=search, bg="blue", fg="white")
    search_button.grid(row=3, column=0, columnspan=5, pady=20)

# Creating Menubar 
menubar = Menu(root) 

# Flights Menu 
flights = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Flights', menu=flights)  
flights.add_command(label='Open...', command=None) 
flights.add_separator() 
flights.add_command(label='Exit', command=quit) 

# Hotels Menu
hotels = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Hotels', menu=hotels) 
hotels.add_command(label='Open', command=None) 
hotels.add_separator() 
hotels.add_command(label='Exit', command=quit) 

# Holidays & Packages Menu
holidays = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Holidays & Packages', menu=holidays) 
holidays.add_command(label='Open Holidays Window', command=open_holidays_window)  # Link to the function
holidays.add_separator() 
holidays.add_command(label='Exit', command=lambda: holidays_window.destroy() if holidays_window else None)

# Display Menu 
root.config(menu=menubar) 
root.mainloop()
