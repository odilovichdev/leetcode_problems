import csv

# Legend_devinput = 3
fields = []
rows = []
with open('phone.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    fields = next(csv_reader)

    for row in csv_reader:
        rows.append(row)
    print("Total no. of rows: %d" % (csv_reader.line_num))

print('Field names are:' + ', '.join(field for field in fields))
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')
    

