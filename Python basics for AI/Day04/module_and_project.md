# 모듈과 패키지

#### 모듈 개요

프로그램에서는 작은 프로그램 조각들, 즉 모듈들을 모아서 하나의 큰 프로그램을 개발한다.

프로그램을 모듈화 시키면 다른 프로그램이 사용하기 쉬워진다. 예를들어 카카오톡 게임을 위한 카카오톡 접속 모듈이 있다.

#### 패키지 개요

모듈을 모아놓은 단위, 하나의 프로그램이다.

## 모듈

파이썬에서의 모듈은 .py 파일을 의미한다.

같은 폴더에 모듈에 해당하는 .py 파일과 사용하는 .py 파일을 저장한 후에 import 문을 사용하여 모듈을 호출한다.

### namespace

모듈을 호출할 때 범위를 정하는 방법이다. 모듈 안에는 함수와 클래스 등이 존재하는데, namespace를 사용하면 이 중 필요한 내용만 골라서 호출할 수 있다.

from과 import 키워드를 사용한다.

```python
# alias(별칭) 설정
from collections import deque as de
# 모든 함수 또는 클래스 호출
from collections import *
```

### Built-in Modules

파이썬이 기본 제공하는 라이브러리로 문자처리, 웹, 수학 등 다양한 모듈이 제공된다. 별다른 조치없이 import 문으로 활용 가능하다.



## 패키지

하나의 대형 프로젝트를 만드는 코드의 묶음이다.

다양한 모듈들의 합, 폴더로 연결되고 `__init__`, `__main__` 등 키워드 파일명이 사용된다.

다양한 오픈 소스들은 모두 패키지로 관리되고 있다.

### Package 만들기

- 폴더별로 `__init__.py` 구성하기
  - 현재 폴더가 패키지임을 알리는 초기화 스크립트
  - 없을 경우 패키지로 간주하지 않는다(3.3 + 부터는 없어도 패키지로 간주한다)
  - 하위 폴더와 py 파일(모듈)을 모두 포함
  - import와 `__all__` 키워드 사용



## 가상환경 설정하기

프로젝트 진행 시 필요한 패키지만 설치하는 환경이다.

기본 인트프리터 + 프로젝트 종류별 패키지를 설치하여 각각의 패키지를 관리할 수 있는 기능이 있다.

다양한 패키지 관리 도구를 사용한다.

대표적인 도구로는 virtualenv와 conda가 있다.