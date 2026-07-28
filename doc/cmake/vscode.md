# vscode config for cmake

## settings

- `.vscode/settings.json`
```json
    // CMake
    "cmake.sourceDirectory" : "${workspaceFolder}",
    "cmake.buildDirectory"  : "${workspaceFolder}/tmp/${workspaceFolderBasename}",
    "cmake.generator"       : "Unix Makefiles",
    "cmake.buildBeforeRun"  : true,
    "cmake.saveBeforeBuild" : true,
    "cmake.parallelJobs"    : 4,
    "cmake.useCMakePresets" : "always",
    "cmake.allowCommentsInPresetsFile" : true,
    "cmake.ignoreCMakeListsMissing"    : false,
    "cmake.debugConfig"     : {
        "cwd" :   "${workspaceFolder}",
        "args": [ "lib/${workspaceFolderBasename}.ini" ] },
```
