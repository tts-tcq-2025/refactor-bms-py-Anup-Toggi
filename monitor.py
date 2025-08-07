from time import sleep
import sys

def is_temperature_ok(temperature):
    return 95 <= temperature <= 102

def is_pulse_rate_ok(pulse_rate):
    return 60 <= pulse_rate <= 100

def is_spo2_ok(spo2):
    return spo2 >= 90

def vitals_status(temperature, pulse_rate, spo2):
    if not is_temperature_ok(temperature):
        return False, 'Temperature critical!'
    if not is_pulse_rate_ok(pulse_rate):
        return False, 'Pulse Rate is out of range!'
    if not is_spo2_ok(spo2):
        return False, 'Oxygen Saturation out of range!'
    return True, 'All vitals normal.'

def blink_warning(times=6, delay=1):
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)

def vitals_ok(temperature, pulse_rate, spo2):
    ok, message = vitals_status(temperature, pulse_rate, spo2)
    if not ok:
        print(message)
        blink_warning()
    return ok
