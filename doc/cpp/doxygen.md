```sh
mkdir doc
doxygen -l ; mv DoxygenLayout.xml doc/
cp ~/icons/control_64x64.png doc/logo.png
git add doc
```

- `/.doxygen`
```e
PROJECT_NAME           = "{APP}"
PROJECT_BRIEF          = "{TITLE}"
PROJECT_LOGO           = doc/logo.png
OUTPUT_DIRECTORY       = doc
HTML_OUTPUT            = html
GENERATE_HTML          = YES
GENERATE_LATEX         = NO
RECURSIVE              = YES
INPUT                  = README.md lib inc src hw cpu arch os
INCLUDE_PATH           = inc lib hw cpu arch os
EXCLUDE                = ref/*
USE_MDFILE_AS_MAINPAGE = README.md
```

![[mk/doc]]

