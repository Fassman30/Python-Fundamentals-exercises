def tareas_pendientes():
    #Creamos la lista
    tareas_pendientes=["Investigar algoritmos", "Preparar datos", "Entrenar modelo", "Evaluar resultados"]
    #Imprimimos la lista completa
    print(f"La lista es {tareas_pendientes}")
    #Imprimimos la primera y ultima Tarea de la lista
    print(f"la primera tarea es: {tareas_pendientes[0]}")
    print(f"la ultima tarea es : {tareas_pendientes[-1]} ")
    #Verificamos si una de las tareas esta lista 
    if "Preparar datos" in tareas_pendientes:
     print("La tarea 'Preparar datos' está en la lista.")
    else:
     print("La tarea 'Preparar datos' NO está en la lista.")   
    #Modificamos el valor dos ya que entrenar esta listo
    tareas_pendientes[2]= 'Entrenar modelo (COMPLETADO) '
    #Modificamos pocisiones
    tarea_mover=tareas_pendientes.pop(0)
    tareas_pendientes.insert(1,tarea_mover)
    #Eliminamos la tarea evaluar resultados
    tareas_pendientes.remove("Evaluar resultados")
    print(f"se ah eliminado evaluar resultados ya que la tarea esta OKS")
    print(f"la lista ahora es : {tareas_pendientes}")
    
tareas_pendientes()