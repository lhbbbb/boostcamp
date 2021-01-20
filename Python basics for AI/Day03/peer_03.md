# 피어세션 정리

### 2021.01.20

## 내용 정리

어제 올라온 과제들을 바탕으로 피어 세션을 진행하였다.

#### basic math

numpy 모듈을 설치해서 평균을 구했더니 에러 발생 이슈.

=> numpy 외부 모듈을 사용했거나 자료형이 numpy 형태여서 에러가 난 것으로 추정됨.

#### textmining1 && textmining2

정규표현식을 사용하거나 파이썬의 str객체 내장함수를 사용하여 해결.

- [정규표현식 사용법](https://wikidocs.net/4308) 참고

textmining2 같은 경우는 문제의 특성상 코드를 깔끔하게 작성하기 힘들다고 논의됨.

#### baseball

입력문자열들의 순서에 신경쓰면서 코드를 작성할 것.

다음의 코드를 통해 굳이 github에서 검사 결과를 기다리지 않고 local에서 테스트해볼 수 있다.

```python
import unittest


def func():
    ...
    
unittest.main() # github에서 검사하는 것과 같이 test를 해볼 수 있다.
```

## 특이사항

- 박민영님, 서동현님 개인사정으로 불참
- 추천 vscode extensions: git graph, gitlens