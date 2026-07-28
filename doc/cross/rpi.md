# hw:rpi

```sh
printf "/// @defgroup rpi rpi\n/// @ingroup hw\n#pragma once\n" > hw/inc/rpi.hpp
for d in hw/*pi*/inc; do
  n=$(basename $(dirname $d))
  printf "/// @defgroup $n $n\n/// @ingroup rpi\n#pragma once\n" > $d/$n.hpp
done
```
```sh
# hw directories
for hw in rpi3 rpi4 rpi5 opi800; do
  mkdir -p hw/$hw/inc hw/$hw/src
  printf "/// @defgroup $hw $hw\n/// @ingroup rpi\n#pragma once\n" > hw/$hw/inc/$hw.hpp
done

# cpu directories
for cpu in bcm2837 bcm2711 bcm2712 rk3399; do
  mkdir -p cpu/$cpu/inc cpu/$cpu/src
  printf "/// @defgroup $cpu $cpu\n/// @ingroup cpurpi\n#pragma once\n" > cpu/$cpu/inc/$cpu.hpp
done
```
