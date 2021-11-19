#!/usr/bin/env python3

# new students rearrangement script (version 1)

import pandas as pd
from datetime import datetime
import os

# opens the original file, and populates a variable for the term, and adds the missing columns to the DataFrame - the term will change depending on which term the script is running. Pkus, the file name means nothing. It can be anything. 
term = '4218'
nwstudents = pd.read_excel('/Users/jelambe/OneDrive - Indiana University/Documents/NewStudents.xlsx', dtype = str)
nwstudents.drop(["EmailID"], axis=1, inplace=True)
# creating the missing columns
nwstudents['Term Code'] = term
nwstudents['LSAC'] = ''
nwstudents['MiddleName'] = ''
nwstudents['AKA'] = ''
nwstudents['Sex'] = ''
nwstudents['Birthdate'] = ''
nwstudents['Ethnicity'] = ''

#writing all the columns to a temp csv document
nwstudents.to_csv('newstudentspd.csv', index=False)

# opening that temp csv file with the columns in correct order
nwstudents = pd.read_csv('newstudentspd.csv', converters={'IUID': lambda x: str(x)}) [['Term Code', 'IUID', 'LSAC', 'LastName', 'FirstName', 'MiddleName', 
	'AKA', 'Sex', 'Birthdate', 'Ethnicity', 'ProgramCode', 'Email']]

# writing the final XLSX with a date-stamped filename
filename = datetime.now().strftime("%Y%m%d")
nwstudents.to_excel('NewStudents' + '-' + filename + '-' + term + '.xlsx', index=False)
# removing the temp file
os.remove('newstudentspd.csv')
# printing the final statement that the script ran
print('new students populated')
