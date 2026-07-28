# [[vm/vm]]
##  for C++ targets

## files

```
lib/
	vm/
		inc/
			vm.hpp
			compiler.hpp
		src/
			vm.cpp
			compiler.cpp
```

## lib/vm/inc/vm.hpp

```c
/// @defgroup vm vm
/// @ingroup lib
/// @{
#pragma once

/// @defgroup config config
/// @{

/// @brief max memory: 64K @ref byte s per single thread
#define Msz 0x10000

/// @brief return stack @ref addr esses
#define Rsz 0x100

/// @brief data strack @ref cell s
#define Dsz 0x10
/// @}

/// @defgroup types types
/// @{
#include <cstdint>
typedef uint8_t byte;   ///< single byte
typedef uint16_t addr;  ///< @ref M address limited with `u16`
typedef int32_t cell;   ///< 32-bit integer
/// @}

/// @defgroup memory memory
/// @{
extern byte M[Msz];  ///< thread memory
extern addr Cp;      ///< compiler pointer
extern addr Ip;      ///< instruction pointer
extern addr R[Rsz];  ///< return stack
extern cell D[Dsz];  ///< data stack
/// @}

/// run VM
/// @returns `int` return from @ref main
extern int vm();
/// @}
```

## lib/vm/src/vm.cpp

```c
#include "vm.hpp"

// stub while bytecode compiler not ready
int vm() { return 0; }

byte M[Msz];
addr Cp = 0;
addr Ip = 0;
```

## lib/vm/inc/compiler.hpp

```c

```

## lib/vm/src/compiler.cpp
