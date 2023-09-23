# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

import pandas as pd
import pprint

from faker import Faker

fake = Faker()

Faker.seed(0)
#for _ in range(10):
#    pprint.pprint(fake.simple_profile())

data = [
{'address': '9382 Taylor Court Suite 892\nCoreyland, MH 90152',
 'birthdate': "1950, 10, 4",
 'mail': 'thomas15@yahoo.com',
 'name': 'Jason Green',
 'sex': 'M',
 'username': 'ysullivan'},
{'address': '753 Padilla Circles\nNew Jeffrey, AS 19178',
 'birthdate': "1974, 4, 25",
 'mail': 'udavis@hotmail.com',
 'name': 'Mrs. Sharon Green',
 'sex': 'F',
 'username': 'davismary'},
{'address': 'USNV Wallace\nFPO AP 50950',
 'birthdate': "2019, 7, 11",
 'mail': 'barbara42@gmail.com',
 'name': 'Doris Martinez',
 'sex': 'F',
 'username': 'lisa83'},
{'address': '86848 Melissa Springs\nRileymouth, NM 87040',
 'birthdate': "1987, 8, 16",
 'mail': 'christopher91@yahoo.com',
 'name': 'Vicki Green',
 'sex': 'F',
 'username': 'daviskatherine'},
{'address': '12309 Anthony Roads Apt. 991\nDavisville, AZ 79865',
 'birthdate': "1924, 8, 1",
 'mail': 'leetara@hotmail.com',
 'name': 'David Dennis',
 'sex': 'M',
 'username': 'thorntonnathan'},
{'address': '14562 William Canyon\nLake Vanessaborough, KS 47497',
 'birthdate': "2002, 9, 5",
 'mail': 'kmassey@gmail.com',
 'name': 'Robert Giles',
 'sex': 'M',
 'username': 'stephenschristine'},
{'address': 'PSC 2076, Box 9845\nAPO AA 86696',
 'birthdate': "1918, 6, 26",
 'mail': 'eric07@hotmail.com',
 'name': 'Mrs. Megan Bruce',
 'sex': 'F',
 'username': 'alyssa19'},
{'address': '466 Aaron Fields\nErnestbury, SC 59238',
 'birthdate': "1964, 2, 15",
 'mail': 'rpage@hotmail.com',
 'name': 'Joshua Taylor',
 'sex': 'M',
 'username': 'sbell'},
{'address': '789 Nicole Park Suite 470\nLopezland, MP 95600',
 'birthdate': "1964, 7, 17",
 'mail': 'valeriemorales@hotmail.com',
 'name': 'Mia Barnes',
 'sex': 'F',
 'username': 'martincaleb'},
{'address': '2176 Andrew Mission Apt. 428\nDarinberg, KY 02935',
 'birthdate': "1950, 7, 22",
 'mail': 'williamserin@hotmail.com',
 'name': 'Adrian Fischer',
 'sex': 'M',
 'username': 'leecharlene'}
]

name_dict = {'name': [record['name'] for record in data]}
sex_dict = {'sex': [record['sex'] for record in data]}
username_dict = {'username': [record['username'] for record in data]}
birthdate_dict = {'birthdate': [record['birthdate'] for record in data]}


print(name_dict)
print(sex_dict)
print(username_dict)
print(birthdate_dict)

df = pd.DataFrame(
    {
     name_dict,
     sex_dict,
     username_dict,
     birthdate_dict
    }
)