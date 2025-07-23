import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Load the trained model
model = joblib.load("water_usage_in_agriculture.pkl")


# Create the main window
root = tk.Tk()
root.title("Water Requirement Predictor")
root.geometry("400x400")

# Define input labels and entry fields
labels = ["N", " P", "K", "Temperature", "Humidity", "Soil Moisture"]
entries = []

for label in labels:
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

# Function to make prediction
def predict_water():
    try:
        # Collect input values from user
        data = [float(entry.get()) for entry in entries]
        data_np = np.array([data])  # Shape: (1, 6)
        
        # Make prediction
        prediction = model.predict(data_np)[0]
        
        # Show result
        messagebox.showinfo("Result", f"Predicted Water Requirement: {prediction:.2f} liters")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")

# Button to trigger prediction
tk.Button(root, text="Predict Water Requirement", command=predict_water).pack(pady=20)

# Run the GUI
root.mainloop()


