# Trabajo de Grado en Ingeniería Electrónica

<p align="center">
  <img width="600" src="https://www.javeriana.edu.co/recursosdb/20125/877826/EdIngenieriaLab1.JPG/f07c9bd5-cb9f-5126-3ce5-2f107c643f89">
</p>

## Detección de Factores de Riesgo en Obras de Construcción
### Autor: Daniel Alejandro Rodriguez Zamudio

Bienvenido a este repositorio que alberga el proyecto de investigación "Detección de Factores de Riesgo en Obras de Construcción mediante Inteligencia Artificial," desarrollado como parte de mi titulación en Ingeniería Electrónica en la Pontificia Universidad Javeriana.

### Resumen

Este trabajo de grado presenta la planificación y ejecución del proyecto implementado, enfocado en la identificación de factores de riesgo clave como la falta de uso de elementos de protección personal (EPP) y el peligro de caídas en proximidad a bordes de losa. Mediante una colaboración con una empresa de seguros de riesgos laborales, se obtuvo acceso a un sitio de construcción para adquirir metraje de video, el cual fue utilizado para entrenar un modelo de inteligencia artificial. El estudio se centró en el entrenamiento de dos topologías de redes neuronales convolucionales: YOLOv4-tiny y YOLOv7. El resultado es un software desarrollado en Python, diseñado para detectar y reportar estos riesgos. El software procesa el video, identifica y marca las áreas de riesgo con cajas delimitadoras, y genera un informe de los riesgos detectados.

### Abstract

This bachelor's degree work presents the planning and execution of the implemented project, focused on the identification of key risk factors such as the lack of use of personal protective equipment (PPE) and the danger of falls near slab edges. Through a collaboration with an occupational risk insurance company, access was gained to a construction site to acquire video footage, which was used to train an artificial intelligence model. The study centered on the training of two convolutional neural network topologies: YOLOv4-tiny and YOLOv7. The result is software developed in Python, designed to detect and report these risks. The software processes the video, identifies and marks risk areas with bounding boxes, and generates a report of the detected risks.

### Documentación Completa

Un análisis exhaustivo y detallado del proceso, desde la planificación hasta la ejecución, se encuentra en el [documento asociado](https://repository.javeriana.edu.co/handle/10554/65196), ubicado en el repositorio público de la universidad.

<details open>
<summary>📂 Ejecutables en Google Drive</summary>

- [Ejecutables](https://drive.google.com/drive/folders/1fD1Zt55NcRXYXGE_T_KE3I7PvjWunfRF?usp=sharing)

</details>

Antes de utilizar los ejecutables, recomiendo revisar el [Manual de Usuario](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/tree/main/user-manual) para una experiencia óptima.

### Redes Neuronales Convolucionales YOLO

#### YOLOv7

- [Configuración de la Red Neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.cfg)
- [Clases de la Red Neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.names)
- [Código Fuente del Proyecto](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.py)

#### YOLOv4-tiny

- [Configuración de la Red Neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.cfg)
- [Clases de la Red Neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.names)
- [Código Fuente del Proyecto](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.py)

<details open>
<summary>📂 Pesos de la Red Neuronal en Google Drive</summary>

Debido a las limitaciones de GitHub para subir archivos mayores a 25 MB, los [pesos de la red neuronal YOLOv7](https://drive.google.com/drive/folders/1E7H8OOU8wHZciFfbfCve8SjCha2ivS07?usp=sharing) y [YOLOv4-tiny](https://drive.google.com/drive/folders/148tr3gdF-iLAOx_Pq7W3ZXVfVS46jqPK?usp=sharing) se encuentran en Google Drive.

</details>

## [Licencia](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/LICENSE.txt)
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Detección de Factores de Riesgo en Obras de Construcción mediante Inteligencia Artificial</span> de <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Daniel Alejandro Rodriguez Zamudio</span> está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional</a>.
