def load_anime(data_file):

    f = open(data_file, 'r')
    raw_text = f.read()
    f.close()
    animes = raw_text.split('#')
    collection = []
    for anime in animes:
        collection.append(anime.split('\n'))
        new_collection = []
        for anime in collection:
            new = {}
            new['name'] = anime[0]
            new['rating'] = anime[1]
            new['type'] = anime[2]
            new['genre'] = anime[3:]
            new_collection.append(new)
    return new_collection

