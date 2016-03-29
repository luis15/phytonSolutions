import csv
from collections import OrderedDict

with open('csv1.csv', 'rb') as f:
    r = csv.reader(f)
    dict2 = {row[0]: row[1:] for row in r}

with open('csv2.csv', 'rb') as f:
    r = csv.reader(f)
    dict1 = OrderedDict((row[0], row[1:]) for row in r)

result = OrderedDict()
for d in (dict1, dict2):
    for key, value in d.iteritems():
        result.setdefault(key, []).extend(value)

with open('csv_combined.csv', 'wb') as f:
    w = csv.writer(f)
    for key, value in result.iteritems():
        w.writerow([key] + value)