# UNIX targets

https://doc.atomvm.org/main/getting-started-guide.html#getting-started-on-the-generic-unix-platform

The AtomVM virtual machine is supported a wide variety of Generic UNIX platforms, including many Linux kernels and target architectures, FreeBSD, and MacOS, allowing users to write Erlang and Elixir programs and run them on a local development machine, server or embedded Linux device.

## files

```
├── src
│   └── platforms
│       ├── generic_unix
│       │   ├── atomvm
│       │   ├── CMakeLists.txt
│       │   ├── lib
│       │   │   ├── CMakeLists.txt
│       │   │   ├── generic_unix_sys.h
│       │   │   ├── jit_stream_mmap.c
│       │   │   ├── jit_stream_mmap.h
│       │   │   ├── mapped_file.c
│       │   │   ├── mapped_file.h
│       │   │   ├── otp_socket_platform.c
│       │   │   ├── otp_socket_platform.h
│       │   │   ├── platform_defaultatoms.c
│       │   │   ├── platform_defaultatoms.def
│       │   │   ├── platform_defaultatoms.h
│       │   │   ├── platform_nifs.c
│       │   │   ├── smp.c
│       │   │   ├── socket_driv├── UPDATING.md
er.c
│       │   │   ├── socket_driver.h
│       │   │   └── sys.c
│       │   └── main.c
```
