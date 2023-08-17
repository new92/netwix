"""
Author: new92
Github: @new92
Leetcode: @new92
"""
import json
import requests
from bs4 import BeautifulSoup
from netwix.exceptions import NetwixValidationError

class Series:
    def __init__(self, seriesid: int):
        self.seriesid = str(seriesid)
        self.type = None
        self.name = None
        self.description = None
        self.url = f'https://www.netflix.com/watch/{self.seriesid}'
        self.contentRating = None
        self.genre = None
        self.imgUrl = None
        self.startDate = None
        self.creationDate = None
        self.awards = None
        self.seasons = None
        self.actors = []
        self.creators = []
        self.directors = []
    
    def fetchData(self):
        response = requests.get(f'https://www.netflix.com/watch/{self.seriesid}')
        soup = BeautifulSoup(response.content, 'html.parser')
        meta = json.loads((soup.find('script', type='application/ld+json')).string)
        self.type = meta['@type']
        if self.type != 'TVSeries':
            raise NetwixValidationError
        self.name = meta['name']
        self.description = meta['description']
        self.contentRating = meta['contentRating']
        self.genre = meta['genre']
        self.imgUrl = meta['image']
        self.creationDate = meta['dateCreated']
        if 'startDate' in meta:
            self.startDate = meta['startDate']
        self.actors = [meta['actors'][i]['name'] for i in range(len(meta['actors']))]
        self.creators = [meta['creator'][i]['name'] for i in range(len(meta['creator']))]
        if meta['director'] != []:
            self.directors = [meta['director'][i]['name'] for i in range(len(meta['director']))]
        if meta['awards']:
            self.awards = meta['awards']
        if meta['numberOfSeasons']:
            self.seasons = meta['numberOfSeasons']

class Movies:
    def __init__(self, movieid: int):
        self.movieid = str(movieid)
        self.type = None
        self.name = None
        self.description = None
        self.url = f'https://www.netflix.com/watch/{self.movieid}'
        self.contentRating = None
        self.genre = None
        self.imgUrl = None
        self.awards = None
        self.startDate = None
        self.creationDate = None
        self.actors = []
        self.creators = []
        self.directors = []
        self.trailer = []

    def fetchData(self):
        response = requests.get(f'https://www.netflix.com/watch/{self.movieid}')
        soup = BeautifulSoup(response.content, 'html.parser')
        meta = json.loads((soup.find('script', type='application/ld+json')).string)
        self.type = meta['@type']
        if self.type != 'Movie':
            raise NetwixValidationError
        self.name = meta['name']
        self.description = meta['description']
        self.contentRating = meta['contentRating']
        self.genre = meta['genre']
        self.imgUrl = meta['image']
        self.creationDate = meta['dateCreated']
        self.actors = [meta['actor'][i]['name'] for i in range(len(meta['actor']))]
        if meta['creator'] != []:
            self.creators = [meta['creator'][i]['name'] for i in range(len(meta['creator']))]
        if meta['director'] != []:
            self.directors = [meta['director'][i]['name'] for i in range(len(meta['director']))]
        if meta['trailer']:
            self.trailer = [meta['trailer'][i]['contentUrl'] for i in range(len(meta['trailer']))]
        if 'awards' in meta:
            self.awards = meta['awards']
        if 'startDate' in meta:
            self.startDate = meta['startDate']
