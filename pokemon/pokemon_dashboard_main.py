import pandas as pd
import panel as pn
import hvplot.pandas

# Initialize the Panel extension
pn.extension()

# Load your Pokémon dataset
pokemon_data = pd.read_csv('Pokemon.csv')

# Create widgets for the Attack Bar Plot
poke_type_select_attack = pn.widgets.Select(
    name='Select Pokémon Type:',
    options=['All'] + list(pokemon_data['Type 1'].unique()),
    value='All',
    sizing_mode='stretch_width'
)
attack_slider = pn.widgets.RangeSlider(
    name='Attack Range:',
    start=0,
    end=190,
    value=(50, 100),
    sizing_mode='stretch_width'
)
num_pokemon_slider_attack = pn.widgets.IntSlider(
    name='Number of Pokémon to Display:',
    start=1,
    end=150,
    value=10,
    sizing_mode='stretch_width'
)

# Create widgets for the Attack vs. Defense Scatter Plot
poke_type_select_scatter = pn.widgets.Select(
    name='Select Pokémon Type (Scatter):',
    options=['All'] + list(pokemon_data['Type 1'].unique()),
    value='All',
    sizing_mode='stretch_width'
)
attack_slider_scatter = pn.widgets.RangeSlider(
    name='Attack Range (Scatter):',
    start=0,
    end=190,
    value=(50, 100),
    sizing_mode='stretch_width'
)
defense_slider = pn.widgets.RangeSlider(
    name='Defense Range:',
    start=0,
    end=190,
    value=(50, 100),
    sizing_mode='stretch_width'
)

# Create widgets for the Speed Histogram
speed_slider = pn.widgets.RangeSlider(
    name='Speed Range:',
    start=0,
    end=180,
    value=(50, 100),
    sizing_mode='stretch_width'
)
num_bins_slider = pn.widgets.IntSlider(
    name='Number of Bins:',
    start=5,
    end=50,
    value=10,
    sizing_mode='stretch_width'
)


# Define a class to manage data filtering
class PokemonAPI:
    def __init__(self, data):
        self.data = data

    def filter_by_type(self, poke_type):
        if poke_type == 'All':
            return self.data
        return self.data[self.data['Type 1'] == poke_type]

    def filter_by_stats(self, min_attack, max_attack):
        return self.data[(self.data['Attack'] >= min_attack) & (self.data['Attack'] <= max_attack)]

    def filter_defense(self, min_defense, max_defense):
        return self.data[(self.data['Defense'] >= min_defense) & (self.data['Defense'] <= max_defense)]

    def filter_speed(self, min_speed, max_speed):
        return self.data[(self.data['Speed'] >= min_speed) & (self.data['Speed'] <= max_speed)]


# Create an instance of the API with the Pokémon data
pokemon_api = PokemonAPI(pokemon_data)


# Update plots based on widget values for Attack Bar Plot
@pn.depends(poke_type_select_attack.param.value, attack_slider.param.value, num_pokemon_slider_attack.param.value)
def update_attack_bar_plot(poke_type, attack_range, num_pokemon):
    filtered_data = pokemon_api.filter_by_type(poke_type)
    filtered_data = pokemon_api.filter_by_stats(attack_range[0], attack_range[1])
    filtered_data = filtered_data.head(num_pokemon)

    # Generate plots
    plot = filtered_data.hvplot.bar(
        x='Name',
        y='Attack',
        title='Filtered Pokémon by Attack',
        width=1000,
        height=400
    ).opts(xrotation=45)
    return plot


# Update plots based on widget values for Attack vs. Defense Scatter Plot
@pn.depends(poke_type_select_scatter.param.value, attack_slider_scatter.param.value, defense_slider.param.value)
def update_attack_defense_scatter_plot(poke_type, attack_range, defense_range):
    filtered_data = pokemon_api.filter_by_type(poke_type)
    filtered_data = pokemon_api.filter_by_stats(attack_range[0], attack_range[1])
    filtered_data = pokemon_api.filter_defense(defense_range[0], defense_range[1])

    # Generate scatter plot
    scatter_plot = filtered_data.hvplot.scatter(
        x='Attack',
        y='Defense',
        title='Attack vs. Defense',
        width=1000,
        height=400
    )
    return scatter_plot


# Update plots based on widget values for Speed Histogram
@pn.depends(speed_slider.param.value, num_bins_slider.param.value)
def update_speed_histogram(speed_range, num_bins):
    filtered_data = pokemon_api.filter_speed(speed_range[0], speed_range[1])

    # Generate histogram
    histogram = filtered_data.hvplot.hist(
        y='Speed',
        bins=num_bins,
        title='Distribution of Speed',
        width=1000,
        height=400
    )
    return histogram


# Create informative descriptions for each component
info_text = pn.pane.Markdown(
    """
    # Pokémon Dashboard (by Lauren and Aarushi)

    Welcome to our Pokémon Dashboard! Use this interactive tool to explore and analyze Pokémon data. 
    Adjust the filters below to see how different Pokémon stack up based on their attributes.

    ## Tab: Attack Bar Plot
    - **Select Pokémon Type**: Choose a specific Pokémon type to filter results.
    - **Attack Range**: Adjust the slider to limit Pokémon displayed by their Attack stats.
    - **Number of Pokémon to Display**: Set the maximum number of Pokémon to display in the chart.

    **Graph Explanation**: This bar plot visualizes the Attack stats of the selected Pokémon. Each bar represents a Pokémon's name on the x-axis and its corresponding Attack value on the y-axis. This visualization helps users compare the Attack power of different Pokémon.

    ## Tab: Attack vs. Defense Scatter Plot
    - **Select Pokémon Type (Scatter)**: Choose a specific Pokémon type for filtering.
    - **Attack Range (Scatter)**: Adjust the slider to set minimum and maximum Attack values.
    - **Defense Range**: Set minimum and maximum Defense values to filter the Pokémon shown.

    **Graph Explanation**: This scatter plot visualizes the relationship between Pokémon's Attack and Defense stats. Each point represents a Pokémon plotted with its Attack on the x-axis and Defense on the y-axis, allowing users to analyze how these two stats correlate.

    ## Tab: Speed Histogram
    - **Speed Range**: Adjust this slider to limit the Pokémon based on their Speed stats.
    - **Number of Bins**: Set the number of bins for the histogram to visualize the Speed distribution.

    **Graph Explanation**: This histogram shows the distribution of Speed values among the selected Pokémon. The x-axis represents Speed intervals (bins), while the y-axis indicates the number of Pokémon that fall within each bin. This visualization helps users understand how Speed is distributed among Pokémon.
    """
)

# Create the dashboard layout with tabs
tabs = pn.Tabs(
    ('Attack Bar Plot', pn.Column(info_text, poke_type_select_attack, attack_slider, num_pokemon_slider_attack,
                                  pn.panel(update_attack_bar_plot))),
    ('Attack vs. Defense Scatter Plot',
     pn.Column(info_text, poke_type_select_scatter, attack_slider_scatter, defense_slider,
               pn.panel(update_attack_defense_scatter_plot))),
    ('Speed Histogram', pn.Column(info_text, speed_slider, num_bins_slider, pn.panel(update_speed_histogram)))
)

# Serve the dashboard
tabs.show()
