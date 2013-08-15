def process_text(list_of_raw_anime):
    """
      >>> result = process_text(['A\\nT\\nS\\nSup\\nAct\\nAdv\\nF'])
      >>> len(result)
      1
      >>> type(result)
      <class 'list'>
      >>> result[0]['name']
      'A'
      >>> result[0]['genre']
      ['Sup', 'Act', 'Adv', 'F']
      >>> result2 = process_text(load_anime('test2.dat'))
      >>> type(result2)
      <class 'list'>
      >>> len(result2)
      2
      >>> result3 = process_text(load_anime('anime.dat'))
    """
    processed_anime = []
    new = {}

    for raw_anime in list_of_raw_anime:
        stripped_anime = raw_anime.strip()
        an_anime = stripped_anime.split('\n')

    new['name'] = an_anime[0]
    new['rating'] = an_anime[1]
    new['type'] = an_anime[2]
    new['genre'] = an_anime[3:]
    processed_anime.append(new)


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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
