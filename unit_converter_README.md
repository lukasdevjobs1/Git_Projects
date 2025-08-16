# 🔄 Unit Converter

A simple desktop application for converting between different units of measurement, built with Python's Tkinter library.

## 📋 Project Overview

This Unit Converter provides an intuitive graphical interface for converting:
- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles

The application features real-time conversion with error handling and a clean, user-friendly interface.

## 🛠️ Technologies Used

### Core Libraries
- **tkinter**: Python's standard GUI library for creating the desktop interface
- **messagebox** (from tkinter): Provides error dialog boxes for user feedback

### Key Features
- Bidirectional conversion support
- Input validation with error handling
- Grid-based layout for organized UI
- Real-time result display

## 🚀 How to Run

```bash
# Run the application
python conversor_unidades.py
```

## 💡 Usage

1. **Temperature Conversion**:
   - Enter a value in either Celsius or Fahrenheit field
   - Click "Convert Temperature"
   - Result appears below the input fields

2. **Distance Conversion**:
   - Enter a value in either Kilometers or Miles field
   - Click "Convert Distance"
   - Result appears below the input fields

## 🔧 Code Structure

- `convert_temperature()`: Handles Celsius/Fahrenheit conversions
- `convert_distance()`: Handles Kilometers/Miles conversions
- `UnitConverter` class: Main GUI application with conversion methods
- Error handling for invalid inputs

## 📊 Conversion Formulas

**Temperature**:
- Celsius to Fahrenheit: `(C × 1.8) + 32`
- Fahrenheit to Celsius: `(F - 32) / 1.8`

**Distance**:
- Kilometers to Miles: `km × 0.621371`
- Miles to Kilometers: `miles × 1.60934`

## 🎯 Project Goals

- Practice GUI development with Tkinter
- Implement mathematical conversions
- Create user-friendly desktop applications
- Apply error handling best practices