def mock_unit_test(dict_inputs_tests: dict[list[any]], outputs_expected: list[any], function) -> bool:
    len_input: int = len(list(dict_inputs_tests.values())[0])
    len_dict: int = len(dict_inputs_tests)

    assert_values_is_ok(dict_inputs_tests, outputs_expected)

    parameters: list[str] = list(dict_inputs_tests.keys())
    
    for i in range(len_input):
        input_test_values = [list(dict_inputs_tests.values())[v][0] for v in range(len_dict)]
        input_test: dict = dict(zip(parameters, input_test_values))
        output_expected = outputs_expected[i]

        output = function(**input_test)
        assert output == output_expected, f"ERROR! Input: {input_test} \nOutput: {output} \nOutput_Expected: {output_expected}"
        print(f"{i+1}° teste: OK!")
        
    print(f"Todos os {len_dict} testes passaram com sucessso!")
    return True


def assert_values_is_ok(dict_inputs_tests: dict[list[any]], outputs_expected: list[any]) -> bool:
    len_input: int = len(list(dict_inputs_tests.values())[0])
    len_dict: int = len(dict_inputs_tests)

    assert len_input == len(outputs_expected), f"Tamanhos incompatíveis (IO): \ninputs_tests ({len_input}) != outputs_expected ({len(outputs_expected)})"
    
    if len_dict > 1:
        for idx, param in enumerate(list(dict_inputs_tests.values())):
            len_input_param = len(param)

            assert len_input == len_input_param, f"Tamanhos incompatíveis nos parâmetros dos inputs: \nlen_param_0 ({len_input}) != len_param_{idx} ({len_input_param})"
        
    return True