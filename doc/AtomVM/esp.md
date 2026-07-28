# [[ESP32]]
## files

```
├── src
│   └── platforms
│       ├── esp32
│       │   ├── CMakeLists.txt
│       │   ├── components
│       │   │   ├── avm_builtins
│       │   │   │   ├── adc_driver.c
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── dac_driver.c
│       │   │   │   ├── gpio_driver.c
│       │   │   │   ├── i2c_driver.c
│       │   │   │   ├── i2c_resource.c
│       │   │   │   ├── idf_component.yml.esp32p4_wifi_remote
│       │   │   │   ├── include
│       │   │   │   │   ├── i2c_driver.h
│       │   │   │   │   └── spi_driver.h
│       │   │   │   ├── Kconfig
│       │   │   │   ├── ledc_nif.c
│       │   │   │   ├── network_driver.c
│       │   │   │   ├── nvs_nif.c
│       │   │   │   ├── otp_crypto_platform.c
│       │   │   │   ├── otp_net_platform.c
│       │   │   │   ├── otp_socket_platform.c
│       │   │   │   ├── otp_ssl_platform.c
│       │   │   │   ├── rtc_slow_nif.c
│       │   │   │   ├── socket_driver.c
│       │   │   │   ├── spi_driver.c
│       │   │   │   ├── storage_nif.c
│       │   │   │   ├── uart_driver.c
│       │   │   │   └── usb_cdc_driver.c
│       │   │   ├── avm_sys
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── include
│       │   │   │   │   ├── esp32_sys.h
│       │   │   │   │   ├── jit_stream_flash_platform.h
│       │   │   │   │   ├── otp_socket_platform.h
│       │   │   │   │   ├── platform_defaultatoms.def
│       │   │   │   │   └── platform_defaultatoms.h
│       │   │   │   ├── jit_stream_flash_platform.c
│       │   │   │   ├── platform_atomic.h
│       │   │   │   ├── platform_defaultatoms.c
│       │   │   │   ├── platform_nifs.c
│       │   │   │   ├── smp.c
│       │   │   │   └── sys.c
│       │   │   └── libatomvm
│       │   │       └── CMakeLists.txt
│       │   ├── GetBootAVM.cmake
│       │   ├── main
│       │   │   ├── CMakeLists.txt
│       │   │   ├── idf_component.yml.example
│       │   │   ├── idf_component.yml.example.license
│       │   │   ├── Kconfig.projbuild
│       │   │   └── main.c
│       │   ├── nvs_partition.csv-example
│       │   ├── nvs_partition.csv-example.license
│       │   ├── partitions.csv
│       │   ├── partitions-elixir.csv
│       │   ├── partitions-jit.csv
│       │   ├── partitions-test.csv
│       │   ├── README.md
│       │   ├── sdkconfig.defaults.esp32c5
│       │   ├── sdkconfig.defaults.esp32h2
│       │   ├── sdkconfig.defaults.esp32h2.license
│       │   ├── sdkconfig.defaults.esp32p4
│       │   ├── sdkconfig.defaults.esp32p4_c6
│       │   ├── sdkconfig.defaults.esp32p4_pre
│       │   ├── sdkconfig.defaults.esp32p4_pre_c6
│       │   ├── sdkconfig.defaults.in
│       │   ├── sdkconfig.defaults.in.license
│       │   ├── sdkconfig.jit
│       │   ├── sdkconfig.jit.license
│       │   ├── sdkconfig.release-defaults.in
│       │   ├── sdkconfig.release-defaults.in.license
│       │   ├── test
│       │   │   ├── CMakeLists.txt
│       │   │   ├── main
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── idf_component.yml
│       │   │   │   ├── idf_component.yml.license
│       │   │   │   ├── Kconfig.projbuild
│       │   │   │   ├── test_erl_sources
│       │   │   │   │   ├── CMakeLists.txt
│       │   │   │   │   ├── test_crypto.erl
│       │   │   │   │   ├── test_deep_sleep_hold.erl
│       │   │   │   │   ├── test_esp_partition.erl
│       │   │   │   │   ├── test_esp_timer_get_time.erl
│       │   │   │   │   ├── test_file.erl
│       │   │   │   │   ├── test_i2c.erl
│       │   │   │   │   ├── test_jit_compile.erl
│       │   │   │   │   ├── test_jit_simple.erl
│       │   │   │   │   ├── test_list_to_atom.erl
│       │   │   │   │   ├── test_list_to_binary.erl
│       │   │   │   │   ├── test_md5.erl
│       │   │   │   │   ├── test_monotonic_time.erl
│       │   │   │   │   ├── test_mount.erl
│       │   │   │   │   ├── test_net.erl
│       │   │   │   │   ├── test_rtc_slow.erl
│       │   │   │   │   ├── test_select.erl
│       │   │   │   │   ├── test_socket.erl
│       │   │   │   │   ├── test_ssl.erl
│       │   │   │   │   ├── test_system_architecture.erl
│       │   │   │   │   ├── test_time_and_processes.erl
│       │   │   │   │   ├── test_twdt.erl
│       │   │   │   │   ├── test_tz.erl
│       │   │   │   │   ├── test_wifi_example.erl
│       │   │   │   │   ├── test_wifi_managed.erl
│       │   │   │   │   └── test_wifi_scan.erl
│       │   │   │   └── test_main.c
│       │   │   ├── partitions.csv
│       │   │   ├── qemu_esp32c3_efuse.bin
│       │   │   ├── qemu_esp32c3_efuse.bin.license
│       │   │   ├── qemu_esp32s3_efuse.bin
│       │   │   ├── qemu_esp32s3_efuse.bin.license
│       │   │   ├── README.md
│       │   │   ├── sdkconfig.ci.wokwi
│       │   │   ├── sdkconfig.ci.wokwi.license
│       │   │   ├── sdkconfig.defaults.license
│       │   │   ├── sim_boards
│       │   │   │   ├── diagram.esp32c3.json
│       │   │   │   ├── diagram.esp32c3.json.license
│       │   │   │   ├── diagram.esp32c5.json
│       │   │   │   ├── diagram.esp32c5.json.license
│       │   │   │   ├── diagram.esp32c61.json
│       │   │   │   ├── diagram.esp32c61.json.license
│       │   │   │   ├── diagram.esp32c6.json
│       │   │   │   ├── diagram.esp32c6.json.license
│       │   │   │   ├── diagram.esp32h2.json
│       │   │   │   ├── diagram.esp32h2.json.license
│       │   │   │   ├── diagram.esp32.json
│       │   │   │   ├── diagram.esp32.json.license
│       │   │   │   ├── diagram.esp32p4.json
│       │   │   │   ├── diagram.esp32p4.json.license
│       │   │   │   ├── diagram.esp32s2.json
│       │   │   │   ├── diagram.esp32s2.json.license
│       │   │   │   ├── diagram.esp32s3.json
│       │   │   │   └── diagram.esp32s3.json.license
│       │   │   ├── test_atomvm.py
│       │   │   ├── wokwi.toml
│       │   │   └── wokwi.toml.license
│       │   └── tools
│       │       ├── CMakeLists.txt
│       │       ├── flashimage.sh.in
│       │       ├── flash.sh.in
│       │       ├── mkimage.config.in
│       │       ├── mkimage.erl
│       │       ├── mkimage_nvs.config.in
│       │       └── mkimage.sh.in
```
