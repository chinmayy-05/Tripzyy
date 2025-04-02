from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from tkcalendar import Calendar
from PIL import Image, ImageTk
import os

# Initialize main window
root = Tk()
root.title("Travel Booking System")
root.geometry("1000x700")  # Larger window for better image display

# ==================== DATABASE & COMMON FUNCTIONS ====================
try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='chinmay'
    )
except:
    messagebox.showerror("Error", "Could not connect to database")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# ==================== IMAGE HANDLING ====================
def load_image(path, size):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        # Return blank image if file not found
        img = Image.new('RGB', size, color='gray')
        return ImageTk.PhotoImage(img)

# Package data with image paths
# Package data with image paths
package_data = {
    "Kashmir": {
        "packages": {
            "Holiday Package 1": {
                "image": "kashmir1.jpg",
                "details": "5D/4N Kashmir Tour\n\nIncluded:\n- Houseboat stay\n- Shikara ride\n- Gondola ticket\n\nPrice: ₹25,000 per person"
            },
            "Holiday Package 2": {
                "image": "kashmir2.jpg",
                "details": "7D/6N Premium Kashmir\n\nIncluded:\n- Luxury hotel\n- All meals\n- Airport transfers\n\nPrice: ₹42,000 per person"
            }
        },
        "image": "kashmir.jpg"
    },
    "Goa": {
        "packages": {
            "Holiday Package 9": {
                "image": "goa1.jpg",
                "details": "4D/3N Goa Beach Vacation\n\nIncluded:\n- Beach resort\n- Breakfast\n- Water sports\n\nPrice: ₹18,000 per person"
            },
            "Holiday Package 10": {
                "image": "goa2.jpg",
                "details": "5D/4N Goa Party Package\n\nIncluded:\n- Club entries\n- Pool villa\n- All meals\n\nPrice: ₹30,000 per person"
            }
        },
        "image": "goa.jpg"
    },
    "Mumbai": {
        "packages": {
            "Mumbai City Explorer": {
                "image": "mumbai1.jpg",
                "details": "3D/2N Mumbai Tour\n\nIncluded:\n- Luxury hotel stay\n- City sightseeing\n- Bollywood studio tour\n\nPrice: ₹15,000 per person"
            },
            "Mumbai Coastal Retreat": {
                "image": "mumbai2.jpg",
                "details": "4D/3N Coastal Package\n\nIncluded:\n- Beachfront resort\n- Elephanta Caves tour\n- Local cuisine tasting\n\nPrice: ₹22,000 per person"
            }
        },
        "image": "mumbai.jpg"
    },
    "Delhi": {
        "packages": {
            "Delhi Heritage Tour": {
                "image": "delhi1.jpg",
                "details": "3D/2N Delhi Experience\n\nIncluded:\n- Heritage hotel\n- Old Delhi food walk\n- All monument entries\n\nPrice: ₹12,000 per person"
            },
            "Delhi Luxury Escape": {
                "image": "delhi2.jpg",
                "details": "5D/4N Premium Stay\n\nIncluded:\n- 5-star accommodation\n- Private guided tours\n- Spa treatments\n\nPrice: ₹35,000 per person"
            }
        },
        "image": "delhi.jpg"
    },
    "Bangalore": {
        "packages": {
            "Bangalore Tech Tour": {
                "image": "bangalore1.jpg",
                "details": "2D/1N IT City Package\n\nIncluded:\n- Tech park visits\n- Local brewery tour\n- Garden city exploration\n\nPrice: ₹8,000 per person"
            },
            "Bangalore Nature Retreat": {
                "image": "bangalore2.jpg",
                "details": "3D/2N Nature Package\n\nIncluded:\n- Resort near Nandi Hills\n- Trekking activities\n- Organic farm meals\n\nPrice: ₹14,000 per person"
            }
        },
        "image": "bangalore.jpg"
    },
    "Himachal": {
        "packages": {
            "Shimla-Manali Combo": {
                "image": "himachal1.jpg",
                "details": "6D/5N Mountain Tour\n\nIncluded:\n- Hill station visits\n- Toy train ride\n- Snow activities\n\nPrice: ₹28,000 per person"
            },
            "Spiti Valley Adventure": {
                "image": "himachal2.jpg",
                "details": "8D/7N Adventure Trip\n\nIncluded:\n- Camping stays\n- Monastery visits\n- Off-road experiences\n\nPrice: ₹45,000 per person"
            }
        },
        "image": "himachal.jpg"
    },
    "Andaman": {
        "packages": {
            "Andaman Island Hopper": {
                "image": "andaman1.jpg",
                "details": "5D/4N Island Tour\n\nIncluded:\n- Scuba diving\n- Cellular jail visit\n- Glass boat ride\n\nPrice: ₹32,000 per person"
            },
            "Andaman Luxury Escape": {
                "image": "andaman2.jpg",
                "details": "7D/6N Premium Package\n\nIncluded:\n- Private beach resort\n- All water activities\n- Candlelight dinners\n\nPrice: ₹55,000 per person"
            }
        },
        "image": "andaman.jpg"
    },
    "Kerala": {
        "packages": {
            "Kerala Backwaters": {
                "image": "kerala1.jpg",
                "details": "4D/3N Houseboat Tour\n\nIncluded:\n- Private houseboat\n- Ayurvedic massage\n- Kathakali show\n\nPrice: ₹24,000 per person"
            },
            "Kerala Wildlife Adventure": {
                "image": "kerala2.jpg",
                "details": "5D/4N Nature Package\n\nIncluded:\n- Jungle resort\n- Safari experiences\n- Spice plantation tour\n\nPrice: ₹30,000 per person"
            }
        },
        "image": "kerala.jpg"
    },
    "Vietnam": {
        "packages": {
            "Vietnam Cultural Tour": {
                "image": "vietnam1.jpg",
                "details": "7D/6N Vietnam Explorer\n\nIncluded:\n- Halong Bay cruise\n- Cu Chi tunnels\n- All internal transfers\n\nPrice: ₹65,000 per person"
            },
            "Vietnam Beaches": {
                "image": "vietnam2.jpg",
                "details": "8D/7N Coastal Retreat\n\nIncluded:\n- Luxury beach resorts\n- Island hopping\n- All meals included\n\nPrice: ₹78,000 per person"
            }
        },
        "image": "vietnam.jpg"
    },
    "Maldives": {
        "packages": {
            "Maldives Paradise": {
                "image": "maldives1.jpg",
                "details": "5D/4N Island Resort\n\nIncluded:\n- Water villa stay\n- Snorkeling gear\n- Sunset cruise\n\nPrice: ₹85,000 per person"
            },
            "Maldives Luxury": {
                "image": "maldives2.jpg",
                "details": "7D/6N Premium Package\n\nIncluded:\n- Private pool villa\n- All water sports\n- Spa treatments\n\nPrice: ₹1,20,000 per person"
            }
        },
        "image": "maldives.jpg"
    }
}

# ==================== WINDOW 1: LOGIN/REGISTER ====================
def show_login():
    clear_window()
    
    # Background
    bg_frame = Frame(root, bg="#1E1E1E")
    bg_frame.pack(fill=BOTH, expand=True)
    
    # Logo/Header
    header_frame = Frame(bg_frame, bg="#1E1E1E")
    header_frame.pack(pady=50)
    
    try:
        logo_img = ImageTk.PhotoImage(Image.open("logo.png").resize((150, 150)))
        logo_label = Label(header_frame, image=logo_img, bg="#1E1E1E")
        logo_label.image = logo_img
        logo_label.pack()
    except:
        Label(header_frame, text="✈ Travel Booking", font=("Arial", 24), fg="white", bg="#1E1E1E").pack()
    
    # Login Form
    form_frame = Frame(bg_frame, bg="#1E1E1E", padx=30, pady=30)
    form_frame.pack()
    
    Label(form_frame, text="Email", fg="white", bg="#1E1E1E", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="w")
    email_entry = Entry(form_frame, width=30, font=("Arial", 12))
    email_entry.grid(row=0, column=1, pady=5)
    
    Label(form_frame, text="Password", fg="white", bg="#1E1E1E", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="w")
    password_entry = Entry(form_frame, show='*', width=30, font=("Arial", 12))
    password_entry.grid(row=1, column=1, pady=5)
    
    Button(form_frame, text="Login", command=lambda: login_action(email_entry, password_entry), 
          bg="#00A86B", fg="white", font=("Arial", 12), width=15).grid(row=2, column=1, pady=15, sticky="e")
    
    Label(form_frame, text="New user?", fg="white", bg="#1E1E1E").grid(row=3, column=0, pady=10)
    Button(form_frame, text="Register", command=show_register, bg="#FF5733", fg="white", font=("Arial", 12)).grid(row=3, column=1, pady=10)

def show_register():
    clear_window()
    
    bg_frame = Frame(root, bg="#1E1E1E")
    bg_frame.pack(fill=BOTH, expand=True)
    
    Label(bg_frame, text="Create Account", font=("Arial", 24), fg="white", bg="#1E1E1E").pack(pady=30)
    
    form_frame = Frame(bg_frame, bg="#1E1E1E", padx=30, pady=20)
    form_frame.pack()
    
    # Registration form fields...
    Label(form_frame, text="Full Name", fg="white", bg="#1E1E1E").grid(row=0, column=0, pady=5, sticky="w")
    name_entry = Entry(form_frame, width=30)
    name_entry.grid(row=0, column=1, pady=5)
    
    Label(form_frame, text="Email", fg="white", bg="#1E1E1E").grid(row=1, column=0, pady=5, sticky="w")
    email_entry = Entry(form_frame, width=30)
    email_entry.grid(row=1, column=1, pady=5)
    
    Label(form_frame, text="Password", fg="white", bg="#1E1E1E").grid(row=2, column=0, pady=5, sticky="w")
    password_entry = Entry(form_frame, show='*', width=30)
    password_entry.grid(row=2, column=1, pady=5)
    
    Button(form_frame, text="Register", command=lambda: register_user(name_entry, email_entry, password_entry),
          bg="#00A86B", fg="white", width=15).grid(row=3, column=1, pady=15, sticky="e")
    
    Button(form_frame, text="Back to Login", command=show_login, bg="#FF5733", fg="white").grid(row=4, column=1, pady=10)

def login_action(email_entry, password_entry):
    email = email_entry.get()
    password = password_entry.get()
    
    if email and password:
        try:
            mycursor = con.cursor()
            query = "SELECT * FROM register WHERE email = %s AND password = %s"
            mycursor.execute(query, (email, password))
            if mycursor.fetchone():
                messagebox.showinfo("Success", "Login successful!")
                show_search_window()
            else:
                messagebox.showerror("Error", "Invalid credentials")
        except:
            messagebox.showerror("Error", "Database error")
    else:
        messagebox.showerror("Error", "Please fill all fields")

def register_user(name_entry, email_entry, password_entry):
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if name and email and password:
        try:
            mycursor = con.cursor()
            query = "INSERT INTO register (username, email, password) VALUES (%s, %s, %s)"
            mycursor.execute(query, (name, email, password))
            con.commit()
            messagebox.showinfo("Success", "Registration complete!")
            show_login()
        except:
            messagebox.showerror("Error", "Database error")
    else:
        messagebox.showerror("Error", "Please fill all fields")

# ==================== WINDOW 2: SEARCH PAGE ====================
def show_search_window():
    clear_window()
    
    bg_frame = Frame(root, bg="#1E1E1E")
    bg_frame.pack(fill=BOTH, expand=True)
    
    # Header
    header_frame = Frame(bg_frame, bg="#1E1E1E", pady=20)
    header_frame.pack()
    
    Label(header_frame, text="Plan Your Trip", font=("Arial", 24), fg="white", bg="#1E1E1E").pack()
    
    # Search Form
    form_frame = Frame(bg_frame, bg="#2E2E2E", padx=30, pady=30, bd=2, relief=GROOVE)
    form_frame.pack(pady=20, padx=50)
    
    cities = sorted(package_data.keys())  # Get available destinations
    
    # From City
    Label(form_frame, text="From City:", fg="white", bg="#2E2E2E", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    from_city = ttk.Combobox(form_frame, values=cities, state="readonly", font=("Arial", 12))
    from_city.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    from_city.current(0)
    
    # To City
    Label(form_frame, text="To City:", fg="white", bg="#2E2E2E", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    to_city = ttk.Combobox(form_frame, values=cities, state="readonly", font=("Arial", 12))
    to_city.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    to_city.current(0)
    
    # Departure Date
    Label(form_frame, text="Departure Date:", fg="white", bg="#2E2E2E", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    date_var = StringVar()
    date_entry = Entry(form_frame, textvariable=date_var, state="readonly", font=("Arial", 12))
    date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    Button(form_frame, text="Select Date", command=lambda: show_calendar(date_var), 
          bg="#00A86B", fg="white", font=("Arial", 12)).grid(row=2, column=2, padx=10)
    
    # Travelers
    Label(form_frame, text="Travelers:", fg="white", bg="#2E2E2E", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    travelers = Spinbox(form_frame, from_=1, to=10, width=5, font=("Arial", 12))
    travelers.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    # Search Button
    Button(form_frame, text="Search Packages", 
          command=lambda: validate_search(from_city.get(), to_city.get(), date_var.get()),
          bg="#00A86B", fg="white", font=("Arial", 14), width=20).grid(row=4, column=0, columnspan=3, pady=30)
    
    # Footer
    Button(bg_frame, text="Logout", command=show_login, bg="#FF5733", fg="white", font=("Arial", 12)).pack(side=BOTTOM, pady=20)

def show_calendar(date_var):
    def set_date():
        date_var.set(cal.get_date())
        top.destroy()
    
    top = Toplevel(root)
    top.title("Select Date")
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)
    Button(top, text="Select", command=set_date, bg="#00A86B", fg="white").pack(pady=10)

def validate_search(from_city, to_city, date):
    if not date:
        messagebox.showerror("Error", "Please select a departure date")
        return
    
    if from_city == to_city:
        messagebox.showerror("Error", "From and To cities cannot be the same")
        return
    
    show_packages_window(to_city)  # Show packages for destination city

# ==================== WINDOW 3: PACKAGES PAGE ====================
def show_packages_window(destination):
    clear_window()
    
    bg_frame = Frame(root, bg="#1E1E1E")
    bg_frame.pack(fill=BOTH, expand=True)
    
    # Header with destination image
    try:
        dest_img = Image.open(package_data[destination]["image"])
        dest_img = dest_img.resize((500, 300), Image.LANCZOS)# image size 
        dest_photo = ImageTk.PhotoImage(dest_img)
        dest_label = Label(bg_frame, image=dest_photo, bg="#1E1E1E")
        dest_label.image = dest_photo
        dest_label.pack(pady=(0, 20))
    except:
        Label(bg_frame, text=destination, font=("Arial", 24), fg="white", bg="#1E1E1E").pack(pady=20)
    
    Label(bg_frame, text=f"Available Packages in {destination}", 
          font=("Arial", 18), fg="white", bg="#1E1E1E").pack()
    
    # Packages Container - using grid for side-by-side layout
    packages_container = Frame(bg_frame, bg="#1E1E1E")
    packages_container.pack(fill=BOTH, expand=True, padx=50, pady=20)
    
    # Get packages for this destination
    packages = list(package_data[destination]["packages"].items())
    
    # Display packages in 2 columns
    for i, (pkg_name, pkg_info) in enumerate(packages):
        col = i % 2  # 0 for left column, 1 for right
        row = i // 2
        
        pkg_frame = Frame(packages_container, bg="#2E2E2E", bd=2, relief=GROOVE)
        pkg_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Configure grid weights
        packages_container.grid_columnconfigure(col, weight=1)
        packages_container.grid_rowconfigure(row, weight=1)
        
        # Package Image - maintaining aspect ratio
        try:
            img = Image.open(pkg_info["image"])
            img.thumbnail((300, 200))  # Maintain aspect ratio
            photo = ImageTk.PhotoImage(img)
            img_label = Label(pkg_frame, image=photo, bg="#2E2E2E")
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            Label(pkg_frame, text="Image not available", width=30, height=8, bg="gray").pack(pady=10)
        
        # Package Info
        #Label(pkg_frame, text=pkg_name, font=("Arial", 14, "bold"), fg="white", bg="#2E2E2E").pack()
        Label(pkg_frame, text="✓ Free cancellation", fg="lightgreen", bg="#2E2E2E").pack()
        Label(pkg_frame, text="✓ Best price guarantee", fg="lightgreen", bg="#2E2E2E").pack()
        
        # View Details Button
        Button(pkg_frame, text="View Details", 
              command=lambda d=pkg_info["details"]: show_package_details(d, destination),
              bg="#00A86B", fg="white", font=("Arial", 12)).pack(pady=10)
    
    # Navigation buttons at bottom
    nav_frame = Frame(bg_frame, bg="#1E1E1E", pady=20)
    nav_frame.pack(side=BOTTOM, fill=X)
    
    Button(nav_frame, text="Back to Search", command=show_search_window, 
          bg="#FF5733", fg="white", font=("Arial", 12)).pack(side=LEFT, padx=20)
    Button(nav_frame, text="Logout", command=show_login, 
          bg="#FF5733", fg="white", font=("Arial", 12)).pack(side=RIGHT, padx=20)

def show_package_details(details, destination):
    top = Toplevel(root)
    top.title("Package Details")
    top.geometry("600x500")
    
    details_frame = Frame(top, padx=20, pady=20)
    details_frame.pack(fill=BOTH, expand=True)
    
    # Header with back button
    header_frame = Frame(details_frame)
    header_frame.pack(fill=X)
    
    Button(header_frame, text="← Back", command=top.destroy,
          bg="#FF5733", fg="white", font=("Arial", 12)).pack(side=LEFT)
    
    Label(header_frame, text="Package Details", 
          font=("Arial", 16, "bold")).pack(side=LEFT, padx=20)
    
    # Details content
    text_frame = Frame(details_frame)
    text_frame.pack(fill=BOTH, expand=True, pady=20)
    
    text = Text(text_frame, wrap=WORD, font=("Arial", 12), 
               height=15, padx=15, pady=15, bg="#F5F5F5")
    text.insert(END, details)
    text.config(state=DISABLED)
    text.pack(fill=BOTH, expand=True)
    
    # Book Now button
    Button(details_frame, text="Book Now", 
          bg="#00A86B", fg="white", font=("Arial", 14, "bold"),
          width=15).pack(pady=20)
# ==================== START APPLICATION ====================
show_login()
root.mainloop()