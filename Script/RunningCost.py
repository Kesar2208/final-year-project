import tkinter as tk
from tkinter import ttk

# Fixed fuel prices
PETROL_PRICE = 94.61  # Rs. per liter
DIESEL_PRICE = 90.28  # Rs. per liter
EV_PRICE = 8          # Rs. per kWh
CNG_PRICE = 80.35     # Rs. per kg

def calculate_savings():
    try:
        # Input mileage and distance
        petrol_mileage = float(entry_petrol_mileage.get())                                                                                                       # type: ignore
        diesel_mileage = float(entry_diesel_mileage.get())                                                                                                          # type: ignore
        ev_range = float(entry_ev_range.get())                                                                                                                                  # type: ignore
        ev_battery_capacity = float(entry_ev_battery.get())                                                                                                                                     # type: ignore
        cng_mileage = float(entry_cng_mileage.get())                                                                                                                                        # type: ignore
        monthly_distance = float(entry_monthly_distance.get())                                                                                                                                           # type: ignore

        # Buying price inputs
        petrol_price = float(entry_petrol_price.get())                                                                                                                           # type: ignore
        ev_price = float(entry_ev_price.get())                                                                                                                                              # type: ignore

        # Running costs (/km)
        petrol_running_cost = PETROL_PRICE / petrol_mileage
        diesel_running_cost = DIESEL_PRICE / diesel_mileage
        ev_efficiency = ev_range / ev_battery_capacity
        ev_running_cost = EV_PRICE / ev_efficiency
        cng_running_cost = CNG_PRICE / cng_mileage

        # Monthly costs
        petrol_monthly_cost = petrol_running_cost * monthly_distance
        diesel_monthly_cost = diesel_running_cost * monthly_distance
        ev_monthly_cost = ev_running_cost * monthly_distance
        cng_monthly_cost = cng_running_cost * monthly_distance

        # Monthly savings
        savings_petrol_ev = petrol_monthly_cost - ev_monthly_cost
        savings_petrol_cng = petrol_monthly_cost - cng_monthly_cost
        savings_diesel_ev = diesel_monthly_cost - ev_monthly_cost
        savings_diesel_cng = diesel_monthly_cost - cng_monthly_cost

        # Break-even for EV vs Petrol
        extra_ev_cost = abs(ev_price - petrol_price)  # Treat as positive
        if savings_petrol_ev > 0:
            months_to_breakeven = extra_ev_cost / savings_petrol_ev
            years = int(months_to_breakeven // 12)
            months = int(months_to_breakeven % 12)
            breakeven_text = f"Extra EV Cost: Rs. {extra_ev_cost:,.0f}\nBreak-even in: {years} years, {months} months"
        else:
            breakeven_text = "Break-even: Not applicable (no monthly savings)"

        result_text = f"""
Running Cost (per km):
Petrol: ₹{petrol_running_cost:.2f} | Diesel: ₹{diesel_running_cost:.2f} | EV: ₹{ev_running_cost:.2f} | CNG: ₹{cng_running_cost:.2f}

Monthly Cost for {monthly_distance} km:
Petrol: ₹{petrol_monthly_cost:.2f} | Diesel: ₹{diesel_monthly_cost:.2f} | EV: ₹{ev_monthly_cost:.2f} | CNG: ₹{cng_monthly_cost:.2f}

Monthly Savings:
Petrol → EV: ₹{savings_petrol_ev:.2f} | Petrol → CNG: ₹{savings_petrol_cng:.2f}
Diesel → EV: ₹{savings_diesel_ev:.2f} | Diesel → CNG: ₹{savings_diesel_cng:.2f}

{breakeven_text}
"""
        label_results.config(text=result_text)
    except ValueError:
        label_results.config(text="Invalid input! Enter numbers only.")

# GUI Setup
root = tk.Tk()
root.title("Fuel Cost & Savings Calculator")
root.geometry("650x800")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="ridge", bd=5)
frame.pack(pady=10)

tk.Label(frame, text="Fixed Fuel Prices:", font=("Arial", 10, "bold"), bg="#ffffff").pack()
tk.Label(frame, text=f"Petrol: ₹{PETROL_PRICE}/L | Diesel: ₹{DIESEL_PRICE}/L | EV: ₹{EV_PRICE}/kWh | CNG: ₹{CNG_PRICE}/kg",
         font=("Arial", 10), bg="#ffffff").pack(pady=(0,10))

tk.Label(frame, text="Enter Vehicle Mileage (km/unit):", font=("Arial", 10, "bold"), bg="#ffffff").pack()
for label, entry_var in [
    ("Petrol Mileage", 'entry_petrol_mileage'),
    ("Diesel Mileage", 'entry_diesel_mileage'),
    ("EV Range (km/full charge)", 'entry_ev_range'),
    ("EV Battery Capacity (kWh)", 'entry_ev_battery'),
    ("CNG Mileage", 'entry_cng_mileage'),
    ("Monthly Driving Distance (km)", 'entry_monthly_distance'),
    ("Petrol Vehicle Price (Rs.)", 'entry_petrol_price'),
    ("EV Vehicle Price (Rs.)", 'entry_ev_price'),
]:
    tk.Label(frame, text=label, bg="#ffffff").pack()
    globals()[entry_var] = tk.Entry(frame)
    globals()[entry_var].pack()

tt_style = ttk.Style()
tt_style.configure("Big.TButton", font=("Arial", 11), padding=10)
ttk.Button(root, text="Calculate Savings", command=calculate_savings, style="Big.TButton").pack(pady=10)

label_results = tk.Label(root, text="", font=("Arial", 11), bg="#f0f0f0", justify="center", anchor="center", wraplength=600)
label_results.pack(pady=10)

root.mainloop()