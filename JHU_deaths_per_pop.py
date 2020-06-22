import pandas as pd 
import math
#index in col 0
#county name in col 1
#county population size in col 2
#daily new death count starting col 3               

JHU_df = pd.read_csv('/Users/Dino-Sunlight/Desktop/COVIDeeDesktop/Texas COVID-19 Fatality Count Data by County 6_15_20.csv') #loads data
#print("The shape of the DataFrame JHU_df is", JHU_df.shape) #okay it is recognizing dimensions correctly

county_data = {}
row_count = 0 #initialize row_count
for row in JHU_df.itertuples(): #this line: names each row as an index...??? below: calculates and stores the total and per capita for each row in the dataframe. Can I just use "JHU_df"??
    county_total_deaths = 0 #resets values for each county
    county_total_deaths_per_capita = 0
    if row[0] > 1 and row_count > 2 and row_count < math.inf: #start on first county line. Also yes, the csv inputs are recognizes as strings wth
        county_name = row[1] #stores the county name the row we're currently working with.
        column_count = 0
        for i in row: #works through each object/column in the tupled row.
            if column_count <= 2: #skip the first two colmns
                column_count += 1
            elif i != '0': #skips over all the 0 columns to quicken process
                county_total_deaths += float(i) #add the current value to the total death value in the next column, starting at the 3rd column
        county_total_per_capita = county_total_deaths / float(row[2]) #calculates per capita for that row
        county_data[county_name] = (county_total_deaths, county_total_per_capita) #all stored in dictionary for this row. Yay!
        if county_name == "Total":
            row_count = math.inf
    row_count += 1

calculated_df = pd.DataFrame.from_dict(county_data, orient = 'index') #treats county names column as index rather than as list of its own
calculated_df.columns = ['Cumulative Deaths','Cumulative Deaths per Capita']
calculated_df.to_csv('JHU_Calculated.csv') #I want to name by date somehow (ugh gotta extract from original csv)

#test    
print(calculated_df.head())
print(calculated_df.index)




