import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Inicialización de Colorama
init()

class Usuario:
    def __init__(self, nombre, edad, peso, altura, ci):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.ci = ci
        self.imc = self.calcular_imc()

    def calcular_imc(self):
        if self.altura > 0:
            return round(self.peso / ((self.altura / 100) ** 2), 2)
        return 0

    def actualizar_peso(self, nuevo_peso):
        self.peso = nuevo_peso
        self.imc = self.calcular_imc()
        self.guardar_datos()
        print("Peso actualizado.")

    def guardar_datos(self):
        filename = "usuarios.csv"
        datos_usuario = {
            'CI': [self.ci],
            'Nombre': [self.nombre],
            'Edad': [self.edad],
            'Peso': [self.peso],
            'Altura': [self.altura],
            'IMC': [self.imc]
        }
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            if str(self.ci) in df['CI'].astype(str).values:
                df.loc[df['CI'].astype(str) == str(self.ci), ['Nombre', 'Edad', 'Peso', 'Altura', 'IMC']] = [
                    self.nombre, self.edad, self.peso, self.altura, self.imc]
            else:
                df = pd.concat([df, pd.DataFrame(datos_usuario)], ignore_index=True)
        else:
            df = pd.DataFrame(datos_usuario)
        
        df.to_csv(filename, index=False)
        print(f"Datos de usuario actualizados en {filename}")

class ConsumoAlimentos:
    def __init__(self, ci_usuario, nombre_alimento, cantidad_gramos, calorias):
        self.ci_usuario = ci_usuario
        self.nombre_alimento = nombre_alimento
        self.cantidad_gramos = cantidad_gramos
        self.calorias = calorias
        self.fecha_hora = datetime.datetime.now()

    def guardar_datos(self):
        filename = "consumo_alimentos.csv"
        datos = {
            'CI Usuario': [self.ci_usuario],
            'Nombre Alimento': [self.nombre_alimento],
            'Cantidad Gramos': [self.cantidad_gramos],
            'Calorías': [self.calorias],
            'Fecha Hora': [self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')]
        }
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            df = pd.concat([df, pd.DataFrame(datos)], ignore_index=True)
        else:
            df = pd.DataFrame(datos)
        df.to_csv(filename, index=False)
        print(f"Datos de consumo de alimentos actualizados en {filename}")

class ActividadFisica:
    def __init__(self, ci_usuario, tipo_actividad, duracion_minutos, calorias_quemadas):
        self.ci_usuario = ci_usuario
        self.tipo_actividad = tipo_actividad
        self.duracion_minutos = duracion_minutos
        self.calorias_quemadas = calorias_quemadas
        self.fecha_hora = datetime.datetime.now()

    def guardar_datos(self):
        filename = "actividad_fisica.csv"
        datos = {
            'CI Usuario': [self.ci_usuario],
            'Tipo Actividad': [self.tipo_actividad],
            'Duración Minutos': [self.duracion_minutos],
            'Calorías Quemadas': [self.calorias_quemadas],
            'Fecha Hora': [self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')]
        }
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            df = pd.concat([df, pd.DataFrame(datos)], ignore_index=True)
        else:
            df = pd.DataFrame(datos)
        df.to_csv(filename, index=False)
        print(f"Datos de actividad física actualizados en {filename}")

class MonitorSueño:
    def __init__(self, ci_usuario, horas_dormidas):
        self.ci_usuario = ci_usuario
        self.horas_dormidas = horas_dormidas
        self.fecha = datetime.date.today()

    def guardar_datos(self):
        filename = "monitor_sueno.csv"
        datos = {
            'CI Usuario': [self.ci_usuario],
            'Horas Dormidas': [self.horas_dormidas],
            'Fecha': [self.fecha.strftime('%Y-%m-%d')]
        }
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            df = pd.concat([df, pd.DataFrame(datos)], ignore_index=True)
        else:
            df = pd.DataFrame(datos)
        df.to_csv(filename, index=False)
        print(f"Datos de sueño actualizados en {filename}")

class SistemaGestionSalud:
    def __init__(self):
        if os.path.exists("usuarios.csv"):
            self.usuarios = pd.read_csv("usuarios.csv")
        else:
            self.usuarios = pd.DataFrame(columns=['CI', 'Nombre', 'Edad', 'Peso', 'Altura', 'IMC'])

    def menu(self):
        while True:
            print(Fore.MAGENTA + Style.BRIGHT + """
                                 _   _            _ _   _     _____  __    ___  
                *   *    *      | | | | ___  __ _| | |_| |__ |___ / / /_  / _ \   *   *    *
                *   *    *      | |_| |/ _ \/ _` | | __| '_ \  |_ \| '_ \| | | | *    *   *
               *   *    *       |  _  |  __/ (_| | | |_| | | |___) | (_) | |_| |    *  *
                *   *    *      |_| |_|\___|\__,_|_|\__|_| |_|____/ \___/ \___/   *     *
                                                                
                                                                
            """)
            print(Fore.RED + Style.BRIGHT + "\n--- Menú del Sistema de Gestión de Salud ---")
            print(Fore.CYAN + Style.BRIGHT +"1. Registrar nuevo usuario")
            print("2. Actualizar perfil de usuario")
            print("3. Registrar consumo de alimentos")
            print("4. Registrar actividad física")
            print("5. Registrar horas de sueño")
            print("6. Evaluar salud del usuario")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_usuario()
            elif opcion == '2':
                ci = input("Ingrese su CI: ")
                nuevo_peso = float(input("Ingrese su nuevo peso: "))
                self.actualizar_usuario(ci, nuevo_peso)
            elif opcion == '3':
                self.registrar_consumo_alimentos()
            elif opcion == '4':
                self.registrar_actividad_fisica()
            elif opcion == '5':
                self.registrar_sueno()
            elif opcion == '6':
                ci = input("Ingrese su CI para evaluar salud: ")
                self.evaluar_salud_usuario(ci)
            elif opcion == '7':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        peso = float(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura en cm: "))
        ci = input("Ingrese su CI: ")
        nuevo_usuario = Usuario(nombre, edad, peso, altura, ci)
        nuevo_usuario.guardar_datos()
        self.usuarios = pd.read_csv("usuarios.csv")
        print("Usuarios después de registrar:")
        print(self.usuarios)

    def actualizar_usuario(self, ci, nuevo_peso):
        ci = str(ci)
        print(f"Actualizando usuario con CI: {ci}")  # Depuración
        print("Usuarios actuales en el sistema:")
        print(self.usuarios)  # Para verificar el contenido del DataFrame

        if ci in self.usuarios['CI'].astype(str).values:
            index = self.usuarios[self.usuarios['CI'].astype(str) == ci].index[0]
            self.usuarios.at[index, 'Peso'] = nuevo_peso
            self.usuarios.at[index, 'IMC'] = Usuario(self.usuarios.at[index, 'Nombre'], self.usuarios.at[index, 'Edad'],
                                                     nuevo_peso, self.usuarios.at[index, 'Altura'], ci).calcular_imc()
            self.usuarios.to_csv("usuarios.csv", index=False)
            print("Perfil actualizado correctamente.")
        else:
            print("Usuario no encontrado.")

    def registrar_consumo_alimentos(self):
        ci = input("Ingrese su CI: ")
        nombre_alimento = input("Ingrese el nombre del alimento: ")
        cantidad_gramos = int(input("Ingrese la cantidad en gramos: "))
        calorias = int(input("Ingrese las calorías: "))
        consumo = ConsumoAlimentos(ci, nombre_alimento, cantidad_gramos, calorias)
        consumo.guardar_datos()

    def registrar_actividad_fisica(self):
        ci = input("Ingrese su CI: ")
        tipo_actividad = input("Ingrese el tipo de actividad: ")
        duracion_minutos = int(input("Ingrese la duración en minutos: "))
        calorias_quemadas = int(input("Ingrese las calorías quemadas: "))
        actividad = ActividadFisica(ci, tipo_actividad, duracion_minutos, calorias_quemadas)
        actividad.guardar_datos()

    def registrar_sueno(self):
        ci = input("Ingrese su CI: ")
        horas_dormidas = float(input("Ingrese las horas dormidas: "))
        sueno = MonitorSueño(ci, horas_dormidas)
        sueno.guardar_datos()

    def evaluar_salud_usuario(self, ci):
        ci = str(ci)
        print(f"Evaluando salud para CI: {ci}")  # Depuración
        print("Usuarios actuales en el sistema:")
        print(self.usuarios)  # Para verificar el contenido del DataFrame

        if ci in self.usuarios['CI'].astype(str).values:
            usuario = self.usuarios[self.usuarios['CI'].astype(str) == ci].iloc[0]
            puntos_salud, detalles_salud = self.calcular_puntuacion_salud(usuario)
            print(f"Evaluación de salud para {usuario['Nombre']}: {puntos_salud} puntos")
            self.generar_grafico_evaluacion(usuario, detalles_salud)
        else:
            print("Usuario no encontrado.")

    def calcular_puntuacion_salud(self, usuario):
        puntos = 0
        detalles_salud = {}

        # Evaluar sueño
        horas_sueno = self.obtener_horas_sueno(usuario['CI'])
        if horas_sueno >= 8:
            puntos += 25
            detalles_salud['Sueño'] = 25
        elif 6 <= horas_sueno < 8:
            puntos += 20
            detalles_salud['Sueño'] = 20
        elif 4 <= horas_sueno < 6:
            puntos += 10
            detalles_salud['Sueño'] = 10
        else:
            detalles_salud['Sueño'] = 0

        # Evaluar IMC
        imc = usuario['IMC']
        if imc <= 16 or imc > 30:
            detalles_salud['IMC'] = 0
        elif 17 <= imc < 18.5:
            puntos += 10
            detalles_salud['IMC'] = 10
        elif 18.5 <= imc < 25:
            puntos += 25
            detalles_salud['IMC'] = 25
        elif 25 <= imc < 30:
            puntos += 10
            detalles_salud['IMC'] = 10

        # Evaluar alimentos
        calorias_consumidas, calorias_quemadas = self.obtener_calorias(usuario['CI'])
        diferencia_calorias = calorias_consumidas - calorias_quemadas
        if diferencia_calorias > 1000:
            detalles_salud['Alimentos'] = 0
        elif 500 < diferencia_calorias <= 1000:
            puntos += 10
            detalles_salud['Alimentos'] = 10
        elif 0 <= diferencia_calorias <= 500:
            puntos += 25
            detalles_salud['Alimentos'] = 25
            puntos += 20
        elif diferencia_calorias < 0 :
            detalles_salud['Alimentos'] = 0
        else:
            puntos += 20
            detalles_salud['Alimentos'] = 20

        # Evaluar ejercicio
        duracion_ejercicio = self.obtener_duracion_ejercicio(usuario['CI'])
        if duracion_ejercicio >= 60:
            puntos += 25
            detalles_salud['Ejercicio'] = 25
        elif 45 <= duracion_ejercicio < 60:
            puntos += 20
            detalles_salud['Ejercicio'] = 20
        elif 30 <= duracion_ejercicio < 45:
            puntos += 15
            detalles_salud['Ejercicio'] = 15
        elif duracion_ejercicio < 30:
            puntos += 10
            detalles_salud['Ejercicio'] = 10
        else:
            detalles_salud['Ejercicio'] = 0

        return puntos, detalles_salud

    def obtener_horas_sueno(self, ci):
        try:
            df = pd.read_csv("monitor_sueno.csv")
            horas_sueno = df[df['CI Usuario'].astype(str) == ci]['Horas Dormidas'].mean()
            return horas_sueno
        except FileNotFoundError:
            return 0

    def obtener_calorias(self, ci):
        try:
            df_alimentos = pd.read_csv("consumo_alimentos.csv")
            df_actividad = pd.read_csv("actividad_fisica.csv")
            calorias_consumidas = df_alimentos[df_alimentos['CI Usuario'].astype(str) == ci]['Calorías'].sum()
            calorias_quemadas = df_actividad[df_actividad['CI Usuario'].astype(str) == ci]['Calorías Quemadas'].sum()
            return calorias_consumidas, calorias_quemadas
        except FileNotFoundError:
            return 0, 0

    def obtener_duracion_ejercicio(self, ci):
        try:
            df = pd.read_csv("actividad_fisica.csv")
            duracion_ejercicio = df[df['CI Usuario'].astype(str) == ci]['Duración Minutos'].sum()
            return duracion_ejercicio
        except FileNotFoundError:
            return 0

    def generar_grafico_evaluacion(self, usuario, detalles_salud):
        categorias = list(detalles_salud.keys())
        puntajes = list(detalles_salud.values())

        plt.figure(figsize=(10, 6))
        plt.bar(categorias, puntajes, color='skyblue')
        plt.xlabel('Categorías')
        plt.ylabel('Puntaje')
        plt.title(f'Evaluación de Salud para {usuario["Nombre"]}')
        plt.ylim(0, 25)

        for i in range(len(categorias)):
            plt.text(i, puntajes[i] + 0.5, str(puntajes[i]), ha='center')

        plt.show()

# Inicialización y ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaGestionSalud()
    sistema.menu()
