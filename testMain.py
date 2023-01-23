import main
import unittest.mock

def test_convert_to_decimal():
    input_str = 'I'
    expected_output = '1'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output

    input_str = 'V'
    expected_output = '5'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output
        
    input_str = 'X'
    expected_output = '10'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output

    input_str = 'L'
    expected_output = '50'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output
        
    input_str = 'C'
    expected_output = '100'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output
    
    input_str = 'D'
    expected_output = '500'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output
    
    input_str = 'M'
    expected_output = '1000'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output

    input_str = 'IV'
    expected_output = '4'
    with unittest.mock.patch('builtins.input', lambda: input_str):
        assert main.convert_to_decimal(input_str) == expected_output
