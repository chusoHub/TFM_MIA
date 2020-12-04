# TFM_MIA
## Inspección visual de los datos
[Archivo: Datos/Inspección_visual_TFM.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Datos/Inspección_visual_TFM.ipynb) <sub>New Tab CTRL+Clik</sub>

## Modelos Keras Secuenciales SGD
<details>
<summary>Listado</summary>
<!--All you need is a blank line-->

### Modelo SGD 1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 1.7178e-05 
*   mean_absolute_error: 0.0017

Test:
*   loss (mse): 4.8378e-04
*   mean_absolute_error: 0.0022

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv1.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv1.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
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

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv4.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv4.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 3
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-6 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 0.0705 
*   mean_absolute_error: 0.1821  

Test:
*   loss (mse): 0.0363 
*   mean_absolute_error: 0.1458 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv5.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv5.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 4
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 9.2932e-06 
*   mean_absolute_error: 0.0014  

Test:
*   loss (mse): 4.6964e-04  
*   mean_absolute_error: 0.0018 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv8.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv8.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 5
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-6 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 0.1981 
*   mean_absolute_error: 0.2315  

Test:
*   loss (mse): 0.0693  
*   mean_absolute_error: 0.1239

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv9.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv9.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 6
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 1000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 9.7216e-06 
*   mean_absolute_error: 0.0014  

Test:
*   loss (mse): 4.8224e-04 
*   mean_absolute_error: 0.0018 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv12.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv12.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 7
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 1.0303e-05 
*   mean_absolute_error: 0.0013 

Test:
*   loss (mse): 4.6974e-04 
*   mean_absolute_error: 0.0018 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv13.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos%20Keras%20Secuenciales/TFM_seq_3cv13.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 8
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 9.7799e-06 
*   mean_absolute_error: 0.0013 

Test:
*   loss (mse): 4.7878e-04 
*   mean_absolute_error: 0.0017

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv15ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv15.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 9
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 1000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 1.0371e-05 
*   mean_absolute_error: 0.0013 

Test:
*   loss (mse): 4.7708e-04 
*   mean_absolute_error: 0.0018

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv18.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv18.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 10
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2  Momentum 0.0
*   2000 epochs

Validación:
*   loss (mse): 9.6351e-06 
*   mean_absolute_error: 0.0012

Test:
*   loss (mse): 4.8066e-04 
*   mean_absolute_error: 0.0017

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv20.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv20.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 11
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1) 
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs


Validación:
*   loss (mse): 9.1313e-06 
*   mean_absolute_error: 0.0010

Test:
*   loss (mse): 4.7173e-04 
*   mean_absolute_error: 0.0015

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv22.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv22.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 12
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs
*   Reentrenamiento 1e-4, 25 epochs

Validación:
*   loss (mse): 9.1313e-06 
*   mean_absolute_error: 0.0010

Test:
*   loss (mse): 9.2066e-06 
*   mean_absolute_error: 0.0010

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv26.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv26.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 13
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 momentum 0.2
*   2000 epochs
*   Reentrenamiento 1e-4, 25 epochs

Validación:
*   loss (mse): 9.6475e-06 
*   mean_absolute_error: 0.0010

Test:
*   loss (mse): 5.1486e-04 
*   mean_absolute_error: 0.0016 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv30.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv30.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 14
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSLE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs

Validación:
*   loss (msle): 7.4050e-06 
*   mean_absolute_error: 0.0020 

Test:
*   loss (msle): 2.3492e-04 
*   mean_absolute_error: 0.0021 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv31.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv31.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 15
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSLE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs
*   Reentrenamiento 1e-4, 25 epochs


Validación:
*   loss (msle): 4.1691e-06 
*   mean_absolute_error: 9.7133e-04

Test:
*   loss (msle): 2.3345e-04 
*   mean_absolute_error: 0.0014 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv33.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv33.ipynb) <sub>New Tab CTRL+Clik</sub>


</details>

## Modelos Keras Secuenciales Adam
<details>
<summary>Listado</summary>

### Modelo Adam  1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 2.8247e-05 
*   mean_absolute_error: 0.0039 

Test:
*   loss (mse): 4.8438e-04 
*   mean_absolute_error: 0.0047 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv3.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv3.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam  2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 3.4023e-05 
*   mean_absolute_error: 0.0044  

Test:
*   loss (mse): 4.9038e-04 
*   mean_absolute_error: 0.0049 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv7.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv7.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam  3
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 1.5672e-05
*   mean_absolute_error: 0.0017  

Test:
*   loss (mse): 4.7965e-04 
*   mean_absolute_error: 0.0020 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv11.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv11.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam  4
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs


Validación:
*   loss (mse): 1.3146e-05 
*   mean_absolute_error: 0.0016  

Test:
*   loss (mse): 4.7908e-04  
*   mean_absolute_error: 0.0018  

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv14.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv14.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam  5
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 1000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 1.4982e-05 
*   mean_absolute_error: 0.0015

Test:
*   loss (mse): 4.8188e-04 
*   mean_absolute_error: 0.0017

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv16.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv16.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam 6
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 2.2877e-05 
*   mean_absolute_error: 0.0015

Test:
*   loss (mse): 5.2285e-04 
*   mean_absolute_error: 0.0018

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv17.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv17.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam 7
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs
*   Reentrenamiento 1e-8 25 epochs

Validación:
*   loss (mse): 1.3088e-05 
*   mean_absolute_error: 0.0016

Test:
*   loss (mse): 4.8191e-04 
*   mean_absolute_error: 0.0019

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv19.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv19.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 8
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-4
*   2000 epochs

Validación:
*   loss (mse): 1.9506e-06 
*   mean_absolute_error: 9.3333e-04 

Test:
*   loss (mse): 8.7174e-04 
*   mean_absolute_error: 0.0032 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv21.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv21.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam 9
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs


Validación:
*   loss (mse): 2.0710e-05 
*   mean_absolute_error: 0.0013 

Test:
*   loss (mse): 5.2445e-04 
*   mean_absolute_error: 0.0017 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv23.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv23.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam 10
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 2.4614e-04 
*   mean_absolute_error: 0.0118 

Test:
*   loss (mse): 6.3948e-04 
*   mean_absolute_error: 0.0108  

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv24.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv24.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo Adam 11
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-4
*   2000 epochs
*   Reentrenamiento 1e-6, 25 epochs


Validación:
*   loss (mse): 1.6204e-06 
*   mean_absolute_error: 8.3836e-04 

Test:
*   loss (mse): 9.5112e-04 
*   mean_absolute_error: 0.0032 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv25.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv25.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 12
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-3
*   Regularización kernel_regularizer='l2'
*   2000 epochs

Validación:
*   loss (mse): 0.0029 
*   mean_absolute_error: 0.0118 

Test:
*   loss (mse): 0.0033 
*   mean_absolute_error: 0.0113 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv27.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv27.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 13
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-5
*   2000 epochs

Validación:
*   loss (mse): 1.8824e-06 
*   mean_absolute_error: 7.7932e-04 

Test:
*   loss (mse): 0.0012 
*   mean_absolute_error: 0.0021 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv28.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv28.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 14
*   6 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-4
*   1 Dropout 0.1
*   2000 epochs

Validación:
*   loss (mse): 1.1545e-05 
*   mean_absolute_error: 0.0023 

Test:
*   loss (mse): 6.6990e-04 
*   mean_absolute_error: 0.0039 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv29.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv29.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 15
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSLE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs


Validación:
*   loss (mse): 3.1211e-06  
*   mean_absolute_error: 0.0023 

Test:
*   loss (mse): 9.7463e-04 
*   mean_absolute_error: 0.0013 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv32.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv32.ipynb) <sub>New Tab CTRL+Clik</sub>


</details>


## Modelos Keras Secuenciales RMSprop
<details>
<summary>Listado</summary>

### Modelo RMSprop 1
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   RMSprop Learning Rate 1e-2
*   2000 epochs

Validación:
*   loss (mse): 6.8896e-05 
*   mean_absolute_error: 0.0056

Test:
*   loss (mse): 5.3990e-04 
*   mean_absolute_error: 0.0057 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv2.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv2.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo RMSprop 2
*   3 capas ocultas densas de 200, 500 y 500 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   RMSprop Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 2.5159e-05 
*   mean_absolute_error: 0.0024

Test:
*   loss (mse): 4.5581e-04 
*   mean_absolute_error: 0.0024 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv6.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv6.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo RMSprop 3
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000 unidades
*   Activación 'Relu'
*   Loss MSE
*   Métrica MAE
*   RMSprop Learning Rate 1e-6
*   2000 epochs

Validación:
*   loss (mse): 1.8369e-05  
*   mean_absolute_error: 0.0023 

Test:
*   loss (mse): 4.5930e-04 
*   mean_absolute_error: 0.0024 

[Archivo: Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv10.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_Keras_Secuenciales/TFM_seq_3cv10.ipynb) <sub>New Tab CTRL+Clik</sub>

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
*   Loss MSE
*   Métrica MAE
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000496
*   Validation Loss (mse): 7.2e-05
*   Validation MAE: 0.005677

Mejor modelo:
*   Validación MAE: 0.005676
*   Test MAE: 0.005525

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_6.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_6.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  2
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Loss MSE
*   Métrica MAE
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000467
*   Validation Loss (mse): 4.4e-05
*   Validation MAE: 0.004237

Mejor modelo:
*   Validación MAE: 0.004171
*   Test MAE: 0.004202

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_1.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_1.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  3
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=5.
*   cutoff_network=HardCutoff
*   Loss MSE
*   Métrica MAE
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000503
*   Validation Loss (mse): 7.5e-05
*   Validation MAE: 0.006146

Mejor modelo:
*   Validación MAE: 0.005361
*   Test MAE: 0.004378

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_4.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_4.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  4
*   n_atom_basis=60
*   n_filters=60
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Loss MSE
*   Métrica MAE
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000665
*   Validation Loss (mse): 0.00023
*   Validation MAE: 0.011497

Mejor modelo:
*   Validación MAE: 0.010837
*   Test MAE: 0.010328

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_2.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_2.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  5
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=HardCutoff
*   Loss MSE
*   Métrica MAE
*   SGD 1e-2 momentum=0.9
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): NaN
*   Validation Loss (mse): NaN
*   Validation MAE: NaN

Mejor modelo:
*   Validación MAE: NaN
*   Test MAE: NaN

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_7.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_7.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo SchNet  6
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000447
*   Validation Loss (mse): 3.2e-05
*   Validation MAE: 0.003575

Mejor modelo:
*   Validación MAE: 0.003342
*   Test MAE: 0.003324

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_3.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_3.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  7
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-7

Modelo final entrenamiento:
*   Train Loss (mse): 0.000463
*   Validation Loss (mse): 6.9e-05
*   Validation MAE: 0.005843

Mejor modelo:
*   Validación MAE: 0.005419
*   Test MAE: 0.006022

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_5.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_5.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  8
*   n_atom_basis=30
*   n_filters=5
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=HardCutoff
*   SGD 1e-4 momentum=0.0
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): NaN
*   Validation Loss (mse): NaN
*   Validation MAE: NaN

Mejor modelo:
*   Validación MAE: NaN
*   Test MAE: NaN

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_8.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_8.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  9
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=20
*   n_interactions=7
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000492
*   Validation Loss (mse): 9.7e-05
*   Validation MAE: 0.006665

Mejor modelo:
*   Validación MAE: 0.005959
*   Test MAE: 0.006080

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_9.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_9.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  10
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=25
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.00051
*   Validation Loss (mse): 7.2e-05
*   Validation MAE: 0.005754

Mejor modelo:
*   Validación MAE: 0.005723
*   Test MAE: 0.005729

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_10.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_10.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  11
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=15
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.00074
*   Validation Loss (mse): 0.000304
*   Validation MAE: 0.012596

Mejor modelo:
*   Validación MAE: 0.012485
*   Test MAE: 0.011284

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_11.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_11.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  12
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=20
*   n_interactions=3
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.00077
*   Validation Loss (mse): 0.000324
*   Validation MAE: 0.013565

Mejor modelo:
*   Validación MAE: 0.013731
*   Test MAE: 0.013398

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_12.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_12.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  13
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=20
*   n_interactions=5
*   cutoff=3.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000509
*   Validation Loss (mse): 9.3e-05
*   Validation MAE: 0.006782

Mejor modelo:
*   Validación MAE: 0.006769
*   Test MAE: 0.007275

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_13.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_13.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet  14
*   n_atom_basis=30
*   n_filters=4
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=HardCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000688
*   Validation Loss (mse): 0.000386
*   Validation MAE: 0.01282

Mejor modelo:
*   Validación MAE: 0.012527
*   Test MAE: 0.011974

[Archivo: Modelos/Modelos_SchNet/SchNet_H2O_14.ipynb](https://nbviewer.jupyter.org/github/chusoHub/TFM_MIA/blob/main/Modelos/Modelos_SchNet/SchNet_H2O_14.ipynb) <sub>New Tab CTRL+Clik</sub>




</details>
