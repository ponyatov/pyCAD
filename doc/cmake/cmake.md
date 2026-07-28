# cmake build

```
cmake/
	any_toolchain.cmake
	version.cmake
	src.cmake
	syntax.cmake
	install.cmake
CMakePresets.json
CMakeLists.txt
```

```sh
mkdir -p cmake
printf '!.gitignore\n' > cmake/.gitignore

touch cmake/any_toolchain.cmake
touch cmake/i386-linux-uclibc.cmake
touch cmake/x86_64-linux-gnu.cmake
touch cmake/i386-w64-mingw32.cmake
touch cmake/x86_64-w64-mingw32.cmake
touch cmake/arm-linux-gnueabihf.cmake
touch cmake/aarch64-linux-gnu.cmake

touch cmake/version.cmake
touch cmake/src.cmake
touch cmake/syntax.cmake
touch cmake/install.cmake

touch CMakePresets.json
touch CMakeLists.txt
git add cmake CMake*
```

## [[cmake/vscode]]
## [[CMakePresets]].json
## [[CMakeLists]].txt

## [[cmake/version]].cmake
## [[cmake/src]].cmake
## [[cmake/syntax]].cmake
## [[cmake/install]].cmake
