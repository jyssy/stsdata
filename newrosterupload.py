# new student rosters script for STS new student upload each semester (usually handled by OSA)

import csv
import pandas as pd
from datetime import datetime
import os
import re

# opening the original extracted text file (renamed with the term added), using regex, and writing that new data to a temp csv file that will be deleted at the end of the script by running os.remove()
with open('extract_14987005-4228.txt', 'r') as extracted:
	filetxt = str(extracted)
	termc = re.findall(r'[0-9]{4}', filetxt)
	termcode = (termc[2])
	extractreader = csv.reader(extracted, delimiter='\t')
	with open('newextract.csv', 'w') as newextract:
		extractwriter = csv.writer(newextract, delimiter=',')
		for line in extractreader:
			extractwriter.writerow(line)
# the section in which pandas selects the necessary columns from the csv
#newextractpd = pd.read_csv('newextract.csv', dtype = str) 
#OR -- if we apply the dtype=str ONLY to specific columns and not ao ALL the columns as the line does above:
newextractpd = pd.read_csv('newextract.csv', converters={'University ID': lambda x: str(x)}) [['Term Code', 'Units Taken', 'Primary Program Code',
	'Class Number', 'Subject Area', 'Course Catalog Number',
	'Course Description', 'Official Grade', 'University ID',
	'Enrollment Status Code', 'Instructor Name', 'Preferred Full Name']]
# 'Preferred Full Name' needs to be 'Primary Full Name' in the final document
newextractpd.rename(columns={"Preferred Full Name":"Primary Full Name"}, inplace=True)
# adding a space after the comma
newextractpd['Primary Full Name'] = newextractpd['Primary Full Name'].str.replace(', *', ', ', regex=True)
newextractpd['Instructor Name'] = newextractpd['Instructor Name'].str.replace(', *', ', ', regex=True)
# writing all tha data to the XLSX according to the template
filedate = datetime.now().strftime("%Y%m%d")
newextractpd.to_excel('NewRosterUpload' + '-' + filedate + '-' + termcode + '.xlsx', index=0)
# removing the temporary csv document
os.remove('newextract.csv')
# final check is a print if all has run as expected
print('roster populated')



