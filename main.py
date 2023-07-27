#classic example of why comments are needevto explain whatcthe code is supposed to do
import csv
from datetime import date


class vaccines_fileCSV_read:
	def __init__(self, vaccines_file):
		self.__vaccines_file = vaccines_file
		self.__vaccines_dict = {}
	

	def opening_vaccinesCSV_file(self):
		with open(self.__vaccines_file, 'r') as vaccines_file:
			csvReader_vaccines = csv.reader(vaccines_file, delimiter = ',')
			line_count = -1

			for row in csvReader_vaccines:
				line_count += 1

				if line_count != 0:
					self.__vaccines_dict[row[0]] = [int(row[1]), str(row[2]).lower()]
		

	def returning_dict(self):
		return self.__vaccines_dict




class patients_fileCSV_read:
	def __init__(self, patients_file):
		self.__patients_file = patients_file
		self.__patients_dict = {}

	
	def opening_patientsCSV_file(self):
		with open(self.__patients_file, 'r') as patients_file:
			csvReader_patients = csv.reader(patients_file, delimiter = ',')
			line_count = -1
			
			for row in csvReader_patients:
				line_count += 1

				if line_count != 0:
					self.__patients_dict[(str(row[1]).lower())] = [str(row[0]).lower(), str(row[1]).lower(), int(row[4]), str(row[5]).lower(), str(row[6]).lower()]


	def returning_dict_pat(self):
		return self.__patients_dict


class distribution_centres_fileCSV_read:
	def __init__(self, distribution_centres_file):
		self.__distribution_centres_file = distribution_centres_file
		self.__distribution_centres_dict = {}


	def opening_distribution_centresCSV_file(self):
		with open(self.__distribution_centres_file) as distribution_centres:
			csvReader_distribution = csv.reader(distribution_centres, delimiter = ',')
			line_count = -1
				
			for row in csvReader_distribution:
				line_count += 1

				if line_count != 0:
					self.__distribution_centres_dict[(str(row[0]).lower())] = [int(row[1]), int(row[2]), int(row[3]), int(row[4])]


	def returning_dict_distrib(self):
		return self.__distribution_centres_dict
			



class distribution_CITY:
	def __init__(self, patients, distribution_centres, vaccines_dict):
		self.__patients_dict = patients
		self.__distribution = distribution_centres
		self.__vaccines_dict = vaccines_dict


	def delivery(self):
		for k, v in self.__vaccines_dict.items():
			self.__date_of_arrival = k
			self.__doses = v[0]
			self.__manufacturer = v[1]

		print(f'{self.__manufacturer.upper()} delivered {self.__doses} vaccines on {self.__date_of_arrival}.\n')
	

	def sector(self):
		sector1 = 0
		sector2 = 0
		sector3 = 0
		sector4 = 0
		sector5 = 0

		for value in self.__patients_dict.values():
			sector = value[2]
			
			if sector == 1:
				sector1 += 1
							
			elif sector == 2:
				sector2 += 1
			
			elif sector == 3:
				sector3 += 1
			
			elif sector == 4:
				sector4 += 1
			
			elif sector == 5:
				sector5 += 1
			
		print(f'Residents In Each Sector')
		print(f'Sector 1: {sector1}')
		print(f'Sector 2: {sector2}')
		print(f'Sector 3: {sector3}')
		print(f'Sector 4: {sector4}')
		print(f'Sector 5: {sector5}\n \n')

		print('Residents Who Did Not Get A Vaccine')
		print(f'Sector 1: {int(sector1 - (int(self.__doses)) / 5)}')
		print(f'Sector 2: {int(sector2 - (int(self.__doses)) / 5)}')
		print(f'Sector 3: {int(sector3 - (int(self.__doses)) / 5)}')
		print(f'Sector 4: {int(sector4 - (int(self.__doses)) / 5)}')
		print(f'Sector 5: {int(sector5 - (int(self.__doses)) / 5)}')


			

def main():
	#opening the vaccines.csv file
	vaccines = vaccines_fileCSV_read('vaccines.csv')
	vaccines.opening_vaccinesCSV_file()
	vaccines_dict = vaccines.returning_dict()


	#opening the patients.csv file
	patients = patients_fileCSV_read('patients.csv')
	patients.opening_patientsCSV_file()
	patients_dict = patients.returning_dict_pat()

	#opening distribution_centres.csv file
	centres = distribution_centres_fileCSV_read('distribution_centres.csv')
	centres.opening_distribution_centresCSV_file()
	distribution_centres = centres.returning_dict_distrib()
	
	#passing the global variable to put distribution into action
	distribution = distribution_CITY(patients_dict, distribution_centres, vaccines_dict)
	distribution.delivery()
	distribution.sector()

main()


