# `.vscode/settings.json`

## required sections order

- files
- editor
- terminal
- js
- clang-format
- c++
- cmake
- python
- mingw

> every section as provided, don't split or change

## files

```json
{
	// files
    "files.exclude": {
        "doc/html": true, "**/node_modules": true,
    },
    "files.watcherExclude": {
        "ref/**": true,
    },
    "files.associations": {
        "*.linux": "properties", "*.uclibc": "properties",
        "*.rc": "shell", "*.service": "systemd-unit-file",
        "*.mk": "makefile", "*.make": "makefile",
        "*.ld": "linkerscript", "*.ld.fix": "linkerscript",
        "*.ini": "properties", "*.e": "properties"
    },
```

## editor

```json
    // editor
    "files.eol": "\n",
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.detectIndentation": false,
    "editor.rulers": [80],
    "editor.lineNumbers": "on",
    "explorer.autoReveal": false,
    "terminal.integrated.copyOnSelection": true,
    "editor.formatOnSave": false,
    "workbench.tree.indent": 24,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 2222,
    "auto-tab-closer.delayMs": 5555,
    "auto-tab-closer.numLeftTabs": 5,
    "auto-tab-closer.numMaxTabs": 5,
    // "git.enabled": false,
```

## terminal

```json
    // terminal
    "SerialTerminal.serial port.configurations": ["115200n1"],
```

## JavaScript

```json
	// JavaScript
    "prettier.configPath"         : ".prettierrc",
    "prettier.requireConfig"      :  true,
    "json.format.enable"          :  true,
    "[json]"      : {
        "editor.defaultFormatter" : "esbenp.prettier-vscode",
        "editor.formatOnSave": false},
    "[jsonc]"     : {
        "editor.defaultFormatter" : "esbenp.prettier-vscode",
        "editor.formatOnSave": false},
    "[html]": {
        "editor.defaultFormatter" : "esbenp.prettier-vscode",
        "editor.formatOnSave": false},
    "[javascript]": {
        "editor.defaultFormatter" : "esbenp.prettier-vscode",
        "editor.formatOnSave": false},
    "[typescript]": {
        "editor.defaultFormatter" : "esbenp.prettier-vscode",
        "editor.formatOnSave": false},
```

[[js/prettierrc]]


## [[clang-format]]

```json
    // clang-format
    "clang-format.executable"     : "clang-format",
    "clang-format.fallbackStyle"  : "Google",
    "clang-format.style"          : "file",
    "clang-format.assumeFilename" : ".clang-format",
```

![[cpp/vscode#settings]]
![[cmake/vscode#settings]]

![[py/vscode#settings]]

## MinGW/MSYS

```json
    // MinGW/MSYS2
    "terminal.integrated.defaultProfile.windows": "UCRT64",
    "terminal.integrated.profiles.windows": {
        "UCRT64": {
            "path": "C:\\msys64\\usr\\bin\\bash.exe",
            "args": ["--login","-i"],
            "env": {
            "MSYSTEM": "UCRT64",
            "CHERE_INVOKING": "1",
    }}}
}
```
