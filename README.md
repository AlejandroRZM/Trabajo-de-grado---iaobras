# Trabajo de Grado en Ingeniería Electrónica

<p align="center">
  <img width="500" src="https://www.javeriana.edu.co/recursosdb/20125/877826/EdIngenieriaLab1.JPG/f07c9bd5-cb9f-5126-3ce5-2f107c643f89">
</p>

Este repositorio contiene todo lo necesario para el correcto funcionamiento del proyecto desarrollado en mi trabajo de grado "Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial" para optar por el título de Ingeniero Electrónico de la Pontificia Universidad Javeriana.

En el siguiente link se encuentra el 'Libro' del proyecto que documenta todo el proceso de planeación y ejecución para llevarlo acabo, este se encuentra en el repositorio público de la universidad.

- [DOCUMENTO: Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial](https://www.google.com)

A continuación, se incluye el link en Google Drive en el que se encuentra la carpeta _'Ejecutable_deteccion_riesgos'_ en el que se encuentran dos subcarpetas, cada una conteniendo la carpeta en donde se encuentran los archivos _yolov4-tiny.exe_ y _yolov7.exe_ según corresponda. La única diferencia entre ambas es que la version YOLOv7 tiene mayor efectividad que YOLOv4-tiny pero esta última toma menos tiempo de procesamiento.

<details open>
<summary>Google Drive</summary>

- [Archivos ejecutables](https://drive.google.com/drive/folders/1fD1Zt55NcRXYXGE_T_KE3I7PvjWunfRF?usp=sharing)

</details>

Si se va a usar el archivo ejecutable se recomienda leer antes el pdf [Manual de Usuario](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/user-manual/Manual%20de%20Usuario%20-%20Deteccion%20de%20factores%20de%20riesgo%20con%20IA.pdf).

También se adjuntan los archivos individuales de la red neuronal convolucional entrenada YOLOv7 y YOLOv4-tiny:

## ARCHIVOS INDIVIDUALES YOLOv7

- [Configuración de la red neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.cfg)
- [Clases de la red neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.names)
- [Código fuente del proyecto](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov7/yolov7.py)

## ARCHIVOS INDIVIDUALES YOLOv4-tiny

- [Configuración de la red neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.cfg)
- [Clases de la red neuronal](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.names)
- [Código fuente del proyecto](https://github.com/AlejandroRZM/Trabajo-de-grado---iaobras/blob/main/yolov4-tiny/yolov4.py)

<details open>
<summary>Google Drive</summary>

Debido a las limitaciones de GitHub para subir archivos más grandes de 25 MB se opta por dejar en un enlace a Google Drive los archivos .weights, estos son los pesos de la red neuronal según cada topología.

- [Pesos de la red neuronal - yolov7_best_weights](https://drive.google.com/drive/folders/1E7H8OOU8wHZciFfbfCve8SjCha2ivS07?usp=sharing)
- [Pesos de la red neuronal - yolov4_tiny_best_weights](https://drive.google.com/drive/folders/148tr3gdF-iLAOx_Pq7W3ZXVfVS46jqPK?usp=sharing)

</details>
