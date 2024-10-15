# HW 3: Dashboards
# Lauren Cummings & Aarushi Attray
# This is our pokemon_dashboard_main.py (our main file for thsi homework containing the dashboard)
# We worked on most parts together, but some were more divided than others

# Importing all the libraries needed for this dashboard
import pandas as pd
import hvplot.pandas
import panel as pn
import sqlite3

pn.extension()

# Mianly worked on by Aarushi
# Setting up SQLite database connection and create the table from CSV (as noted from the assignment directions)
def setup_database():
    conn = sqlite3.connect('pokemon.db')
    pokemon_data = pd.read_csv('cleaned_pokemon.csv')
    pokemon_data.to_sql('pokemon', conn, if_exists='replace', index=False)
    print("Database created successfully.")  # Confirmation of database creation
    conn.close()

setup_database()

# Mainly worked on by Aarushi
# Defining an API-like function to gte the filtered data from SQLite
def get_filtered_data(type1=None, generation=None, legendary=None):
    conn = sqlite3.connect('pokemon.db')
    query = "SELECT * FROM pokemon WHERE 1=1"

    if type1:
        query += f" AND type1 = '{type1}'"
    if generation:
        query += f" AND generation = {generation}"
    if legendary is not None:
        query += f" AND legendary = {int(legendary)}"

    filtered_data = pd.read_sql(query, conn)
    conn.close()
    return filtered_data

# Mainly worked on by Lauren
# These are the widgets for filtering Pokémon data
poke_type_select = pn.widgets.Select(
    name='Type 1',
    options=['All'] + sorted(get_filtered_data()['type1'].unique().tolist())
)
poke_generation_select = pn.widgets.IntSlider(
    name='Generation',
    start=1,
    end=7,
    value=1
)
poke_legendary_toggle = pn.widgets.Checkbox(
    name='Legendary Only'
)

# More widgets for range selection and color (sliders)
poke_hp_slider = pn.widgets.IntSlider(
    name='HP Range',
    start=0,
    end=255,
    value=0,
    step=5
)
poke_attack_slider = pn.widgets.IntSlider(
    name='Attack Range',
    start=0,
    end=255,
    value=0,
    step=5
)
plot_color_picker = pn.widgets.ColorPicker(
    name='Bar Color',
    value='#0073e6'
)

# Mainly worked on by Aarushi
# This function gets the filtered data based on widget values
@pn.depends(poke_type_select.param.value, poke_generation_select.param.value, poke_legendary_toggle.param.value)
def filter_pokemon_data(type_selected, generation_selected, legendary_toggle):
    type1 = None if type_selected == 'All' else type_selected
    filtered_data = get_filtered_data(type1=type1, generation=generation_selected, legendary=legendary_toggle)
    return filtered_data

# Mainly worked on by Lauren
# This function updates the first bar plot based on filtered data
@pn.depends(poke_type_select.param.value, poke_generation_select.param.value, poke_legendary_toggle.param.value,
            plot_color_picker.param.value)
def update_overall_bar_plot(type_selected, generation_selected, legendary_toggle, color):
    type1 = None if type_selected == 'All' else type_selected
    filtered_data = get_filtered_data(type1=type1, generation=generation_selected, legendary=legendary_toggle)

    if filtered_data.empty:
        return pn.pane.Markdown("### No Pokémon found for this filter combination.")

    plot = filtered_data.hvplot.bar(
        x='name', y='overall capabilities', color=color,
        title=f"Pokémon Overall Capabilities - {type_selected} (Gen {generation_selected})",
        width=700, height=400
    ).opts(show_grid=True)

    return plot

# Mainly worked on by Aarushi
# This function for updating HP distribution plot
@pn.depends(poke_hp_slider.param.value, poke_type_select.param.value)
def update_hp_plot(hp_value, type_selected):
    type1 = None if type_selected == 'All' else type_selected
    filtered_data = get_filtered_data(type1=type1)
    filtered_data = filtered_data[filtered_data['hp'] >= hp_value]

    if filtered_data.empty:
        return pn.pane.Markdown("### No Pokémon found for this HP range.")

    plot = filtered_data.hvplot.hist(
        y='hp', bins=20, color='orange', width=700, height=400,
        title=f"HP Distribution for Pokémon with HP >= {hp_value}"
    )

    return plot

# Mainly worked on by Lauren
# This function for updating Attack vs Defense comparison plot
@pn.depends(poke_attack_slider.param.value, poke_type_select.param.value)
def update_attack_defense_plot(attack_value, type_selected):
    type1 = None if type_selected == 'All' else type_selected
    filtered_data = get_filtered_data(type1=type1)
    filtered_data = filtered_data[filtered_data['attack'] >= attack_value]

    if filtered_data.empty:
        return pn.pane.Markdown("### No Pokémon found for this attack range.")

    plot = filtered_data.hvplot.scatter(
        x='attack', y='defense', color='purple', width=700, height=400,
        title=f"Attack vs Defense for Pokémon with Attack >= {attack_value}"
    ).opts(size=10)

    return plot

# Mainly worked on by Aarushi
# This function for updating the plot for Attack and HP comparison
@pn.depends(poke_attack_slider.param.value, poke_hp_slider.param.value)
def update_attack_hp_plot(attack_value, hp_value):
    filtered_data = get_filtered_data()
    filtered_data = filtered_data[(filtered_data['attack'] >= attack_value) & (filtered_data['hp'] >= hp_value)]

    if filtered_data.empty:
        return pn.pane.Markdown("### No Pokémon found for this attack and HP range.")

    plot = filtered_data.hvplot.scatter(
        x='attack', y='hp', color='green', width=700, height=400,
        title=f"Attack vs HP for Pokémon with Attack >= {attack_value} and HP >= {hp_value}"
    ).opts(size=10)

    return plot

# Mainly worked on by Aarushi and Lauren
# General message for the page
welcome_message = pn.pane.Markdown(
    "### Welcome to our Pokémon Dashboard! 🐾\n"
    "This dashboard allows you to explore Pokémon data interactively.\n"
    "Please use the filters below to analyze various aspects of Pokémon capabilities.\n\n"
    "**HP (Hit Points)** is a measure of a Pokémon's health. A Pokémon's HP decreases when it takes damage in battle. "
    "If its HP drops to zero, the Pokémon is knocked out."
)

# Makes the layout of the dashboard using tabs - got this from lecture and TA
first_tab = pn.Column(
    welcome_message,
    pn.Row(poke_type_select, poke_generation_select, poke_legendary_toggle),
    pn.pane.Markdown("#### Overall Capabilities\n"
                     "In this section, you can filter Pokémon by their type, generation, and whether they are legendary.\n"
                     "The bar plot displays the overall capabilities of the selected Pokémon (a summary metric that reflects a Pokémon's general strength or performance across various attributes), where you can customize the bar color."),
    update_overall_bar_plot,
    poke_hp_slider,
    update_hp_plot,
    width = 700,
    height = 400
)

second_tab = pn.Column(
    welcome_message,
    pn.pane.Markdown("### Attack vs Defense\n"
                     "In this tab, you can analyze the relationship between Pokémon attack and defense stats.\n"
                     "Filter the Pokémon by their type, and select an attack value to visualize the data."),
    pn.Row(poke_type_select, poke_attack_slider, plot_color_picker),
    update_attack_defense_plot,
    width = 700,
    height = 400
)

third_tab = pn.Column(
    welcome_message,
    pn.pane.Markdown("### Attack vs HP\n"
                     "In this tab, you can compare Pokémon's attack and HP values.\n"
                     "Use the sliders to set minimum values for attack and HP, and see how they correlate."),
    pn.Row(poke_attack_slider, poke_hp_slider),
    update_attack_hp_plot,
    width = 700,
    height = 400
)


# Panel dashboard with tabs
tabs = pn.Tabs(
    ("Overall Capabilities", first_tab),
    ("Attack vs Defense", second_tab),
    ("Attack vs HP", third_tab)
)

if __name__ == '__main__':
    pn.serve(tabs)
