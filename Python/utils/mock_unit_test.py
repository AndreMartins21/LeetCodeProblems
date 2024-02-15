def mock_unit_test(dict_io_tests: dict[list[list[any]]], function) -> bool:
    inputs_tests, outputs_expected = dict_io_tests.values()

    assert len(inputs_tests) == len(outputs_expected), f"Tamanhos incompatíveis: \ninputs_tests ({len(inputs_tests)}) != outputs_expected ({len(outputs_expected)})"

    for i in range(len(inputs_tests)):
        input_test = inputs_tests[i]
        output_expected = outputs_expected[i]

        output = function(input_test)
        assert output == output_expected, f"ERROR! Input: {input_test} \nOutput: {output} \nOutput_Expected: {output_expected}"
    print(f"Todos os {len(inputs_tests)} testes passaram com sucessso!")
    return True