# VSCode integration

## generic project

```sh
mkdir -p .vscode
touch .vscode/.gitignore
touch .vscode/extensions.json
touch .vscode/settings.json
touch .vscode/tasks.json
touch .vscode/c_cpp_properties.json
touch .vscode/launch.json
git add .vscode
```

- [[extensions]]
- [[settings]]
- [[tasks]]
- [[c_cpp_properties]]
- [[launch]]

## project with bytecode or my own compiler/script

```sh
mkdir vscode
touch vscode/.gitignore
cp ~/icons/control_64x64.png vscode/logo.png
git add vscode
```
