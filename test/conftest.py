from datetime import datetime
from typing import List, Optional, TypeVar

T = TypeVar('T')

def generate_invalid_values(valid_type: T):
    TEST_PATTERN = [None, 'string', 100, 1.0, True, datetime(2022, 1, 1, 1, 1, 1)]
    TEST_PATTERN.extend([[], ['str1, str2'], [100, 200], [1.0, 2.1], [True, False], [datetime(2012, 1, 1, 1, 1, 1), datetime(2022, 2, 2, 2, 2, 2)]])
    invalid_values = []

    if valid_type == str:
        invalid_values = [value for value in TEST_PATTERN if not isinstance(value, str)]
    elif valid_type == int:
        invalid_values = [value for value in TEST_PATTERN if not isinstance(value, int)]
    elif valid_type == float:
        invalid_values = [value for value in TEST_PATTERN if not isinstance(value, float)]
    elif valid_type == bool:
        invalid_values = [value for value in TEST_PATTERN if not isinstance(value, bool)]
    elif valid_type == datetime:
        invalid_values = [value for value in TEST_PATTERN if not isinstance(value, datetime)]
    # List
    elif valid_type == List[str]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, str) for i in value))]
    elif valid_type == List[int]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, int) for i in value))]
    elif valid_type == List[float]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, float) for i in value))]
    elif valid_type == List[bool]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, bool) for i in value))]
    elif valid_type == List[datetime]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, datetime) for i in value))]
    # Optional
    elif valid_type == Optional[str]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, str) or value is None)]
    elif valid_type == Optional[int]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, int) or value is None)]
    elif valid_type == Optional[float]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, float) or value is None)]
    elif valid_type == Optional[bool]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, bool) or value is None)]
    elif valid_type == Optional[datetime]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, datetime) or value is None)]
    # Optional List
    elif valid_type == Optional[List[str]]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, str) for i in value) or value is None)]
    elif valid_type == Optional[List[int]]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, int) for i in value) or value is None)]
    elif valid_type == Optional[List[float]]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, float) for i in value) or value is None)]
    elif valid_type == Optional[List[bool]]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, bool) for i in value) or value is None)]
    elif valid_type == Optional[List[datetime]]:
        invalid_values = [value for value in TEST_PATTERN if not (isinstance(value, List) and all(isinstance(i, datetime) for i in value) or value is None)]

    return invalid_values

### TEST ###
def test_generate_invalid_values():
    # Test for str type
    invalid_values_str = generate_invalid_values(str)
    assert not str in invalid_values_str
    # Test for int type
    invalid_values_int = generate_invalid_values(int)
    assert not int in invalid_values_int
    # Test for float type
    invalid_values_float = generate_invalid_values(float)
    assert not float in invalid_values_float
    # Test for bool type
    invalid_values_bool = generate_invalid_values(bool)
    assert not bool in invalid_values_bool
    # Test for datetime type
    invalid_values_datetime = generate_invalid_values(datetime)
    assert not datetime in invalid_values_datetime

def test_generate_invalid_values_list():
    # Test for List[str] type
    invalid_values_list_str = generate_invalid_values(List[str])
    for value in invalid_values_list_str:
        assert not isinstance(value, List) or not all(isinstance(i, str) for i in value)
    # Test for List[int] type
    invalid_values_list_int = generate_invalid_values(List[int])
    for value in invalid_values_list_int:
        assert not isinstance(value, List) or not all(isinstance(i, int) for i in value)
    # Test for List[float] type
    invalid_values_list_float = generate_invalid_values(List[float])
    for value in invalid_values_list_float:
        assert not isinstance(value, List) or not all(isinstance(i, float) for i in value)
    # Test for List[bool] type
    invalid_values_list_bool = generate_invalid_values(List[bool])
    for value in invalid_values_list_bool:
        assert not isinstance(value, List) or not all(isinstance(i, bool) for i in value)
    # Test for List[datetime] type
    invalid_values_list_datetime = generate_invalid_values(List[datetime])
    for value in invalid_values_list_datetime:
        assert not isinstance(value, List) or not all(isinstance(i, datetime) for i in value)

def test_generate_invalid_values_optional():
    # Test for Optional[str] type
    invalid_values_optional_str = generate_invalid_values(Optional[str])
    for value in invalid_values_optional_str:
        assert not isinstance(value, str) and value is not None
    # Test for Optional[int] type
    invalid_values_optional_int = generate_invalid_values(Optional[int])
    for value in invalid_values_optional_int:
        assert not isinstance(value, int) and value is not None
    # Test for Optional[float] type
    invalid_values_optional_float = generate_invalid_values(Optional[float])
    for value in invalid_values_optional_float:
        assert not isinstance(value, float) and value is not None
    # Test for Optional[bool] type
    invalid_values_optional_bool = generate_invalid_values(Optional[bool])
    for value in invalid_values_optional_bool:
        assert not isinstance(value, bool) and value is not None
    # Test for Optional[datetime] type
    invalid_values_optional_datetime = generate_invalid_values(Optional[datetime])
    for value in invalid_values_optional_datetime:
        assert not isinstance(value, datetime) and value is not None

def test_generate_invalid_values_optional_list():
    # Test for Optional[List[str]] type
    invalid_values_optional_list_str = generate_invalid_values(Optional[List[str]])
    for value in invalid_values_optional_list_str:
        assert not (isinstance(value, List) and all(isinstance(i, str) for i in value)) and value is not None
    # Test for Optional[List[int]] type
    invalid_values_optional_list_int = generate_invalid_values(Optional[List[int]])
    for value in invalid_values_optional_list_int:
        assert not (isinstance(value, List) and all(isinstance(i, int) for i in value)) and value is not None
    # Test for Optional[List[float]] type
    invalid_values_optional_list_float = generate_invalid_values(Optional[List[float]])
    for value in invalid_values_optional_list_float:
        assert not (isinstance(value, List) and all(isinstance(i, float) for i in value)) and value is not None
    # Test for Optional[List[bool]] type
    invalid_values_optional_list_bool = generate_invalid_values(Optional[List[bool]])
    for value in invalid_values_optional_list_bool:
        assert not (isinstance(value, List) and all(isinstance(i, bool) for i in value)) and value is not None
    # Test for Optional[List[datetime]] type
    invalid_values_optional_list_datetime = generate_invalid_values(Optional[List[datetime]])
    for value in invalid_values_optional_list_datetime:
        assert not (isinstance(value, List) and all(isinstance(i, datetime) for i in value)) and value is not None


if __name__ == "__main__":
    print("str: ", generate_invalid_values(str))
    print("int: ", generate_invalid_values(int))
    print("float: ", generate_invalid_values(float))
    print("bool: ", generate_invalid_values(bool))
    print("datetime: ", generate_invalid_values(datetime))
    print("List[str]: ", generate_invalid_values(List[str]))
    print("List[int]: ", generate_invalid_values(List[int]))
    print("List[float]: ", generate_invalid_values(List[float]))
    print("List[bool]: ", generate_invalid_values(List[bool]))
    print("List[datetime]: ", generate_invalid_values(List[datetime]))
    print("Optional[str]: ", generate_invalid_values(Optional[str]))
    print("Optional[int]: ", generate_invalid_values(Optional[int]))
    print("Optional[float]: ", generate_invalid_values(Optional[float]))
    print("Optional[bool]: ", generate_invalid_values(Optional[bool]))
    print("Optional[datetime]: ", generate_invalid_values(Optional[datetime]))
    print("Optional[List[str]]: ", generate_invalid_values(Optional[List[str]]))
    print("Optional[List[int]]: ", generate_invalid_values(Optional[List[int]]))
    print("Optional[List[float]]: ", generate_invalid_values(Optional[List[float]]))
    print("Optional[List[bool]]: ", generate_invalid_values(Optional[List[bool]]))
    print("Optional[List[datetime]]: ", generate_invalid_values(Optional[List[datetime]]))
