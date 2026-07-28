# emscripten
## files

```
├── src
│   └── platforms
│       ├── emscripten
│       │   ├── CMakeLists.txt
│       │   ├── src
│       │   │   ├── atomvm.extern-post.js
│       │   │   ├── atomvm.pre.js
│       │   │   ├── CMakeLists.txt
│       │   │   ├── lib
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── emscripten_sys.h
│       │   │   │   ├── jit_stream_wasm.c
│       │   │   │   ├── jit_stream_wasm.h
│       │   │   │   ├── platform_defaultatoms.c
│       │   │   │   ├── platform_defaultatoms.def
│       │   │   │   ├── platform_defaultatoms.h
│       │   │   │   ├── platform_nifs.c
│       │   │   │   ├── smp.c
│       │   │   │   ├── sys.c
│       │   │   │   ├── websocket_nifs.c
│       │   │   │   └── websocket_nifs.h
│       │   │   └── main.c
│       │   └── tests
│       │       ├── cypress
│       │       │   └── e2e
│       │       │       ├── atomvm.spec.cy.js
│       │       │       ├── call.spec.cy.js
│       │       │       ├── examples.spec.cy.js
│       │       │       ├── html5.spec.cy.js
│       │       │       └── websockets.spec.cy.js
│       │       ├── cypress.config.js
│       │       └── src
│       │           ├── CMakeLists.txt
│       │           ├── test_atomvm.erl
│       │           ├── test_atomvm.html
│       │           ├── test_call.erl
│       │           ├── test_call.html
│       │           ├── test_html5.erl
│       │           ├── test_html5.html
│       │           ├── test_websockets.erl
│       │           └── test_websockets.html
```
