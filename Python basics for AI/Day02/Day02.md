# Day02

2021.01.19

## variables

### 변수의 개요

- 데이터(값)을 저장하기 위한 메모리 공간에 붙여준 이름
- 변수에 값을 할당한다는 것은 해당 메모리 주소의 공간에 값을 저장한다는 것이다.

## function_and_io

### 함수의 개요

- 코드를 논리적인 단위로 분리
- parameter: 함수의 입력 값 인터페이스, argument: 실제 parameter에 대입된 값

## conditionals and loops

### 디버깅

코드의 오류를 발견하여 수정하는 과정으로 오류의 '원인'을 알고 '해결책'을 찾아야 한다.

보통 발생하는 오류는 문법적 에러와 논리적 에러 두가지로 나뉠 수 있다.

#### 문법적 에러

문법적 에러는 인터프리터가 직접적으로 터미널에 무슨 에러가 났는지 알려주기 때문에 쉽게 수정 가능하다.

#### 논리적 에러

논리적 에러는 내가 만든 코드가 의도한 바를 제대로 수행하지 못했을 때 발생한다. 논리적 흐름 단위로 프린트 문을 찍어서 값이 제대로 나왔는지 확인하거나 브레이킹 포인트를 걸고 디버깅 툴을 활용하여 해결한다.

## str and advanced function

### 함수 호출 방식

- 값에 의한 호출
- 참조에 의한 호출
- 객체 참조에 의한 호출

파이썬의 함수 호출 방식은 객체 참조에 의한 호출 방식이다. 즉, 객체의 주소가 함수로 전달되는 방식이다.

전달된 객체를 참조하여 변경 시 호출자에게 영향을 주나, 새로운 객체를 만들 경우 호출자에게 영향을 주지 않는다.

```python
def hi(x):
    x.append(1)
    x = [2,3]
    
y = [0]
hi(y)
print(y)
```

### function type hints

파이썬의 가장 큰 특징은 동적 타이핑으로 인터프리터가 코드 실행 단계에서 데이터의 타입을 자동으로 정해주는 것이다. 굉장히 편리한 기능이지만, 미리 타입을 지정해주지 않기 때문에 속도가 느리고 처음 함수를 사용하는 사용자가 interface를 알기 어렵다는 단점이 있다.

이 때문에, python 3.5 버전 이후로는 PEP 484에 기반하여 type hints 기능을 제공한다.

type hints는 다음과 같은 장점이 있다.

- 사용자에게 인터페이스를 명확히 알려줄 수 있다.
- 함수의 문서화시 parameter에 대한 정보를 명확히 알 수 있다.
- mypy, IDE, linter 등을 통해 코드의 발생 가능한 오류를 사전에 확인 가능하다.

```python
# def function_name(param: type) -> return_type
def swap(x: int, y: int) -> int:
    tmp = x
    x = y
    y = tmp
    return x
```

개인적으로 몰랐던 기능인데 알아두면 굉장히 유용할 것 같다.

### function docstring

함수에 대한 상세스펙을 사전에 작성하면 함수 사용자의 이해도가 올라갈 수 있다.

파이썬에서는 보통 함수명 아래에 세개의 따옴표로 docstring 영역을 표시한다.

```python
def func():
    """
    This is Function!!
    """
```

VScode IDE 에서는 Extension에서 docstring을 검색하여 Python Docstring Generator를 설치한 후, `f1`키를 눌러 Generate docstring을 검색해주면 편하게 일정 포맷의 docstring을 사용할 수 있다.

```python
def swap(x:int,y:int) -> None:
    """[summary]

    Args:
        x (int): [description]
        y (int): [description]

    Returns:
        [type]: [description]
    """    
    tmp = x
    x = y
    y = tmp

    return None
```

### 코딩 컨벤션

코딩을 할 때, 사람의 이해를 돕기 위해서는 규칙이 필요한데 그러한 규칙을 코딩 컨벤션이라 한다.

파이썬에서는 최근에 black 모듈을 활용하여 pep8 like 수준을 준수한다. `conda install black` 명령어를 통해 모듈 설치한 후, `black [file_name].py` 명령어를 사용하면 컨벤션에 맞춰서 파일을 재설정해준다. 파일 재설정 후 flake8 모듈로 체크해볼 수도 있다.

```bash
conda install black
conda install flake8
black test.py
flake8 test.py
```

