# Reto Yale Face Recognition
## Descripción
El [Yale Face Database](http://vision.ucsd.edu/~leekc/ExtYaleDatabase/ExtYaleB.html) es un conjunto de 2696 imágenes de caras de 39 personas distintas, con diferentes poses e iluminación. Las imagenes fueron recortadas, centradas y alineadas manualmente para mostrar únicamente rostros de las personas. El tamaño por defecto es 168x192.

![alt text][s1]

El reto es construir un clasificador de imágenes que sea capaz de reconocer las 39 personas.

### Ranking
Ver [ranking](https://github.com/charlielito/supervised-intermedio-yale-face-recognition/blob/master/ranking.md).

### Formato Datos
Todos los datos están en la carpeta `.dataget/data/yale-face-rec` y se dividen en 2 grupos
```
|- .dataget
   |- data
      |- yale-face-rec
         |- traning-set
         |- test-set
```

**Estructura** <br>
Cada sub conjunto de datos (training-set o test-set) tiene la siguiente estructura
```
|- {subset}
   |- {class_id}
      |- {image_id}.pgm
```
Donde
* `subset`: es `training-set` o `test-set`
* `class_id`: es el identificador de una clase, e.g. 1, 2, ..., 39
* `image_id`: es el nombre de una imagen.

### Variables
Cada imagen como tal puede ser representada por una matriz de dimensiones `height x width` dado que estan en escala de grises.

### Objetivo
1. Crear un algoritmo que tome una imagen de entrada, ya sea como vector o matriz, y retorne el clase (`class_id`) a la que pertenece esa imagen.
1. Entrenar este algoritmo utilizando los datos de la carpeta `data/training-set`.
1. Medir el performance/score del algoritmo utilizando los datos de la carpeta `data/test-set`. El performance debe ser medido como
```python
score = n_aciertos / n_imagenes * 100
```
donde `n_aciertos` es el numero de imagenes clasificadas de forma correcta y `n_imagenes` es el numero total de imagenes en el `test-set`.

### Notas Teóricas
* Es usual resolver problemas de imágenes con [redes neuronales](https://en.wikipedia.org/wiki/Artificial_neural_network). Sin embargo, algoritmos menos potentes pueden ser usados con buenos resultados en este tipo de dataset, por ejemplo haciendo uso de algoritmos tipo [Nearest neighbor search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) teniendo representadas las imágenes en otro espacio vectorial, como [PCA](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_componentes_principales), [Linear Discriminant Analysis (LDA)](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) o usando [Local Binary Patterns Histograms](https://en.wikipedia.org/wiki/Local_binary_patterns).

### Solución
Ver procedimiento de [solución](https://github.com/colomb-ia/formato-retos#solucion)

##### Requerimientos
*Indica los requerimientos para utilizar el codigo de tu solucion*

##### Procedimiento
*Indica el procedimiento que se debe seguir para reproducir tu solucion*

##### Método
*Indica el metodo que utilizaste para solucionar el reto*

##### Resultados
*Indica el metodo que utilizaste para solucionar el reto*

## Getting Started
Para resolver este reto primero has un [fork](https://help.github.com/articles/fork-a-repo/) de este repositorio y [clona](https://help.github.com/articles/cloning-a-repository/) el fork en tu maquina.

```bash
git clone https://github.com/{username}/supervised-avanzado-yale-face-recognition
cd supervised-avanzado-yale-face-recognition
```

*Nota: reemplaza `{username}` con tu nombre de usuario de Github.*

### Requerimientos
Para descargar y visualizar los datos necesitas Python 2 o 3. Las dependencias las puedes encontrar en el archivo `requirements.txt`, el cual incluye
* pillow
* pandas
* numpy
* jupyter
* dataget

Puedes instalarlas fácilmente utilizando el commando

```bash
pip install -r requirements.txt
```
Dependiendo de tu entorno puede que necesites instalar paquetes del sistema adicionales, si tienes problemas revisa la documentación de estas librerías.

### Descarga y Preprocesamiento
Para descargar los datos ejecuta el comando
```bash
dataget get yale-face-rec
```
Esto descarga los archivos en la carpeta `.dataget/data`, los divide en los conjuntos `training-set` y `test-set`, convierte las imagenes en `jpg` de dimensiones `32x32`. Las imágenes originalmente vienen en formato `.pgm` con dimensiones `168x192`. Si deseas mantener el formato original ejecuta en vez

```bash
dataget get --dont-process yale-face-rec
```

# Starter Code Python
Para iniciar con este reto puedes correr el codigo de Python en Jupyter del archivo `python-sample.ipynb`. Este código que ayudará a cargar y visualizar algunas imágenes. Las dependencias son las mismas que se instalaron durante la descarga de los datos, ver [Requerimientos](#requerimientos).

Para iniciar el código solo hay que prender Jupyter en esta carpeta

```bash
jupyter notebook .
```
y abrir el archivo `python-sample.ipynb`.


[s1]: http://vision.ucsd.edu/~leekc/ExtYaleDatabase/images/ExpImgs.png "S"
