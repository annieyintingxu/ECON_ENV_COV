import pandas as pd #hm cannot find pandas module. I need to download it. 
                    #Import just means import someth that is stored in VSCode. Apparently, I should use
                    #itertuples or vectorized or someth else, see pandas.pydata.org instead of iterrows,
                    #but I'll just use itertuples

#county name in 1st entry
#county population size in 2nd entry
#daily new death count starting 3rd entry                
'''
what I want to do:
- run county by county. Only 1 file, so I guess this just means row by row
- make a different list for each county. So, append values into a list? Maybe this is overly complicated for
  such a simple program
- sum deaths for each county up to the latest date, and return that as the total death count.
- divide total death count for each county by population, return as the deaths per capita
- store outputs as csv with, for each county, county name, total deaths, and deaths per capita
'''
JHU_df = pd.read_csv('/Users/Dino-Sunlight/Desktop/COVIDee/JHU Texas COVID-19 Case Count Data by County - Cases by County.csv') #loads data
columns = list(JHU_df) #hm what am I doing here
county_total_deaths = 0
county_total_deaths_per_capita = 0
line_count = 0
column_number = 0

def total_average(county): #helper function to find total deaths per county and total deaths per capita from 3/4/20 up to 9:30 am CST
                    # forlatest date in file
    county_data = []
    #for row in JHU_df.itertuples(): #hm do I need this? damn I'm so confused
        if row[3] != 0 #is this does 'not equal'?
            return
        else:
            county_name = row[1]
            #county_total_deaths = county_name + "_total deaths"
            for i in columns: #I want to work from 3rd column onwards
                column_number = i + 2 #to start adding at 3rd column
                for column_number <=: #___total number of columns___
                    county_total_deaths += row[column_number] #add the death value in the next column, starting at the 3rd column
            county_total_per_capita = county_total_deaths / row[2]
            county_data.append(county_total_deaths)
            county_data.append(county_total_per_capita)
            #now I want to store these three -- county_name, county_total deaths, and county_total_per_capita
            #and then keep going
            
            



