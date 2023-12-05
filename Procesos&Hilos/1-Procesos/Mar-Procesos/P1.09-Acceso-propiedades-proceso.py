import psutil
import os
import subprocess
import sys

def ProcesoActual ():
  return psutil.Process(os.getpid())

def esWindows():
  try:
    sys.getwindowsversion()
  except AttributeError:
    return (False)
  else:
    return (True)

print (ProcesoActual().name())  #nombre:   python3
# Obtener y mostrar el nombre del proceso actual

print (ProcesoActual().cwd()) 
# Obtener y mostrar el directorio de trabajo actual (cwd)

print  (ProcesoActual().nice())
# Obtener y mostrar la prioridad del proceso antes del cambio

if esWindows():
  subprocess.check_output("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"below normal\"") 
else:
  os.nice(1)

#prioridad después del cambio
print (ProcesoActual().nice())