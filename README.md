## Tweets controversiales

### Objetivo
Dado un tweet queremos detectar si el mismo es controversial, es decir, el mismo posee respuestas en la que varios usuarios defienden opiniones contrarias. Identificando aquellos usuarios que estan en contra, a favor, o aquellos que no es posible determinar su postura hacia el tweet.

### Primera aproximación
Uno de los primeros objetivos consiste en etiquetar las respuestas de un tweet dependiendo su opinion. Se definieron las siguientes etiquetas <span style="color:yellow">**neutral**</span> , <span style="color:red">**attack**</span> y <span style="color:green">**support**</span> el cual van a ser utilizadas para categorizar las distintas posturas.

Para determinar la postura de un tweet se definio un vocabulario inicial el cual llamaremos *lexicon* este contendra palabras que posiblemente caractericen a las distintas posturas, es decir, *lexicon_attack* inicialmente  tendra las palabras **mentiroso** y **falso**.

Luego para detectar que un tweet es controversial, observaremos si algunas de las repuestas tienen al menos una palabra del los *lexicons* definidos.

Como segundo objetivo es ampliar el vocabulario de los *lexicons* utilizando Word embedding, y luego volver a etiquetar las respuestas con el vocabulario ampleado.

Por ultimo y como tercer objetivo es visualizar el resultado obtenido.
  
### Arquitectura

![Alt text](./readme/arquitectura.svg)

#### Obtencion de Twets
Para la recoleción de los tweets se utilizo la herramienta [Twarc](https://github.com/DocNow/twarc), la cual brinda facilidad para obtener tweets con su respectivas respuestas.

#### Preprocesamiento
En el preprocesamiento al tweet se lo tranforma en texto en minuscula, y luego se lo tokeniza utilizando la libreria [NLTK](http://www.nltk.org/).
Inicialmente los tweets son etiquetados como <span style="color:yellow">**neutral**</span>.

#### Etiquetado
Se definio la siguiente funcion ```tagged(tweets, root, lexicon, model, n)``` la cual tiene como objetivo etiquetar las respuestas y ampliar el vocabulario.
Para la parte de ampliar se utilizaron words embeddings de un modelo ya pre-entrenado obtenido de SBWCE<sup>1</sup>, el cual vemos las palabras mas similares del modelos con respecto al *lexicon*.

Un problema que surge con la primera aproximacion, es ¿Que *lexicon* definimos para caracterizar los tweets que estan a favor?, ya que es mas dificil determinar las palabras que tienden a ser utilizadas para un tweet que esta a favor de la opinion. Una solucion planteada fue hacer analisis de sentimiento utilizando [TextBlob](https://textblob.readthedocs.io/en/dev/), esta es una libreria para procesamiento del lenguaje de natural que tiene como caracterisitca la implementacion de analisis de sentimientos.

 Esta solución no es buena ya que al hacer analisis de sentimiento estamos decidiendo que postura tiene el tweet analizandolo sintacticamente,  es decir si partes del texto estan usando lenguaje positivo, negativo o neutral.

#### Visualización
Se utilizo [flask](https://palletsprojects.com/p/flask/) usando un template imitando la visualizacion de Twitter.

### Propuestas
Una alternativa que se propuso para ampliar el vocabulario fue de usar el mismo vacabulario de los tweets, y comparandolo con un modelo de Words embeddings pre-entrenado con FastText de [francolq@famaf.unc.edu.ar](). 
 
![](./readme/idea.png) 

donde *u* denota al umbral elegido.

### Resultados


### Problemas
Un problema principal que se presento en el procedimiento fue la recoleccion de tweet con sus respectivas respuesta, ya que la API de Twitter no posee esta funcionalidad. Una primera solucion fue scrappear Twitter, por ultimo se utilizo Twarc.

Otro problema fue mencionado en la seccion de etiquetado, sobre el *lexicon* para tweets a favor.

### Instalacion y uso


Instalacion de requerimientos

```pip install -r requirements.txt```

Instalacion del paquete Tweet

```pip install package/dist/tweet-0.1.tar.gz```

Obtencion de tweets

```twarc replies <id_tweet> --recursive > data/<file_name>.json```

Visualización

```cd visualization/ && flask run```

### Referencias
1.[Cristian Cardellino: Spanish Billion Words Corpus and Embeddings (March 2016)]( https://crscardellino.github.io/SBWCE/).
