# `/.unison`

```e
# ln -fs ~/{APP}/.unison ~/.unison/{APP}.prf
# unison {APP}

root = ./doc
root = /home/dponyatov/E/doc

prefer = newer
watch = true
batch = true

ignore = Name {.git}
ignore = Name {*~,*.log,*.sw?}
ignore = Name {bin,tmp,ref,_build,target}
ignore = Name {doc/html}
ignore = Name {node_modules,.cache}
ignore = Name {*.pyc,__pycache__}
```
