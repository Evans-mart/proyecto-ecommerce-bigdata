from pyspark.sql import SparkSession
import time

if __name__ == "__main__":
    # Inicialización de la sesión de Spark
    spark = SparkSession.builder \
        .appName("Validacion_Final_Sincronizada_Blanca") \
        .getOrCreate()

    sc = spark.sparkContext
    
    print("\n" + "="*80)
    print("   CLUSTER VALIDADO: BLANCA + EVANS + GAMALIEL")
    print(f"   IP Master: 10.150.6.118")
    print("="*80)

    # 500 particiones para forzar el reparto de tareas
    num_elementos = 20000000
    rdd = sc.parallelize(range(num_elementos), 500)

    def tarea_con_carga(x):
        time.sleep(0.08)
        return x + 1

    print("\n[INFO] Lanzando procesamiento distribuido masivo...")
    inicio = time.time()
    
    # Realizamos la acción
    total_procesado = rdd.map(tarea_con_carga).count()
    
    fin = time.time()

    print(f"\n[ÉXITO] El cluster completo procesó {total_procesado} registros.")
    print(f"[TIEMPO] Duración: {fin - inicio:.2f} segundos")

    # Pausa de Auditoría
    print("\n" + "!"*80)
    print(">>> AUDITORÍA: Tienes 90 segundos para capturar la tabla de Executors.")
    print(">>> URL: http://10.150.6.118:4040/executors/")
    print("!"*80)
    
    time.sleep(90)
    spark.stop()