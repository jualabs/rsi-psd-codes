import requests
import configparser
import json

class climaNaEstrada():

    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
        
        config = configparser.ConfigParser()
        config.sections()
        config.read('.key.api')
        self.key=config["keys"]["googleapi"]
    
    def getGoogleDirections(self):
        url = 'https://maps.googleapis.com/maps/api/directions/json'
    
        params = dict(
            origin=self.origem,
            destination=self.destino,
            language='pt-BR',
            key=self.key
        )
    
        #Obtem dados da rota entre as cidades
        resp = requests.get(url=url, params=params)
        
        if resp.status_code == 200:
            return json.loads(resp.text)
        else:
            return "error"

    def getNearStation(self,lat,lng):
        url = 'http://api.geonames.org/findNearByWeatherJSON'
    
        params = dict(
            username='glaucogoncalves',
            lat=lat,
            lng=lng
        )
        
        #Obtem dados sobre o clima
        resp = requests.get(url=url, params=params)
        
        return json.loads(resp.text)
        
    def getLocation(self,lat,lng):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
    
        params = dict(
            latlng=lat+","+lng,
            language='pt-BR',
            result_type="country|administrative_area_level_1|administrative_area_level_2",
            key=self.key
        )
        
        #Obtem dados sobre o clima
        resp = requests.get(url=url, params=params)
        
        respjson = json.loads(resp.text)
        
        try:
            shortAddress = map(lambda address: address['short_name'], respjson['results'][0]['address_components'])
        except:
            print(respjson)
            shortAddress = []
        return tuple(shortAddress)


    def resolve(self):
    
        directions = self.getGoogleDirections()
        
        observations = {}
        cities = {}
            
        for route in directions['routes']:
            cnt = 0
            leg = route['legs'][0]
            for step in leg['steps']:
                lat = step['start_location']['lat']
                lng = step['start_location']['lng']
                city = self.getLocation(str(lat),str(lng))
                if len(city) == 3 and not city in cities:
                    cnt += 1
                    cities[city]=1
                    clima = self.getNearStation(lat,lng)
                    try:
                        observations[(cnt,city)]=(clima['weatherObservation']['temperature'],clima['weatherObservation']['humidity'])
                    except:
                        print(clima)
            
        return(observations)

if __name__ == '__main__':
    observacoes = climaNaEstrada('recife', 'natal')
    print(sorted(observacoes.resolve()))
    
    