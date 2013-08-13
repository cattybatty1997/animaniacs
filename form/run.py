#!usr/bin/env python3
import bottle

@bottle.route('/<name>')
def index(name='Form'):
    the_message = 'Welcome Otaku {0}!'.format(name)
    return bottle.template('layout.tpl', message=the_message)

bottle.run(host='0.0.0.0', port=8090)
                                            
