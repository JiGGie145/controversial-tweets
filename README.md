## Tweets controversiales

### Objetivo
Dado un tweet queremos detectar si el mismo es controversial, es decir, el mismo posee respuestas en la que varios usuarios defienden opiniones contrarias. Identificando aquellos usuarios que estan en contra, a favor del tweet, o aquellos que no es posible determinar su postura.

### Arquitectura

![Alt text](./readme/arquitectura.svg)

#### Obtencion de Twets
Para la recoleción de los tweets se utilizo la herramienta [Twarc](https://github.com/DocNow/twarc), la cual brinda facilidad para obtener tweets con su respectivas respuestas.

#### Preprocesamiento
En el preprocesamiento al tweet se lo tranforma en texto en minuscula, y luego se lo tokeniza utilizando la libreria NLTK.

#### Etiquetado
Se definieron las siguientes etiquetas para determinar que opinion tiene un usuario hacia el tweet principal **attack**(usuario en contra), **support**(usuario a favor) y **neutral**(no se puede determinar si esta favor o no).
 
 Para determinar que respuestas estan en contra se definio una lista inicial de palabras denominada *lexicon*, el cual contiene palabras que posiblemente aparezcan en una respuesta que este en contra.
  
Como nuestro principal objetivo es determinar que tweets estan en contra o favor de

Para esta parte del procedimiento se utilizaron words embeddings de un modelo ya prentrenado de SBWCE<sup>1</sup>.

#### Visualización
Se uso flask usando un template imitando la visualizacion de Twitter.

### Propuestas


### Problemas
Un problema principal que se presento en el procedimiento fue la recoleccion de tweet con sus respectivas respuesta, ya que la API de Twitter no posee esta funcionalidad. Una primera solucion fue scrappear Twitter, por ultimo se utilizo Twarc.

## Referencias
1.[Cristian Cardellino: Spanish Billion Words Corpus and Embeddings (March 2016)]( https://crscardellino.github.io/SBWCE/).
