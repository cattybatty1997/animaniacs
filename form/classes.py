from anime import load_anime


class Anime:
    def __init__ (self, raw_anime):
    """
      >>> anime = Anime('A\\nTeen\\nSeries\\nAction\\nAdventure\\nFantasy')
      >>> anime.name
      'A'
      >>> anime.rating
      'Teen'
      >>> anime.type
      'Series'
      >>> anime.genre
      ['Action', 'Adventure', 'Fantasy']
    """
    for raw_anime in self:
        stripped_anime = raw_anime.strip()
        an_anime = stripped_anime.split('\n')

    self.name = an_anime[0]
    self.rating = an_anime[1]
    self.type = an_anime[2]
    self.genre = an_anime[3:]
    processed_anime.append(self)


    return processed_anime


def load_anime(data_file):
    """
      >>> result = load_anime('test2.dat')
      >>> len(result)
      2
      >>> result[0]
      'A\\nT\\nS\\nSup\\nAct\\nAdv\\nF'
      >>> result[1]
      'B\\nAd\\nM\\nF\\nAct\\nSci'
      >>> result = load_anime('anime.dat')
    """
    f = open(data_file, 'r')
    raw_text = f.read()
    f.close()

    raw_anime = raw_text.split('##!##')

    for i in range(len(raw_anime)):
        raw_anime[i] = raw_anime[i].strip()

    return raw_anime

class Collection:

    def __init__(self):
        self.anime = []
    def add(self, anime):
        self.anime.append(processed_anime)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

