# TFM_MIA
## Inspección visual de los datos
[Archivo: Datos/Inspección_visual_TFM.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Datos/Inspección_visual_TFM.ipynb) <sub>New Tab CTRL+Clik</sub>

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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_1.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_1.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_2.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_2.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_3.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_3.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_4.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_4.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_5.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_5.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_6.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_6.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_7.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos%20Keras%20Secuenciales/keras_seq_sgd_7.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_8.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_8.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_9.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_9.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_10.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_10.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_11.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_11.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 12
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   2000 epochs
*   Reentrenamiento 1e-4, 25 epochs

Validación:
*   loss (mse): 9.2066e-06
*   mean_absolute_error: 0.0010

Test:
*   loss (mse): 4.7189e-04 
*   mean_absolute_error: 0.0015

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_12.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_12.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_13.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_13.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_14.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_14.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_15.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_15.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SGD 16
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   SGD Learning Rate 1e-2 Momentum 0.0
*   ReduceLrEarlyStoppingBest 1e-6
*   5000 epochs


Validación:
*   loss (mse): 0.0011
*   mean_absolute_error: 1.0106e-05

Test:
*   loss (msle): 4.7435e-04
*   mean_absolute_error: 0.0016

[Archivo: Modelos_Keras_Secuenciales/keras_seq_sgd_16.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_sgd_16.ipynb) <sub>New Tab CTRL+Clik</sub>


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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_1.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_1.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_2.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_2.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_3.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_3.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_4.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_4.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_5.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_5.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_6.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_6.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_7.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_7.ipynb) <sub>New Tab CTRL+Clik</sub>

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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_8.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_8.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_9.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_9.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_10.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_10.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_11.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_11.ipynb) <sub>New Tab CTRL+Clik</sub>

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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_12.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_12.ipynb) <sub>New Tab CTRL+Clik</sub>

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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_13.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_13.ipynb) <sub>New Tab CTRL+Clik</sub>

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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_14.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_14.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 15
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSLE
*   Métrica MAE
*   Adam Learning Rate 1e-6
*   2000 epochs


Validación:
*   loss (msle): 3.1211e-06  
*   mean_absolute_error: 0.0023 

Test:
*   loss (msle): 9.7463e-04 
*   mean_absolute_error: 0.0013 

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_15.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_15.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 16
*   5 capas ocultas densas de 500, 1000, 1000, 2000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-4
*   ReduceLrEarlyStoppingBest 1e-10
*   5000 epochs

Validación:
*   loss (mse): 3.6459e-07
*   mean_absolute_error: 3.5422e-04

Test:
*   loss (mse): 0.0011
*   mean_absolute_error: 0.0023

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_16.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_16.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo Adam 17
*   5 capas ocultas densas de 200, 500, 500, 1000, 1000, 2000 unidades
*   Activación LeakyReLU(alpha=0.1)
*   Loss MSE
*   Métrica MAE
*   Adam Learning Rate 1e-2
*   15 epochs
*   Reentrenamiento 1e-4 50
*   Reentrenamiento 1e-6 1500

Validación:
*   loss (mse): 2.8956e-05
*   mean_absolute_error: 0.0033

Test:
*   loss (mse): 0.0015
*   mean_absolute_error: 0.0246

[Archivo: Modelos_Keras_Secuenciales/keras_seq_adam_17.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_adam_17.ipynb) <sub>New Tab CTRL+Clik</sub>


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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_rmsprop_1.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_rmsprop_1.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_rmsprop_2.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_rmsprop_2.ipynb) <sub>New Tab CTRL+Clik</sub>
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

[Archivo: Modelos_Keras_Secuenciales/keras_seq_rmsprop_3.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_Keras_Secuenciales/keras_seq_rmsprop_3.ipynb) <sub>New Tab CTRL+Clik</sub>

</details>

## Modelos SchNet
<details>
<summary>Listado</summary>

### Modelo SchNet 1
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
*   Train Loss (mse): 0.000449
*   Validation Loss (mse): 4.7e-05
*   Validation MAE:  0.004662

Mejor modelo:
*   Validación MAE: 0.003593
*   Test MAE: 0.003493

[Archivo: Modelos_SchNet/schnet_1.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_1.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet 2
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
*   Train Loss (mse): 0.000441
*   Validation Loss (mse): 3.8e-05
*   Validation MAE: 0.003866

Mejor modelo:
*   Validación MAE: 0.003486
*   Test MAE: 0.003183

[Archivo: Modelos_SchNet/schnet_2.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_2.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet 3
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
*   Train Loss (mse): 0.000517
*   Validation Loss (mse): 9.5e-05
*   Validation MAE: 0.006974

Mejor modelo:
*   Validación MAE: 0.006181
*   Test MAE: 0.006842

[Archivo: Modelos_SchNet/schnet_3.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_3.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet 4
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
*   Train Loss (mse): 0.00057
*   Validation Loss (mse): 0.000148
*   Validation MAE: 0.008312

Mejor modelo:
*   Validación MAE: 0.008167
*   Test MAE: 0.006875

[Archivo: Modelos_SchNet/schnet_4.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_4.ipynb) <sub>New Tab CTRL+Clik</sub>
### Modelo SchNet 5
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

[Archivo: Modelos_SchNet/schnet_5.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_5.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo SchNet 6
*   n_atom_basis=30
*   n_filters=10
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse): 0.000457
*   Validation Loss (mse): 3.7e-05
*   Validation MAE: 0.003695

Mejor modelo:
*   Validación MAE: 0.003515
*   Test MAE: 0.003460

[Archivo: Modelos_SchNet/schnet_6.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_6.ipynb) <sub>New Tab CTRL+Clik</sub>
<!--### Modelo SchNet  7
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6
*   Loss MSLE

Modelo final entrenamiento:
*   Train Loss (msle): 
*   Validation Loss (msle): 
*   Validation MAE: 

Mejor modelo:
*   Validación MAE: 
*   Test MAE: 

[Archivo: Modelos_SchNet/schnet_7.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_7.ipynb) <sub>New Tab CTRL+Clik</sub>-->

### Modelo SchNet 7
*   n_atom_basis=20
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-2
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento:
*   Train Loss (mse):  0.000478
*   Validation Loss (mse): 5.1e-05
*   Validation MAE: 0.004724

Mejor modelo:
*   Validación MAE: 0.004733
*   Test MAE: 0.005014

[Archivo: Modelos_SchNet/schnet_7.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_7.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo SchNet 8
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

[Archivo: Modelos_SchNet/schnet_8.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_8.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.000724
*   Validation Loss (mse): 0.000303
*   Validation MAE: 0.012093

Mejor modelo:
*   Validación MAE: 0.011866
*   Test MAE: 0.012190

[Archivo: Modelos_SchNet/schnet_9.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_9.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.000505
*   Validation Loss (mse): 0.000117
*   Validation MAE: 0.007442

Mejor modelo:
*   Validación MAE: 0.007177
*   Test MAE: 0.007547

[Archivo: Modelos_SchNet/schnet_10.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_10.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.00048
*   Validation Loss (mse): 5.3e-05
*   Validation MAE: 0.004568

Mejor modelo:
*   Validación MAE: 0.004423
*   Test MAE: 0.004422

[Archivo: Modelos_SchNet/schnet_11.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_11.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.000483
*   Validation Loss (mse): 9.9e-05
*   Validation MAE: 0.00697

Mejor modelo:
*   Validación MAE: 0.006397
*   Test MAE: 0.006441

[Archivo: Modelos_SchNet/schnet_12.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_12.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.000468
*   Validation Loss (mse): 5.2e-05
*   Validation MAE: 0.005068

Mejor modelo:
*   Validación MAE: 0.004998
*   Test MAE: 0.005234

[Archivo: Modelos_SchNet/schnet_13.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_13.ipynb) <sub>New Tab CTRL+Clik</sub>
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
*   Train Loss (mse): 0.000605
*   Validation Loss (mse): 0.000194
*   Validation MAE: 0.009697

Mejor modelo:
*   Validación MAE: 0.009563
*   Test MAE: 0.008450

[Archivo: Modelos_SchNet/schnet_14.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_14.ipynb) <sub>New Tab CTRL+Clik</sub>

### Modelo SchNet  15
*   n_atom_basis=30
*   n_filters=30
*   n_gaussians=20
*   n_interactions=5
*   cutoff=4.
*   cutoff_network=CosineCutoff
*   Adam 1e-4
*   ReduceLROnPlateauHook hasta 1e-6

Modelo final entrenamiento: 
*   Train Loss (mse): 0.001561
*   Validation Loss (mse): 0.000982
*   Validation MAE: 0.023362

Mejor modelo:
*   Validación MAE: 0.021679
*   Test MAE: 0.023327

[Archivo: Modelos_SchNet/schnet_15.ipynb](https://github.com/chusoHub/TFM_MIA/blob/main/Modelos_SchNet/schnet_15.ipynb) <sub>New Tab CTRL+Clik</sub>

</details>
