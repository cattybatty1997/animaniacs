def verify_data(list_of_raw_anime):
    """
    """
    processed_anime = []

    for raw_anime in list_of_raw_anime:
        stripped_anime = raw_anime.strip()
        if stripped_anime.count('\n') < 3:
            return stripped_anime 
    return 'Valid Data' 



def load_anime(data_file):
    """
      >>> result = load_anime('test2.dat')
      >>> len(result)
      2
      >>> result[0]
      'A\\nT\\nS\\nSup\\nAct\\nAdv\\nF'
      >>> result[1]
      'B\\nAd\\nM\\nF\\nAct\\nSci'
      >>> load_anime('test_broken.dat')
      ['Laputa Castle in the Sky']
    """
    f = open(data_file, 'r')
    raw_text = f.read()
    f.close()
    
    raw_anime = raw_text.split('##!##')

    test_data = verify_data(raw_anime)
    if test_data != 'Valid Data':
        return [test_data]

    for i in range(len(raw_anime)):
        raw_anime[i] = raw_anime[i].strip()

    return raw_anime


if __name__ == '__main__':
    import doctest
    doctest.testmod()
