import psutil
#obter informações da cpu
cpu=psutil.cpu_percent()
memory = psutil.virtual_memory()
disk_usage = psutil.disk_usage("/")
print(f"Uso de disco: {disk_usage.percent}%")
print(f"Uso de memória: {memory.percent}%")
print(f'uso da cpu:{cpu}%')
