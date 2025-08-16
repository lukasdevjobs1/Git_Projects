# UNIT CONVERTER
"""
Unit Converter Application

A desktop GUI application for converting between different units of measurement.
Built using Python's Tkinter library for cross-platform compatibility.

Supported Conversions:
- Temperature: Celsius ↔ Fahrenheit
- Distance: Kilometers ↔ Miles

Libraries Used:
- tkinter: Python's standard GUI toolkit for creating desktop applications
- messagebox: Tkinter module for displaying error dialogs and user notifications

Author: Daily Coding Projects
Date: 2024
"""

import tkinter as tk
from tkinter import messagebox

def convert_temperature(celsius, fahrenheit):
    """
    Convert between Celsius and Fahrenheit temperatures.
    
    Args:
        celsius (float): Temperature in Celsius (None if converting from Fahrenheit)
        fahrenheit (float): Temperature in Fahrenheit (None if converting from Celsius)
    
    Returns:
        float: Converted temperature value
    """
    if celsius:
        return (celsius * 1.8) + 32
    elif fahrenheit:
        return (fahrenheit - 32) / 1.8

def convert_distance(kilometers, miles):
    """
    Convert between kilometers and miles.
    
    Args:
        kilometers (float): Distance in kilometers (None if converting from miles)
        miles (float): Distance in miles (None if converting from kilometers)
    
    Returns:
        float: Converted distance value
    """
    if kilometers:
        return kilometers * 0.621371
    elif miles:
        return miles * 1.60934

class UnitConverter:
    """
    Main GUI application class for the Unit Converter.
    
    Creates a desktop interface using Tkinter with input fields, buttons,
    and result labels for temperature and distance conversions.
    
    Attributes:
        root (tk.Tk): Main application window
        entry_* (tk.Entry): Input fields for user values
        button_* (tk.Button): Conversion trigger buttons
        label_* (tk.Label): Result display labels
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Unit Converter")

        # Create input fields and buttons
        self.entry_celsius = tk.Entry(self.root)
        self.entry_fahrenheit = tk.Entry(self.root)
        self.entry_kilometers = tk.Entry(self.root)
        self.entry_miles = tk.Entry(self.root)

        self.button_temperature = tk.Button(self.root, text="Convert Temperature")
        self.button_distance = tk.Button(self.root, text="Convert Distance")

        # Create labels to display results
        self.label_temperature = tk.Label(self.root, text="")
        self.label_distance = tk.Label(self.root, text="")

        # Organize elements in the interface
        self.entry_celsius.grid(row=0, column=0)
        self.entry_fahrenheit.grid(row=0, column=1)
        self.button_temperature.grid(row=0, column=2)

        self.entry_kilometers.grid(row=1, column=0)
        self.entry_miles.grid(row=1, column=1)
        self.button_distance.grid(row=1, column=2)

        self.label_temperature.grid(row=2, column=0)
        self.label_distance.grid(row=2, column=1)

        # Define button actions
        self.button_temperature.config(command=self.convert_temp)
        self.button_distance.config(command=self.convert_dist)

    def convert_temp(self):
        """
        Handle temperature conversion from GUI inputs.
        
        Reads values from Celsius or Fahrenheit entry fields,
        performs conversion, and displays result in label.
        Shows error dialog for invalid inputs.
        """
        try:
            celsius_val = self.entry_celsius.get()
            fahrenheit_val = self.entry_fahrenheit.get()
            
            if celsius_val:
                celsius = float(celsius_val)
                result = convert_temperature(celsius, None)
                self.label_temperature.config(text=f"{celsius}°C = {result:.1f}°F")
            elif fahrenheit_val:
                fahrenheit = float(fahrenheit_val)
                result = convert_temperature(None, fahrenheit)
                self.label_temperature.config(text=f"{fahrenheit}°F = {result:.1f}°C")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def convert_dist(self):
        """
        Handle distance conversion from GUI inputs.
        
        Reads values from kilometers or miles entry fields,
        performs conversion, and displays result in label.
        Shows error dialog for invalid inputs.
        """
        try:
            km_val = self.entry_kilometers.get()
            miles_val = self.entry_miles.get()
            
            if km_val:
                kilometers = float(km_val)
                result = convert_distance(kilometers, None)
                self.label_distance.config(text=f"{kilometers} km = {result:.2f} miles")
            elif miles_val:
                miles = float(miles_val)
                result = convert_distance(None, miles)
                self.label_distance.config(text=f"{miles} miles = {result:.2f} km")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def run(self):
        """
        Start the GUI application main loop.
        
        Launches the Tkinter event loop to display the interface
        and handle user interactions.
        """
        self.root.mainloop()

if __name__ == "__main__":
    """
    Application entry point.
    
    Creates and runs the Unit Converter GUI application when
    the script is executed directly.
    """
    converter = UnitConverter()
    converter.run()