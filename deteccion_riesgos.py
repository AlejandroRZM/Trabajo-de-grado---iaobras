# -*- coding: utf-8 -*-

"""
Pontificia Universidad Javeriana

Por: Daniel Alejandro Rodriguez Zamudio

Junio, 2023

Proyecto de grado para optar por el título de Ingeniero Electrónico

    'Este proyecto realiza la selección de un video de entrada, luego
    selecciona el área a procesar y finalmente realiza las detecciones de
    los factores de riesgo en el video, para luego entregar los resultados
    en la carpeta especificada.'

# Este archivo es parte de 'Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial'.
# Copyright (c) [2023] Daniel Alejandro Rodriguez Zamudio
# 
# 'Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial' is free software: you can redistribute it and/or modify
# it under the terms of the Creative Commons Attribution-NonCommercial 4.0 International License.
#
# 'Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial' is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Creative Commons Attribution-NonCommercial 4.0 International License for more details.
#
# You should have received a copy of the Creative Commons Attribution-NonCommercial 4.0 International License
# along with 'Detección de factores de riesgo en obras de construcción por medio de inteligencia artificial'. If not, see <http://creativecommons.org/licenses/by-nc/4.0/>.
"""

import os
import sys
import cv2
import time
import threading
import numpy as np
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from tkinter import Tk, Button, Label, Entry, Message, filedialog, StringVar, Frame
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime


def code_1():
  clicks = []

  # Selecciona los clicks
  def select_points(event, x, y, flags, params):
      if event == cv2.EVENT_LBUTTONDOWN:
          # Se marca con un círculo el lugar seleccionado
          cv2.circle(params['frame'], (x, y), 5, (0, 0, 255), -1)
          clicks.append((x, y)) #Asigna las coordenadas a la lista creada anteriormente clicks

  # Selecciona el video de entrada
  def select_input_video():
      # Selecciona el archivo
      input_video_path = filedialog.askopenfilename(title="Seleccione el video de entrada")
      input_video_entry.delete(0, 'end')
      input_video_entry.insert(0, input_video_path)

  # Selecciona la carpeta donde se guarda el archivo de salida
  def select_output_folder():
      global output_folder
      # Se selecciona la carpeta
      output_folder = filedialog.askdirectory(title="Seleccione la carpeta de salida")
      output_folder_entry.delete(0, 'end')
      output_folder_entry.insert(0, output_folder)

  # Función que realiza el proceso del video
  def process_video():
      global output_video_name
      input_video_path = input_video_entry.get()
      output_folder = output_folder_entry.get()

      # Crea un objeto que abre el video en la ubicación seleccionada
      cap = cv2.VideoCapture(input_video_path)
      # Obtiene los fps del video
      fps = cap.get(cv2.CAP_PROP_FPS)
      # Define el codec del video de salida
      fourcc = cv2.VideoWriter_fourcc(*'mp4v')

      # Lee el primer fotograma del video
      ret, frame = cap.read()
      # Se sale del programa si hubo algún error
      if not ret:
          print("Error al leer el video")
          sys.exit()

      # Muestra el fotograma #1 para realizar la seleeción de los puntos
      cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
      cv2.resizeWindow('frame', 1920, 1080) # Se ajusta a un tamaño estandard
      # Asociar la función que se ejecutará cuando se haga clic en la ventana
      cv2.setMouseCallback("frame", select_points, {'frame': frame})

      # Mostrar el primer fotograma hasta que el usuario seleccione 4 puntos
      while len(clicks) < 4:
          cv2.imshow("frame", frame)
          cv2.waitKey(1)

      # Cerrar la ventana
      cv2.destroyAllWindows()

      # Crear un array con las coordenadas de los 4 puntos seleccionados
      pts1 = np.float32([list(clicks[0]), list(clicks[1]), list(clicks[2]), list(clicks[3])])

      # Calcular la anchura y la altura del rectángulo que engloba los puntos seleccionados
      X_width = (max(click[0] for click in clicks) - min(click[0] for click in clicks)) * 1.1
      Y_height = (max(click[1] for click in clicks) - min(click[1] for click in clicks)) * 1.1

      # Coordenadas de los 4 puntos en el video de salida
      pts2 = np.float32([[0, 0], [X_width, 0], [0, Y_height], [X_width, Y_height]])

      # Calcular la matriz de transformación que se aplicará a cada fotograma
      matrix = cv2.getPerspectiveTransform(pts1, pts2)

      # Crear el objeto que escribirá el video de salida
      output_video_name = output_folder + "/transformado.mp4"
      out = cv2.VideoWriter(output_video_name, fourcc, fps, (int(X_width), int(Y_height)))

      # Leer y procesar cada fotograma del video
      while True:
          ret, frame = cap.read()
          if not ret:
              break

          # Aplicar la transformación al fotograma
          result = cv2.warpPerspective(frame, matrix, (int(X_width), int(Y_height)))
          # Guardar el fotograma procesado en el video de salida
          out.write(result)

      # Cerrar el video y el archivo de salida
      cap.release()
      out.release()
      
      root.destroy()


  # Crear la interfaz gráfica
  root = Tk()
  root.title("Detección de factores de riesgo en obras de construcción mediante inteligencia artificial")

  # Crear los widgets de la interfaz gráfica
  title_label = Label(root, text="Detección de factores de riesgo en obras de construcción mediante inteligencia artificial", font=("Arial", 14, "bold"), pady=10)
  title_label.pack()
  author_label = Label(root, text="Por: Daniel A. Rodriguez", font=("Arial", 10), pady=5)
  author_label.pack(anchor="sw", padx=10)

  # Crear el marco que contendrá los botones y la nota de texto
  frame = Frame(root)
  frame.pack(padx=10,pady=10)

  # Crear la nota de texto dentro del marco
  note = "NOTA: En el PRIMER PASO usted elegirá el archivo de video que requiera procesar, en el SEGUNDO PASO usted elije la carpeta en donde se guardará el video de salida 'detecciones.mp4, seguido a esto usted va a elejir los puntos que conforman el área donde se encuentran los trabajadores, seleccione de los puntos de la siguiente manera: 1. Esquina Superior Izquiera, 2. Esquina Superior Derecha, 3. Esquina Inferior Izquierda, 4. Esquina Inferior Derecha. ¡¡ES DE SUMA IMPORTANCIA QUE SIGA DICHO ORDEN!!!"
  note_message = Message(frame, text=note, width=500)
  note_message.pack(side='right', fill='y', expand=False, padx=10, pady=10)

  # Crear los botones dentro del marco
  input_video_label = Label(frame, text="Primer paso: Video de entrada:")
  input_video_label.pack(pady=5)
  input_video_entry = Entry(frame, width=50)
  input_video_entry.pack()
  input_video_button = Button(frame, text="Seleccionar video", command=select_input_video)
  input_video_button.pack(pady=5)
  output_folder_label = Label(frame, text="Segundo paso: Carpeta de salida:")
  output_folder_label.pack(pady=5)
  output_folder_entry = Entry(frame, width=50)
  output_folder_entry.pack()
  output_folder_button = Button(frame, text="Seleccionar carpeta", command=select_output_folder)
  output_folder_button.pack(pady=5)
  process_button = Button(frame, text="Procesar video", command=process_video)
  process_button.pack(pady=20)

  # Iniciar la interf as similar to the last one. Show instead.


  # Iniciar la interfaz gráfica
  root.mainloop()
  
  

def code_2():
  # Define an event object that will be set when object detection is done
  detection_done = threading.Event()

  def show_message():
      window = tk.Tk()
      window.title("Detección en Progreso")
      label = tk.Label(window, text="Se están realizando las detecciones, por favor espere mientras termina este proceso")
      label.pack()

      # Check every 500ms if the object detection is done
      def check_if_done():
          if detection_done.is_set():
              window.destroy()
          else:
              window.after(500, check_if_done)

      check_if_done()

      window.mainloop()


  # Define your object detection function here
  def object_detection():
      # Crear el archivo pdf
      reporte_name = "reporte_detecciones.pdf"
      path_reporte = os.path.join(output_folder, reporte_name)

      c = canvas.Canvas(path_reporte, pagesize=letter)

      # Titulo y subtítulo
      c.setFont("Helvetica", 18)
      c.drawString(30,750,"Detección de factores de riesgo en obras")
      c.drawString(80,730,"de construcción por medio de inteligencia artificial")
      c.setFont("Helvetica", 14)
      c.drawString(250,710,"Por: Daniel Alejandro Rodriguez Zamudio")

      start_time = time.time()

      # Fecha y hora del reporte de detección
      c.setFont("Helvetica", 12)
      now = datetime.now()
      current_time = now.strftime("%d/%m/%Y, %H:%M:%S")
      c.drawString(30,690,"Fecha y hora del reporte de detección: " + current_time)
      
      # Preparar para agregar las detecciones
      # Antes de escribir la detección en el archivo PDF, agrega esta línea
      textobject = c.beginText()
      textobject.setTextOrigin(30, 670)

      # Cargar los nombres de las clases
      with open("yolov7.names", "r") as f:
          classes = [line.strip() for line in f.readlines()]

      # Definir un color para cada clase (en formato BGR para OpenCV)
      # Debes tener tantos colores como clases
      colores = [(0, 0, 255),(0, 255, 0),(0, 255, 255),(19, 69, 139),(255, 0, 255),(255, 0, 0),(0, 165, 255)]  # por ejemplo


      risk_color = (255, 165, 0)  # Color de la caja delimitadora cuando está en la zona de riesgo, en este caso rojo.

      # Cargar la red de YOLO
      net = cv2.dnn.readNet("yolov7_best.weights", "yolov7.cfg")

      # Cargar el video
      cap = cv2.VideoCapture('transformado.mp4')

      # Obtener los fps del video original para mantenerlos en el video de salida
      fps = cap.get(cv2.CAP_PROP_FPS)


      # Crear el objeto VideoWriter
      width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ancho del frame
      height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Alto del frame

      detecciones_name = "detecciones.mp4"
      path_detecciones = os.path.join(output_folder, detecciones_name)
      
      video_writer = cv2.VideoWriter(path_detecciones, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

      frame_number = 0

      # Definir el tamaño de la zona de riesgo como el 1% del tamaño del frame
      limit_width = int(0.01 * width)
      limit_height = int(0.01 * height)

      text_y = 670

      alert_classes = ["no-helmet", "no-vest", "no-harness"]

      while True:
          ret, frame = cap.read()
          frame_number += 1
          if not ret:
              break

          height, width, channels = frame.shape

          # Detectar objetos
          blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
          net.setInput(blob)
          outs = net.forward(net.getUnconnectedOutLayersNames())

          # Mostrar información en la pantalla
          class_ids = []
          confidences = []
          boxes = []
          for out in outs:
              for detection in out:
                  scores = detection[5:]
                  class_id = np.argmax(scores)
                  confidence = scores[class_id]
                  if confidence > 0.5:
                      # Object detected
                      center_x = int(detection[0] * width)
                      center_y = int(detection[1] * height)
                      w = int(detection[2] * width)
                      h = int(detection[3] * height)

                      # Rectangle coordinates
                      x = int(center_x - w / 2)
                      y = int(center_y - h / 2)

                      boxes.append([x, y, w, h])
                      confidences.append(float(confidence))
                      class_ids.append(class_id)

          indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
          for i in range(len(boxes)):
              if i in indexes:
                  x, y, w, h = boxes[i]
                  label = str(classes[class_ids[i]])
                  color = colores[class_ids[i]]  # Usar el color correspondiente a la clase

                  # Verificar si la caja delimitadora está en la zona de riesgo
                  if (y < limit_height) or (y + h > height - limit_height) or (x < limit_width) or (x + w > width - limit_width):
                      # Si la caja delimitadora se encuentra en la zona de riesgo, cambiamos el color y escribimos una alerta en el informe
                      color = risk_color
                      time_in_video = frame_number / fps
                      textobject.setFillColor(colors.red)
                      textobject.textLine(f"ALERTA! Riesgo de caida de borde de la loza detectado {time_in_video:.2f}s - Frame: {frame_number}")
                      textobject.setFillColor(colors.black)
                      
                  cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                  cv2.putText(frame, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 3, color, 2)

                  # Escribe el reporte en el archivo pdf
                  time_in_video = frame_number / fps
                  detection_name = classes[class_ids[i]]
                  detection_accuracy = confidences[i]
                  
                  textobject.setFillColor(colors.black)
                  
                  if detection_name in alert_classes:
                      # Si es así, cambia el color del texto a rojo
                      textobject.setFillColor(colors.red)
                  
                  textobject.textLine(f"Tiempo: {time_in_video:.2f}s - Frame: {frame_number} - Deteccion: {detection_name} - Eficacia: {detection_accuracy:.2f}")

                  textobject.setFillColor(colors.black)

                  text_y -= 14  # Reduce la posición y en 14 para la próxima línea

                  # Verifica si hemos llegado al final de la página
                  if text_y < 30:  # Ajusta este número según tus necesidades
                      # Dibuja el texto en la página actual y comienza una nueva página
                      c.drawText(textobject)
                      c.showPage()  # Comienza una nueva página
              
                      # Reinicia el objeto de texto y la posición y
                      textobject = c.beginText()
                      textobject.setTextOrigin(30, 750)  # Reinicia la posición del texto en la página
                      text_y = 750  # Reinicia la posición y

          # Guardar el frame en el video de salida
          video_writer.write(frame)


      cap.release()
      video_writer.release()  # No olvides cerrar el VideoWriter
      cv2.destroyAllWindows()

      # Terminar de escribir en el PDF y guardarlo
      c.drawText(textobject)
      c.save()
      end_time = time.time()
      total_time = end_time - start_time
      with open('total_detection_time.txt', 'w') as f:
        f.write(f'Tiempo total de deteccion: {total_time:.2f} segundos')
      detection_done.set()

  
  # Run your object detection in a new thread
  detection_thread = threading.Thread(target=object_detection)
  detection_thread.start()

  # Show the message window in the main thread
  show_message()

  # Wait for the object detection thread to finish
  detection_thread.join()

if __name__ == "__main__":
  code_1()
  time.sleep(1)
  code_2()
