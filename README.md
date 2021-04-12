## NOTES:
* this code uses pygatt, which I've only been able to test/run on a Raspberry Pi. It did everything as I needed (update the date and time on an outdated BLE device) but use at your own risk.
* I tested my code on a Braceli wristband. It functions as a pedometer and watch. The app that it syncs with was made in China and no longer syncs with my watch (their app seems to have been broken for a long time).
* So I was only able to find out how to set the date and time (via bluetooth packet sniffing). This methodology works best if you run the script right after booting the BLE device.

## MAIN REFERENCES:
* https://medium.com/@arunmag/my-journey-towards-reverse-engineering-a-smart-band-bluetooth-le-re-d1dea00e4de2
* https://www.evilsocket.net/2015/01/29/Nike-FuelBand-SE-BLE-Protocol-Reversed/
* https://www.instructables.com/Control-Bluetooth-LE-Devices-From-A-Raspberry-Pi/
