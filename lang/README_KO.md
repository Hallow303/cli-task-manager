## Python CLI 작업 관리자

🌐 **Languages**

[![English](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](README_PT.md)
[![Español](https://img.shields.io/badge/Español-red?style=for-the-badge)](README_ES.md)

Python으로 만든 간단한 명령줄 기반 작업 관리자입니다. 이 프로젝트는 사용자가 터미널에서 빠르고 실용적으로 일상적인 작업을 관리할 수 있도록 합니다.

### 기능

* 새로운 작업 추가
* 모든 작업 목록 보기
* 작업 완료로 표시
* 작업 삭제
* JSON 파일을 사용한 데이터 영구 저장
* 간단하고 직관적인 명령줄 인터페이스

### 작동 방식

작업은 로컬 `tasks.json` 파일에 저장됩니다. 각 작업에는 다음 정보가 포함됩니다:

* **ID** – 고유 식별자
* **작업 설명**
* **상태** – "진행 중" 또는 "완료"

프로그램이 시작될 때 JSON 파일을 불러오며, 작업이 생성되거나 완료되거나 삭제될 때마다 파일이 업데이트됩니다.

### 사용된 기술

* **Python 3**
* **JSON** 데이터 저장
* **OS 모듈** 터미널 유틸리티

### 사용 방법

1. 저장소 클론:

```
git clone https://github.com/Hallow303/cli-task-manager.git
```

2. 프로젝트 폴더로 이동:

```
cd cli-task-manager
```

3. 프로그램 실행:

```
python main.py
```

4. 터미널 메뉴를 사용하여 작업 관리:

* 작업 추가
* 작업 보기
* 작업 완료로 표시
* 작업 삭제

### 목적

이 프로젝트는 다음을 연습하기 위한 학습 프로젝트로 만들어졌습니다:

* Python에서 파일 처리
* JSON 데이터 다루기
* 간단한 CLI 애플리케이션 만들기
* 함수로 코드 구조화
