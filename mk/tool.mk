CURL   = curl -L -o
CF     = clang-format -style=file -i
GITREF = git clone -o gh --depth 1
PEP    = $(CWD)/bin/autopep8 --ignore $(PEPS) -i
PY     = $(CWD)/bin/python3
PIP    = $(CWD)/bin/pip3
RUSTUP = $(CAR)/bin/rustup
CARGO  = $(CAR)/bin/cargo
