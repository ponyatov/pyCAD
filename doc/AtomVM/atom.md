# atom

**Атом** — неизменяемая константа, идентифицируемая своим именем.

- Начинается со **строчной буквы** или заключается в **одинарные кавычки** (`'`).
- Внутреннее представление — целочисленный индекс в **таблице атомов** (`atom_index_t`).
- Используется как **идентификатор** (ключи, теги, имена функций/модулей).
- Существует только **один экземпляр** атома с данным именем в системе.

```e
// @brief Atoms manipulation functions
module atom {

// Atom encoding: counted string with final zero char
struct ATOM_STR { LENSTR:u8, STR:asciiz }

// указатель на значение атома
type AtomString: const void*

// индекс в глобальной таблице атомов
type atom_index_t: u32


```

[[bib]]

## atom.h

[[ATOM_STR]]
[[AtomString]]
[[atom_index_t]]

[[atom_string_to_c]]
[[atom_are_equals]]
[[atom_string_len]]
[[atom_string_data]]

[[atom_write_mfa]]
