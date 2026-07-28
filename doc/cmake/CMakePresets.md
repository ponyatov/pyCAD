# CMakePresets.json

```json
{
    "version": 3,
```
## buildPresets

```json
    "buildPresets": [
        {
            "name"            : "linux",
            "configurePreset" : "linux"
        }
    ],
```
## configurePresets
```json
    "configurePresets": [
        {
            "name"            : "common",
            "hidden"          :  true,
            "binaryDir"       : "${sourceDir}/tmp/${presetName}",
            "generator"       : "Unix Makefiles",
            "cacheVariables"  : {
                "CMAKE_INSTALL_PREFIX"    : "${sourceDir}/bin",
                "CMAKE_MODULE_PATH"       : "${sourceDir}/cmake",
                "CMAKE_BUILD_TYPE"        : "Debug",
                "CMAKE_COLOR_DIAGNOSTICS" :  false,
                "CMAKE_VERBOSE_MAKEFILE"  :  false
            }
        },
    ]
}
```

## hw

```json
        {
            "name"            : "pc",
            "inherits"        : "common",
            "hidden"          : true,
            "cacheVariables"  : {"HW":"pc", "CPU":"i5", "ARCH":"x86_64"}
        },
```

## os

```json
        {
            "name"            : "linux",
            "inherits"        : "pc",
            "displayName"     : "x86_64-linux-gnu",
            "toolchainFile"   : "${sourceDir}/cmake/x86_64-linux-gnu.cmake",
            "cacheVariables"  : {"OS":"linux"}
        }
```


[[core/MIT]]