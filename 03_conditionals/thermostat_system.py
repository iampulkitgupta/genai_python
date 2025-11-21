device_status = "off"
target_temperature = 40

if device_status == "active" and target_temperature > 35:
    print("High temperature detected")
elif device_status == "active" and target_temperature <= 35:
    print("Temperature is normal")
else:
    print("Device is offline")