# Pokemon Dashboard

Welcome to the **Pokémon Dashboard**! This interactive tool provides a detailed exploration of Pokémon data, allowing users to visualize stats and filter Pokémon by type, generation, attack, HP, and more. Below is a guide on how to use the various components of the dashboard and navigate through its features.

---

## Table of Contents
1. **Setup and Requirements**
2. **Features by Tab**
3. **How to Use the Widgets**
4. **Development and Customization**
5. **Running the Dashboard**


---

## 1. Setup and Requirements

### Prerequisites
- Python 3.x
- Required Libraries:
  - `pandas`
  - `hvplot`
  - `panel`
  - `sqlite3`

### Database Initialization  
The dashboard uses an SQLite database populated from a Pokémon dataset (`cleaned_pokemon.csv`).  
During the **first run**, the `setup_database()` function will:
1. Create a new SQLite database (`pokemon.db`).
2. Load the data from `cleaned_pokemon.csv` into a table named `pokemon`.

Make sure the `cleaned_pokemon.csv` file is present in the same directory before running the script.

---

## 2. Features by Tab

### **Tab 1: Overall Capabilities**  
- **Description:** Explore Pokémon by filtering based on type, generation, and legendary status.
- **Bar Plot:** Displays Pokémon's **overall capabilities** based on selected filters. You can change the bar color using a color picker.
- **HP Distribution:** Visualize how Pokémon are distributed based on their HP values, with a slider to set minimum HP.

---

### **Tab 3: Attack vs Defense**  
- **Description:** Compare Pokémon’s **attack and defense stats** using a scatter plot.
- **Widgets:** 
  - Type selector to filter Pokémon by primary type.
  - Attack slider to set a minimum attack value.
  - Color picker to customize plot points.

---

### **Tab 4: Attack vs HP**  
- **Description:** Analyze the relationship between Pokémon’s **attack** and **HP**.
- **Widgets:**
  - Attack and HP sliders to filter based on minimum values.
  - Scatter plot showing the correlation between attack and HP.

---

## 3. How to Use the Widgets

1. **Select Pokémon Type:**  
   Use the dropdown to filter by Pokémon's primary type (e.g., Water, Fire). Select “All” to include all types.

2. **Set Generation:**  
   Use the slider to choose a specific generation (1 to 7).

3. **Legendary Filter:**  
   Toggle the checkbox to filter only legendary Pokémon.

4. **Adjust HP and Attack Ranges:**  
   Use the sliders to set minimum HP or attack values to refine the plots.

5. **Customize Plot Colors:**  
   Use the color picker to change the color of bar or scatter plots.

---

## 4. Development and Customization

- **Modify the SQL Queries:**  
  You can customize the filtering logic by modifying the `get_filtered_data()` function.

- **Add New Visualizations:**  
  Use the `hvplot` library to extend the visualizations. Add more tabs and plots based on your analysis needs.

- **Change Widget Defaults:**  
  Adjust the default widget values, such as generation range or bar plot color, directly in the code.

---

## 5. Running the Dashboard

To run the dashboard:

1. Ensure you have all required dependencies installed.
2. Run the script in a terminal:
   ```bash
   python pokemon_dashboard.py
   ```
3. The dashboard will be served locally on `http://localhost:60608/`. Open this URL in your browser to access the dashboard.

---

Enjoy exploring your Pokémon data! Feel free to modify the dashboard as needed and uncover interesting insights!
