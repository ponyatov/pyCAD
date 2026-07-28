# `.vscode/tasks.json`

add fragment:

```json
        {
            "label"          : "doxy: gen",
            "type"           : "shell",
            "group"          : {"kind": "build", "isDefault": true },
            // "dependsOn"      : "CMake: build",
            "command"        : "make doxy",
            "problemMatcher" : [],
            "presentation"   : {"showReuseMessage": false, "focus": false, "reveal": "silent", "close": false}
        },
```
