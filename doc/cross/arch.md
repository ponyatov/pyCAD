`arch/inc/arch.hpp`
```cpp
/// @defgroup arch arch
/// @ingroup cross
/// @defgroup archx86 x86
/// @ingroup arch
/// @defgroup archrpi rpi
/// @ingroup arch
#pragma once
```
```sh
for d in arch/i386 arch/x86_64; do
  mkdir -p $d/inc $d/src
  touch $d/inc $d/src/.gitignore
  n=$(basename $d)
  printf "/// @defgroup $n $n\n/// @ingroup archx86\n#pragma once\n" > $d/inc/$n.hpp
done
```
```sh
for d in arch/arm7 arch/aarch64; do
  mkdir -p $d/inc $d/src
  touch $d/inc $d/src/.gitignore
  n=$(basename $d)
  printf "/// @defgroup $n $n\n/// @ingroup archrpi\n#pragma once\n" > $d/inc/$n.hpp
done
```
