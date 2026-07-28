# MQTT

```e
mqtt Machine {
	ID: string<UID> {
		Config {}       // vending machine/group configuration
		States {}       // component state flags
		Monitoring {}   // component state values
		Command {}      // BI command income
		Response {}     // machine reports on BI command
		HID {
			RFID        // RFID reader notifications
			QR          // QR   reader notifications
		}
		Control {}      // Machine control (reset/halt)
		Descriptions {} // this specification pulication for BI in ???? format
	}
}
```

- [[Config]]
- [[States]]
- [[Monitoring]]
- [[Command]]
- [[Response]]
- [[HID]]
- [[Control]]
- [[Descriptions]]
