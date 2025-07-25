import keras
import numpy
import pandas as pd
from data import DataList


class Red:
    def __init__(self,ruta):
       self.model = keras.models.load_model(ruta)

    def Predict(self,data):
       return self.model.predict(data)
    
    def GenerarCasos(self,
                     edad, 
                      desempleado,
                      ocupado, 
                      hombre,
                      mujer, 
                      especialidadrequerida, 
                      discapacidad,
                      pld, 
                      titulacion, 
                      orientacion,
                      bajacualificacion,
                      rsb,
                      cobraprestacion,
                      hacursadoaf, 
                      hasuperadoaf):
       self.datos = numpy.zeros(197)
       self.datos[0]=1
       self.datos[182] = edad
       self.datos[183] = desempleado
       self.datos[184] = ocupado
       self.datos[185] = hombre
       self.datos[186] = mujer
       self.datos[187] = especialidadrequerida
       self.datos[188] = discapacidad
       self.datos[189] = pld
       self.datos[190] = titulacion
       self.datos[191] = orientacion
       self.datos[192] = bajacualificacion
       self.datos[193] = rsb
       self.datos[194] = cobraprestacion
       self.datos[195] = hacursadoaf
       self.datos[196] = hasuperadoaf

       for i in range (1,182):
          caso = numpy.zeros(197)
          caso[i]=1
          caso[182] = edad
          caso[183] = desempleado
          caso[184] = ocupado
          caso[185] = hombre
          caso[186] = mujer
          caso[187] = especialidadrequerida
          caso[188] = discapacidad
          caso[189] = pld
          caso[190] = titulacion
          caso[191] = orientacion
          caso[192] = bajacualificacion
          caso[193] = rsb
          caso[194] = cobraprestacion
          caso[195] = hacursadoaf
          caso[196] = hasuperadoaf
          self.datos=numpy.concatenate((self.datos, caso), axis=None)
       return self.datos.reshape(182,197)


