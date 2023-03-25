def images_identifiers(image_labels: list, k: int, x: int)->list:

    """
    Devuelve el número identificador de las k imágenes más cercanas a un instante del tiempo
    x en segundos.
    
    Parameters
    ----------
    image_labels : list
        Lista de los identificadores de las imagenes.
    k : int
        Numero de imagenes que se desena más cercanas al instante de tiempo x.
    x : int
        Instante de tiempo del que se desean conocer las imagenes más cercanas.

    Returns
    -------
    List
        ILista con el identificador de las k imágenes más cercanas a un instante del tiempo x
        en segundos.
    """

    # Declara la lista donde se guardaran las imágenes de respuesta.
    result = []

    # Calcula la diferencia de segundos entre el instante de tiempo objetivo y el tiempo en
    # el que fueron tomadas las demas imagenes.
    image_distances = {}
    for image in image_labels:
        distance = x - image
        image_distances[image] = abs(distance)

    # Declara e inicializa un dictionario donde las llaves corresponderas a las diferencias
    # calculadas en el bloque de código anterior y como valor una lista donde se encuentran
    # los identificadores de todas las imagenes que se encuentran a esas diferencias.
    distance_images = {}
    for distance in sorted(image_distances.values()):
        distance_images[distance] = []
    for image in image_distances:
        distance = image_distances[image]
        distance_images[distance].append(image)

    # Inserta a la lista a retornar los identificadores de las k imagenes que se encuentran
    # a menor distancia del tiempo objetivo x.
    if len(image_labels) > 0:
        distance_pos = 0
        distances = list(distance_images.keys())
        while len(result) <= k and distance_pos < len(distances):
            distance = distances[distance_pos]
            result += distance_images[distance]
            distance_pos += 1
    else:
        print("La lista de imagenes esta vacia.")

    # Ordena la lista de identificadores de imagenes a retornar.
    if len(result) >= k:
        result = sorted(result[:k])
    else: 
        print("El numero de imagenes que desea es mayor a la cantidad de imagenes en la lista de imagenes.")
        result = sorted(result)
        
    return result