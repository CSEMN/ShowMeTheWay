import csv

with open('names.csv','w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
data=list()
with open('names.csv','r') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append({'first_name':row['first_name']})
    print(data)


with open('names.csv','w') as csvfile:
    fieldnames = ['first_name']

    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)