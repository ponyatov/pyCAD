# cross

- build cross-compiler toolchain from source
- [[cross/files]] directory structure

## dirs

```
cross/     # project-local cross-compiler toolchain's
root/      # root for embedded Linux
```

```sh
mkdir -p {cross,root,root/boot,root/etc,root/isolinux}
touch    {cross,root,root/boot,root/etc,root/isolinux}/.gitignore
cp bin/.gitignore cross/
cp bin/.gitignore root/
```
