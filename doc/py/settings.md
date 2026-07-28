# `.vscode/settings.json`

```json
    // Python
    "python.defaultInterpreterPath"   :  "${workspaceFolder}/.venv/bin/python3",
    "autopep8.path"                   : ["${workspaceFolder}/.venv/bin/autopep8"],
    // "ruff.interpreter"             : ["${workspaceFolder}/.venv/bin/python3"],
    "autopep8.args"                   : ["--ignore","E26,E302,E305,E401,E402,E701,E702"],
    "python.analysis.extraPaths"      : ["${workspaceFolder}/src"],
    "python.testing.pytestEnabled"    : true,
    "python.testing.unittestEnabled"  : false,
    "[python]": {
        "editor.defaultFormatter"     : "ms-python.autopep8",
        "editor.formatOnSave"         :  true},
```
