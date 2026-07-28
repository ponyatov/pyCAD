# ESP32-S3-WROOM-1U
## Kincony [[KC868-A16]]-V3.1

## USB-C

```
[80937.596825] usb 3-3: new full-speed USB device number 6 using xhci_hcd
[80937.750025] usb 3-3: New USB device found, idVendor=303a, idProduct=1001, bcdDevice= 1.01
[80937.750042] usb 3-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[80937.750049] usb 3-3: Product: USB JTAG/serial debug unit
[80937.750053] usb 3-3: Manufacturer: Espressif
[80937.750057] usb 3-3: SerialNumber: 1C:DB:D4:44:2B:94
[80937.751611] cdc_acm 3-3:1.0: ttyACM0: USB ACM device
```
- `idVendor=303a` [[Espressif Systems]]
- `idProduct=1001` ???
- ESP32-S3's built-in USB JTAG/serial controller

## chip-id

```sh
esptool chip-id
```
```
Connected to ESP32-S3 on /dev/ttyACM0:
Chip type:          ESP32-S3 (QFN56) (revision v0.2)
Features:           Wi-Fi, BT 5 (LE), Dual Core + LP Core, 240MHz, Embedded PSRAM 8MB (AP_3v3)
Crystal frequency:  40MHz
USB mode:           USB-Serial/JTAG

Warning: ESP32-S3 has no chip ID. Reading MAC address instead.
MAC:                1c:db:d4:44:2b:94
```


[[vending/vending]]