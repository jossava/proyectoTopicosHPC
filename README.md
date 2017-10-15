# proyectoTopicosHPC

#### EJECUCIÓN

1. Serial
Cuando se requiera ejecutar el programa en serial se debe estar en la carpeta donde se encuentra se debe poner la siguiente línea,
$ python2.7 serialCode.py ./{Carpeta donde se encuentran los documentos}/

2. Paralelo
Cuando se requiera ejecutar el programa en paralelo se debe estar en la carpeta donde se encuentra poner la siguiente línea, 
$ mpiexec -np {número de nucleos} python2.7 parallelCode.py ./{Carpeta donde se encuentran los documentos}/

# 1. Realizado por:
1. Dillan Alexis Muñeton Avendaño - dmuneto1@eafit.edu.co
2. Juan Fernando Ossa Vásquez - jossava@eafit.edu.co

# 2. Introducción:

*Aquí se pueden encontrar dos carpetas, serialCode la cual contiene el código en serial de la aplicación y parallelCode la cual contiene el código en paralelo de la misma, estos sirven para encontrar similitudes entre documentos, utilizando algoritmos de similitud y agrupamiento, tales como Jaccard y Kmeans.
El dataset se obtuvo de Gutenberg por medio del siguiente link, https://goo.gl/LL4CgA, en este dataset se encuentran alrededor de 3000 documentos con los cuales se pueden correr en estos programas.*

# 3. Palabras clave:
Stopwords: lista de palabras que no deberian ser tomadas en cuenta al momento de comparar los documentos.

Kmeans: es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos.

Jaccard: mide el grado de similitud entre dos conjuntos.

# 4. Análisis y Diseño de algoritmos:
El análisis de los algoritmos fue posible gracias a la lectura de los papers indicados por el orientador, en los cuales, tomaban en cuenta ciertas comparaciones entre los métodos que median el grado de similitud, además mostraban claramente las excepciones y detalles que debían ser tenidos en cuenta.
Los algoritmos que se utilizaron fueron Jaccard para obtener las distancias entre los documentos y KMeans para agrupar los documentos en sus respectivos centroides*
#### Jaccard:
*El índice de Jaccard o coeficiente de Jaccard mide el grado de similitud entre dos conjuntos, sea cual sea el tipo de elementos.

La formulación es la siguiente:

J(A,B) = |A ∩ B| / |A ∪ B|*
*Éste algoritmo se obtuvo de la siguiente página:
http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/*
*Aquí se puede entender claramente como funciona el mismo*

#### KMeans:
K-means es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano. Es un método utilizado en minería de datos. El código para el Kmeans se obtuvo de varios links y repositorios de dónde se trató de entender su funcionamiento y gracias a los cuáles se pudo realizar el KMeans que se encuentra en los programas realizados.

*Éste algoritmo se hizo basado en el algoritmo del siguiente link:
https://gist.github.com/bistaumanga/6023692*
*Aquí se puede entender claramente como funciona el mismo*

# 5. Análisis de solución:

Para analizar el uso de recursos al ejecutar el los códigos en serial y paralelo utilizamos "htop", el cual nos muestra la siguiente interfaz (sin ejecutar ninguno de los programas).

![alt text](https://preview.ibb.co/euEco6/estado_Normal.png)

Al ejecutar el código serial, podemos observar que se usa toda la capacidad de un único núcleo:

![alt text](https://preview.ibb.co/jwFvam/estado_Serial.png)

Al ejecutar el código serial, podemos observar que se usa toda la capacidad de todos los núcleos de la máquina:

![alt text](https://preview.ibb.co/mxwe1R/estado_Paralelo.png)

Por último, para hacer un análisis de velocidad se hicieron varias ejecuciones de los programas (serial y paralelo), utilizando diferentes cantidades de documentos, con lo cual es notable la disminución de tiempo de ejecución del código en paralelo con respecto al serial, esto se muestra en la siguiente gráfica:

![alt text](https://preview.ibb.co/dTLso6/serialvs_Paralelo.png)


# 6.Bibliografía:
1. http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
2. https://es.wikipedia.org/wiki/K-means
3. https://es.wikipedia.org/wiki/%C3%8Dndice_Jaccard
4. https://goo.gl/LL4CgA
