import csv
import json

driver_reg = csv.reader(open('sample-data/one_driver_registration.csv', newline=''),
                        delimiter=',', quotechar='"')

attributes = ['id', 'date_created', 'date_last_modified', 'active_date', 'name',
              'phone', 'resign_date', 'resign_reason', 'status', 'tipe', 'area',
              'operator_id', 'modified_by', 'vehicle_type', 'helmet_qty',
              'jacket_qty', 'vehicle_brand', 'vehicle_year', 'bike_type',
              'first_ride_bonus_awarded', 'is_doc_completed']

for row_array in driver_reg:
  data = {}
  for i in range(len(row_array)):
    attribute = attributes[i]
    data[attribute] = row_array[i]
  print(json.dumps(data))
