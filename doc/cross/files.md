# multitarget projects

## dirs

```
hw/
    pc/
    rpi3/
    rpi4/
    rpi5/
    opi800/
cpu/
    i486/
    i5/
    rk3399/
arch/
    i386/
    x86_64/
    arm7/
    aarch64/
os/
    linux/
    win32/
    none/
    rtos/
```

- every dir
    - must have .gitignore
    - must have `inc/` `src/`
        - some/inc/some.hpp

```sh
mkdir -p hw/{pc,rpi3,rpi4,rpi5,opi800}/{inc,src}
touch    hw/{pc,rpi3,rpi4,rpi5,opi800}/{inc,src}/.gitignore
mkdir -p cpu/{i486,i5,rk3399}/{inc,src}
touch    cpu/{i486,i5,rk3399}/{inc,src}/.gitignore
mkdir -p arch/{i386,x86_64,arm7,aarch64}/{inc,src}
touch    arch/{i386,x86_64,arm7,aarch64}/{inc,src}/.gitignore
mkdir -p os/{linux,win32,none,rtos}/{inc,src}
touch    os/{linux,win32,none,rtos}/{inc,src}/.gitignore
```

```sh
for g in hw cpu arch os; do
  mkdir -p $g/inc
  printf "/// @defgroup $g $g\n/// @ingroup cross\n#pragma once\n" > $g/inc/$g.hpp
done
```

## hw

- `hw/inc/cross.hpp`
```cpp
/// @defgroup cross cross
```
- `hw/inc/hw.hpp`
```cpp
/// @defgroup hw hw
/// @ingroup cross
```
	`hw/inc/rpi.hpp`
		```cpp
		/// @defgroup rpi rpi
		/// @ingroup hw
		```

	- [[cross/x86]]
	- [[cross/rpi]]
- `cpu/inc/cpu.hpp`
- `arch/inc/arch.hpp`
- `os/inc/os.hpp`

## [[cross/cpu]]
## [[cross/arch]]
## [[cross/os]]

## finish

```sh
git add hw cpu arch os
```
