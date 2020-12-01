# TFM_MIA
## Inspección visual de los datos
[Archivo: Datos/Inspección_visual_TFM.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Datos/Inspección_visual_TFM.ipynb) <sub>New Tab CTRL+Clik</sub>

## Modelos Secuenciales SGD
<details>
<summary>Listado</summary>
<!--All you need is a blank line-->

### Modelo SGD 1
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

[Archivo: Modelos_Secuencial/TFM_seq_3cv1.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv1.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 2
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

[Archivo: Modelos_Secuencial/TFM_seq_3cv4.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv4.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 3
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

[Archivo: Modelos_Secuencial/TFM_seq_3cv5.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv5.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 4
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación 'Relu'
*   SGD Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 9.2932e-06 
*   mean_absolute_error: 0.0014  

Test:
*   loss (mse): 4.6964e-04  
*   mean_absolute_error: 0.0018 

[Archivo: Modelos_Secuencial/TFM_seq_3cv8ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv8.ipynb) <sub>New Tab CTRL+Clik</sub>



</details>

## Modelos Secuenciales Adam
<details>
<summary>Listado</summary>

### Modelo Adam  1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Adam Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 2.8247e-05 
*   mean_absolute_error: 0.0039 

Test:
*   loss (mse): 4.8438e-04 
*   mean_absolute_error: 0.0047 

[Archivo: Modelos_Secuencial/TFM_seq_3cv3.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv3.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam  2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Adam Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 3.4023e-05 
*   mean_absolute_error: 0.0044  

Test:
*   loss (mse): 4.9038e-04 
*   mean_absolute_error: 0.0049 

[Archivo: Modelos_Secuencial/TFM_seq_3cv7.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv7.ipynb) <sub>New Tab CTRL+Clik</sub>

</details>


## Modelos Secuenciales RMSprop
<details>
<summary>Listado</summary>

### Modelo RMSprop  1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   RMSprop Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 6.8896e-05 
*   mean_absolute_error: 0.0056

Test:
*   loss (mse): 5.3990e-04 
*   mean_absolute_error: 0.0057 

[Archivo: Modelos_Secuencial/TFM_seq_3cv2.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv2.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo RMSprop  2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   RMSprop Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 2.5159e-05 
*   mean_absolute_error: 0.0024

Test:
*   loss (mse): 4.5581e-04 
*   mean_absolute_error: 0.0024 

[Archivo: Modelos_Secuencial/TFM_seq_3cv6.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Secuencial/TFM_seq_3cv6.ipynb) <sub>New Tab CTRL+Clik</sub>

</details>

## Modelos SchNet
<details>
<summary>Listado</summary>

### Modelo SchNet  1
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=HardCutoff


Validación:
*   mean_absolute_error: 0.005676

Test:
*   mean_absolute_error: 0.005525

[Archivo: Modelos_Schnet/SchNet_H2O_6.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos_Schnet/SchNet_H2O_6.ipynb) <sub>New Tab CTRL+Clik</sub>


</details>
