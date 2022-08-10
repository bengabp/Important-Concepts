"""Lambdas and Map/Filter/Reduce functions"""

from pprint import pprint
from functools import reduce

"""Lambdas are single line functions"""

my_single_line_function = lambda a: a * 8
print(my_single_line_function(9))

my_mad_single_line_function = lambda a: 9 * (lambda b: b + 1).__call__(9)
print(my_mad_single_line_function(6),"\n")

"""Map"""

beautiful_cities = [
    {'name': 'USA', 'is_english_speaking': None},
    {'name': 'China', 'is_english_speaking': None},
    {'name': 'Japan', 'is_english_speaking': None},
    {'name': 'Korea', 'is_english_speaking': None},
    {'name': 'Canada', 'is_english_speaking': None},
    {'name': 'Germany', 'is_english_speaking': None},
    {'name': 'Italy', 'is_english_speaking': None},
]

non_english_speaking_countries = ['china', 'korea', 'japan']

# Now lets modify our list of beautiful cities accordingly using a map
beautiful_cities_map = map(lambda city: {
    'name':city['name'],
    'is_english_speaking':True if city['name'].lower() not in non_english_speaking_countries else False
} , beautiful_cities)

all_countries = list(beautiful_cities_map)
print("All countries")
pprint(all_countries)

country_names = [country.get('name') for country in all_countries]

""" Filter """
# Let us use filter to filter out non english speaking countries
only_english_speaking_countries = filter(lambda cname:cname.lower() not in non_english_speaking_countries, country_names)
print("\n",f"Only english speaking countries --> {list(only_english_speaking_countries)}")

# """ Reduce """
# sum_of_only_english_speaking_countries_names = reduce(lambda name1,name2:name1[1]+name2[1],country_names)
# print(sum_of_only_english_speaking_countries_names)