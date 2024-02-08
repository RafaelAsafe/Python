from httpx import Client

poke = 'ivysaur'

with Client(base_url='https://pokeapi.co/api/v2/') as client:

    response = client.get(f'/pokemon/{poke}')
    poke_id = response.json().get('id')

    print(poke_id)

    response = client.get(f'/pokemon-species/{poke_id}')
    evolution_chain = response.json().get('evolution_chain').get('url')

    response = client.get(evolution_chain)

    evolution_name = response.json().get('chain').get(
        'evolves_to')[0].get('species').get('name')

    print(evolution_name)