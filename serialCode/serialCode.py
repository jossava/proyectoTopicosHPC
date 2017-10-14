import operator, os, sys
import numpy as np
import time, collections


# Se extraen las palabras mas relevantes
def getMainWords(rootDir):
    T = []
    stopwords = ["a", "able", "about", "above", "according", "accordingly", "across", "actually", "after", "afterwards", "again", "against", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c", "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "course", "currently", "d", "definitely", "described", "despite", "did", "different", "do", "does", "doing", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f", "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former", "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "happens", "hardly", "has", "have", "having", "he", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "i", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar", "instead", "into", "inward", "is", "it", "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "like", "liked", "likely", "little", "ll", "look", "looking", "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she", "should", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us", "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "ve", "very", "via", "viz", "vs", "w", "want", "wants", "was", "way", "we", "welcome", "well", "went", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without", "wonder", "would", "would", "x", "y", "yes", "yet", "you", "your", "yours", "yourself", "yourselves", "z", "zero"]
    for dirName, subdirList,files in os.walk(rootDir): # Obtenemos la lista de archivos a procesar.
        nWords =  10 if len(files) < 100 else 5 # Cantidad de palabras a tomar dependiendo de la cantidad de archivos.
        for f in files: # Recorremos cada archivo.
            file = open(rootDir + f, 'r') # Abrimos el archivo actual a procesar.
            mainwords = [] # Creamos un diccionario para guardar cada palabra (que no sea una stop word) con sus repeticiones.
            for line in file: # Recorremos cada linea del documento.
                for word in line.split(): # Recorremos la linea por palabras, quitandole a cada palabra signos especiales.
                    word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-","").replace(".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    # Si la palabra no esta es los stopwords, se guarda en mainwords
                    if word not in stopwords and word != '':
                        mainwords.append(word)
            sorted_mainwords = collections.Counter(mainwords).most_common(nWords) #Se toman las 10 palabras mas repetidas.
            finalwords = {}
            # guarda sorted_mainwords como un diccionario.
            for i in range(nWords):
                finalwords[sorted_mainwords[i][0]] = sorted_mainwords[i][1]
            T.extend([element for element in list(finalwords.keys()) if element not in T]) # Guarda en T las nuevas palabras encontradas.
            file.close()
    return T

# Encuentra las veces que se repite cada una de las palabras de T en cada archivo.
def findT(T):
    ft = {}
    for dirName, subdirList, files in os.walk(rootDir):
        for f in files:
            t = []
            file = open(rootDir + f, 'r')
            for i in range(len(T)): # inicializa t en ceros.
                t.append(0)
            for line in file:
                for word in line.split():
                    word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-","").replace(".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    if word in T:
                        t[T.index(word)] += 1 # Si word esta en T contar +1
            file.close()
            ft[f] = t # agregar al diccionario k = archivo, v = t
    return ft

# Se llena toda la matriz con las distancias entre pares de documentos.
def jaccardDistances(findT):
    nDoc = len(findT) # numero de documentos
    jaccardDist = np.empty((nDoc, nDoc)) # se crea una matriz cuadrada de tamano nDoc.
    fileList = list(findT.keys()) # se crea una lista con los nombres de los documentos.
    for i in range(nDoc):
        for j in range(nDoc):
            # se calcula la distancia con jaccard_similarity entre cada par de documentos y se guarda en la matriz.
            jaccardDist[i][j] = 1.0 - (jaccard_similarity(findT[fileList[i]], findT[fileList[j]]))
    return jaccardDist

# se tomo de http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    # print(intersection_cardinality)
    union_cardinality = len(set.union(*[set(x), set(y)]))
    # print(list(set.union(*[set(x), set(y)])))
    return intersection_cardinality / float(union_cardinality)

# este metodo se hizo con base en https://gist.github.com/bistaumanga/6023692
def kMeans(X, K, maxIters=10):
    centroids = X[np.random.choice(np.arange(len(X)), K), :] # Se asignan centroides aleatorios, teniendo en cuenta len(X) y K
    C = []
    for i in range(maxIters):
        argminList = []
        # Se agrega a C el centroide en el que queda cada documento.
        for x_i in X:
            dotList = []
            for y_k in centroids:
                dotList.append(np.dot(x_i - y_k, x_i - y_k)) 
            argminList.append(np.argmin(dotList))
        C = np.array(argminList)
        # Se reubican los centrodes teniendo en cuenta el promedio de sus documentos.
        centroidesTemp = []
        for k in range(K):
            truefalseArr = C == k
            propiosKArr = X[truefalseArr]
            promedioArr = propiosKArr.mean(axis=0)
            centroidesTemp.append(promedioArr)
        centroids = centroidesTemp
    return np.array(centroids), C


if __name__ == '__main__':
    timeini = time.time()
    k = 3
    rootDir = sys.argv[1]
    T = getMainWords(rootDir)
    findT = findT(T)
    matrizJaccard = jaccardDistances(findT)
    centroides, C = kMeans(matrizJaccard, k)
    print("Tiempo final: ", time.time() - timeini)
    fileList = list(findT.keys()) # nombres de los documentos
    for i in range(k):
        cluster = []
        for j in range(len(fileList)):
            if(C[j]==i):
                cluster.append(fileList[j]) # agregamos el documento si pertenece al cluster i
        if len(cluster) != 0:
            print ("cluster " + str(i) + ": " + str(cluster))