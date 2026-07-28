# generic project file structure

## dirs

```sh
mkdir {.vscode,bin,doc,lib,inc,src,tmp,ref,mk}
touch {.,.vscode,bin,doc,lib,inc,src,tmp,ref,mk}/.gitignore
```

## .gitignore's

- any `.gitignore` must include `!.gitignore` at end of file
- `.gitignore` in this dirs: bin,tmp,ref,root,cross:
```
*
!.gitignore
```
- `doc/.gitignore`
```
html/
!.gitignore
```
![[py/gitignore#lib]]
- `/.gitignore`
```
*~
*.swp
*.log
!.gitignore
```

```sh
printf '*\n!.gitignore\n' > bin/.gitignore
printf '*\n!.gitignore\n' > tmp/.gitignore
printf '*\n!.gitignore\n' > ref/.gitignore
printf 'html/\n!.gitignore\n' > doc/.gitignore
printf '*~\n*.swp\n*.log\n!.gitignore\n' > .gitignore
```

## `/README.md`

```e
'
# ![](doc/logo.png) `{APP}` {VERSION}
## {TITLE}

(c) {AUTHOR} <<{EMAIL}>> {YEAR} {LICENSE}
' >> README.md
```
