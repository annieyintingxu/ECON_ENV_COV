import pandas as pd 
import math
#index in col 0 bc we converted the csv into a dataframe
#county name in col 1
#county population size in col 2
#daily new death count starting col 3               

#remove all rows that do not describe counties: can iterate from top and find total row and remove all else or iterate from bottom
def per_pop(df):
    name = "Deaths by Population: " + list(df.columns.values)[0] #extracts date of latest update from the name of first column
    name = name.replace("/","-")
    row_count = 0 #initializes row_count
    for row in df.itertuples(): #this line: makes each row of the csv a tuple and then names it "row." nested block: removes appendix rows. 
                                        #removes the second row and all after total
                                        #takes about 6 seconds to run through all rows
        if row[3] != "0" or row_count == math.inf: 
            df.drop(index = row[0], axis = 0, inplace = True)
        elif row[1] == "Total": #lol this is finally working
            row_count = math.inf
    #remove all but 1st, 2nd, and last columnn
    df.drop(df.columns.to_series()[2:(len(df.columns) - 1)], axis = 1, inplace = True) #assume that the index column is not counted as a column       

    #rename columns and covert to float
    df.columns = ['County','Total Population','Cumulative Deaths']
    df['Total Population'] = pd.to_numeric(df['Total Population'])
    df['Cumulative Deaths'] = pd.to_numeric(df['Cumulative Deaths'])

    #add columns that contains deaths per capita
    df.loc[:,"Cumulative Deaths per Million Population"] = (df.loc[:,'Cumulative Deaths']) / (df.loc[:,'Total Population']) * 1000000 #hmm I have to convert to float some other way

    #return this edited dataframe as a csv
    df.to_csv(name + '.csv') #change naming to the original name of the first column, first row

#run function with any csv.
TXD_df = pd.read_csv('/Users/Dino-Sunlight/Desktop/COVIDeeDesktop/Texas COVID-19 Fatality Count Data by County 6_15_20.csv') #loads data. LOL ok it takes the first row as column titles....great...





