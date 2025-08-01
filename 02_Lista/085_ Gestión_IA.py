def gestion_IA_organizada():
    proyectos_ia = {
        "Reconocimiento Facial": {
            "descripcion": "Modelo para identificar rostros en imágenes.",
            "tareas":
            [
                ("Recopilar dataset", True),
                ("Entrenar CNN", False),
                ("Optimizar rendimiento", False)
            ],
            "configuracion": {
                "learning_rate": 0.001,
                "epochs": 50,
                "modelo_base": "ResNet50"
            }
        },
        "Procesamiento Lenguaje Natural": { # Añadimos otro proyecto para ver la iteración
            "descripcion": "Análisis de sentimientos en reseñas de clientes.",
            "tareas": [
                ("Limpiar texto", True),
                ("Vectorizar datos", True),
                ("Construir modelo NLP", False)
            ],
            "configuracion": {
                "embedding_dim": 100,
                "vocab_size": 10000
            }
        }
    }

    # --- Realizamos las modificaciones como antes ---
    # Modificar tarea
    tareas_rf = proyectos_ia["Reconocimiento Facial"]["tareas"]
    nueva_tarea_entrenar_cnn = ("Entrenar CNN", True)
    tareas_rf[1] = nueva_tarea_entrenar_cnn

    # Añadir batch_size
    proyectos_ia["Reconocimiento Facial"]["configuracion"]["batch_size"] = 32

    print("\n--- ¡Aquí tus proyectos de IA organizados! ---")
   # Iteramos sobre cada proyecto en el diccionario principal
    for nombre_proyecto, datos_proyecto in proyectos_ia.items():
        print(f"\n## Proyecto: {nombre_proyecto}")
        print(f"  Descripción: {datos_proyecto['descripcion']}")

        # Imprimir Tareas
        print("  Tareas:")
        tareas_pendientes_count = 0
        for i, (tarea_nombre, estado) in enumerate(datos_proyecto["tareas"]):
            # Usamos enumerate para obtener también el índice (i)
            # Y ajustamos el conteo de pendientes aquí también
            estado_str = "✔️ Completada" if estado else "❌ Pendiente"
            print(f"    {i + 1}. {tarea_nombre}: {estado_str}")
            if not estado:
                tareas_pendientes_count += 1
        print(f"  Total tareas pendientes para este proyecto: {tareas_pendientes_count}")

        # Imprimir Configuración
        print("  Configuración del Modelo:")
        for parametro, valor in datos_proyecto["configuracion"].items():
            print(f"    - {parametro}: {valor}")
        
        print("---") # Separador visual entre proyectos

# Llama a la función para ver el resultado organizado
gestion_IA_organizada()