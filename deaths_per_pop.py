import pandas as pd 
#county name in col 0
#county population size in col 1
#daily new death count starting col 2               
'''
what I want to do:
- run county by county. Only 1 file, so I guess this just means row by row
- make a different list for each county. So, append values into a list? Maybe this is overly complicated for
  such a simple program
- sum deaths for each county up to the latest date, and return that as the total death count.
- divide total death count for each county by population, return as the deaths per capita
- store outputs as csv with, for each county, county name, total deaths, and deaths per capita

what I don't know to do:
- create a dataframe in pandas
- convert dataframe to a csv: https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
- less than or equal to
- the number of columns in a dataframe
'''
JHU_df = pd.read_csv('/Users/Dino-Sunlight/Desktop/COVIDeeDesktop/Texas COVID-19 Fatality Count Data by County 6_15_20.csv') #loads data
#columns = list(JHU_df) #hm what am I doing here
print(JHU_df.shape) #okay it is recognizing the number of columns
#print(JHU_df.row[3])
county_total_deaths = 0
county_total_deaths_per_capita = 0
#JHU_df.columns

#def total_and_per_capita_deaths(): #not sure if I need function and 'for' row...anyways, helper function to find total deaths per county and total deaths per capita from 3/4/20 up to 9:30 am CST
                    # forlatest date in file
county_data = {}
for row in JHU_df.itertuples(): #calculates and stores the total and per capita for each row in the dataframe. Can I just use "JHU_df"??
    #if row[3] != 0: #starts at first row with death counts. I guess I could also load county names.
        #do I need to have something after my if statement?
    if row[0] == 0:
        county_name = row[1] #stores the county name the row we're currently working with
        #county_total_deaths = county_name + "_total deaths"
        for i in JHU_df.columns: #works through each column in the row.
            if i > 1: #want to work from 3rd column onwards
            #don't need this? if column_number <= len(county_data.columns): #sums for a given row, from the value in 3rd column to last. Once done with last, 
                county_total_deaths += row[column_number] #add the current value to the total death value in the next column, starting at the 3rd column
        county_total_per_capita = county_total_deaths / row[2] #calculates per capital for that row
        county_data[county_name] = [county_total_deaths, county_total_per_capita] #all stored for this row. Yay!
for county_name in consumption:
    print()
                
            #now I want to store these three -- county_name, county_total deaths, and county_total_per_capita into a dictionary
            #and then convert the dictionary to a csv once all row are done

            
            



