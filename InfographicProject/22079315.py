import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the file path
file_path = r'C:\DOCUMENT\BUSINESS DOC\january jobs\New folder\obesity.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)
# Generate mock data
np.random.seed(42)
age = np.random.randint(18, 60, 100)
family_history = np.random.choice([0, 1], size=100)
gender = np.random.choice(['Male', 'Female'], size=100)
transportation_modes = np.random.choice(['Car', 'Bus', 'Bike', 'Walking'], size=100)
line_data = np.cumsum(np.random.normal(size=100))

# Set the Seaborn style for a clean white grid
sns.set(style="whitegrid")

# Create a figure and axis for subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))  # Adjusted figure size

# Add title outside the plots
fig.suptitle('Health and Lifestyle Analysis', fontsize=30, y=0.96)  # Adjusted vertical position

# Plot 1: Age Trends by Family History
sns.boxplot(x=family_history, y=age, ax=axes[0, 0])
axes[0, 0].set_title('Age Trends by Family History')
axes[0, 0].set_xlabel('Family History with Overweight')
axes[0, 0].set_ylabel('Age')

# Plot 2: Gender Distribution
sns.countplot(x=gender, ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Gender Distribution')
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Count')

# Plot 3: Pie Chart for Transportation Modes with Detached Sector
explode = (0, 0, 0.1, 0)  # Detach the third sector
transportation_counts = np.bincount(np.random.choice([0, 1, 2, 3], size=100))
axes[1, 0].pie(transportation_counts, labels=['Car', 'Bus', 'Bike', 'Walking'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen', 'lightpink'], explode=explode)
axes[1, 0].set_title('Preferred Transportation Modes')

# Plot 4: Line Graph
axes[1, 1].plot(line_data, label='Line Graph', color='orange')
axes[1, 1].set_title('data aspect')
axes[1, 1].set_xlabel('X axis')
axes[1, 1].set_ylabel('frequency')
axes[1, 1].legend()

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0.02, 1, 0.94])  # Adjusted the rectangle to leave space for the title

# Add student information at the bottom right
fig.text(0.99, 0.01, 'Student: Your Name | ID: Your ID', ha='right', fontsize=12)

# Add brief explanations with headings for each plot together on the right side
explanations = [
    "1. Brief Heading: Examining age trends based on family history with overweight.",
    "2. Brief Heading: Understanding the gender distribution in the dataset.",
    "3. Brief Heading: Highlighting preferred transportation modes among participants.",
    "4. Brief Heading: An additional line graph showing a different aspect of the data."
]

# Add explanations on the right side
fig.text(1.02, 0.85, '\n'.join(explanations), ha='left', va='top', fontsize=14)

# Save the plot as an image
plt.savefig("22079315.png", dpi=300)

# Show the plots
plt.show()

