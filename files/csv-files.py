import csv

with open('my_new_file.csv', 'w') as csv_file:
  spamwriter = csv.writer(csv_file, delimiter=',')
  spamwriter.writerow(['one', 'two', 'three'])
  spamwriter.writerow(['four', 'five', 'six'])