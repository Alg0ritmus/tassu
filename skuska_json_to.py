# P.Z. Tassu ci jak

# https://docs.python.org/3/library/csv.html
# https://pandas.pydata.org/docs/

import csv
import pandas as pd



def JSON_to_CSVfile(my_json,name_of_output_file="out"):
	with open(name_of_output_file+".csv","a", newline="") as f:
		writer= csv.writer(f)

		metadate_temp_touple = ()
		for i in my_json["Data"][0]:
			metadate_temp_touple += (i,)
		writer.writerow(metadate_temp_touple)


		for faktura in my_json["Data"]:
			temp_touple = ()
			for i in faktura:
				temp_touple += (faktura[i],)

			writer.writerow(temp_touple)


def CSVfile_to_Excelfile(CSVfilename):
	

	filename = CSVfilename+".csv"
	excel_filename = CSVfilename+"_excel.xlsx"

	read_file = pd.read_csv (filename, encoding = "ISO-8859-1")
	read_file.to_excel (excel_filename, index = None, header=True)

