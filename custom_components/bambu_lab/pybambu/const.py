from enum import Enum
import logging

LOGGER = logging.getLogger(__package__)

class Features(Enum):
    AUX_FAN = 1,
    CHAMBER_LIGHT = 2,
    CHAMBER_FAN = 3,
    CHAMBER_TEMPERATURE = 4,
    CURRENT_STAGE = 5,
    PRINT_LAYERS = 6,
    AMS = 7,
    EXTERNAL_SPOOL = 8,
    K_VALUE = 9,
    START_TIME = 10,
    AMS_TEMPERATURE = 11,
    AMS_RAW_HUMIDITY = 12,

ACTION_IDS = {
    "default": "Unknown",
    -1: "Idle",
    0: "Printing",
    1: "Auto Bed Leveling",
    2: "Heatbed Preheating",
    3: "Sweeping XY Mech Mode",
    4: "Changing Filament",
    5: "M400 Pause",
    6: "Paused due to filament runout",
    7: "Heating Hotend",
    8: "Calibrating Extrusion",
    9: "Scanning Bed Surface",
    10: "Inspecting First Layer",
    11: "Identifying Build Plate Type",
    12: "Calibrating Micro Lidar",
    13: "Homing Toolhead",
    14: "Cleaning Nozzle Tip",
    15: "Checking Extruder Temperature",
    16: "Printing was paused by the user",
    17: "Pause of front cover falling",
    18: "Calibrating Micro Lidar",
    19: "Calibrating Extrusion Flow",
    20: "Paused due to nozzle temperature malfunction",
    21: "Paused due to heat bed temperature malfunction"
}

SPEED_PROFILE = {
    "default": "Unknown",
    1: "Silent",
    2: "Standard",
    3: "Sport",
    4: "Ludicrous"
}

FILAMENT_NAMES = {
    "default": "Unknown",
    "GFA00": "Bambu PLA Basic",
    "GFA01": "Bambu PLA Matte",
    "GFA05": "Generic PLA Silk",
    "GFB00": "Bambu ABS",
    "GFB98": "Generic ASA",
    "GFB99": "Generic ABS",
    "GFC00": "Bambu PC",
    "GFC99": "Generic PC",
    "GFG99": "Generic PETG",
    "GFL00": "PolyLite PLA",
    "GFL01": "PolyTerra PLA",
    "GFL98": "Generic PLA-CF",
    "GFL99": "Generic PLA",
    "GFN03": "Bambu PC-CF",
    "GFN98": "Generic PA-CF",
    "GFN99": "Generic PA",
    "GFS00": "Bambu Support W",
    "GFS01": "Bambu Support G",
    "GFS99": "Generic PVA",
    "GFSL99_01": "Generic PLA Silk",
    "GFSL99_12": "Generic PLA Silk",
    "GFU01": "Bambu TPU 95A",
    "GFU99": "Generic TPU",
}

HMS_ERRORS = {
    "0300_1000_0002_0001": "The 1st order mechanical resonance mode of X axis is low.", 
    "0300_1000_0002_0002": "The 1st order mechanical resonance mode of X axis differ much...", 
    "0300_0F00_0001_0001": "The accelerometer data is unavalable", 
    "0300_0D00_0001_000B": "The Z axis motor seems got stuck when moving up)", 
    "0300_0D00_0001_0002": "Hotbed homing failed . The environmental vibration is too great", 
    "0300_0D00_0001_0003": "The build plate is not placed properly ...", 
    "0300_0D00_0002_0001": "Heatbed homing abnormal. There may be a bulge on the ...", 
    "0300_0A00_0001_0005": "the static voltage of force sensor 1/2/3 is not 0 ...", 
    "0300_0A00_0001_0004": "External disturbance was detected when testing the force sensor", 
    "0300_0A00_0001_0003": "The sensititvity of heatbed force sensor 1/2/3 is too low....", 
    "0300_0A00_0001_0002": "The sensititvity of heatbed force sensor 1/2/3 is low...", 
    "0300_0A00_0001_0001": "The sensititvity of heatbed force sensor 1/2/3 is too high...", 
    "0300_0400_0002_0001": "The speed of part cooling fan if too slow or stopped ...", 
    "0300_0300_0002_0002": "The speed of hotend fan is slow ...", 
    "0300_0300_0001_0001": "The speed of the hotend fan is too slow or stopped...", 
    "0300_0600_0001_0001": "Motor-A has an open-circuit. There may be a loose connection, or the motor may have failed.", 
    "0300_0600_0001_0002": "Motor-A has a short-circuit. It may have failed.", 
    "0300_0600_0001_0003": "The resistance of Motor-A is abnormal, the motor may have failed.", 
    "0300_0100_0001_0001": "The heatbed temperature is abnormal; the heater may have a short circuit.", 
    "0300_0100_0001_0002": "The heatbed temperature is abnormal; the heater may have an open circuit, or the thermal switch may be open.", 
    "0300_0100_0001_0003": "The heatbed temperature is abnormal; the heater is over temperature.", 
    "0300_0100_0001_0006": "The heatbed temperature is abnormal; the sensor may have a short circuit.", 
    "0300_0100_0001_0007": "The heatbed temperature is abnormal; the sensor may have an open circuit.", 
    "0300_1300_0001_0001": "The current sensor of Motor-A is abnormal. This may be caused by a failure of the hardware sampling circuit.", 
    "0300_4000_0002_0001": "Data transmission over the serial port is abnormal; the software system may be faulty.", 
    "0300_4100_0001_0001": "The system voltage is unstable; triggering the power failure protection function.", 
    "0300_0200_0001_0001": "The nozzle temperature is abnormal,the heater may be short circuit.", 
    "0300_0200_0001_0002": "The nozzle temperature is abnormal,the heater may be open circuit.", 
    "0300_0200_0001_0003": "The nozzle temperature is abnormal,the heater is over temperature.", 
    "0300_0200_0001_0006": "The nozzle temperature is abnormal,the sensor may be short circuit.", 
    "0300_0200_0001_0007": "The nozzle temperature is abnormal,the sensor may be open circuit.", 
    "0300_1200_0002_0001": "The front cover of the toolhead fell off.", 
    "0C00_0100_0001_0001": "The Micro Lidar camera is offline", 
    "0C00_0100_0002_0002": "The Micro Lidar camera is malfunctioning", 
    "0C00_0100_0001_0003": "Synchronization between Micro Lidar camera and MCU is abnormal", 
    "0C00_0100_0001_0004": "The Micro Lidar camera lens seems to be dirty", 
    "0C00_0100_0001_0005": "Micro Lidar OTP parameter is abnormal", 
    "0C00_0100_0002_0006": "Micro Lidar extrinsic parameter abnormal", 
    "0C00_0100_0002_0007": "Micro Lidar laser parameters are drifted", 
    "0C00_0100_0002_0008": "Failed to get image from chamber camera", 
    "0C00_0100_0001_0009": "Chamber camera dirty", 
    "0C00_0100_0001_000A": "The Micro Lidar LED may be broken", 
    "0C00_0100_0001_000B": "Failed to calibrate Micro Lidar", 
    "0C00_0200_0001_0001": "The horizontal laser is not lit", 
    "0C00_0200_0002_0002": "The horizontal laser is too thick", 
    "0C00_0200_0002_0003": "The horizontal laser is not bright enough", 
    "0C00_0200_0002_0004": "Nozzle height seems too low", 
    "0C00_0200_0001_0005": "A new Micro Lidar is detected", 
    "0C00_0200_0002_0006": "Nozzle height seems too high", 
    "0C00_0300_0002_0001": "Filament exposure metering failed", 
    "0C00_0300_0002_0002": "First layer inspection terminated due to abnormal lidar data", 
    "0C00_0300_0002_0004": "First layer inspection not supported for current print", 
    "0C00_0300_0002_0005": "First layer inspection timeout", 
    "0C00_0300_0003_0006": "Purged filaments may have piled up", 
    "0C00_0300_0003_0007": "Possible first layer were defected", 
    "0C00_0300_0003_0008": "Possible spaghetti defects were detected", 
    "0C00_0300_0001_0009": "The first layer inspection module rebooted abornmally", 
    "0C00_0300_0003_000B": "Inspecting first layer", 
    "0C00_0300_0002_000C": "The build plate localization marker is not detected", 
    "0500_0100_0002_0001": "The media pipeline is malfunctioning.", 
    "0500_0100_0002_0002": "USB camera is not connected.", 
    "0500_0100_0002_0003": "USB camera is malfunctioning.", 
    "0500_0100_0003_0004": "Not enough space in SD Card.", 
    "0500_0100_0003_0005": "Error in SD Card.", 
    "0500_0100_0003_0006": "Unformatted SD Card.", 
    "0500_0200_0002_0001": "Failed to connect internet, please check the network connection.", 
    "0500_0200_0002_0002": "Failed to login device.", 
    "0500_0200_0002_0004": "Unauthorized user.", 
    "0500_0200_0002_0006": "Liveview service is malfunctioning.", 
    "0500_0300_0001_0001": "The MC module is malfunctioning. Please restart the device.", 
    "0500_0300_0001_0002": "The toolhead is malfunctioning. Please restart the device.", 
    "0500_0300_0001_0003": "The AMS module is malfunctioning. Please restart the device.", 
    "0500_0300_0001_000A": "System state is abnormal. Please restore factory settings.", 
    "0500_0300_0001_000B": "The screen is malfunctioning.", 
    "0500_0300_0002_000C": "Wireless hardware error. Please turn off/on WiFi or restart the device.", 
    "0500_0400_0001_0001": "Failed to download print job. Please check your network connection.", 
    "0500_0400_0001_0002": "Failed to report print state. Please check your network connection.", 
    "0500_0400_0001_0003": "The content of print file is unreadable. Please resend the print job.", 
    "0500_0400_0001_0004": "The print file is unauthorized.", 
    "0500_0400_0001_0006": "Failed to resume previous print.", 
    "0500_0400_0002_0007": "The bed temperature exceeds the filament's vitrification temperature, which may cause a nozzle clog.", 
    "0700_0100_0001_0001": "The AMS assist motor has slipped.The extrusion wheel may be worn down,or the filament may be too thin.", 
    "0700_0100_0001_0003": "The AMS assist motor torque control is malfunctioning.The current sensor may be faulty.", 
    "0700_0100_0001_0004": "The AMS assist motor speed control is malfunctioning.The speed sensor may be faulty.", 
    "0700_0100_0002_0002": "The AMS assist motor is overloaded.The filament may be tangled or stuck.", 
    "0700_0200_0001_0001": "AMS filament speed and length error.The filament odometry may be faulty.", 
    "0700_1000_0001_0001": "The AMS slot1 motor has slipped.The extrusion wheel may be malfunctioning,or the filament may be too thin.", 
    "0700_1000_0001_0003": "The AMS slot1 motor torque control is malfunctioning.The current sensor may be faulty.", 
    "0700_1000_0002_0002": "The AMS slot1 motor is overloaded.The filament may be tangled or stuck.", 
    "0700_2000_0002_0001": "The AMS slot1 filament has been ran out.", 
    "0700_2000_0002_0002": "The AMS slot1 is empty.", 
    "0700_2000_0002_0003": "The AMS slot1 filament may be broken in AMS.", 
    "0700_2000_0002_0004": "The AMS slot1 filament may be broken in the tool head.", 
    "0700_2000_0002_0005": "AMS1 Slot1 filament has run out, and purging the old filament went abnormally; please check whether the filament is stuck in the tool head.", 
    "0700_2000_0003_0001": "AMS1 Slot1 filament has run out. Please wait while old filament is purged.", 
    "0700_2000_0003_0002": "AMS1 Slot1 filament has run out and automatically switched to the slot with the same filament.", 
    "0700_4000_0002_0001": "The filament buffer signal lost,the cable or position sensor may be malfunctioning.", 
    "0700_4000_0002_0002": "The filament buffer position signal error,the position sensor may be malfunctioning.", 
    "0700_4000_0002_0003": "The AMS Hub communication is abnormal,the cable may be not well connected.", 
    "0700_4000_0002_0004": "The filament buffer signal is abnormal,the spring may be stuck.", 
    "0700_4500_0002_0001": "The filament cutter sensor is malfunctioning.The sensor may be disconected or damaged.", 
    "0700_4500_0002_0002": "The filament cutter's cutting distance is too large.The XY motor may lose steps.", 
    "0700_4500_0002_0003": "The filament cutter handle has not released.The handle or blade ay be stuck.", 
    "0700_5100_0003_0001": "The AMS is disabled; please load filament from spool holder.", 
    "0700_6000_0002_0001": "The AMS1 slot1 is overloaded. The filament may be tangled or the spool may be stuck.", 
}