# Evangelos Kontopantelis, Ivan Olier, Claire Planner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Sioban Reilly, 2024.

import sys, csv, re

codes = [{"code":"H33z.11","system":"readv2"},{"code":"H47y000","system":"readv2"},{"code":"H33z.00","system":"readv2"},{"code":"H33zz00","system":"readv2"},{"code":"H332.00","system":"readv2"},{"code":"663V100","system":"readv2"},{"code":"663j.00","system":"readv2"},{"code":"H35y700","system":"readv2"},{"code":"1O2..00","system":"readv2"},{"code":"173c.00","system":"readv2"},{"code":"173d.00","system":"readv2"},{"code":"H33..00","system":"readv2"},{"code":"H334.00","system":"readv2"},{"code":"493 C","system":"readv2"},{"code":"493","system":"readv2"},{"code":"3052AT","system":"readv2"},{"code":"493 NA","system":"readv2"},{"code":"493 EP","system":"readv2"},{"code":"493 AE","system":"readv2"},{"code":"493 AA","system":"readv2"},{"code":"691 TM","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
