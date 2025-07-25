import pandas as pd             # Manejo de datasets
import numpy

# Clase simple de acceso al dataset

class DataList:

   def __init__(self, ruta):
        self.data_lis = pd.read_csv(ruta, delimiter=";")
        self.data_lis['code_des']= self.data_lis['code']  + ' - ' + self.data_lis['description']
        self.data_lis = self.data_lis[['idx','code_des']]
        self.data_lis = self.data_lis.iloc[0:-18,0:2]

   # Retorna el dataset leido
   # 
   def GetData(self):
        return (self.data_lis)
   
   # Prepara las filas del dataset para mostrarlas en la lista de selección
   #
   def GetList(self): 
       return (self.data_lis.values.tolist())
   
   def GetItem(self, id):
      return self.data_lis.iloc[id,1:2].values.tolist()

   def ConcatPrediccion(self,prediccion):
      
     df1 = self.data_lis['code_des']
     df2 = prediccion
     result = pd.concat([df1, df2],axis=1)
     return result
      
# Clase que encapsula el comportamiento de los hechos de la red neuronal      

class Hecho:
    def __init__(self):
       self.hecho=  {i:0 for i in range (0,197)} # Deja el hecho todo a cero

    def __init__ (self, 
                    especialidad,
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
       
       self.hecho=  {i:0 for i in range (0,197)} # Deja el hecho todo a cero
       self.hecho.update({especialidad:1})
       self.hecho.update({182:edad})
       self.hecho.update({183: desempleado})
       self.hecho.update({184: ocupado})
       self.hecho.update({186: hombre})
       self.hecho.update({186: mujer})
       self.hecho.update({187: especialidadrequerida})
       self.hecho.update({188: discapacidad})
       self.hecho.update({189: pld})
       self.hecho.update({190: titulacion})
       self.hecho.update({191: orientacion})
       self.hecho.update({192: bajacualificacion})
       self.hecho.update({193: rsb})
       self.hecho.update({194: cobraprestacion})
       self.hecho.update({195: hacursadoaf})
       self.hecho.update({196: hasuperadoaf})

    def GetHecho(self):
        auxdict = self.hecho
        res=pd.Series(auxdict)
        data=numpy.array(res)
        data=data.reshape(1,197)
        return data
    
    def Clear(self):
        self.hecho=  {i:0 for i in range (0,197)} # Deja el hecho todo a cero

    def GetHechoRaw(self):
       return self.hecho
    

# Clase de utilidad que traslada un result WEB a los valores adecuados
# 
#      

class DataWeb:
    def __init__(self):
       self.especialidad=0
       self.edad=0 
       self.desempleado=0 
       self.ocupado=0 
       self.hombre=0
       self.mujer=0 
       self.especialidadrequerida=0 
       self.discapacidad=0
       self.pld=0 
       self.titulacion=0 
       self.orientacion=0
       self.bajacualificacion=0
       self.rsb=0
       self.cobraprestacion=0
       self.hacursadoaf=0 
       self.hasuperadoaf=0

    def __init__(self, especialidad,
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
       
       self.SetEspecialidad(especialidad)
       self.SetEdad(edad)
       self.SetDesempleado(desempleado) 
       self.SetOcupado(ocupado)
       self.SetHombre(hombre)
       self.SetMujer(mujer)
       self.SetEspecialidadRequerida(especialidadrequerida) 
       self.SetDiscapacidad(discapacidad)
       self.SetPld(pld)
       self.SetTitulacion(titulacion) 
       self.SetOrientacion(orientacion)
       self.SetBajaCualificacion(bajacualificacion)
       self.SetRsb(rsb)
       self.SetCobraPrestacion(cobraprestacion)
       self.SetHaCursadoAf(hacursadoaf)
       self.SetHaSuperadoAf(hasuperadoaf)

    def GetEspecialidad(self):
       return self.especialidad
     
    def GetEdad(self):
       return self.edad
    
    def GetDesempleado(self):
       return self.desempleado
    
    def GetOcupado(self):
       return self.ocupado

    def GetHombre(self):
       return self.hombre
    
    def GetMujer(self):
       return self.mujer

    def GetEspecialidadRequerida(self):
       return self.especialidadrequerida
    
    def GetDiscapacidad(self):
       return self.discapacidad
    
    def GetPld(self):
       return self.pld

    def GetTitulacion(self):
       return self.titulacion
    
    def GetOrientacion(self):
       return self.orientacion
    
    def GetBajaCualificacion(self):
       return self.bajacualificacion
    
    def GetRsb(self):
       return self.rsb
    
    def GetCobraPrestacion(self):
       return self.cobraprestacion
    
    def GetHaCursadoAf(self):
       return self.hacursadoaf

    def GetHaSuperadoAf(self):
       return self.hasuperadoaf

    # Setters
    # 

    def SetEspecialidad(self,especialidad):
       self.especialidad = especialidad
    
    def SetEdad(self,edad):
       self.edad = edad

    def SetDesempleado(self,desempleado):
       if desempleado == True:         # Desempleado 
          self.desempleado = 1
       else:
          self.desempleado = 0
    
    def SetOcupado(self,desempleado):
       if desempleado == True:
          self.ocupado = 0
       else:
          self.ocupado = 1
    
    def SetHombre(self,hombre):
       if hombre == True:              # Hombre / mujer
          self.hombre = 1
       else:
          self.hombre = 0
     
    def SetMujer(self,hombre):
       if hombre == True:
          self.mujer = 0
       else:
          self.mujer = 1
    
    def SetEspecialidadRequerida(self, especialidadrequerida): 
       if especialidadrequerida == True: #Especialidad requerida
          self.especialidadrequerida = 1
       else:
          self.especialidadrequerida = 0   
    
    def SetDiscapacidad(self, discapacidad):
       
       if discapacidad == True: #Discapacdad
          self.discapacidad = 1
       else:
          self.discapacidad = 0

    def SetPld(self, pld):  
       if pld == True: #Pld
          self.pld = 1
       else:
          self.pld = 0
    
    def SetTitulacion(self, titulacion):
       if titulacion == True: #Titulacion
          self.titulacion = 1
       else:
          self.titulacion = 0
    def SetOrientacion(self,orientacion):
       if orientacion == True: #orientacion
          self.orientacion = 1
       else:
          self.orientacion = 0
    
    def SetBajaCualificacion(self, bajacualificacion):  
       if bajacualificacion == True: #bajaCualificacion
          self.bajacualificacion = 1
       else:
          self.bajacualificacion = 0

    def SetRsb(self, rsb):   
       if rsb == True: #rsb
          self.rsb = 1
       else:
          self.rsb = 0

    def SetCobraPrestacion(self, cobraprestacion):  
       if cobraprestacion == True: #cobraPrestacion
          self.cobraprestacion = 1
       else:
          self.cobraprestacion = 0  
       
    def SetHaCursadoAf(self, hacursadoaf):   
       if hacursadoaf == True: #haCursadoAf
          self.hacursadoaf = 1
       else:
          self.hacursadoaf = 0  
       
    def SetHaSuperadoAf(self, hasuperadoaf):   
       if hasuperadoaf == True: #haSuperadoAf
          self.hasuperadoaf = 1
       else:
          self.hasuperadoaf = 0  
