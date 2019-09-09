from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

THINGSBOARD_HOST = "172.16.206.223"
ACCESS_TOKEN = "5fCX5oI4LncCpngaogOy"

telemetry = {"temperature": 41.9, "enabled": False, "currentFirmwareVersion": "v1.2.2"}

client = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN)
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
# Disconnect from ThingsBoard
client.disconnect()