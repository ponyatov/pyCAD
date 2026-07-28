# ATOM_STR
## [[atom]]

```c
 * @param LENSTR must be less than 255 (\\xFF), to fit within a uint8.
 * @param STR the string to be used as an atom.
 */
#define ATOM_STR(LENSTR, STR) (LENSTR STR)
```

- первый байт: длина строки-атома
	- до 255 символов: `LENSTR < 255`
- атом кодируется ASCIIZ байт-строкой
