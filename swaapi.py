import random, requests, json


count = requests.get('https://swapi.co/api/people/')
count = count.json()
character_count = count['count']


def get_random_dude(character_count):
	api_url = requests.get(f'https://swapi.co/api/people/{random.randint (1, character_count)}')
	api_url = api_url.json()
	random_dude = api_url['name']
	return random_dude


def random_planets():
	count = requests.get('https://swapi.co/api/planets/')
	count = count.json()
	planet_count = count['count']
	api_url = requests.get(f'https://swapi.co/api/planets/{random.randint (1, character_count)}')
	api_url = api_url.json()
	random_planets  = api_url['name']
	return random_planets


first_character = get_random_dude(character_count)

print(
	f'{first_character} is a kind person.\n' 
	f'He likes talking to everybody and cheering them up:\n'
	f'when he talks to {get_random_dude(character_count)}, \n'
	f'he says that he loves spending time with them  and listening to music;\n'
	f'when he talks to {get_random_dude(character_count)} , he likes to remember all of the funny \n'
	f'situations they have been together in.All in all, {first_character}\n'
	f'is a kind person and he has really\n'
	f'earned a place on his planet {random_planets()}.\n'
)
