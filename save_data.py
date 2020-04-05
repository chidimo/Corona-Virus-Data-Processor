import csv
import requests
from contextlib import closing

from mongoengine import connect, disconnect, StringField, IntField, ReferenceField, DateField, Document
from utils import country_codes, setup_logger

logger = setup_logger('log.log')
disconnect()
connect(db='corona', host='mongodb+srv://primary:JYfLLsBVc3LgkPmx@coronacluster-0g0lt.gcp.mongodb.net/corona')
logger.info('\n\n\n*******Starting a new run *******\n')
logger.info('Database connection successfully established\n')

class Countries(Document):
  name = StringField()
  short_name = StringField()

class Cases(Document):
  new_cases = IntField(default=0)
  new_deaths = IntField(default=0)
  total_cases = IntField(default=0)
  total_deaths = IntField(default=0)
  country = ReferenceField(Countries)
  recordDate = DateField(required=True)
  country_name = StringField(required=True)

def save_countries_to_db(countries):
  print('Saving countries')
  for name in countries:
    if name == 'location':
      pass
    if name == 'International':
        pass
    short_name = country_codes.get(name.upper(), '')
    try:
      Countries.objects(name=name).modify(name=name, short_name=short_name, upsert=True)
    except Exception as err:
      logger.info(name)
      logger.debug(f'{err}/n')
  logger.info('Countries saved successfully\n\n')

def save_data_to_db(data_list):
  print('Saving data')
  for row in data_list:
    try:
      country = Countries.objects(name=row[1]).get()
    except Exception as err:
      logger.info(row[1])
      logger.debug(f'{err}\n')

    try:
      Cases.objects(
        recordDate=row[0], country=country,
      ).modify(
        upsert=True, recordDate=row[0], country=country, country_name=row[1],
        new_cases=row[2], new_deaths=row[3], total_cases=row[4], total_deaths=row[5],
      )
    except Exception as err:
      logger.info(country.name)
      logger.debug(f'{err}\n')
  logger.info('Done saving data\n\n')

url = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'

countries = set()
data_list = []

with closing(requests.get(url)) as r:
  f = (line.decode('utf-8') for line in r.iter_lines())
  reader = csv.reader(f)
  for row in reader:
    countries.add(row[1])
    if row[0] == 'date':
      pass
    else:
      data_list.append(row)

save_countries_to_db(countries)
save_data_to_db(data_list)
