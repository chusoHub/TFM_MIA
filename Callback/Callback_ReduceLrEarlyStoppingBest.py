class ReduceLrEarlyStoppingBest(tf.keras.callbacks.Callback):
  """Detener el entrenamiento cuando la monitorización deja de disminuir.
     Y al acabar el modelo se carga con los pesos del mejor epoch.
     Combina EarlyStopping, ReduceLROnPlateau. 

     Creado a partir del ejemplo EarlyStoppingAtMinLoss de 
     https://www.tensorflow.org/guide/keras/custom_callback?hl=es-419

  Arguments:
      patience: Número de epochs a esperar despues de no haber mejora.
      factor: Número que se multiplicará por lr cuando no mejoré 
              tras cumplirse patience.
      min_lr: Límite inferior de learning rate. Menor valor posible 1e-9!!
      monitor: columna de logs a monitorizar. Menor diferencia detectada 1e-5!!.
  """

  def __init__(self, patience=10, factor=0.1, min_lr = 1e-8, monitor= 'loss'):
    #Inicia class Callback del que toma herencia
    super(ReduceLrEarlyStoppingBest, self).__init__() 

    self.patience = patience
    self.factor= factor
    self.min_lr= min_lr
    self.monitor= monitor

  def on_train_begin(self, logs=None): 
    print('Comienza entrenamiento')
    self.wait = 0 # Número de epoch sin mejora
    self.stopped_epoch = 0 # Epoch de detención anticipada
    self.best = np.inf # mejor valor para monitor
    self.best_epoch = 0 # mejor epoch para monitor
    self.actual_epoch = 0 # epoch actual
    self.best_weights = self.model.get_weights()

  def on_epoch_end(self, epoch, logs=None):
    current = logs.get(self.monitor)
    self.actual_epoch = epoch
    #Si mejora
    if np.less(np.round(current,5), np.round(self.best,5)):
      self.best = current
      self.best_epoch = epoch
      self.wait = 0
      self.best_weights = self.model.get_weights() # Guardar los mejores pesos
      print('Mejor modelo monitor {:g} epoch {:05d}'.format(current, epoch))
    #Si no mejora
    else:
      self.wait += 1
      #Si ha esperado toda la paciencia sin mejorar
      if self.wait >= self.patience:
        lr_actual = tf.keras.backend.get_value(self.model.optimizer.lr)
        #Si ya está en el mínimode lr para
        if not np.greater(np.round(lr_actual,10), np.round(self.min_lr,10)):
            self.stopped_epoch = epoch
            self.model.stop_training = True
            print('Restaurando los pesos del modelo del final de la mejor epoch.')
            self.model.set_weights(self.best_weights)
        #Si no ha llegado al mínimode lr continúa partiendo del mejor
        else:
            self.wait = 0
            lr_futuro = max(lr_actual* self.factor, self.min_lr)
            tf.keras.backend.set_value(self.model.optimizer.lr, lr_futuro)
            print('Nuevo lr {:.2E} en epoch {:05d}.'.format(lr_futuro, epoch+1))
            print('Restaurando pesos del modelo del mejor epoch.')
            self.model.set_weights(self.best_weights)

  def on_train_end(self, logs=None):
    if self.stopped_epoch > 0:
      print('Detencion anticipada!!')
    print('Epoch final %05d' % (self.actual_epoch+1))
    print('{} final: {:g} recuperado del mejor epoch:{:05d}'.format(self.monitor, self.best, self.best_epoch+1))