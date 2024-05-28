# Romi Haas, Ljoudmila Busija, Alexandra Gorelik, Denise A O'Connor, Christopher Pierce, Danielle Mazza, Rochelle Buchbinder, 2024.

import sys, csv, re

codes = [{"code":"38341003","system":"snomedct"},{"code":"59621000","system":"snomedct"},{"code":"276789009","system":"snomedct"},{"code":"50490005","system":"snomedct"},{"code":"64715009","system":"snomedct"},{"code":"70272006","system":"snomedct"},{"code":"56218007","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertensive-cardiovascular-comorbidities---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertensive-cardiovascular-comorbidities---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertensive-cardiovascular-comorbidities---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
