import platform
import psutil
computer_name=platform.node()
processor_name = platform.processor()
os_information=platform.system(), platform.release()
ram_information=round(psutil.virtual_memory().total / (1024. ** 3), 2)
print("Computer name: ", computer_name, '\n' "Processor name: ", processor_name, '\n' "Infornation adout your os: ", os_information, '\n' "Your ram: ", ram_information, "GB")
