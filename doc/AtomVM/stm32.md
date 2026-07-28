# AtomVM/stm32
## files

```
├── src
│   └── platforms
│       └── stm32
│           ├── clock_configs
│           │   ├── clock_config_f2.c
│           │   ├── clock_config_f4.c
│           │   ├── clock_config_f7.c
│           │   ├── clock_config_g0.c
│           │   ├── clock_config_g4.c
│           │   ├── clock_config.h
│           │   ├── clock_config_h5.c
│           │   ├── clock_config_h7.c
│           │   ├── clock_config_l4.c
│           │   ├── clock_config_l5.c
│           │   ├── clock_config_u3.c
│           │   ├── clock_config_u5.c
│           │   └── clock_config_wb.c
│           ├── cmake
│           │   ├── arm-toolchain.cmake
│           │   ├── atomvm_dev_config.cmake
│           │   ├── compile-flags.cmake
│           │   ├── picolibc.cmake
│           │   ├── stm32_device_atoms.h.in
│           │   ├── stm32_device.cmake
│           │   ├── stm32_hal_conf.h.in
│           │   ├── stm32_linker.ld.in
│           │   ├── stm32_sdk.cmake
│           │   └── stm32_tinyusb.cmake
│           ├── CMakeLists.txt
│           ├── MAINTENANCE.md
│           ├── src
│           │   ├── CMakeLists.txt
│           │   ├── lib
│           │   │   ├── avm_devcfg.h
│           │   │   ├── avm_log.h
│           │   │   ├── CMakeLists.txt
│           │   │   ├── gpio_driver.c
│           │   │   ├── gpio_driver.h
│           │   │   ├── i2c_driver.c
│           │   │   ├── jit_stream_flash.c
│           │   │   ├── mbedtls_stm32_user_config.h
│           │   │   ├── otp_crypto_platform.c
│           │   │   ├── platform_nifs.c
│           │   │   ├── spi_driver.c
│           │   │   ├── stm32_hal_platform.h
│           │   │   ├── stm_sys.h
│           │   │   ├── sys.c
│           │   │   ├── tusb_config.h
│           │   │   ├── uart_driver.c
│           │   │   ├── usb_cdc_driver.c
│           │   │   ├── usb_cdc_driver.h
│           │   │   ├── usb_descriptors.c
│           │   │   ├── usb_hw_init.c
│           │   │   ├── usb_hw_init.h
│           │   │   └── usb_irq_handlers.c
│           │   └── main.c
│           ├── tests
│           │   ├── renode
│           │   │   ├── stm32_boot_test.robot
│           │   │   ├── stm32_crypto_test.robot
│           │   │   ├── stm32g0b1.repl
│           │   │   ├── stm32_gpio_test.robot
│           │   │   ├── stm32h743.repl
│           │   │   ├── stm32_i2c_test.robot
│           │   │   ├── stm32l562.repl
│           │   │   ├── stm32_spi_test.robot
│           │   │   └── stm32_uart_test.robot
│           │   └── test_erl_sources
│           │       ├── CMakeLists.txt
│           │       ├── test_boot.erl
│           │       ├── test_crypto.erl
│           │       ├── test_gpio.erl
│           │       ├── test_i2c.erl
│           │       ├── test_spi.erl
│           │       └── test_uart.erl
│           └── tools
│               ├── atomvm_stm32_config_query.erl
│               └── device_config.hrl
```
