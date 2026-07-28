# vscode config for C/C++

## settings

- `.vscode/settings.json`
```json
    // C++
    "[c]"  : {
        "editor.defaultFormatter" : "xaver.clang-format",
        "editor.formatOnSave"     : false },
    "[cpp]": {
        "editor.defaultFormatter" : "xaver.clang-format",
        "editor.formatOnSave"     : false },
    "C_Cpp.default.configurationProvider": "ms-vscode.cmake-tools",
    "C_Cpp.files.exclude": { "ref": true },
```
