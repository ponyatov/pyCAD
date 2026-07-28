# libAtomVM

```e
module libAtomVM {
    module atom {
        module atom_table
        module defaultatoms
    }
    module avmpack
    module bif
    module bitstring
    module context
    module globalcontext
    module debug
    module dictionary
    module dist_nifs
    module ets
    module ets_multimap
    module exportedfunction
    module external_term
    module float_utils
    module iff
    module inet
    module interop
    module intn
    module jit
    module jit_stream_flash
    module listeners
    module list
    module mailbox
    module memory
    module module
    module nifs
    module opcodes
    module opcodesswitch
    module otp_crypto
    module otp_net
    module otp_socket
    module otp_ssl
    module overflow_helpers
    module platform_nifs
    module port
    module portnifloader
    module posix_nifs
    module refc_binary
    module resources
    module scheduler
    module smp
    module stacktrace
    module synclist
    module sys
    module sys_mbedtls
    module tempstack
    module term
    module term_typedef
    module timer_list
    module trace
    module unicode
    module unlocalized
    module utils
    module valueshashtable
    module version
}
```

## files

```
├── src
│   ├── libAtomVM
│   │   ├── atom.c
│   │   ├── atom.h
│   │   ├── atom_table.c
│   │   ├── atom_table.h
│   │   ├── atomvm_version.h
│   │   ├── avmpack.c
│   │   ├── avmpack.h
│   │   ├── bif.c
│   │   ├── bif.h
│   │   ├── bifs.gperf
│   │   ├── bitstring.c
│   │   ├── bitstring.h
│   │   ├── CMakeLists.txt
│   │   ├── context.c
│   │   ├── context.h
│   │   ├── debug.c
│   │   ├── debug.h
│   │   ├── defaultatoms.c
│   │   ├── defaultatoms.def
│   │   ├── defaultatoms.h
│   │   ├── dictionary.c
│   │   ├── dictionary.h
│   │   ├── dist_nifs.c
│   │   ├── dist_nifs.h
│   │   ├── erl_nif.h
│   │   ├── erl_nif_priv.h
│   │   ├── ets.c
│   │   ├── ets.h
│   │   ├── ets_multimap.c
│   │   ├── ets_multimap.h
│   │   ├── exportedfunction.h
│   │   ├── external_term.c
│   │   ├── external_term.h
│   │   ├── float_utils.c
│   │   ├── float_utils.h
│   │   ├── globalcontext.c
│   │   ├── globalcontext.h
│   │   ├── iff.c
│   │   ├── iff.h
│   │   ├── inet.c
│   │   ├── inet.h
│   │   ├── interop.c
│   │   ├── interop.h
│   │   ├── intn.c
│   │   ├── intn.h
│   │   ├── jit.c
│   │   ├── jit.h
│   │   ├── jit_stream_flash.c
│   │   ├── jit_stream_flash.h
│   │   ├── listeners.h
│   │   ├── list.h
│   │   ├── mailbox.c
│   │   ├── mailbox.h
│   │   ├── memory.c
│   │   ├── memory.h
│   │   ├── module.c
│   │   ├── module.h
│   │   ├── nifs.c
│   │   ├── nifs.gperf
│   │   ├── nifs.h
│   │   ├── opcodes.def
│   │   ├── opcodesswitch.h
│   │   ├── otp_crypto.c
│   │   ├── otp_crypto.h
│   │   ├── otp_net.c
│   │   ├── otp_net.h
│   │   ├── otp_socket.c
│   │   ├── otp_socket.h
│   │   ├── otp_ssl.c
│   │   ├── otp_ssl.h
│   │   ├── overflow_helpers.h
│   │   ├── platform_nifs.h
│   │   ├── port.c
│   │   ├── port.h
│   │   ├── portnifloader.c
│   │   ├── portnifloader.h
│   │   ├── posix_nifs.c
│   │   ├── posix_nifs.h
│   │   ├── refc_binary.c
│   │   ├── refc_binary.h
│   │   ├── resources.c
│   │   ├── resources.h
│   │   ├── scheduler.c
│   │   ├── scheduler.h
│   │   ├── smp.h
│   │   ├── stacktrace.c
│   │   ├── stacktrace.h
│   │   ├── synclist.h
│   │   ├── sys.h
│   │   ├── sys_mbedtls.h
│   │   ├── tempstack.h
│   │   ├── term.c
│   │   ├── term.h
│   │   ├── term_typedef.h
│   │   ├── timer_list.c
│   │   ├── timer_list.h
│   │   ├── trace.h
│   │   ├── unicode.c
│   │   ├── unicode.h
│   │   ├── unlocalized.c
│   │   ├── unlocalized.h
│   │   ├── utils.c
│   │   ├── utils.h
│   │   ├── valueshashtable.c
│   │   ├── valueshashtable.h
│   │   └── version.h.in
```

## [[atom]]
## [[atom_table]]
## [[avmpack]]
## [[bif]]
## [[bifs]].gperf
## [[bitstring]]
CMakeLists.txt
## [[context]]
## [[debug]]
## [[defaultatoms]]
## [[dictionary]]
## [[dist_nifs]]
## [[erl_nif]]
## [[erl_nif_priv]]
## [[ets]]
## [[ets_multimap]]
## [[exportedfunction]]
## [[external_term]]
## [[float_utils]]
## [[globalcontext]]
## [[iff]]
## [[inet]]
## [[interop]]
## [[intn]]
## [[jit]]
## [[listeners]]
## [[list]]
## [[mailbox]]
## [[memory]]
## [[module]]
## [[nifs]]
## [[opcodes]].def
## [[opcodesswitch]]
## [[otp_crypto]]
## [[otp_net]]
## [[otp_socket]]
## [[otp_ssl]]
## [[overflow_helpers]]
## [[platform_nifs]]
## [[port]]
## [[portnifloader]]
## [[posix_nifs]]
## [[refc_binary]]
## [[resources]]
## [[scheduler]]
## [[smp]]
## [[stacktrace]]
## [[synclist]]
## [[sys]]
## [[sys_mbedtls]]
## [[tempstack]]
## [[term]]
## [[term_typedef]]
## [[timer_list]]
## [[trace]]
## [[unicode]]
## [[unlocalized]]
## [[utils]]
## [[valueshashtable]]
## [[AromVM/version|version]]
