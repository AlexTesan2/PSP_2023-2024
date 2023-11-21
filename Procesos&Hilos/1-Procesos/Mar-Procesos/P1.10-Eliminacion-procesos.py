import psutil

for proc in psutil.process_iter():    # Itera sobre todos los procesos en ejecución.
  try:
    # Obtener el nombre del proceso
    nombreProceso = proc.name()   
    
    if proc.name() == "gedit":

      # Obtener el ID de proceso (gedit)
      PID = proc.pid

      # Obtener el nombre de usuario del propietario del proceso
      print(proc.username())
      print("Eliminando el proceso: ", nombreProceso , ' ::: ', PID)

      # Eliminar el proceso
      proc.kill()    
  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    print ("error")

