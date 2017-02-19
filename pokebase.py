 # -*- coding: utf-8 -*-

import json
import os

import requests


BASE_URL = 'http://pokeapi.co/api/v2'
CACHE = os.path.join(os.path.expanduser('~'), '.pokebase')
if not os.path.exists(CACHE):
    os.makedirs(CACHE)

    
def lookup_data(sub_dir, name):

    cwd = os.getcwd()
    os.chdir(CACHE)

    if not os.path.exists(sub_dir):
        lookup_resource(sub_dir)

    os.chdir(sub_dir)

    if isinstance(name, int):
        name = str(name)

    if os.path.exists('.'.join([name, 'json'])):
        with open('.'.join([name, 'json']), 'r') as file:
            data = json.load(file)
    else:
        r = requests.get('/'.join([BASE_URL, sub_dir, name]))
        r.raise_for_status()
        data = json.loads(r.text)
        with open('.'.join([name, 'json']), 'w') as file:
            json.dump(data, file, indent=2)

    os.chdir(cwd)
    return data


def lookup_resource(name):

    cwd = os.getcwd()
    os.chdir(CACHE)

    if os.path.exists(name):
        os.chdir(name)

        with open('resource.json', 'r') as file:
            resource = json.load(file)

    else:
        os.mkdir(name)
        os.chdir(name)

        url = '/'.join([BASE_URL, name])
        r = requests.get(url)
        r.raise_for_status()
        resource = json.loads(r.text)

        if resource['count'] != len(resource['results']):
            items = resource['count']
            url = '/'.join([BASE_URL, name, '?limit={}'.format(items)])

            r = requests.get(url)
            r.raise_for_status()
            resource = json.loads(r.text)

        with open('resource.json', 'w') as file:
            json.dump(resource, file, indent=2)

    os.chdir(cwd)
    return resource


def make_obj(d):
    
    if 'url' in d.keys():
        url = d['url']
        name = url.split('/')[-2]
        location = url.split('/')[-3]
        return NamedAPIResource(location, name, False)
    else:
        return APIMetadata(d)
    

class NamedAPIResource:

    def __init__(self, resource, name, lookup=True):
        
        r = resource.replace(' ', '-').lower()
        n = APIResourceList(r).id_to_name(name)
        
        self.__data = {'type': r, 'name': n,
               'url': '/'.join([BASE_URL, r, n])}
        
        if lookup:
            self.load()
            self.__isloaded = True
        else:
            self.__isloaded = False
            
    def __getattr__(self, attr):
        
        if not self.__isloaded:
            self.load()
            self.__isloaded = True
            
            return self.__getattribute__(attr)
        
        else:
            raise AttributeError(f'{type(self)} object has no attribute {attr}')
    
    def __str__(self):
        return f'{self.name}'
        
    def load(self):
        
        self.__data.update(lookup_data(self.__data['type'], self.__data['name']))

        for k, v in self.__data.items():
            
            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))
                
            elif isinstance(v, list):
                self.__setattr__(k, [make_obj(i) for i in v])
            else:
                self.__setattr__(k, v)
        
        self.__isloaded = True

        
class APIResourceList:

    def __init__(self, name):

        response = lookup_resource(name)

        self.__results = [i for i in response['results']]
        self.count = response['count']

    def __len__(self):
        return self.count
        
    def __iter__(self):
        return self.__results
    
    def __str__(self):
        return str(self.__results)
    
    def id_to_name(self, id_):
        for res in self.__results:
            if res.get('name', res['url'].split('/')[-2]) == id_:
                return id_
            if res['url'].split('/')[-2] == str(id_):
                return res.get('name', res['url'].split('/')[-2])


    @property
    def names(self):
        for result in self.__results:
            yield result.get('name', result['url'].split('/')[-2])

    @property
    def urls(self):
        for result in self.__results:
            yield result['url']

            
class APIMetadata:

    def __init__(self, data):
        self.__data = data
        
        for k, v in self.__data.items():
            
            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))
            else:
                self.__setattr__(k, v)
                
    def __str__(self):
        return str(self.__data)
            