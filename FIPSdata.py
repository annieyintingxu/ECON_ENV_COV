import csv
import statistics

# create dictionary with every county FIPS mapped to county name
# file being read contains county FIPS code matched to county name
# from https://www.dshs.texas.gov/chs/info/info_txco.shtm
with open('FIPSlist.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    FIPS_list = {}                  # dictionary of all Texas counties (FIPS key, county name value)
    for row in reader:
        if line_count == 0:
            line_count += 1
        else:
            FIPS_list[48000+int(row[1])] = row[0][:-1][1:] # get rid of beginning and ending whitespaces

# from Harvard's US county data, if the county is in Texas, record its 2000-2016 pm levels in a list
# file being read is Harvard's master list of PM2.5 levels for most American counties from 2000-2016
# from https://github.com/wxwx1993/PM_COVID/blob/master/Data/county_pm25.csv
with open('pm25data.csv') as csv_file1:
    texas_FIPS = {}         # dictionary of 2000-2016 PM values in list (value) for Texas counties (FIPS key)
    reader1 = csv.reader(csv_file1, delimiter=',')
    for row in reader1:
        fips = int(row[0])
        pm25 = row[2]
        if fips in FIPS_list:
            if fips not in texas_FIPS:      # create list if first encounter of FIPS
                texas_FIPS[fips] = []
            texas_FIPS[fips].append(float(pm25))

# check if any FIPS don't have 17 years of values (2000-2016 inclusive)
# result: they all have 17
for i in texas_FIPS:
    if len(texas_FIPS[i]) != 17:
        print(str(i) + ': ' + str(len(texas_FIPS[i])))

# replace list of all recorded values with 2000-2016 average (average of list) in each entry of texas_FIPS
for i in texas_FIPS:
    texas_FIPS[i] = statistics.mean(texas_FIPS[i])

# write Texas FIPS 2000-2016 PM2.5 levels
with open('texasFIPS.csv', mode='w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["FIPS", "County", "2000-2016 avg"])
    for i in sorted(texas_FIPS):
        csv_writer.writerow([i, FIPS_list[i], texas_FIPS[i]])



