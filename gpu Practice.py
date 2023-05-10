import pynvml
import time

pynvml.nvmlInit()

period = input( )
sleepTime = input()

for i in range(int(period)):
    deviceCount = pynvml.nvmlDeviceGetCount()
    print("deviceCount : " + str(deviceCount))
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)

        
        name = pynvml.nvmlDeviceGetName(handle)
        print(f"GPU {i} : {name.encode('utf-8').decode()}")

        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        print(f"Total memory: {meminfo.total/1024/1024:.2f} MB")
        print(f"Free memory: {meminfo.free/1024/1024:.2f} MB")
        print(f"Used memory: {meminfo.used/1024/1024:.2f} MB")

        
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        print(f"GPU utilization: {utilization.gpu} %")
        print(f"Memory utilization: {utilization.memory} %")

        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        print(f"GPU temperature: {temperature} C")

        power = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000 #inja mW mide , so -> convert mW to W
        print(f"Power usage: {power:.2f} W")

        print(" . . . ")
        time.sleep(int(sleepTime))


pynvml.nvmlShutdown()
