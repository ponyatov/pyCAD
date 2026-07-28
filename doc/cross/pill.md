# hw:pill

- hw/pill030 stm32f030f4
- hw/pill103 stm32f103c8
- hw/pill411 stm32f411ce

```sh
for hw in pill030 pill103 pill411; do
  mkdir -p hw/$hw/inc hw/$hw/src
  touch hw/$hw/inc hw/$hw/src/.gitignore
  printf "/// @defgroup $hw $hw\n/// @ingroup pill\n#pragma once\n" > hw/$hw/inc/$hw.hpp
done
```
