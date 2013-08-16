from anime_utils import load_anime


def print_anime_list(list_of_anime):
    s = ''
    if list_of_anime:
        for anime in list_of_anime[:-1]:
            s += "{0}, ".format(anime)

        s += "{0}".format(list_of_anime[-1])

    return s


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
        return self.name


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
            if  genre not in self.genres:
                return False
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
        return str(self.anime)

    def matching_anime(self, rating=None, type=None, genres=[]):
        """
          >>> alist = ['A\\nTeen\\nSeries\\nAction\\nAdventure\\nFantasy']
          >>> anime = Collection(alist)
          >>> result = anime.matching_anime(rating='Teen', type='Movie')
          >>> print_anime_list(result)
          ''
          >>> result2 = anime.matching_anime(rating='Teen',
          ...                     genres=['Action', 'Fantasy'])
          >>> print_anime_list(result2)
          'A'
          >>> my_anime = Collection(load_anime('test4.dat'))
          >>> result3 = my_anime.matching_anime(rating='Teen', type='Series',
          ...                       genres=['Fantasy', 'Action'])
          >>> print_anime_list(result3)
          '07 Ghost, Angel Beats, Arata the Legend'
        """
        matches = []

        for anime in self.anime:
            if anime.match(rating, type, genres):
               matches.append(anime)

        return matches


        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
