import tkinter as tk
from tkinter import messagebox

# Predefined depreciation rates based on vehicle type and age
DEPRECIATION_RATES = {
    "Petrol": {0.5: 0.05, 1: 0.15, 2: 0.20, 3: 0.30, 4: 0.40, 5: 0.50},
    "Diesel": {0.5: 0.05, 1: 0.15, 2: 0.20, 3: 0.30, 4: 0.40, 5: 0.50},
    "EV": {0.5: 0.05, 1: 0.10, 2: 0.15, 3: 0.25, 4: 0.35, 5: 0.45},
    "CNG": {0.5: 0.05, 1: 0.12, 2: 0.18, 3: 0.28, 4: 0.38, 5: 0.48},
}

# Ownership & Maintenance Impact Factors
OWNERSHIP_IMPACT = {"First Owner": 1.0, "Second Owner": 0.9, "Third Owner": 0.8}
MAINTENANCE_IMPACT = {"Well-Maintained": 1.0, "Moderate": 0.9, "Poor": 0.75}


def set_depreciation_rate(event=None):
    """Update the depreciation rate based on vehicle type and age."""
    vehicle_type = dropdown_var.get()
    age = float(age_var.get())
    rate = DEPRECIATION_RATES[vehicle_type][age]
    entry_rate.delete(0, tk.END)
    entry_rate.insert(0, rate)


def calculate_resale():
    """Calculate resale value based on depreciation, ownership, and maintenance."""
    try:
        original_price = float(entry_price.get())
        age = int(float(age_var.get()))  # Convert age (0.5 for 6 months)
        vehicle_type = dropdown_var.get()
        
        # Ownership & Maintenance factors
        ownership_factor = OWNERSHIP_IMPACT[ownership_var.get()]
        maintenance_factor = MAINTENANCE_IMPACT[maintenance_var.get()]

        # Apply yearly depreciation dynamically
        resale_price = original_price
        for year in range(1, age + 1):  # Loop through each year
            depreciation_rate = DEPRECIATION_RATES[vehicle_type].get(year, 0.5)  # Default max rate
            resale_price *= (1 - depreciation_rate)

        # Apply ownership & maintenance impact
        resale_price *= ownership_factor * maintenance_factor

        # Display result
        label_result.config(text=f"Resale Price: ₹{resale_price:,.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# Create main window
root = tk.Tk()
root.title("Vehicle Resale Price Calculator")
root.geometry("450x480")

# Vehicle type dropdown
tk.Label(root, text="Select Vehicle Type:", font=("Arial", 10)).pack(pady=5)
dropdown_var = tk.StringVar(root)
dropdown_var.set("Petrol")  
dropdown_menu = tk.OptionMenu(root, dropdown_var, *DEPRECIATION_RATES.keys(), command=set_depreciation_rate)
dropdown_menu.pack(pady=5)

# Age dropdown (6 months to 5 years)
tk.Label(root, text="Select Vehicle Age:", font=("Arial", 10)).pack(pady=5)
age_var = tk.StringVar(root)
age_var.set("1")  # Default 1 year
age_options = ["0.5", "1", "2", "3", "4", "5"]
age_menu = tk.OptionMenu(root, age_var, *age_options, command=set_depreciation_rate)
age_menu.pack(pady=5)

# Ownership history dropdown
tk.Label(root, text="Ownership History:", font=("Arial", 10)).pack(pady=5)
ownership_var = tk.StringVar(root)
ownership_var.set("First Owner")  # Default selection
ownership_menu = tk.OptionMenu(root, ownership_var, *OWNERSHIP_IMPACT.keys())
ownership_menu.pack(pady=5)

# Maintenance condition dropdown
tk.Label(root, text="Maintenance Condition:", font=("Arial", 10)).pack(pady=5)
maintenance_var = tk.StringVar(root)
maintenance_var.set("Well-Maintained")  # Default selection
maintenance_menu = tk.OptionMenu(root, maintenance_var, *MAINTENANCE_IMPACT.keys())
maintenance_menu.pack(pady=5)

# Labels and Entry fields
tk.Label(root, text="Original Price (₹):", font=("Arial", 10)).pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack(pady=5)

tk.Label(root, text="Depreciation Rate (Auto-filled)", font=("Arial", 10)).pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate Resale Price", command=calculate_resale)
btn_calculate.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Resale Price: ₹0.00", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# Set default depreciation rate
set_depreciation_rate()

# Run GUI
root.mainloop()
