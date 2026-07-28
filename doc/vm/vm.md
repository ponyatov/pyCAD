# embedded bytecode VM

```e
module VM {

	type byte = u8  // single byte
	type addr = u16 // every thread address space limited with 16-bit (64K max)
	type cell = i32 // 32-bit integers (VM mostly for MCU targets)
}
```

## actor

**actor** = active object:
- methods can be used syncronously by `call`
- or async by using priority-queued messages
- has own `context`:
	- `data stack` as temp data storage
	- separate `return stack` for holding addresses for `call`/`ret` and execution markers
	- every actor uses `local heap` to minimize garbage collection lags
	- actor has `mailbox` for incoming messages should be processes one by one

## vat

**vat** is a
- containter for multiple actors
- managed by a single-[[#thread]]ed VM
- has own preemptive scheduler switches [[#actor]]s with RTOS-like priority

## thread

- thread is OS `thread` -- term not used for clearance
- thread is equal to FreeRTOS task (@MCU)

## process

- process is OS `process` -- term not used for clearance
- process is equal to whole MCU (no MMU, single shared memory)


[[cad/cad]]