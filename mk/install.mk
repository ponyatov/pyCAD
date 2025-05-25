.PHONY : install update ref gz
install: $(WS)_install $(PIP) doc ref gz
	$(MAKE) update
update : $(WS)_update $(PIP)
	$(PIP) install -U -r requirements.txt
ref    : $(RF)
gz     : $(GZ)

Debian_install: Debian_update
# sudo dpkg --add-architecture i386
Debian_update:
	sudo apt update
	sudo apt install -uy `cat apt.$(WS)` $(APT)
	$(PIP) install -U    pip
	$(PIP) install -U -r requirements.txt

Msys_install: doc ref gz
	pacman -Suy
Msys_update:
	pacman -S $(shell cat apt.$(WS) | tr '\n' ' ') $(MSYS)

$(PY) $(PIP):
	python3 -m venv .
