# 커맨드 패턴(Command Pattern)

## Problem

![요청과 작업 사이에 요청은 일련의 검사를 통과해야 한다.](./images/image-1.png)

- 요청과 작업 사이에 요청은 일련의 검사를 통과해야 한다.

![Alt text](./images/image.png)

- 기능이 추가되면 검사 과정을 거치는 클래스를 수정하거나 새로 만들어 규모가 커짐

## Solution

- 특정 행동들을 핸들러라는 독립 실행형 객체들로 변환함으로써 문제를 해결할 수 있다.

![Alt text](./images/image-2.png)

![Alt text](./images/image-3.png)

## Common Structure

![Alt text](./images/image-4.png)
