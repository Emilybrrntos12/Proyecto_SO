def planificacion_prioridad():
    num_procesos = int(input("Ingrese el número de procesos: "))

    # Crear listas separadas para procesos con tiempo de llegada 0 y otros procesos
    procesos_llegada_cero = []
    procesos_prioridad = []

    # Solicitar información de cada proceso al usuario
    for i in range(num_procesos):
        nombre = input(f"Ingrese el nombre del proceso {i + 1}: ")
        rafaga = int(input(f"Ingrese la Rafaga de CPU del proceso {i + 1}: "))
        tiempoLlegada = int(input(f"Ingrese la duración del proceso {i + 1}: "))
        prioridad = int(input(f"Ingrese el tiempo de llegada del proceso {i + 1}: "))

        proceso = {"nombre": nombre, "rafaga": rafaga, "tiempoLlegada": tiempoLlegada, "prioridad" : prioridad}

        if tiempoLlegada == 0:
            procesos_llegada_cero.append(proceso)
        else:
            procesos_prioridad.append(proceso)


    # Ordenar los procesos de llegada cero por duración y luego por prioridad
    procesos_llegada_cero.sort(key=lambda x: (x["tiempoLlegada"], x["prioridad"]))
    
    # Inicializar la variable tiempo_total
    tiempo_total = 0

    # Si solo hay un proceso con tiempo de llegada igual a 0, ejecutarlo de inmediato
    if len(procesos_llegada_cero) == 1:
        proceso_unico = procesos_llegada_cero.pop(0)
        print(f"Ejecutando {proceso_unico['nombre']} (Rafaga: {proceso_unico['rafaga']}, TiempoLlegada: {proceso_unico['tiempoLlegada']}, Prioridad: {proceso_unico['prioridad']})")
        tiempo_total += proceso_unico['rafaga']

    # Si hay más de un proceso con llegada igual a 0, tomar el de menor duración
    if len(procesos_llegada_cero) > 1:
        # Ordenar los procesos de llegada cero por prioridad
        procesos_llegada_cero.sort(key=lambda x: x["prioridad"])
        # Tomar el proceso de menor prioridad
        proceso_elegido = procesos_llegada_cero.pop(0)
        print(f"Ejecutando {proceso['nombre']} (Rafaga: {proceso['rafaga']}, TiempoLlegada: {proceso['tiempoLlegada']}, Prioridad: {proceso['prioridad']})")
        tiempo_total += proceso_elegido['rafaga']

        # Insertar los demás procesos de llegada cero en la lista ordenada
        for proceso in procesos_llegada_cero:
            procesos_prioridad.insert(0, proceso)

    # Ordenar los otros procesos por prioridad y luego por duración
    procesos_prioridad.sort(key=lambda x: (x["prioridad"], x["tiempoLlegada"]))

    # Ejecutar los demás procesos por prioridad y duración
    for proceso in procesos_prioridad:
        print(f"Ejecutando {proceso['nombre']} (Rafaga: {proceso['rafaga']}, TiempoLlegada: {proceso['tiempoLlegada']}, Prioridad: {proceso['prioridad']})")
        tiempo_total += proceso['rafaga']


    print(f"Tiempo total de ejecución: {tiempo_total}")

if __name__ == "__main__":
    planificacion_prioridad()





