import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

def process_and_plot_data(file_path, title, ylabel):
    
    """
    
    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    -------
    df : TYPE
        DESCRIPTION.
    df_t : TYPE
        DESCRIPTION.

    """
    
    # Read data from CSV file
    df = pd.read_csv(file_path)

    # Set 'Country Name' as the index
    df.set_index('Country Name', inplace=True)

    # Drop rows with NaN values
    df = df.dropna()

    # Exclude unnecessary columns
    df = df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Convert columns to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Transpose the DataFrame
    df_transposed = df.T

    # Plot the transposed DataFrame
    ax = df_transposed.plot(kind='bar', figsize=(12, 6), width=0.8)

    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()

    # Display the summary statistics using describe
    summary_stats = df.describe()
    print("\nSummary Statistics:")
    print(summary_stats)

# Access to Electricity Data
access_to_electricity_file = 'Access to electricity.csv'
process_and_plot_data(access_to_electricity_file, 
                      'Access to Electricity Over the Years by Country', 
                      'Access to Electricity (%)')

# Renewable Energy Consumption Data
renewable_energy_file = 'Renewable energy consumption.csv'
process_and_plot_data(renewable_energy_file, 
          'Renewable Energy Consumption Over the Years by Country', 
          'Renewable Energy Consumption (% of Total Final Energy Consumption)')



# Read data from the CSV file
df = pd.read_csv('Electricity production from renewable sources.csv')

# Transpose the DataFrame for easier plotting
df_transposed = df.set_index('Country Name').T

df_transposed = df_transposed.apply(pd.to_numeric, errors='coerce')

# Plot the data for each country excluding columns with all NaN values
def plot_line_chart(data, title, xlabel, ylabel):
    ax = data.loc[:, ~data.isna().all()].plot(kind='line', marker='o',
                                              figsize=(10, 6))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

# Use the UDF to make the line plot
plot_line_chart(df_transposed, 'Renewable Energy Production Over Time',
                'Year', 'Percentage of Total Electricity Production')

# Show the plot
plt.show()
plt.savefig('Renewable Energy Production Over Time.png')



# Read data from the CSV file
df_fossil = pd.read_csv
('Electricity production from oil, gas and coal sources.csv')

# Transpose the DataFrame for easier plotting
df_fossil_transposed = df_fossil.set_index('Country Name').T

df_fossil_transposed = df_fossil_transposed.apply(pd.to_numeric, 
                                                  errors='coerce')

# Plot the data for each country excluding columns with all NaN values
def plot_line_chart(data, title, xlabel, ylabel):
    ax = data.loc[:, ~data.isna().all()].plot(kind='line', marker='o', 
                                              figsize=(10, 6))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

# Use the UDF to make the line plot
plot_line_chart(df_fossil_transposed,
                'Electricity Production from Fossil Sources Over Time', 'Year',
                'Percentage of Total Electricity Production')

# Show the plot
plt.show()
plt.savefig('Electricity Production from Fossil Sources Over Time.png')



# Read data from the CSV file
df_greenhouse_gas = pd.read_csv('greenhouse gas emissions.csv')

# Transpose the DataFrame for easier plotting
df_greenhouse_gas_transposed = df_greenhouse_gas.set_index('Country Name').T

df_greenhouse_gas_transposed = df_greenhouse_gas_transposed.apply(pd.to_numeric
                                                            ,errors='coerce')

# Plot the data for each country excluding columns with all NaN values
def plot_line_chart(data, title, xlabel, ylabel):
    ax = data.loc[:, ~data.isna().all()].plot(kind='line', marker='o',
                                              figsize=(10, 6))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

# Use the UDF to make the line plot
plot_line_chart(df_greenhouse_gas_transposed, 
                'Total Greenhouse Gas Emissions Over Time', 'Year', 
                'Total Emissions (kt of CO2 equivalent)')

# Show the plot
plt.show()
plt.savefig('Total Greenhouse Gas Emissions Over Time.png')


def generate_describe_func(title, data_df):
    '''
    Print statistical properties of a dataset including skewness,
    kurtosis, and median.

    Parameters
    ----------
    title : str
        The title of the dataset.

    data_df : pd.DataFrame
        The dataset in Pandas DataFrame format.

    Returns
    -------
    None.
    '''
    # Print the title
    print("Analyzing: " + title)

    # Print the general description of the dataset
    print("----- General Statistics -----")
    print(data_df.describe())

    # Print skewness information
    print("----- Skewness -----")
    skewness_df = pd.DataFrame(ss.skew(data_df), index=data_df.columns,
                               columns=["Skewness"])
    print(skewness_df)

    # Print kurtosis information
    print("----- Kurtosis -----")
    kurtosis_df = pd.DataFrame(ss.kurtosis(data_df), index=data_df.columns,
                               columns=["Kurtosis"])
    print(kurtosis_df)

    # Print median values
    print("----- Median -----")
    print("Median values:")
    print(data_df.median())



def generate_heatmap(country, df_greenhouse_gas, df_urban_population, 
    df_fossil_transposed, df_transposed, df_Access_to_electricity, 
    df_Renewable_energy_consumption):
    """
    

    Parameters
    ----------
    country : TYPE
        DESCRIPTION.
    df_greenhouse_gas: TYPE
        DESCRIPTION.
    df_urban_population : TYPE
        DESCRIPTION.
    df_fossil_transposed : TYPE
        DESCRIPTION.
    df_transposed : TYPE
        DESCRIPTION.
    df_Access_to_electricity : TYPE
        DESCRIPTION.
    df_Renewable_energy_consumption : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    # create dataframe
    df_corr = pd.DataFrame()
    
    # accessing data from data frame and create columns
    df_corr["greenhouse gas emissions"] = df_greenhouse_gas[country].values
    df_corr["urban_population"] = df_urban_population[country].values
    df_corr["Electricity production from oil, gas and coal sources"] = df_fossil_transposed[country].values
    df_corr["Electricity production from renewable sources"] = df_transposed[country].values
    df_corr["Access to electricity"] = df_Access_to_electricity[country].values
    df_corr["Renewable energy consumption"] = df_Renewable_energy_consumption[country].values
    
    
    # create heatmap
    corr_mat = df_corr.corr().round(2)
    plt.figure()
    
    # show heatmap
    plt.imshow(corr_mat, cmap="Accent_r")
    plt.colorbar()
    
    # create ticks 
    plt.xticks(np.arange(len(corr_mat.columns)),
               labels=corr_mat.columns, rotation=90)
    plt.yticks(np.arange(len(corr_mat.columns)), labels=corr_mat.columns)

    plt.title(country)

    # looping
    for(i, j), corr_xy in np.ndenumerate(corr_mat):
        plt.text(i, j, corr_xy, ha="center", va="center")

    plt.savefig(country+".png", dpi=200)  # ,va="center"



# function calling
# generate line chart
var_x = "greenhouse gas emissions.csv"
df_greenhouse_gas, df_greenhouse_gas_t = process_and_plot_data(var_x)

var_x = "urban_population.csv"
df_urban_population, df_urban_population_t = process_and_plot_data(var_x)

var_x = "Electricity production from oil, gas and coal sources.csv"
df_fossil_transposed, df_fossil_transposed_t = process_and_plot_data(var_x)

var_x = "Electricity production from renewable sources.csv"
df_transposed, df_transposed_t = process_and_plot_data(var_x)

var_x = "Access to electricity.csv"
df_Access_to_electricity, df_Access_to_electricity_t = process_and_plot_data(var_x)

var_x = "Renewable energy consumption.csv"
df_Renewable_energy_consumption, df_Renewable_energy_consumption_t = process_and_plot_data(var_x)

# # call function to generate heatmap
all_country = ["Denmark", "Indonesia", "Spain"]
for country in all_country:
    generate_heatmap(country, df_greenhouse_gas_t, df_urban_population_t, 
                     df_fossil_transposed_t, df_transposed_t, 
                     df_Access_to_electricity_t, 
                     df_Renewable_energy_consumption_t)

plt.show()

