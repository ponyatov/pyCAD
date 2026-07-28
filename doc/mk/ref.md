# mk/ref.mk

```Makefile
RF += ref/AtomVM/LICENSE
ref/AtomVM/LICENSE:
	$(GITREF) https://github.com/atomvm/AtomVM.git $(dir $@)

.PHONY: ref
ref: $(RF)
```
