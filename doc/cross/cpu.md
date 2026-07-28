# cpu

- `cpu/inc/cpu.hpp`
```cpp
/// @defgroup cpu cpu
/// @ingroup cross
/// @defgroup cpux86 x86
/// @ingroup cpu
/// @defgroup cpurpi rpi
/// @ingroup cpu
#pragma once
```
```sh
for d in cpu/i486 cpu/i686 cpu/i5; do
  mkdir -p $d/inc $d/src
  touch $d/inc $d/src/.gitignore
  n=$(basename $d)
  printf "/// @defgroup $n $n\n/// @ingroup cpux86\n#pragma once\n" > $d/inc/$n.hpp
done
```
```sh
for d in cpu/rk3399; do
  mkdir -p $d/inc $d/src
  touch $d/inc $d/src/.gitignore
  n=$(basename $d)
  printf "/// @defgroup $n $n\n/// @ingroup cpurpi\n#pragma once\n" > $d/inc/$n.hpp
done
```
