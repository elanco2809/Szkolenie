#
# https://psutil.readthedocs.io/en/latest/
# pip install psutil first :)
#
import psutil


# https://psutil.readthedocs.io/en/latest/#psutil.cpu_times
print("Return system CPU times:", psutil.cpu_times(True))

# https://psutil.readthedocs.io/en/latest/#psutil.cpu_stats
print("CPU statistics :",psutil.cpu_stats())

# https://psutil.readthedocs.io/en/latest/#psutil.getloadavg
print("Load over the last 1, 5 and 15 minutes:",psutil.getloadavg())

# https://psutil.readthedocs.io/en/latest/#psutil.virtual_memory
print("About virtual memory:",psutil.virtual_memory())

# https://psutil.readthedocs.io/en/latest/#psutil.disk_partitions
print("Partitions:",psutil.disk_partitions())

# https://psutil.readthedocs.io/en/latest/#psutil.sensors_battery
print("Batttery info:",psutil.sensors_battery())

# https://psutil.readthedocs.io/en/latest/#other-system-info
print("Boot at (unix timestamp):",psutil.boot_time())


print("\nGet process list and iterate:")
for process_elem in psutil.process_iter():
    print(process_elem.pid, " - ", process_elem.name()," - ", process_elem.username())