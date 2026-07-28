# Config
## конфигурация аппарата

```e
mqtt Machine {
    ID: UID {
        Config {
            Global          // Аппаратная конфигурация аппарата
            Power           // Подсистема электропитания
            Env             // Подсистема климатического контроля
            Net             // Сетевые настройки
            Camera          // Подсистема фотовидеоконтроля
            MODBUS          // Шина MODBUS
            IO              // Подсистема ввода/вывода
            LED             // Конфигурация LED-подсветки
            Sections        // Набор секций аппарата
        }
    }
}
```

- [[Global]]
- [[Power]]
- [[Env]]
- [[Net]]
- [[Camera]]
- [[vending/MODBUS|MODBUS]]
- [[IO]]
- [[LED]]
- [[Sections]]
