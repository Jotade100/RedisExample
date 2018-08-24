import redis
import json
from flask import Flask, render_template, request


# Configuranciones de la conexión con REDIS
conexion = redis.Redis(host='192.168.99.100', port=6379)
app = Flask('JD')

# añadiendo datos al Redis
conexion.set('positivo', '{"imagenes":["https://mfas3.s3.amazonaws.com/objects/SC14445.jpg","http://girolamofrescobaldi.com/wp-content/uploads/2018/05/11.1.-WIng-shaped-organ-a-ala..jpg","https://www.harpsichord.com/All%20Instrument%20Images/2979org_1.jpg"]}')
conexion.set('hammond', '{"imagenes":["https://www.picclickimg.com/00/s/NDgwWDY0MA==/z/b2UAAOSwdjNZBjLt/$/Hammond-Organ-Model-232272-Console-Very-Nice-to-_1.jpg","http://beta.asoundstrategy.com/sitemaster/userUploads/site153/get-attachment-19.aspx17..jpg","https://keyboardexchange.com/inventory/205-large.jpg"]}')
conexion.set('armonio', '{"imagenes":["https://cdn.shopify.com/s/files/1/1800/7761/products/HBDELX-2.jpg?v=1505936889","http://www.armonio.net/s/img/emotionheader.JPG?1505836883.800px.325px","https://media-cdn.tripadvisor.com/media/photo-s/09/85/82/83/armonio-de-la-santa.jpg"]}')
conexion.set('clave', '{"imagenes":["http://www.baroquemusic.org/Hieronymus%20Albrecht%20Hass%20Harpsichord%20(Hamburg,%201740).jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/ClavecinRuckers%26Taskin.JPG/300px-ClavecinRuckers%26Taskin.JPG","https://www.harpsichord.com/All%20Instrument%20Images/dolmetsch%20dbl%20closeup_72dpi.jpg"]}')
conexion.set('pianoforte', '{"imagenes":["http://www.harpgallery.com/ebay/er/pia81617no.jpg","http://cdn-2-wdh.habsburger.net/files/styles/large/public/originale/hammerfluegel_wolfgang_amadeus_mozarts_von_anton_walter_um_1780_original.jpg?itok=PdL4vRxU","http://www.chrismaene.be/websites/1/uploads/images/tekstMetAfbeelding/28-10-2016_11_28_20_4-pianoforte-longman-clementi-london-1798.jpg","http://www.realsamples.de/WebRoot/Store8/Shops/17831984/MediaGallery/Produkte/edition-beurmann/early_pianoforte/Stein_Hammerfluegel.jpg"]}')
conexion.set('órgano', '{"imagenes":["http://www.gracechurchprovidence.org/wp-content/uploads/2011/07/Organ-Gallery-BK-1-web.jpg","https://fowlerorgan.com/wp-content/uploads/2018/02/carousel10.jpg","http://3.bp.blogspot.com/-wUtvF2ZUp7o/WN8rARJsVJI/AAAAAAAAEaU/yz_V5JiSEOELGGEzvpE3iv8G6KNQZmS0gCK4B/s1600/P1010071.jpg", "https://i.ytimg.com/vi/gYz7p8grZKU/maxresdefault.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2kUxJBUT6FRld12EYf6M0zmGZ6t6qSlxPYiDOJ7B9XLX6n2Tn", "https://rosales.com/wp-content/uploads/2016/08/mobile-home-3.jpg"]}')
conexion.set('piano', '{"imagenes":["https://www.yamaha.com/en/musical_instrument_guide/common/images/piano/parts_viewer01.jpg","http://www.pianorecording.co.uk/studio%20gallery/Bosendorfer%20Imperial.png","http://www.sherwoodphoenix.co.uk/wp-content/uploads/2018/01/Steinmayer-SG-143-Baby-Grand-Piano-Black-Polyester-At-Sherwood-Phoenix-Pianos-1.jpg", "https://kaldenbachpiano.nl/kaldenbach/img/template/tile_pianos.jpg?1524120850"]}')
conexion.set('acordeón', '{"imagenes":["https://gabbanelli.com/wp-content/uploads/2017/05/d19d470df7b372eadb7db39c1767b5e5.jpg","https://gabbanelli-live-ccvxlcomim8z9.netdna-ssl.com/wp-content/uploads/2017/12/N2067-1000x699.jpg","http://mla-s1-p.mlstatic.com/roland-fr3x-bk-acordeon-digital-v-accord-piano-keys-5011-MLA4119170742_042013-F.jpg"]}')
conexion.set('melódica', '{"imagenes":["https://www.thomann.de/pics/bdb/146646/11552114_800.jpg","https://www.thomann.de/pics/bdb/402321/12348187_800.jpg","https://www.guitaraudio.com/media/catalog/product/8/1/81gew-p0fcl._sl1500_.jpg"]}')


# Prueba 1
#print("Lo que se obtiene de la conexión: ", conexion.get('positivo'))

# Convirtiéndolo a JSON
#resultado = json.loads(conexion.get('positivo'))
#print(resultado["imagenes"])


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/result' ,methods = ['POST', 'GET'])
def result():
	termino = request.form['termino'].lower()
	if conexion.get(termino) != None:
		resultado = json.loads(conexion.get(termino))
		return render_template('imagenes.html', termino=termino, imagenes=resultado["imagenes"])
	else:
		return render_template('index.html')
	
app.run(host="localhost",port=5000)