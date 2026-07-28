# AtomVM
## Erlang VM for tiny systems

AtomVM implements from scratch a minimal Erlang VM that supports a subset of Erlang features and that is able to run unmodified BEAM binaries on really small systems like MCUs.

## Supported Platforms

- [[UNIX]]: Linux, macOS, FreeBSD
- [[ESP32]] SoCs
- STM32 MCUs
- Raspberry Pi Pico / Pico 2
- Browsers and NodeJS with WebAssembly

AtomVM aims to be easily portable to new platforms with a minimum effort

## Getting Started

https://doc.atomvm.org/main/getting-started-guide.html

you can run Erlang or Elixir programs on the AtomVM platform as quickly as possible

you will need to provision your device (depending on the device type) with the AtomVM virtual machine. Typically, you only need to do this once (per release of the VM you would like to use).

Once the VM is provisioned on the device, you can then deploy your application onto the device using any supported I/O interface or protocol, and we expect this process to your typical “deploy, test, debug” development lifecycle.

## Components

- [[libAtomVM]]


