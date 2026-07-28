# [[AtomVM]] files

## [[AtomVM/cmake#files]]

## 

```
.
├── code-queries
│   ├── allocations-exceeding-ensure-free.ql
│   ├── allocations-without-ensure-free.ql
│   ├── mismatched-atom-string-length.ql
│   ├── mismatched-free-type.ql
│   ├── non-term-to-term-func.ql
│   ├── qlpack.yml
│   ├── term-to-non-term-func.ql
│   └── term-use-after-gc.ql
├── CONTRIBUTING.md
```
## [[AtomVM/doc#files]]
## [[AtomVM/examples#files]]
## [[AtomVM/libs#files]]
```
├── renovate.json
├── renovate.json.license
```
## [[AtomVM/src#files]]
## [[AtomVM/test#files]]
```
├── tests
│   ├── CMakeLists.txt
│   ├── erlang_tests
│   │   ├── absovf.erl
│   │   ├── add.erl
│   │   ├── addovf32.erl
│   │   ├── addovf64.erl
│   │   ├── alisp.erl
│   │   ├── bif_bin_arith_ops.erl
│   │   ├── bigfact2.erl
│   │   ├── bigfact3.erl
│   │   ├── bigfact.erl
│   │   ├── biggerdifference.erl
│   │   ├── biggerintegers.erl
│   │   ├── bigint.erl
│   │   ├── bigint_stress.erl
│   │   ├── binary_at_test.erl
│   │   ├── binary_first_test.erl
│   │   ├── binary_is_iolist.erl
│   │   ├── binary_last_test.erl
│   │   ├── bnot64.erl
│   │   ├── booleans2_test.erl
│   │   ├── booleans_test.erl
│   │   ├── boxedabs.erl
│   │   ├── boxed_is_not_float.erl
│   │   ├── boxedlit.erl
│   │   ├── boxedmul.erl
│   │   ├── boxedneg.erl
│   │   ├── bs_append_extra_words.erl
│   │   ├── bs_context_byte_size.erl
│   │   ├── bs_context_to_binary_with_offset.erl
│   │   ├── bs_get_binary2_all_asm.S
│   │   ├── bs_get_binary_fixed_size.erl
│   │   ├── bs_get_float_dynamic_size.erl
│   │   ├── bs_get_integer_fixed_size.erl
│   │   ├── bs_restore2_start_offset.erl
│   │   ├── byte_size_test.erl
│   │   ├── call_with_ref_test.erl
│   │   ├── catch_badmatch.erl
│   │   ├── catch_from_other_module.erl
│   │   ├── catch_nocasematch.erl
│   │   ├── catch_noifmatch.erl
│   │   ├── ceilbadarg.erl
│   │   ├── ceilfloat.erl
│   │   ├── ceilfloatovf.erl
│   │   ├── ceilint.erl
│   │   ├── CMakeLists.txt
│   │   ├── code_load
│   │   │   ├── CMakeLists.txt
│   │   │   └── export_test_module.erl
│   │   ├── compact15bitsinteger.erl
│   │   ├── compact23bitsinteger.erl
│   │   ├── compact23bitsneginteger.erl
│   │   ├── compact27bitsinteger.erl
│   │   ├── complex_list_match_xregs.erl
│   │   ├── complex_struct_size0.erl
│   │   ├── complex_struct_size1.erl
│   │   ├── complex_struct_size2.erl
│   │   ├── complex_struct_size3.erl
│   │   ├── complex_struct_size4.erl
│   │   ├── copy_terms0.erl
│   │   ├── copy_terms10.erl
│   │   ├── copy_terms11.erl
│   │   ├── copy_terms12.erl
│   │   ├── copy_terms13.erl
│   │   ├── copy_terms14.erl
│   │   ├── copy_terms15.erl
│   │   ├── copy_terms16.erl
│   │   ├── copy_terms17.erl
│   │   ├── copy_terms18.erl
│   │   ├── copy_terms1.erl
│   │   ├── copy_terms2.erl
│   │   ├── copy_terms3.erl
│   │   ├── copy_terms4.erl
│   │   ├── copy_terms5.erl
│   │   ├── copy_terms6.erl
│   │   ├── copy_terms7.erl
│   │   ├── copy_terms8.erl
│   │   ├── copy_terms9.erl
│   │   ├── count_char2_bs.erl
│   │   ├── count_char3_bs.erl
│   │   ├── count_char_bs.erl
│   │   ├── count_char.erl
│   │   ├── count_pairs.erl
│   │   ├── datetime.erl
│   │   ├── decode_int24.erl
│   │   ├── decode_int32.erl
│   │   ├── decode_int48.erl
│   │   ├── decode_mqtt.erl
│   │   ├── echo.erl
│   │   ├── erlang_module_loaded.erl
│   │   ├── exactly_eq.erl
│   │   ├── external_proplist_test.erl
│   │   ├── fact.erl
│   │   ├── fail_apply.erl
│   │   ├── fail_apply_last.erl
│   │   ├── fconv_fail_invalid.erl
│   │   ├── float2bin2decimals.erl
│   │   ├── float2bin2.erl
│   │   ├── float2bin2scientific.erl
│   │   ├── float2bin.erl
│   │   ├── float2list2decimals.erl
│   │   ├── float2list2.erl
│   │   ├── float2list2scientific.erl
│   │   ├── float2list.erl
│   │   ├── floatabs.erl
│   │   ├── floatadd.erl
│   │   ├── floataddovf.erl
│   │   ├── float_bif.erl
│   │   ├── float_decode.erl
│   │   ├── floatdiv.erl
│   │   ├── floatext.erl
│   │   ├── float_is_float.erl
│   │   ├── float_is_number.erl
│   │   ├── floatmath.erl
│   │   ├── floatmul.erl
│   │   ├── floatmulovf.erl
│   │   ├── floatneg.erl
│   │   ├── floatsub.erl
│   │   ├── floatsubovf.erl
│   │   ├── float_to_short.erl
│   │   ├── floorbadarg.erl
│   │   ├── floorfloat.erl
│   │   ├── floorfloatovf.erl
│   │   ├── floorint.erl
│   │   ├── fun_call_bif.erl
│   │   ├── function_reference_decode.erl
│   │   ├── gc_safe_x_reg_write.erl
│   │   ├── gen_server_like_test.erl
│   │   ├── guards1.erl
│   │   ├── guards2.erl
│   │   ├── guards3.erl
│   │   ├── guards4.erl
│   │   ├── guards5.erl
│   │   ├── hello_world.erl
│   │   ├── huge.erl
│   │   ├── if_test.erl
│   │   ├── improper_cmp.erl
│   │   ├── improper_concat.erl
│   │   ├── improper_length.erl
│   │   ├── improper_literal.erl
│   │   ├── int28mul.erl
│   │   ├── int28mulneg2.erl
│   │   ├── int28mulneg.erl
│   │   ├── int64_build_binary.erl
│   │   ├── iolist_concat_bin.erl
│   │   ├── is_fun_2_with_frozen2.erl
│   │   ├── is_fun_2_with_frozen.erl
│   │   ├── is_record.erl
│   │   ├── is_ref_test.erl
│   │   ├── is_type.erl
│   │   ├── jsonish_encode.erl
│   │   ├── just_receive_test.erl
│   │   ├── large_int_literal.erl
│   │   ├── len_test.erl
│   │   ├── link_kill_parent.erl
│   │   ├── link_throw.erl
│   │   ├── list2float.erl
│   │   ├── list_concat.erl
│   │   ├── literal_test0.erl
│   │   ├── literal_test1.erl
│   │   ├── literal_test2.erl
│   │   ├── long_atoms.erl
│   │   ├── lowercase.erl
│   │   ├── makefunref.erl
│   │   ├── make_garbage0.erl
│   │   ├── make_garbage1.erl
│   │   ├── make_garbage2.erl
│   │   ├── make_garbage3.erl
│   │   ├── make_garbage4.erl
│   │   ├── make_garbage5.erl
│   │   ├── make_garbage6.erl
│   │   ├── make_garbage7.erl
│   │   ├── makelist_test.erl
│   │   ├── make_ref_test.erl
│   │   ├── map_comparisons.erl
│   │   ├── maps_nifs.erl
│   │   ├── match.erl
│   │   ├── memlimit.erl
│   │   ├── minusone2.erl
│   │   ├── minusone.erl
│   │   ├── minuspow31abs.erl
│   │   ├── minuspow31divminusone.erl
│   │   ├── minuspow31minusone.erl
│   │   ├── minuspow31plusoneabs.erl
│   │   ├── minuspow31plustwoabs.erl
│   │   ├── minuspow63plusoneabs.erl
│   │   ├── minuspow63plustwoabs.erl
│   │   ├── moda.erl
│   │   ├── modb.erl
│   │   ├── modc.erl
│   │   ├── moreintegertests.erl
│   │   ├── morelabels.erl
│   │   ├── mutrec.erl
│   │   ├── negatives2.erl
│   │   ├── negatives.erl
│   │   ├── negdiv.erl
│   │   ├── negovf32.erl
│   │   ├── negovf64.erl
│   │   ├── negovf.erl
│   │   ├── nested_list_size0.erl
│   │   ├── nested_list_size1.erl
│   │   ├── nested_list_size2.erl
│   │   ├── nested_list_size3.erl
│   │   ├── nested_list_size4.erl
│   │   ├── nested_tuple_size0.erl
│   │   ├── nested_tuple_size1.erl
│   │   ├── nested_tuple_size2.erl
│   │   ├── nested_tuple_size3.erl
│   │   ├── nested_tuple_size4.erl
│   │   ├── patternmatchfunc.erl
│   │   ├── pid_to_list_test.erl
│   │   ├── pingpong.erl
│   │   ├── plusone2.erl
│   │   ├── plusone3.erl
│   │   ├── plusone4.erl
│   │   ├── plusone.erl
│   │   ├── pow31abs.erl
│   │   ├── pow31minusoneabs.erl
│   │   ├── pow31plusone.erl
│   │   ├── pow32.erl
│   │   ├── pow32_is_integer.erl
│   │   ├── pow64.erl
│   │   ├── pow64_is_integer.erl
│   │   ├── powsquare.erl
│   │   ├── prime.erl
│   │   ├── prime_ext.erl
│   │   ├── prime_smp.erl
│   │   ├── raise_badmatch.erl
│   │   ├── raise_case_end.erl
│   │   ├── raise_if_end.erl
│   │   ├── ref_to_list_test.erl
│   │   ├── register_and_whereis_badarg.erl
│   │   ├── register_unregister.erl
│   │   ├── rem_and_comp_test.erl
│   │   ├── reraise_raiser.erl
│   │   ├── reraise_reraiser.erl
│   │   ├── roundbadarg.erl
│   │   ├── roundfloat.erl
│   │   ├── roundfloatovf.erl
│   │   ├── roundint.erl
│   │   ├── selval.erl
│   │   ├── send_receive.erl
│   │   ├── send_to_dead_process.erl
│   │   ├── sexp_lexer.erl
│   │   ├── sexp_parser.erl
│   │   ├── simple_list_size0.erl
│   │   ├── simple_list_size1.erl
│   │   ├── sleep.erl
│   │   ├── small_big_ext.erl
│   │   ├── spawn_fun1.erl
│   │   ├── spawn_fun2.erl
│   │   ├── spawn_fun3.erl
│   │   ├── spawn_opt_demonitor_normal.erl
│   │   ├── spawn_opt_link_normal.erl
│   │   ├── spawn_opt_link_throw.erl
│   │   ├── spawn_opt_monitor_error.erl
│   │   ├── spawn_opt_monitor_normal.erl
│   │   ├── spawn_opt_monitor_throw.erl
│   │   ├── stacktrace_function_args.erl
│   │   ├── state_test2.erl
│   │   ├── state_test2_sender.erl
│   │   ├── state_test3.erl
│   │   ├── state_test3_server.erl
│   │   ├── state_test.erl
│   │   ├── string2float.erl
│   │   ├── subovf32.erl
│   │   ├── subovf64.erl
│   │   ├── tagged_tuple_test.erl
│   │   ├── test_abs.erl
│   │   ├── test_add_avm_pack_binary.erl
│   │   ├── test_add_avm_pack_file.erl
│   │   ├── test_allocate_zero.erl
│   │   ├── test_apply.erl
│   │   ├── test_apply_last.erl
│   │   ├── test_atom_ordering.erl
│   │   ├── test_atom_to_binary.erl
│   │   ├── test_atom_to_list.erl
│   │   ├── test_atomvm_random.erl
│   │   ├── test_badarith2.erl
│   │   ├── test_badarith3.erl
│   │   ├── test_badarith4.erl
│   │   ├── test_badarith.erl
│   │   ├── test_base64.erl
│   │   ├── test_bif_badargument2.erl
│   │   ├── test_bif_badargument3.erl
│   │   ├── test_bif_badargument.erl
│   │   ├── test_bigintegers_ordering.erl
│   │   ├── test_bigint_eq.erl
│   │   ├── test_binaries_ordering.erl
│   │   ├── test_binary_copy.erl
│   │   ├── test_binary_eq.erl
│   │   ├── test_binary_longest_common_prefix.erl
│   │   ├── test_binary_match.erl
│   │   ├── test_binary_part.erl
│   │   ├── test_binary_replace.erl
│   │   ├── test_binary_split.erl
│   │   ├── test_binary_to_atom.erl
│   │   ├── test_binary_to_existing_atom.erl
│   │   ├── test_binary_to_integer_2.erl
│   │   ├── test_binary_to_integer.erl
│   │   ├── test_binary_to_list.erl
│   │   ├── test_binary_to_term.erl
│   │   ├── test_bitshift.erl
│   │   ├── test_bitwise2.erl
│   │   ├── test_bitwise.erl
│   │   ├── test_bitwise_large.erl
│   │   ├── test_boolean.erl
│   │   ├── test_bs_create_bin_accum_asm.S
│   │   ├── test_bs_create_bin_accum.erl
│   │   ├── test_bs.erl
│   │   ├── test_bs_init2_heap_allocation.erl
│   │   ├── test_bs_int_any_flags.erl
│   │   ├── test_bs_int.erl
│   │   ├── test_bs_int_unaligned.erl
│   │   ├── test_bs_match_ensure_at_least.erl
│   │   ├── test_bs_match_get_tail.erl
│   │   ├── test_bs_start_match_live.erl
│   │   ├── test_bs_utf.erl
│   │   ├── test_catch.erl
│   │   ├── test_catch_return_atom.erl
│   │   ├── test_close_avm_pack.erl
│   │   ├── test_close_console_driver.erl
│   │   ├── test_close_echo_driver.erl
│   │   ├── test_cmp_term.erl
│   │   ├── test_code_all_available_loaded.erl
│   │   ├── test_code_ensure_loaded.erl
│   │   ├── test_code_get_object_code.erl
│   │   ├── test_code_load_abs.erl
│   │   ├── test_code_load_binary.erl
│   │   ├── test_code_server_nifs.erl
│   │   ├── test_concat_badarg.erl
│   │   ├── test_crc32.erl
│   │   ├── test_crypto_aead.erl
│   │   ├── test_crypto_crypto.erl
│   │   ├── test_crypto.erl
│   │   ├── test_crypto_hash_update.erl
│   │   ├── test_crypto_mac.erl
│   │   ├── test_crypto_misc.erl
│   │   ├── test_crypto_pbkdf2_hmac.erl
│   │   ├── test_crypto_pk.erl
│   │   ├── test_crypto_strong_rand_bytes.erl
│   │   ├── test_debug_line.erl
│   │   ├── test_delete_element.erl
│   │   ├── test_dict.erl
│   │   ├── test_display.erl
│   │   ├── test_display_string.erl
│   │   ├── test_echo_driver.erl
│   │   ├── test_element.erl
│   │   ├── test_erlang_builtins.erl
│   │   ├── test_erlang_loaded.erl
│   │   ├── test_ets.erl
│   │   ├── test_exception_classes.erl
│   │   ├── test_executable_line.erl
│   │   ├── test_exit1.erl
│   │   ├── test_exit2.erl
│   │   ├── test_extended_literal_large.erl
│   │   ├── test_fp_allocate_heap_zero.erl
│   │   ├── test_func_info2.erl
│   │   ├── test_func_info3.erl
│   │   ├── test_func_info.erl
│   │   ├── test_function_exported.erl
│   │   ├── test_function_ordering.erl
│   │   ├── test_fun_info.erl
│   │   ├── test_funs0.erl
│   │   ├── test_funs10.erl
│   │   ├── test_funs11.erl
│   │   ├── test_funs12.erl
│   │   ├── test_funs1.erl
│   │   ├── test_funs2.erl
│   │   ├── test_funs3.erl
│   │   ├── test_funs4.erl
│   │   ├── test_funs5.erl
│   │   ├── test_funs6.erl
│   │   ├── test_funs7.erl
│   │   ├── test_funs8.erl
│   │   ├── test_funs9.erl
│   │   ├── test_fun_to_list.erl
│   │   ├── test_gc.erl
│   │   ├── test_gt_and_le.erl
│   │   ├── test_guards_do_not_raise.erl
│   │   ├── test_has_map_fields.erl
│   │   ├── test_heap_growth.erl
│   │   ├── test_inline_arith.erl
│   │   ├── test_insert_element.erl
│   │   ├── test_integer_to_binary.erl
│   │   ├── test_integer_to_list.erl
│   │   ├── test_is_bitstring_is_binary.erl
│   │   ├── test_is_integer_3.erl
│   │   ├── test_is_not_equal_asm.S
│   │   ├── test_is_not_equal.erl
│   │   ├── test_is_not_type.erl
│   │   ├── test_is_process_alive.erl
│   │   ├── test_link_port.erl
│   │   ├── test_list_eq.erl
│   │   ├── test_list_gc.erl
│   │   ├── test_list_match.erl
│   │   ├── test_list_processes.erl
│   │   ├── test_lists_keyfind.erl
│   │   ├── test_lists_keymember.erl
│   │   ├── test_lists_member.erl
│   │   ├── test_lists_ordering.erl
│   │   ├── test_lists_reverse.erl
│   │   ├── test_list_to_atom.erl
│   │   ├── test_list_to_binary.erl
│   │   ├── test_list_to_bitstring.erl
│   │   ├── test_list_to_existing_atom.erl
│   │   ├── test_list_to_integer.erl
│   │   ├── test_list_to_tuple.erl
│   │   ├── test_list_tuple_eq.erl
│   │   ├── test_make_fun2.erl
│   │   ├── test_make_fun3.erl
│   │   ├── test_make_list.erl
│   │   ├── test_make_tuple.erl
│   │   ├── test_map.erl
│   │   ├── test_match.erl
│   │   ├── test_min_heap_size.erl
│   │   ├── test_min_max_guard.erl
│   │   ├── test_module_info.erl
│   │   ├── test_monitor.erl
│   │   ├── test_monotonic_time.erl
│   │   ├── test_multi_value_comprehension.erl
│   │   ├── test_no_bs_create_bin.erl
│   │   ├── test_node.erl
│   │   ├── test_op_bs_create_bin_asm.S
│   │   ├── test_op_bs_create_bin.erl
│   │   ├── test_op_bs_start_match_asm.S
│   │   ├── test_op_bs_start_match.erl
│   │   ├── test_op_bs_test_unit.erl
│   │   ├── test_open_port_badargs.erl
│   │   ├── test_ordering_0.erl
│   │   ├── test_ordering_1.erl
│   │   ├── test_pids_ordering.erl
│   │   ├── test_port_to_list.erl
│   │   ├── test_process_info.erl
│   │   ├── test_raise_built_stacktrace.erl
│   │   ├── test_raise.erl
│   │   ├── test_raw_raise.erl
│   │   ├── test_recursion_and_try_catch.erl
│   │   ├── test_refc_binaries.erl
│   │   ├── test_ref_eq.erl
│   │   ├── test_refs_ordering.erl
│   │   ├── test_regecho_driver.erl
│   │   ├── test_reraise.erl
│   │   ├── test_selective_receive.erl
│   │   ├── test_send.erl
│   │   ├── test_send_nif_and_echo.erl
│   │   ├── test_setelement.erl
│   │   ├── test_set_tuple_element.erl
│   │   ├── test_size.erl
│   │   ├── test_split_binary.erl
│   │   ├── test_stacktrace.erl
│   │   ├── test_stacktrace.hrl
│   │   ├── test_sub_binaries.erl
│   │   ├── test_system_flag.erl
│   │   ├── test_system_info.erl
│   │   ├── test_system_time.erl
│   │   ├── test_throw_call_ext_last.erl
│   │   ├── test_timeout_not_integer.erl
│   │   ├── test_timestamp.erl
│   │   ├── test_tl.erl
│   │   ├── test_try_case_end.erl
│   │   ├── test_tuple_eq.erl
│   │   ├── test_tuple_is_not_map.erl
│   │   ├── test_tuple_list_eq.erl
│   │   ├── test_tuple_nifs_badargs.erl
│   │   ├── test_tuple_size.erl
│   │   ├── test_tuples_ordering.erl
│   │   ├── test_tuple_to_list.erl
│   │   ├── test_types_ordering.erl
│   │   ├── test_undef.erl
│   │   ├── test_unicode.erl
│   │   ├── test_utf8_atoms.erl
│   │   ├── test_zlib_compress.erl
│   │   ├── throwtest.erl
│   │   ├── to_hrl.erl
│   │   ├── trap_exit_flag.erl
│   │   ├── truncbadarg.erl
│   │   ├── truncfloat.erl
│   │   ├── truncfloatovf.erl
│   │   ├── truncint.erl
│   │   ├── try_catch_test.erl
│   │   ├── try_error2_nif.erl
│   │   ├── try_error_nif.erl
│   │   ├── try_noerror.erl
│   │   ├── tuple_comparisons.erl
│   │   ├── tuple.erl
│   │   ├── tuples_and_list_size0.erl
│   │   ├── tuples_and_list_size1.erl
│   │   ├── tuples_and_list_size2.erl
│   │   ├── tuple_size0.erl
│   │   ├── tuple_size1.erl
│   │   ├── tuple_size2.erl
│   │   ├── tuple_size3.erl
│   │   ├── tuple_size4.erl
│   │   ├── tuple_size5.erl
│   │   ├── tuple_size6.erl
│   │   ├── twentyone_param_function.erl
│   │   ├── twentyone_param_fun.erl
│   │   ├── unary_plus.erl
│   │   ├── unique.erl
│   │   ├── unlink_error.erl
│   │   ├── whereis_dead_process.erl
│   │   └── whereis_fail.erl
│   ├── jit_stream_flash_platform.h
│   ├── libs
│   │   ├── alisp
│   │   │   ├── CMakeLists.txt
│   │   │   ├── rebar.config
│   │   │   ├── test_alisp.erl
│   │   │   └── tests.erl
│   │   ├── eavmlib
│   │   │   ├── CMakeLists.txt
│   │   │   ├── test_ahttp_client.erl
│   │   │   ├── test_dir.erl
│   │   │   ├── test_file.erl
│   │   │   ├── test_http_server.erl
│   │   │   ├── test_mdns.erl
│   │   │   ├── test_port.erl
│   │   │   ├── tests.erl
│   │   │   └── test_timer_manager.erl
│   │   ├── estdlib
│   │   │   ├── CMakeLists.txt
│   │   │   ├── file_uart_hal.erl
│   │   │   ├── mock_uart_hal.erl
│   │   │   ├── notify_init_server.erl
│   │   │   ├── ping_pong_server.erl
│   │   │   ├── test_apply.erl
│   │   │   ├── test_binary.erl
│   │   │   ├── test_calendar.erl
│   │   │   ├── test_epmd.erl
│   │   │   ├── test_file.erl
│   │   │   ├── test_filename.erl
│   │   │   ├── test_gen_event.erl
│   │   │   ├── test_gen_server.erl
│   │   │   ├── test_gen_statem.erl
│   │   │   ├── test_gen_tcp.erl
│   │   │   ├── test_gen_udp.erl
│   │   │   ├── test_inet.erl
│   │   │   ├── test_io_lib.erl
│   │   │   ├── test_json.erl
│   │   │   ├── test_lists.erl
│   │   │   ├── test_lists_subtraction.erl
│   │   │   ├── test_logger.erl
│   │   │   ├── test_maps.erl
│   │   │   ├── test_net.erl
│   │   │   ├── test_net_kernel.erl
│   │   │   ├── test_os.erl
│   │   │   ├── test_proc_lib.erl
│   │   │   ├── test_proplists.erl
│   │   │   ├── test_queue.erl
│   │   │   ├── test_serial_dist_beam_peer.erl
│   │   │   ├── test_serial_dist.erl
│   │   │   ├── test_serial_dist_socat.erl
│   │   │   ├── test_serial_dist_socat_peer.erl
│   │   │   ├── tests.erl
│   │   │   ├── test_sets.erl
│   │   │   ├── test_spawn.erl
│   │   │   ├── test_ssl.erl
│   │   │   ├── test_string.erl
│   │   │   ├── test_supervisor.erl
│   │   │   ├── test_sys.erl
│   │   │   ├── test_tcp_socket.erl
│   │   │   ├── test_timer.erl
│   │   │   ├── test_uart.erl
│   │   │   └── test_udp_socket.erl
│   │   ├── etest
│   │   │   ├── CMakeLists.txt
│   │   │   └── test_eunit.erl
│   │   ├── exavmlib
│   │   │   ├── CMakeLists.txt
│   │   │   ├── GenServerTest.CustomStack.ex
│   │   │   ├── GenServerTest.Stack.ex
│   │   │   ├── Some.Submodule.ex
│   │   │   ├── SupervisorTest.Stack.ex
│   │   │   ├── SupervisorTest.Stack.Sup.ex
│   │   │   └── Tests.ex
│   │   └── jit
│   │       ├── CMakeLists.txt
│   │       ├── jit_aarch64_asm_tests.erl
│   │       ├── jit_aarch64_tests.erl
│   │       ├── jit_arm32_asm_tests.erl
│   │       ├── jit_arm32_tests.erl
│   │       ├── jit_armv6m_asm_tests.erl
│   │       ├── jit_armv6m_tests.erl
│   │       ├── jit_armv7m_asm_tests.erl
│   │       ├── jit_armv7m_tests.erl
│   │       ├── jit_dwarf_tests.erl
│   │       ├── jit_regs_tests.erl
│   │       ├── jit_riscv32_asm_tests.erl
│   │       ├── jit_riscv32_tests.erl
│   │       ├── jit_riscv64_asm_tests.erl
│   │       ├── jit_riscv64_tests.erl
│   │       ├── jit_tests_common.erl
│   │       ├── jit_tests_common.hrl
│   │       ├── jit_tests.erl
│   │       ├── jit_wasm32_asm_tests.erl
│   │       ├── jit_wasm32_tests.erl
│   │       ├── jit_x86_64_asm_tests.erl
│   │       ├── jit_x86_64_tests.erl
│   │       ├── jit_xtensa_asm_tests.erl
│   │       ├── jit_xtensa_tests.erl
│   │       └── tests.erl
│   ├── test.c
│   ├── test-enif.c
│   ├── test-heap.c
│   ├── test-jit_stream_flash.c
│   ├── test-mailbox.c
│   └── test-structs.c
```
## [[AtomVM/tools#files]]
```
```
```
123 directories, 1450 files
```