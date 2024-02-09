import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


df = pd.read_csv('archive\AtMid_Wingers.csv')
df2 = pd.read_csv('archive\CenterBacks.csv')
df3 = pd.read_csv('archive\Forwards.csv')
df4 = pd.read_csv('archive\FullBacks.csv')
df5 = pd.read_csv('archive\GoalKeepers.csv')
df6 = pd.read_csv('archive/Midfielders.csv')


Non_GK= {'Non-GK': ['Non-Penalty Goals', 'Non-Penalty xG', 'Shots Total', 'Assists', 'xAG',
                     'npxG + xAG', 'Shot-Creating Actions', 'Passes Attempted', 'Pass Completion %',
                     'Progressive Passes', 'Progressive Carries', 'Successful Take-Ons',
                     'Touches (Att Pen)', 'Progressive Passes Rec', 'Tackles', 'Interceptions',
                     'Blocks', 'Clearances', 'Aerials won']
}
GK ={'GK': ['PSxG-GA', 'Goals Against', 'Save Percentage', 'PSxG/SoT',
                 'Save% (Penalty Kicks)', 'Clean Sheet Percentage', 'Touches', 'Launch %',
                 'Goal Kicks', 'Avg. Length of Goal Kicks', 'Crosses Stopped %',
                 'Def. Actions Outside Pen. Area', 'Avg. Distance of Def. Actions']
}

# Define color mappings for non-GK players
category_colors_non_gk = {
    'Non-Penalty Goals': 'red',
    'Non-Penalty xG': 'red',
    'Shots Total': 'red',
    'Assists': 'red',
    'xAG': 'red',
    'npxG + xAG': 'red',
    'Shot-Creating Actions': 'red',
    'Passes Attempted': 'yellow',
    'Pass Completion %': 'yellow',
    'Progressive Passes': 'yellow',
    'Progressive Carries': 'yellow',
    'Successful Take-Ons': 'yellow',
    'Touches (Att Pen)': 'yellow',
    'Progressive Passes Rec': 'yellow',
    'Tackles': 'green',
    'Interceptions': 'green',
    'Blocks': 'green',
    'Clearances': 'green',
    'Aerials won': 'green'
}

# Define color mappings for GK players
category_colors_gk = {
    'PSxG-GA': 'blue',
    'Goals Against': 'red',
    'Save Percentage': 'green',
    'PSxG/SoT': 'orange',
    'Save% (Penalty Kicks)': 'purple',
    'Clean Sheet Percentage': 'pink',
    'Touches': 'cyan',
    'Launch %': 'magenta',
    'Goal Kicks': 'yellow',
    'Avg. Length of Goal Kicks': 'brown',
    'Crosses Stopped %': 'lime',
    'Def. Actions Outside Pen. Area': 'teal',
    'Avg. Distance of Def. Actions': 'navy'
}

df7 = pd.DataFrame(Non_GK)
df8 = pd.DataFrame(GK)
labels = df7['Non-GK']
labels_gk = df8['GK']


"""""
print(labels.shape)
row_index=0
#Assuming 'Attribute Vector' contains string representations of arrays
values_str = df.loc[row_index, 'Attribute Vector']
values = np.fromstring(values_str[1:-1], dtype= float , sep=',')  # Assuming the string representation is in the form '[1 2 3]'
print(values.shape)
"""

def print_player_stats(df, user_input, labels,category_colors):
    player_data = df[df['Name'] == user_input]

    if player_data.empty:
        print(f"No data found for player '{user_input}'.")
        return
    
    index = df.loc[df['Name'] == user_input].index[0]
    #print(index)
    values_str = df.loc[index, 'Percentiles']
    values = np.fromstring(values_str[1:-1], dtype= float , sep=',')
    #print("Values", values.shape)
    #print("Labels",labels.shape)


    num_vars = len(labels)
   

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    # Define width for each bar
    bar_width = 2 * np.pi / num_vars

    # Plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    if category_colors:
            for i, (label, value) in enumerate(zip(labels, values)):
                color = category_colors.get(label, 'blue')  # Default to blue if category not found
                ax.bar(angles[i], value, width=bar_width, alpha=0.6, color=color, edgecolor="black")
                ax.bar(angles[i], 100, width=bar_width, alpha=0.1, color=color, edgecolor="black", linestyle='--')
                ax.text(angles[i], value+5, str(round(value, 2)), ha='center', va='bottom',fontsize=7)

         
    else:
        ax.bar(angles, values, width=bar_width, alpha=0.7)


    ax.spines['polar'].set_color('grey') 
    plt.grid(axis='x')
    plt.title(user_input)

    labelPadding = 4
    lowerLimit = 30
    for angle, label in zip(angles, labels):
        rotation = np.rad2deg(angle)
        if angle >= np.pi/2 and angle < 3*np.pi/2:
            alignment = "right"
            rotation += 180
        else:
            alignment = "left"

        if len(label.split())>1:
             label = '\n'.join(label.split())

        ax.text(
            x=angle,
            y=lowerLimit + labelPadding + 80,
            s=label,
            ha=alignment,
            va='center',
            rotation=rotation,
            rotation_mode="anchor",
            wrap=True
        )  

    ax.set_yticklabels([])
    plt.xticks([])
    plt.show()

# Get name from user input
user_input = input("Enter a name to search in the dataset: ")
print_player_stats(df, user_input, labels,category_colors_non_gk)
print_player_stats(df2, user_input, labels,category_colors_non_gk)
print_player_stats(df3, user_input, labels,category_colors_non_gk)
print_player_stats(df4, user_input, labels,category_colors_non_gk)
print_player_stats(df6, user_input, labels,category_colors_non_gk)

