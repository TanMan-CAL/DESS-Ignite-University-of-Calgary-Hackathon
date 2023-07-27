
import csv
import random

with open('patients.csv', 'w', newline = '') as file:
	new = csv.writer(file)
	used = []

	while len(used) < 100:
		f_name = ['Max', 'John', 'Steve', 'Elizabeth', 'Cathy', 'Karen', 'Robert']
		l_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BA', 'CA', 'DA', 'EA', 'FA', 'GA', 'HA', 'IA', 'JA', 'KA', 'LA', 'MA', 'NA', 'OA', 'PA', 'QA', 'RA', 'SA', 'TA', 'UA', 'VA', 'WA', 'XA', 'YA', 'ZA', 'AB', 'BB', 'CB', 'DB', 'EB', 'FB', 'GB', 'HB', 'IB', 'JB', 'KB', 'LB', 'MB', 'NB', 'OB', 'PB', 'QB', 'RB', 'SB', 'TB', 'UB', 'VB', 'WB', 'XB', 'YB', 'ZB', 'AC', 'BC', 'CC', 'DC', 'EC', 'FC', 'GC', 'HC', 'IC', 'JC', 'KC', 'LC', 'MC', 'NC', 'OC', 'PC', 'QC', 'RC', 'SC', 'TC', 'UC', 'VC', 'WC', 'XC', 'YC', 'ZC']

		gender = ['Male', 'Female']
		date_l = ['2007-02-02', '2013-11-24', '2002-09-13', '1986-01-30', '2006-09-26']
		occupation = ['Doctor', 'Lawyer', 'Mechanic', 'Accountant']
		addresses = ['202 Auburn Bay', '47 Nolan Hills', '1110 Cranston', '64 Evergreen', '24 Walden']

		


		first = random.choice(f_name)
		last = random.choice(l_name)
		sector = random.randint(1, 5)
		gen = random.choice(gender)
		birth = random.choice(date_l)
		occ = random.choice(occupation)
		add = random.choice(addresses)

		if last not in used:
			data = [first, last, gen, add, sector, birth, occ]
			used.append(last)
				
			new.writerow(data)
		

