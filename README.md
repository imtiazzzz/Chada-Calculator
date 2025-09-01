# 🚌🛺 Chada Calculator – Deshnetar Calculator System  

## 📌 Description  
The **Chada Calculator** (Deshnetar Calculator System) is a satirical yet enterprise-level Python application that calculates the hidden charges (*chadabazi*) of different transportation services in Bangladesh.  

It is built with **Object-Oriented Programming (OOP)** concepts such as **abstraction, inheritance, and polymorphism**.  
The system models two main services:  

- **Bus** 🚍 – Straightforward fare calculation with optional multiplier and extra percentage.  
- **Auto Rickshaw** 🛺 – Fare calculation that includes:  
  - Extra 10% "priority passenger experience"  
  - Mandatory *singara & coke* costs 🍴🥤  

The program follows clean coding practices with **logging, custom exceptions, and enterprise-level structure**.  

---

## ❓ Problem Statement  
> **Question:**  
Design a Python program that represents different transportation services with unique fare calculation rules. The program should:  
1. Let the user choose a transport type (Bus or Auto).  
2. Take input for multiplier (e.g., number of rides) and extra percentage (e.g., festival surcharge).  
3. Demonstrate OOP principles such as abstraction, inheritance, and polymorphism.  
4. Be written in an enterprise-level coding style with logging, error handling, and extensibility.  

---

## ✅ Solution  
- **Abstract Base Class (`Transportation`)**  
  - Defines shared structure (base fare, service name, fare calculation).  

- **Bus Class**  
  - Implements a simple fare calculation with multiplier and percentage.  

- **Auto Class**  
  - Overrides the calculation by adding a **priority charge (10%)** and a **flat snack cost (15.0)**.  

- **Custom Exception (`FareCalculationError`)**  
  - Ensures invalid inputs (negative values) are properly handled.  

- **Service Layer**  
  - Demonstrates polymorphism by calculating fares across multiple services in a uniform way.  

- **User Input Driven**  
  - Users interactively choose transport, enter multiplier, and extra percentage to get the final fare.  

---

## 🚀 Installation & Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/chada-calculator.git
cd chada-calculator

### 2. Run the Program  
```bash
python deshnetar_calculator.py

### 3. Example Interaction
```bash
=== Deshnetar Calculator ===
Choose transportation:
1. Bus
2. Auto
Enter your choice (1/2): 2
Enter multiplier (default=1): 3
Enter extra percentage (default=0): 20

=== Fare Calculation Result ===
Auto Stand, Base Fare: 80
Includes: 10% priority charge + singara coke cost (15.0)
Final Fare: 319.00


