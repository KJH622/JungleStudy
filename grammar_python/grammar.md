## 헷갈리는 개념 모음집

### 줄 바꿈 없이 인쇄

```
print("Hello", end=" ")
print("World!")

# 출력 : Hello World!
```

### 텍스트와 숫자 혼합

```
print("I am", 27, "years old.")

# 출력 : I am 27 years old.
# 콤마(,)를 이용하면 띄어쓰기가 된다.
```

### 표기법

- **카멜 케이스**

    ```
    myVariableName = "John"
    ```

- **파스칼 사건**

    ```
    MyVariableName = "John"
    ```

- **뱀 케이스**

    ```
    my_variable_name = "John"
    ```

### Unpack

- list : `[ ]` => 변경 가능

- tuple : `( )` => 변경 불가능

### 전역 변수

- 함수 외부에서 생성된 변수

- 단, 같은 변수명으로 지역 변수가 존재하면 지역 변수가 우선

### global

- 함수 내부에서 함수 외부(전역 범위)에 선언된 변수를 수정하거나 사용하고자 할 때 사용

### Data Types

- Text Type : `str`

- Numeric Types : `int`, `float`, `complex`

- Sequence Types : `list`, `tuple`, `range`

- Mapping Type : `dict`

- Set Types : `set`, `frozenset`

- Boolean Type : `bool`

- Binary Types : `bytes`, `bytearray`, `memoryview`

- None Type : `NoneType`

### range

```
x = range(3, 10)

# display x:
print(x) # range(3, 10)

# convert to list to display the content of x:
print(list(x)) # [3, 4, 5, 6, 7, 8, 9]
```

### dict

```
x = dict(name="John", age = 36)

# display x:
print(x) # {'name': 'John', 'age': 36}

# display the data type of x:
print(type(x)) # <class 'dict'>
```

### set

- 무작위, 중복 X, 수정 가능

```
x = set(("apple", "banana", "cherry"))

# display x:
print(x) # {'apple', 'cherry', 'banana'}

# display the data type of x:
print(type(x)) # <class 'set'>
```

### fronzenset

- 무작위, 중복 X, 수정 불가능

```
x = fronzenset(("apple", "banana", "cherry"))

# display x:
print(x) # fronzenset({'apple'. 'cherry', 'banana'})

# display the data type of x:
print(type(x)) # <class 'fronzenset'>
```

### bytes

- 불변

- 요소 변경/추가/삭제 불가능

- 데이터 수정이 필요 없는 경우

### bytearray

- 가변

- 요소 변경/추가/삭제 가능

- 데이터를 계속 수정/조작해야 하는 경우

### memoryview

- Python에서 제공하는 내장 라이브러리

- 다양한 데이터 유형의 메모리 버퍼에 대한 안전한 접근 방법

- 메모리 효율성을 극대화하고 성능을 향상시키기 위한 강력한 도구

### 숫자 데이터

- int, float, complex

- **int** : 소수점이 없는 양수 또는 음수

- **float** : 소수점 이하 자릿수가 하나 이상인 숫자

    - e를 사용하여 10의 거듭제곱 표현 가능

- **complex** : 허수 부분을 j로 표현

### 난수 (Random Number)

- 파이썬은 `random()` 함수 없다.

- 단, random() 내장 모듈이 있다.

```
import random

print(random.randrange(1, 10))
```

### 여러 줄 문자열

- 세 개의 따옴표 사용

### 문자열에 특정 구문이나 문자가 존재하는지 확인

- `in` : 존재하는가

- `not in` : 존재하지 않는가


### Slicing

- 문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분하여 지정한다.

- 시작 인덱스는 0

- 끝 인덱스는 출력 시 포함되지 않음

```
b = "Hello, World!"
print(b[2:5]) # llo
```

- 시작 인덱스 생략 시 첫 번째 문자부터 시작된다.

```
b = "Hello, World!"
print(b[:5]) # Hello
```

- 끝 인덱스를 생략하면 맨 끝까지 이동한다.

```
b = "Hello, World!"
print(b[2:]) # llo, World!
```

- 문자열의 끝에서부터 슬라이스를 하려면 음수 인덱스를 사용한다.

```
b = "Hello, World!"
print(b[-5:-2]) # orl
```

### 문자열 수정

- 내장 메서드가 존재한다.

#### Upper Case

- 대문자로 변환

```
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!
```

### Lower Case

- 소문자로 변환

```
a = "Hello, World!"
print(a.lower()) # hello, world!
```

### 공백 제거

- 실제 텍스트 앞

```
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

### 문자열 바꾸기

```
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!
```

### 문자열 분할

- 구분자를 발견하면 문자열을 부분 문자열로 분할한다.

```
a = "Hello, World!"
print(a.split(",")) # ['Hello', 'World!']
```

### F-Strings

```
age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36
```

### Placeholders and Modifiers

- Placeholder는 변수, operations, functions 값을 format하는 modifiers를 포함한다.

```
price = 59
txt = f"The price is {price} dollars"
print(txt) # 59
```

- `.2f`는 소수점 이하 두 자리까지 표시되는 고정 소수점 숫자를 의미한다.

```
price = 59
txt = f"The price is {price:.2f} dollars"
price(txt)
# The price is 59.00 dollars
```

- Placeholder에는 수학 연산과 같은 파이썬 코드가 포함될 수 있다.

```
txt = f"The price is {20 * 59} dollars"
print(txt)
# The price is 1180 dollars
```

### 이스케이프 문자

- 백슬래시(`\`) 뒤에 삽입하려는 문자를 붙인 것이다.

- `\'` : 작은 따옴표

- `\\` : 백슬래시

- `\n` : 줄바꿈

- `\r` : Carriage Return. 커서를 현재 줄의 맨 앞으로 이동시키라는 명령

- `\t` : 탭

- `\b` : backspace

- `\f` : 페이지 구분 기호

- `\ooo` : 8진수 이스케이프 시퀀스

- `\xxx` : 16진수 이스케이프 시퀀스

### Boolean

- True, False로 반환

- `bool()` 함수를 이용

- 즉, 빈 문자열을 제외한 모든 문자열은 True

- 0을 제외한 모든 숫자는 True

- 