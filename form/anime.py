from anime_utils import load_anime

class Anime:
    def __init__(self, raw_anime):
        """
          >>> anime = Anime('A\\nTeen\\nSeries\\nAction\\nAdventure\\nFantasy')
          >>> anime.name
          'A'
          >>> anime.rating
          'Teen'
          >>> anime.type
          'Series'
          >>> anime.genres
          ['Action', 'Adventure', 'Fantasy']
        """
        raw_anime = raw_anime.strip()
        split_raw = raw_anime.split('\n')
    
        self.name = split_raw[0]
        self.rating = split_raw[1]
        self.type = split_raw[2]
        self.genres = split_raw[3:]

    def __str__(self):
        s = 'Name: {0}\n'.format(self.name)
        s += '    Rating: {0}\n'.format(self.rating)
        s += '    Type: {0}\n'.format(self.type)
        s += '    Genre: '
        for genre in self.genres[:-1]:
            s += '{0}, '.format(genre)
        s += '{0}\n'.format(self.genres[-1])

        return s

    def match(self, rating=None, type=None, genres=[]):
        """
          >>> anime = Anime('A\\nTeen\\nSeries\\nAction\\nAdventure\\nFantasy')
          >>> anime.match(rating='Teen')
          True
          >>> anime.match(rating='Teen', type='Movie')
          False
          >>> anime.match(rating='Teen', genres=['Action', 'Fantasy'])
          True
          >>> anime.match(rating='Teen', genres=['Action', 'Sports'])
          False
        """

        if rating and self.rating != rating:
            return False
        if type and self.type != type:
            return False
        for genre in genres:
            if genre not in self.genres and genres:
                return False
        else:
            return True



class Collection:
    def __init__(self, raw_anime_list):
        """
          >>> my_anime = Collection(load_anime('test2.dat'))
          >>> len(my_anime.anime)
          2
          >>> new_collection = Collection(load_anime('test3.dat'))
          >>> len(new_collection.anime)
          4
        """
        self.anime = []

        for raw_anime in raw_anime_list:
           self.anime.append(Anime(raw_anime)) 

    def __str__(self):
        s = ''
        for anime in self.anime:
            s += str(anime)
        return s

    def matching_anime(self):
        """
        """
        matches = []
        for anime in anime.match:
            matches.append(anime)

        return matches


        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
