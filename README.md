Football Player Stats Visualization
This Python script visualizes football player statistics using radar charts. The script reads data from CSV files containing player statistics categorized into different positions on the field. It then allows users to input a player's name and visualize their stats on a radar chart, highlighting different attributes with distinct colors.

Dependencies
Python 3.x
NumPy
Pandas
Matplotlib
How to Use
Clone the repository or download the Python script.

Ensure you have all dependencies installed.

Place the CSV files containing player statistics in the 'archive' directory. The CSV files should be named as follows:

'AtMid_Wingers.csv'
'CenterBacks.csv'
'Forwards.csv'
'FullBacks.csv'
'GoalKeepers.csv'
'Midfielders.csv'
Run the Python script.

Enter the name of the player you want to visualize when prompted.

The script will display a radar chart representing the player's statistics, with each attribute color-coded according to its category.

File Structure
football_player_stats.py: The main Python script for visualizing player statistics.
archive/: Directory containing CSV files with player statistics for different positions.
README.md: This file, providing instructions and information about the script.