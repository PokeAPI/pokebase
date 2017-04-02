import json
import os

import requests


BASE_URL = 'http://pokeapi.co/api/v2'
CACHE = os.path.join(os.path.expanduser('~'), '.pokebase')
if not os.path.exists(CACHE):
    os.makedirs(CACHE)

    
def lookup_data(sub_dir, name, force_reload=False):
    """Locates and saves a specific reference, and then returns the data.

    If the resource desired is already cached, this function will return the
    cached copy. However, data files can be forced to re-download using the
    force_reload parameter. Reference are saved to the user's home directory 
    in a folder "~/.pokebase".
    """

    cwd = os.getcwd()
    os.chdir(CACHE)

    # Create the data directory if it does not exist.
    if not os.path.exists(sub_dir):
        lookup_resource(sub_dir)
    
    # Go to that directory.
    os.chdir(sub_dir)

    # Some resources don't have names, so use their ID.
    if isinstance(name, int):
        name = str(name)

    if os.path.exists('.'.join([name, 'json'])) and not force_reload:
        # If the resources wanted already exists, load it from disk.

        with open('.'.join([name, 'json']), 'r') as file:
            data = json.load(file)
    else:
        # If it doesn't exist, go download and save the resources.
        r = requests.get('/'.join([BASE_URL, sub_dir, name]))
        r.raise_for_status()
        data = json.loads(r.text)
        with open('.'.join([name, 'json']), 'w') as file:
            json.dump(data, file, indent=2)

    os.chdir(cwd)  # Return to original working directory.
    return data


def lookup_resource(name, force_reload=False):
    """Returns a resource with all of the data references in the category.
    
    If the resource desired is already cached, this function will return the
    cached copy. However, data files can be forced to re-download using the
    force_reload parameter. Reference are saved to the user's home directory 
    in a folder "~/.pokebase".
    """

    cwd = os.getcwd()
    os.chdir(CACHE)

    if os.path.exists(name) and not force_reload:
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
            # We got multiple pages of results; we want ALL of them.
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
    """Takes a dictionary and returns a NamedAPIResource or APIMetadata.

    The names and values of the data will match exactly with those found 
    in the online docs at https://pokeapi.co/docsv2/ .
    """
    
    if 'url' in d.keys():
        url = d['url']
        name = url.split('/')[-2]      # Name of the data.
        location = url.split('/')[-3]  # Where the data is located.
        return NamedAPIResource(location, name, False)
    else:
        return APIMetadata(d)
    

class NamedAPIResource:
    """Core API class, used for accessing the bulk of the data.
    """

    def __init__(self, resource, name, lookup=True):
        
        r = resource.replace(' ', '-').lower()
        n = APIResourceList(r).id_to_name(name)
        
        self.__data = {'type': r, 'name': n,
                       'url': '/'.join([BASE_URL, r, n])}
        
        if lookup:
            self.load()
            self.__is_loaded = True
        else:
            self.__is_loaded = False
            
    def __getattr__(self, attr):
        
        if not self.__is_loaded:
            self.load()
            self.__is_loaded = True
            
            return self.__getattribute__(attr)
        
        else:
            t = type(self)
            raise AttributeError(f'{t} object has no attribute {attr}')
    
    def __str__(self):
        return f'{self.name}'
        
    def load(self):
        
        self.__data.update(lookup_data(self.__data['type'], 
                                       self.__data['name']))

        for k, v in self.__data.items():
            
            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))
                
            elif isinstance(v, list):
                self.__setattr__(k, [make_obj(i) for i in v])
            else:
                self.__setattr__(k, v)
        
        self.__is_loaded = True

        
class APIResourceList:
    """Class for a data container.

    Used to access data corresponding to a category, rather than an individual
    reference. Ex. APIResourceList('berry') gives information about all 
    berries, such as which ID's correspond to which berry names, and 
    how many berries there are.
    """

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
    """Helper class for smaller references.

    Used for "Common Models" classes and NamedAPIResource helper classes.
    https://pokeapi.co/docsv2/#common-models
    """

    def __init__(self, data):
        self.__data = data
        
        for k, v in self.__data.items():
            
            if isinstance(v, dict):
                self.__setattr__(k, make_obj(v))
            else:
                self.__setattr__(k, v)
                
    def __str__(self):
        return str(self.__data)
