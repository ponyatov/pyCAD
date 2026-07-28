# mk/install.mk

```Makefile
.PHONY: install update ref gz
install: ref gz py
	$(MAKE) update
update:
	sudo apt update
	sudo apt install -uy `cat apt.Debian` $(APT)
ref: $(RF)
gz:  $(GZ)
```

## [[Python]]

```Makefile
.PHONY: py
py: .venv/bin/pip
.venv/bin/pip: requirements.txt
	python3 -m venv .venv
	$@ install -U pip
	$@ install -U -r $<
```
