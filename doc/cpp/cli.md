# lib/cli
## uses [[cpp/syntax|syntax parser]]

```
mkdir -p lib/cli/inc lib/cli/src
touch lib/cli/inc/syntax.hpp
touch lib/cli/inc/cli.hpp
touch lib/cli/src/cli.cpp
touch lib/cli/src/syntax.cpp
printf '!\n.gitignore\n' > lib/cli/.gitignore
printf '!\n.gitignore\n' > lib/cli/inc/.gitignore
printf '!\n.gitignore\n' > lib/cli/src/.gitignore
```

## lib/cli/inc/cli.hpp

```cpp
/// @defgroup cli cli
/// @ingroup lib
#pragma once

#include "syntax.hpp"
#include "vm.hpp"
```

- [[cpp/syntax|syntax]]
- [[vm]]

## lib/cli/src/cli.cpp

```cpp
#include "cli.hpp"
```
