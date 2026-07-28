# os

```sh
for d in os/*/inc; do
  n=$(basename $(dirname $d))
  printf "/// @defgroup $n $n\n/// @ingroup os\n#pragma once\n" > $d/$n.hpp
done
```
