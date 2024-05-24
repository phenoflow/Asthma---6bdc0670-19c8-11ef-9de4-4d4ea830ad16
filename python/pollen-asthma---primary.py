# Evangelos Kontopantelis, Ivan Olier, Claire Planner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Sioban Reilly, 2024.

import sys, csv, re

codes = [{"code":"H330.14","system":"readv2"},{"code":"493 GS","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pollen-asthma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pollen-asthma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pollen-asthma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
