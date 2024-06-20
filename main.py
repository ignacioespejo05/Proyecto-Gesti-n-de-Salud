import datetime
import pandas as pd

# Clase Usuario
class Usuario:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.actividades = []
        self.alimentos = []
        self.sueno = []

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")
    
    def agregar_actividad(self, actividad):
        if isinstance(actividad, ActividadFisica):
            self.actividades.append(actividad)
        else:
            raise ValueError("El objeto no es una instancia de ActividadFisica")

    def agregar_alimento(self, alimento):
        if isinstance(alimento, ConsumoAlimentos):
            self.alimentos.append(alimento)
        else:
            raise ValueError("El objeto no es una instancia de ConsumoAlimentos")

    def agregar_sueno(self, sueno):
        if isinstance(sueno, MonitorSueño):
            self.sueno.append(sueno)
        else:
            raise ValueError("El objeto no es una instancia de MonitorSueño")

    def guardar_datos(self, filename):
        datos = {
            "actividades": [actividad.__dict__ for actividad in self.actividades],
            "alimentos": [alimento.__dict__ for alimento in self.alimentos],
            "sueno": [sueno.__dict__ for sueno in self.sueno]
        }
        df = pd.DataFrame(datos)
        df.to_csv(filename, index=False)
        print(f"Datos guardados en {filename}")

    def cargar_datos(self, filename):
        df = pd.read_csv(filename)
        for idx, row in df.iterrows():
            self.actividades.append(ActividadFisica(**row["actividades"]))
            self.alimentos.append(ConsumoAlimentos(**row["alimentos"]))
            self.sueno.append(MonitorSueño(**row["sueno"]))
        print(f"Datos cargados desde {filename}")

class ActividadFisica:
    def __init__(self, tipo, duracion_minutos, calorias_quemadas):
        self.tipo = tipo
        self.duracion_minutos = duracion_minutos
        self.calorias_quemadas = calorias_quemadas
        self.fecha_hora = datetime.datetime.now()

    def mostrar_actividad(self):
        print(f"Actividad: {self.tipo}")
        print(f"Duración: {self.duracion_minutos} minutos")
        print(f"Calorías quemadas: {self.calorias_quemadas}")
        print(f"Fecha y hora: {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}")

class ConsumoAlimentos:
    def __init__(self, nombre, cantidad_gramos, calorias):
        self.nombre = nombre
        self.cantidad_gramos = cantidad_gramos
        self.calorias = calorias
        self.fecha_hora = datetime.datetime.now()

    def mostrar_alimento(self):
        print(f"Alimento: {self.nombre}")
        print(f"Cantidad: {self.cantidad_gramos} gramos")
        print(f"Calorías: {self.calorias}")
        print(f"Fecha y hora: {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}")

class MonitorSueño:
    def __init__(self, horas_dormidas, calidad_sueno):
        self.horas_dormidas = horas_dormidas
        self.calidad_sueno = calidad_sueno
        self.fecha = datetime.date.today()

    def mostrar_sueno(self):
        print(f"Horas dormidas: {self.horas_dormidas}")
        print(f"Calidad del sueño: {self.calidad_sueno}")
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d')}")
