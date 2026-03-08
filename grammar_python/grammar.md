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

- 0 또는 False를 반환하는 `__len_` 함수가 있는 클래스로 구성된 객체 : False

    ```
    class myclass():
        def __len__(self):
            return 0
    
    myobj = myclass()
    print(bool(myobj)) # False
    ```

- Boolean 값을 반환하는 함수 생성 가능

    ```
    def myFunction():
        return True
    
    print(myFunction()) # True
    ```

### isinstance()

- 객체가 특정 데이터 유형인지 여부를 판단하는 데 사용할 수 있는 함수

    ```
    x = 200
    print(isinstance(x, int)) # True
    ```

### 연산자 (Operator)

#### 산술 연산자

- `+`, `-`, `*`, `/`, `% (나머지)`, `**(거듭제곱)`, `//(몫)`

- `/` : 실수형 값 반환

- `//` : 정수를 반환

#### 할당 연산자

- `=` : `x = 5` == `x = 5`

- `+=` : `x += 3` == `x = x + 3`

- `-=` : `x -= 3` == `x = x - 3`

- `*=` : `x *= 3` == `x = x * 3`

- `/=` : `x /= 3` == `x = x / 3`

- `%=` : `x %= 3` == `x = x % 3`

- `//=` : `x //= 3` == `x = x // 3`

- `**=` : `x **= 3` == `x = x ** 3`

- `&=` : `x &= 3` == `x = x & 3`

    - 좌측 변수에 우측 값을 비트 단위 AND 연산한 결과를 다시 좌측 변수에 할당하는 복합 대입 연산자

- `|=` : `x |= 3` == `x = x | 3`

    - 왼쪽 변수에 오른쪽 값을 비트 단위 OR(|) 연산한 후, 그 결과를 다시 왼쪽 변수에 저장하는 복합 대입 연산자

- `^=` : `x ^= 3` == `x = x ^ 3`

    - XOR 후 할당

    - 같으면 0, 다르면 1

- `>>=` : `x >>= 3` == `x = x >> 3`

    - 오른쪽 시프트 후 할당

    - `>>`는 비트를 오른쪽으로 3칸 이동시키는 연산

- `<<=` : `x <<= 3` == `x = x << 3`

    - 왼쪽 시프트 후 연산

    - `<<`는 비트를 왼쪽으로 3칸 이동시키는 연산

- `:=` : `print(x:=3)` == `x = 3; print(x);`

    - 할당 표현식이다.

    - 값을 대입하면서 동시에 그 값을 식 안에서 사용할 수 있다.

#### 비교 연산자

- `==`, `!=`, `>`, `<`, `>=`, `<=`

- `1 < x < 10` == `1 < x and x < 10`

#### 논리 연산자

- `and` : 둘 다 true 이면 true

- `or` : 둘 중 하나만 true이면 true

- `not` : reverse the result

#### 아이디 연산자 (Identity Operators)

- 실제로 동일한 객체인지, 즉 동일한 메모리 위치에 있는지를 비교

- **is**

    ```
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x

    print(x is z) # True
    print(x is y) # False
    print(x == y) # True
    ```

- **is not**

    ```
    x = ["apple", "banana"]
    y = ["apple", "banana"]

    print(x is not y) # True
    ```

- **`is` VS `==`**

    - **is** : 두 변수가 메모리에서 동일한 객체를 가리키는지 확인

    - **==** : 두 변수의 값이 같은지 확인

    ```
    x = [1, 2, 3]
    y = [1, 2, 3]

    print(x == y) # True
    print(x is y) # False
    ```

#### 멤버십 연산자 (Membership Operators)

- 시퀀스가 객체에 존재하는지 여부를 테스트하는데 사용

- **in** : `x in y`

    ```
    fruits = ["apple", "banana", "cherry"]
    print("banana" in fruits) # True
    ```

- **not in** : `x not in y`

    ```
    fruits = ["apple", "banana", "cherry"]
    print("pineapple" not in fruits) # True
    ```

- 멤버십 연산자는 문자열에서도 작동한다.

#### 비트 연산자

- `&` : AND -> `x & y`

- `|` : OR -> `x|y`

- `^` : XOR -> `x^y`

    - 같으면 1, 다르면 0

- `~` : NOT -> `~x`

    - `-(x + 1)` 하면 된다.

- `<<` : Zero fill left shirt -> `x << 2`

    - 왼쪽으로 2칸 당기기

- `>>` : Signed right shift -> `x >> 2`

    - 오른쪽으로 2칸 밀기

#### 연산자 우선순위

우선순위가 높은 순

1. `()`

2. `**`

3. `+x`, `-x`, `~x`

4. `*`, `/`, `//`, `%`

5. `+`, `-`

6. `<<`, `>>`

7. `&`

8. `^`

9. `|`

10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`

11. `not`

12. `and`

13. `or`

### 리스트 (Lists)

- 리스트는 하나의 변수에 여러 항목을 저장하는 데 사용된다.

- 목록은 대괄호를 사용하여 만든다.

```
thislist = ["apple", "banana", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry']
```

- **특징**

    - 정해진 순서가 있고 그 순서는 변하지 않는다.

        새 항목을 추가하면 목록의 맨 끝에 추가된다.
    
    - 항목을 변경, 추가, 삭제를 할 수 있다.

    - 중복 허용

- **list() 생성자**

    - 새로운 리스트를 생성할 때 `list()` 생성자를 사용한다.

    ```
    thislist = list(("apple", "banana", "cherry"))
    print(thislist) # ['apple', 'banana', 'cherry']
    ```

#### Python Arrays

- **List** : 순서 O, 변경 가능, 중복 허용

- **Tuple** : 순서 O, 변경 불가능, 중복 허용

- **Set** : 순서 X, 변경 불가능, 인덱싱 X, 중복 불가

- **Set** : 순서 O, 변경 가능, 중복 불가

#### List Access Items

- 인덱스 number 사용

> 인덱스가 0부터 시작

- **음수 인덱싱**

    - 인덱스가 -1부터 시작 (뒤에서부터)

- **인덱스 범위**

    - 슬라이싱처럼 하면 된다.

    - 교체 시, 교체할 항목보다 새 항목을 더 많이 삽입하면 새 항목은 지정한 위치에 삽입되고 나머지 항목은 그에 따라 이동한다.

        ```
        thislist = ["apple", "banana", "cherry"]
        thislist[1:2] = ["blackcurrant", "watermelon"]
        print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']
        ```
    
    - 교체 시, 교체할 항목보다 새로 삽입할 항목이 적은 경우, 새 항목은 지정한 위치에 삽입되고 나머지 항목은 그에 따라 이동한다.

        ```
        thislist = ["apple", "banana", "cherry"]
        thislist[1:3] = ["watermelon"]
        print(thislist) # ['apple', 'watermelon']
        ```
    
- **insert()**

    ```
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist) # ['apple', banana', 'watermelon', 'cherry']
    ```

#### Add List Items

- **append()** : 추가

    ```
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist) # ['apple', 'banana', 'cherry', 'orange']
    ```

- **extend()** : 확장

    - 해당 요소들은 목록의 끝에 추가한다.

    - 튜플, 세트, 딕셔너리 등 모든 반복 가능한 객체를 추가할 수 있다.

    ```
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#### Remove List Items

- **remove()**

    ```
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist) # ['apple', 'cherry']
    ```

- 지정된 값을 가진 항목이 두 개 이상이면 첫 번째 항목을 제거한다.

    ```
    thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
    thislist.remove("banana")
    print(thislist) # ['apple', 'cherry', 'banana', 'kiwi']
    ```

- **pop() (지정된 인덱스 제거)**

    ```
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist) # ['apple', 'cherry']
    ```

    - 인덱스 지정하지 않으면 마지막 항목을 제거

        ```
        thislist = ["apple", "banana", "cherry"]
        thislist.pop()
        print(thislist) # ['apple', 'banana']
        ```

- **del()**

    - 지정된 인덱스도 제거

    ```
    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist) # ['banana', 'cherry']
    ```

    - 목록을 완전히 삭제

    ```
    thislist = ["apple", "banana", "cherry"]
    del thislist
    ```

- **clear()**

    - 리스트를 비운다.

    - 목록은 여전히 남아 있지만 내용은 없다.

    ```
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist) # []
    ```

#### List Comprehension

```
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# apple
# banana
# cherry
```

- 기존 리스트의 값을 기반으로 새 리스트를 만들 때 더 간결하다.

    => for문으로

    ```
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)
    
    print(newlist) # ['apple', 'banana', 'mango']
    ```

    => List Comprehension으로

    ```
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist) # ['apple', 'banana', 'mango']
    ```

#### 리스트 정렬

- **sort()**

    - 영숫자 순으로, 오름차순으로 정렬

    - 모든 대문자가 소문자보다 먼저 정렬된다.

    ```
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
    ```

    ```
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist) # [23, 50, 65, 82, 100]
    ```

- **reverse = True**

    - 내림차순 정렬

    ```
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort(reverse = True)
    print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
    ```

    ```
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse = True)
    print(thislist) # [100, 82, 65, 50, 23]
    ```

- **정렬 기능 사용자 지정**

    - 키워드 인수 사용하여 사용자 지정 함수 만들 수 있다.

        `key = function`

    - 이는 리스트를 정렬하는 데 사용될 숫자(가장 작은 숫자부터) 반환한다.

    ```
    def myfunc(n):
        return abs(n - 50) # 절댓값 반환 함수
    
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key = myfunc)
    print(thislist) # [50, 65, 23, 82, 100]
    ```

    - 대소문자 구분하지 않는 정렬 : `str.lower`

    ```
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key = str.lower)
    print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']
    ```

    - 역순 : `reverse()`

    ```
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']
    ```

#### 리스트 복사

- **copy()**

    - 리스트 복사하는 내장된 List 메서드

    ```
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist) # ['apple', 'banana', 'cherry']
    ```

- **list()**

    ```
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist) # ['apple', 'banana', 'cherry']
    ```

- **[:]**

    ```
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist[:]
    print(mylist) # ['apple', 'banana', 'cherry'] 
    ```

#### Join Lists

- **목록 결합 : `+`**

    ```
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3) # ['a', 'b', 'c', 1, 2, 3]
    ```

- **append()**

    ```
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    for x in list2:
        list1.append(x)
    
    print(list1) # ['a', 'b', 'c', 1, 2, 3]
    ```

- **extend()**

    - 한 리스트의 요소를 다른 리스트에 추가

    ```
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1) # ['a', 'b', 'c', 1, 2, 3]
    ```

#### 리스트 메서드

- `append()` : 목록 끝에 요소 추가

- `clear()` : 목록에서 모든 요소 제거

- `copy()` : 목록의 복사본 반환

- `count()` : 지정된 값을 가진 요소의 수 반환

- `extend()` : 현재 목록의 끝에 목록의 요소를 추가

- `index()` : 지정된 값으로 첫 번째 요소의 인덱스를 반환

- `insert()` : 지정된 위치에 요소를 추가

- `pop()` : 지정된 위치에서 요소를 제거

- `remove()` : 지정된 값으로 항목을 제거

- `reverse()` : 목록의 순서를 반대로 바꾼다.

- `sort()` : 목록 정렬