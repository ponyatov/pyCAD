# Power

```e
mqtt Config {
    Power {
        Mains {
            Voltage   : number<V> = 230      // сетевое напряжение, В
            VoltageMin: number<V> = 170      // минимальное сетевое напряжение, В
            VoltageMax: number<V> = 250      // максимальное сетевое напряжение, В
            PowerMax  : number<W> = 200      // максимальная потребляемая мощность, Вт
        }
        PSU<index=1..> : [{
            RefDes     : string<RefDes>      // обозначение на монтажной схеме
            Model      : string              // модель источника
            Bus        : u8                  // номер подключенной шины
            VoltageIn  : number<V> = 230     // входное напряжение, В
            VoltageOut : number<V;12,24>     // выходное напряжение, В
            CurrentMax : number<A;..10>      // ограничение тока, А
        }]
        Bus<index=0..> : [{
            source     : int<PSU.index>      // индекс источника питания
            sink       : RefDes[]            // список подключенных устройств
            Voltage    : number<V;12,24,230> // номинальное напряжение, В
            CurrentMax : number<A>           // ограничение тока, А
        }]
    }
}
```
