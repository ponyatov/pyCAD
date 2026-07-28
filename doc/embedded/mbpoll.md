# mbpoll
## [[MODBUS]]

```sh
mbpoll 10.130.2.51 -p 501 -m tcp -a 51 -r 1 -c 1 -t 4:hex -1
```

- `-m tcp`: TCP mode
- `-a 51`: Slave/unit ID (default often 1)
- `-r 0`: Starting register address
- `-c 17`: Count of registers to read
- `-t 4:hex`: Type (4=16-bit registers, display as hex)
- `10.130.2.51`: Device IP address

```sh
mbpoll /dev/ttyACM0 -b 115200 -m rtu -a 51 -r 1 -c 1 -t 4:hex -1
```
