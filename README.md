# 💰 Employee Salary & Insurance Calculator (GUI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Library-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
This project is a desktop application developed with **Python** and **Tkinter**. It calculates the net wage and insurance premiums for employees based on their job title, daily working hours, and total working days.

The project demonstrates **Object-Oriented Programming (OOP)** principles by separating the business logic (`Personel` class) from the graphical user interface (`PersonelApp` class).

## 🚀 Features
* **Role-Based Calculation:** Automatically adjusts insurance premium rates based on the job title (Apprentice, Journeyman, Master).
* **OOP Design:** Clean code structure separating logic and UI.
* **Input Validation:** Error handling for invalid numeric inputs.
* **Interactive GUI:** User-friendly interface built with Tkinter widgets (Combobox, Entry, Grid Layout).

## 🧮 Calculation Logic

### Insurance Premium (Sigorta Primi)
The premium is calculated as a percentage of the base salary depending on the title:
* **Apprentice (Çırak):** 10%
* **Journeyman (Kalfa):** 20%
* **Master (Usta):** 30%

### Net Wage (Verilecek Ücret)
The wage is calculated based on the daily effort relative to a standard 8-hour shift and 30-day month:
$$\text{Wage} = \left( \frac{\text{Daily Hours}}{8} \right) \times \left( \frac{\text{Base Salary}}{30} \right) \times \text{Days Worked}$$

## 🛠 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/employee-salary-calculator-gui.git
    cd employee-salary-calculator-gui
    ```

2.  **Run the application:**
    *(Note: Tkinter is included with standard Python installations)*
    ```bash
    python main.py
    ```



## 📝 License
This project is open-source and available under the MIT License.
