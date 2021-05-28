# Session 4 assignment of EPAi3.0
## Numeric Types - II

### Qualean class Implementation
 Qualean class is inspired by Boolean+Quantum concepts. 
 We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. 
 The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 

#### **Functions**

#### **1) __init__ function**:
This is the constructor of the class 
**Parameters**
1) number: 
    a) this is an optional parameter
    b) accepted values are (1,0,-1)
    c) default value is 1 
Note: Default value can be either 1 or -1 as test_million_qualeans_sum test case assumes the sum of million Qualean decimal values moves away from 0 and test_million_qualeans_mul assumes product of million values moves towards 0
If Default value is 0 test_million_qualeans_sum test case fails

**Exceptions**
1) any value other than (1,0,-1) are not allowed
2) string value is not allowed

**Implementation**
1) Qualean value is calculated by round(number*(random.uniform(-1,1)),10)

#### **2) __repr__ function**:
By Default this function returns the location of the object.
**Implementation**
This is overridden to print f'Qualean Class Instance'

#### **3) __str__ function**:
This function is called by print function
**Implementation**
This returns 'Qualean String for number: {0}'.format(self.number)

#### **4) return_qualean function**:
This function returns the qualean value
**Implementation**
return self.value

#### **5) __sqrt__ function**:
This function returen square root value of qualean
**Implementation**
1) If qualean value is true it returns square root rounded to 10 decimal places
round(Decimal(self.value).sqrt(), 10)
2) If If qualean value is true it returns square root of invertsign rounded to 10 decimal places
str(round(Decimal(self.__invertsign__()).sqrt(), 10)) + 'i'

#### **6) __add__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean sum of qualean values is returned
2) else default addition of qualean value and other object is returned

#### **7) __mul__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean product of qualean values is returned
2) else default product of qualean value and other object is returned

#### **8) __eq__ function**:
**Parameters**
1) other_object: any object

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **9) __float__ function**:
This function returns float value of qualean
**Implementation**
return float(self.value)

#### **10) __ge__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **11) __gt__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **12) __le__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **13) __lt__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **14) __invertsign__ function**:
This function converts sign of qualean
**Implementation**
return -self.value

#### **15) __eq__ function**:
**Parameters**
1) other_object: any object 

**Exceptions**
1) TypeError if other_object is string

**Implementation**
1) if other object is instance of qualean comparition of qualean values is returned
2) else default comparition of qualean value and other object is returned

#### **16) __bool__ function**
This function converts qualean to boolean value
**Parameters**
1) other_object: any object 

**Implementation**
return self.value != 0

#### **17) __and__ function**:
This function performs conditional "and" operation
**Implementation**
1) if either of both quealean values is 0 then return false
2) if both quealean values are not 0 then return true

#### **18) __or__ function**:
This function performs conditional "or" operation
**Implementation**
1) if either of both quealean values is 0 then return true
2) if both quealean values are 0 then return false



pytest -v (local output)

Note: Locally "import test_session4" is added to test_session4 but not pushed to github

PS D:\TSAI\EPAi\Session4_Numerical_Types_II\session-4-shravankgl> pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.8.3, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- c:\python38\python.exe
cachedir: .pytest_cache
rootdir: D:\TSAI\EPAi\Session4_Numerical_Types_II\session-4-shravankgl
collected 42 items

test_session4.py::test_readme_exists PASSED                                                                      [  2%]
test_session4.py::test_readme_contents PASSED                                                                    [  4%]
test_session4.py::test_readme_proper_description PASSED                                                          [  7%]
test_session4.py::test_readme_file_for_formatting PASSED                                                         [  9%]
test_session4.py::test_indentations PASSED                                                                       [ 11%]
test_session4.py::test_function_name_had_cap_letter PASSED                                                       [ 14%]
test_session4.py::test_qualean_repr PASSED                                                                       [ 16%]
test_session4.py::test_qualean_str PASSED                                                                        [ 19%]
test_session4.py::test_function_qualean_type PASSED                                                              [ 21%]
test_session4.py::test_qualean_decimal_precision PASSED                                                          [ 23%]
test_session4.py::test_function_count PASSED                                                                     [ 26%]
test_session4.py::test_function_repeatations PASSED                                                              [ 28%]
test_session4.py::test_100_qualeans PASSED                                                                       [ 30%]
test_session4.py::test_function_sqrt PASSED                                                                      [ 33%]
test_session4.py::test_million_qualeans_sum PASSED                                                               [ 35%]
test_session4.py::test_million_qualeans_mul PASSED                                                               [ 38%]
test_session4.py::test_qualean_valid_input PASSED                                                                [ 40%]
test_session4.py::test_invalid_input_valueerror_provides_relevant_message PASSED                                 [ 42%]
test_session4.py::test_qualean_validity PASSED                                                                   [ 45%]
test_session4.py::test_function_and PASSED                                                                       [ 47%]
test_session4.py::test_and_q_notdefined PASSED                                                                   [ 50%]
test_session4.py::test_and_q_false PASSED                                                                        [ 52%]
test_session4.py::test_function_or PASSED                                                                        [ 54%]
test_session4.py::test_or_q_notdefined PASSED                                                                    [ 57%]
test_session4.py::test_or_q_false PASSED                                                                         [ 59%]
test_session4.py::test_function_add PASSED                                                                       [ 61%]
test_session4.py::test_function_add_non_qualean PASSED                                                           [ 64%]
test_session4.py::test_function_mul PASSED                                                                       [ 66%]
test_session4.py::test_function_mul_non_qualean PASSED                                                           [ 69%]
test_session4.py::test_function_ge PASSED                                                                        [ 71%]
test_session4.py::test_function_ge_non_qualean PASSED                                                            [ 73%]
test_session4.py::test_function_gt PASSED                                                                        [ 76%]
test_session4.py::test_function_gt_non_qualean PASSED                                                            [ 78%]
test_session4.py::test_function_le PASSED                                                                        [ 80%]
test_session4.py::test_function_le_non_qualean PASSED                                                            [ 83%]
test_session4.py::test_function_lt PASSED                                                                        [ 85%]
test_session4.py::test_function_lt_non_qualean PASSED                                                            [ 88%]
test_session4.py::test_function_with_non_number PASSED                                                           [ 90%]
test_session4.py::test_function_bool PASSED                                                                      [ 92%]
test_session4.py::test_function_eq PASSED                                                                        [ 95%]
test_session4.py::test_function_float PASSED                                                                     [ 97%]
test_session4.py::test_function_invertsign PASSED                                                                [100%]

================================================= 42 passed in 3.45s ==================================================