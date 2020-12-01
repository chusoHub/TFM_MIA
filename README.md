# TFM_MIA
## Inspección visual de los datos
[Archivo: Datos/Inspección_visual_TFM.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Datos/Inspección_visual_TFM.ipynb)

## Modelos Secuenciales SGD
<details>
<summary>Write Markdown!</summary>
<!--All you need is a blank line-->

## Modelo SGD 1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   SGD Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 1.7178e-05 
*   mean_absolute_error: 0.0017

Test:
*   loss (mse): 4.8378e-04
*   mean_absolute_error: 0.0022

[Archivo: Modelos_Secuencial/TFM_seq_3cv1.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv1.ipynb)
## Modelo SGD 2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   SGD Learning Rate 1e-2
*   2000 epochs
*   Reentrenamiento 1e-4 100 epochs
*   Reentrenamiento 1e-6 100 epochs
*   Reentrenamiento 1e-8 100 epochs

Validación:
*   loss (mse): 1.6339e-05  
*   mean_absolute_error: 0.0016 

Test:
*   loss (mse): 4.8143e-04 
*   mean_absolute_error: 0.0021

[Archivo: Modelos_Secuencial/TFM_seq_3cv4.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv4.ipynb)
## Modelo SGD 3
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   SGD Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 0.0705 
*   mean_absolute_error: 0.1821  

Test:
*   loss (mse): 0.0363 
*   mean_absolute_error: 0.1458 

[Archivo: Modelos_Secuencial/TFM_seq_3cv5.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv5.ipynb)
</details>
### Modelo RMSprop  1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   RMSprop Learning Rate 1e-2

Validación:
*   loss (mse): 6.8896e-05 
*   mean_absolute_error: 0.0056

Test:
*   loss (mse): 5.3990e-04 
*   mean_absolute_error: 0.0057 

[Archivo: Modelos_Secuencial/TFM_seq_3cv2.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv2.ipynb)
### Modelo Adam  1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Adam Learning Rate 1e-2

Validación:
*   loss (mse): 2.8247e-05 
*   mean_absolute_error: 0.0039 

Test:
*   loss (mse): 4.8438e-04 
*   mean_absolute_error: 0.0047 

[Archivo: Modelos_Secuencial/TFM_seq_3cv3.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv3.ipynb)