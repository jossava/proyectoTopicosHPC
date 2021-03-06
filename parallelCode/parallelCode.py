import operator, os, sys
import time
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
sendbuf = []
root = 0

stopwords = ["a", "able", "about", "above", "according", "accordingly", "across", "actually", "after", "afterwards", "again", "against", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c", "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "course", "currently", "d", "definitely", "described", "despite", "did", "different", "do", "does", "doing", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f", "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former", "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "happens", "hardly", "has", "have", "having", "he", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "i", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar", "instead", "into", "inward", "is", "it", "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "like", "liked", "likely", "little", "ll", "look", "looking", "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she", "should", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us", "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "ve", "very", "via", "viz", "vs", "w", "want", "wants", "was", "way", "we", "welcome", "well", "went", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without", "wonder", "would", "would", "x", "y", "yes", "yet", "you", "your", "yours", "yourself", "yourselves", "z", "zero"]

# Se extraen las palabras mas relevantes
def getMainWords(v):
    leidos = []
    finalwords = {}
    toSend = []
    for i in range(comm.rank, len(v), comm.size):
        file = open(rootDir + v[i], 'r')
        mainwords = {}
        for line in file:
            line = line.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-", "").replace(".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
            for word in line.split():
                if word not in stopwords:
                    if word in mainwords and word != '':
                        mainwords[word] += 1
                    else:
                        mainwords[word] = 1
        file.close()
        sorted_mainwords = sorted(mainwords.items(), key=operator.itemgetter(1))[::-1]

        for i in range(10):
            toSend.append(sorted_mainwords[i][0])
    return toSend

# Encuentra las veces que se repite cada una de las palabras de T en cada archivo.
def findT(w):
    frecuency = {}
    for i in range(comm.rank, len(v), comm.size):
        result = []
        for j in range(len(w)):
            result.append(0)

        file = open(rootDir + v[i], 'r')
        for line in file:
            line = line.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-", "").replace(".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
            for word in line.split():
                if word in w:
                    result[w.index(word)] += 1

        frecuency[v[i]] = result
    return frecuency

# Se llena toda la matrix con las distancias entre pares de documentos.
def jaccardDistances(x):
    tam = len(x)
    matrixC = np.zeros((tam, tam))
    listaFiles = list(x.keys())
    for i in range(comm.rank, len(x), comm.size):
        for j in range(tam):
            matrixC[i][j] = 1.0 - (jaccard_similarity(x[listaFiles[i]], x[listaFiles[j]]))
    return matrixC

# se tomo de http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    # print(intersection_cardinality)
    union_cardinality = len(set.union(*[set(x), set(y)]))
    # print(list(set.union(*[set(x), set(y)])))
    return intersection_cardinality / float(union_cardinality)

# Se agrega a C el centroide en el que queda cada documento.
def kMeansC(mJack, cent):
    tam2 = len(mJack)
    argminList = np.zeros(tam2)

    for i in range(comm.rank, len(mJack), comm.size):
        dotList = []
        for y_k in cent:
            dotList.append(np.dot(mJack[i] - y_k, mJack[i] - y_k))
        argminList[i] = np.argmin(dotList)
    return argminList

# Se reubican los centrodes teniendo en cuenta el promedio de sus documentos.
def kMeansRc(z):
    centroidsTemp = []
    for i in range(k):
        centroidsTemp.insert(i, [])
    for i in range(comm.rank, k, comm.size):
        truefalseArr = z == i
        propiosKArr = mJack[truefalseArr]
        promedioArr = propiosKArr.mean(axis=0)
        centroidsTemp[i]=list(promedioArr)
    return centroidsTemp

if __name__ == '__main__':
    timeini = time.time()
    k = 2  # se recibe la nueva matriz con los centroides, realizada por cada nucleo
    maxIters = 10 # numero maximo de iteraciones del kmeans
    rootDir = sys.argv[1]
    T = []
    fileList = []
    if comm.rank == 0:
        fileList = list(os.walk(rootDir))[0][2] # el nucleo 0 lee la lista de archivos
    v = comm.bcast(fileList, root) # se hace un broadcast para enviar la lista de archivos a todos los nucleos
    toSend = getMainWords(v) # Se obtiene Ti con i = 0,1,2,3 -> nucleos
    recibV = comm.gather(toSend,root) # el nucleo 0 recibe Ti con i = 0,1,2,3 -> nucleos
    tFinal = [] 
    if comm.rank == 0:
        for i in range(len(recibV)):
            tFinal.extend([element for element in recibV[i] if element not in tFinal]) # se unen los Ti en tFinal
    w = comm.bcast(tFinal, root) # se envia el tFinal a todos los nucleos
    frecuency = findT(w) # se obtienen los tij con i = nucleos y j = documentos
    recibfrecuency = comm.gather(frecuency,root)
    finalMap = {}
    if(comm.rank == 0):
        for i in range(len(recibfrecuency)):
            finalMap.update(recibfrecuency[i]) # se unen los tij
    x = comm.bcast(finalMap, root) # se envian los tij a todos los nucleos
    matrixC = jaccardDistances(x) # se callculan las distacias con jaccard, esto lo hace cada nucleo
    recibMatrixC = comm.gather(matrixC, root) # El nucleo 0 recible la matriz i (i es cada nucleo) con las distancias.
    C = []
    centroids = []
    matrixFinal = 0
    if comm.rank == 0:
        for matrix in recibMatrixC:
            matrixFinal += matrix # se unen las mattrices i
        centroids = matrixFinal[np.random.choice(np.arange(len(matrixFinal)), k), :] # se ubican los centroides aleatoriamente.
    for i in range(maxIters):
        mJack = comm.bcast(matrixFinal,root) # se envia la matriz con las distancias a cada nucleo
        cent = comm.bcast(centroids, root) # Se envia el arreglo que me dice en que centroide esta cada documento
        argminList = kMeansC(mJack,cent) # se recibe la nueva matriz con los centroides, realizada por cada nucleo
        recibC = comm.gather(argminList, root)  # el nodo 0 recibe recibC
        cFinal = []
        if comm.rank == 0:
            cFinal = np.zeros(len(recibC[0]))
            for li in range(len(recibC)):
                cFinal += recibC[li]
        finalC = comm.bcast(cFinal,root) # se envia cFinal a todos los nucleos
        centroidsTemp = kMeansRc(finalC) # se reubican los centroides, esto lo hacen todos los nucleos
        recibFinalC = comm.gather(centroidsTemp,root) # el nucleo 0 recibe la reubicacion de los centroides
        finalCentroids = []
        for j in range(k):
            finalCentroids.append([])
        if comm.rank == 0:
            for i in range(len(recibFinalC)):
                for j in range(len(recibFinalC[i])):
                    finalCentroids[j] += recibFinalC[i][j]
            centroids = finalCentroids

    if comm.rank == 0:
        # el nucleo 0 imprime cada k cluster con sus respectivos documentos
        print("Tiempo final: ", time.time()-timeini)
        listaFiles = list(x.keys())
        for i in range(k):
            cluster = []
            for j in range(len(fileList)):
                if(finalC[j]==i):
                    cluster.append(fileList[j]) # agregamos el documento si pertenece al cluster i
            if len(cluster) != 0:
                print ""
                #print ("Cluster " + str(i) + ": " + str(cluster))