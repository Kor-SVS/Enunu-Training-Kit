# ENUNU Training Kit

> 해당 repo는 한국어 ENUNU를 위해 부분 수정 되었습니다.  
> lang_mode 옵션과 hed 및 table 파일을 변경하면 일본어 모델을 학습시킬 수 있습니다.

## 설치 방법

> Windows 환경을 기준으로 작성되었습니다.

### 파이썬 설치

[Python 3.8.\* Download](https://www.python.org/downloads/release/python-3810) 클릭하여 다운로드 및 설치합니다.

-   가상환경 (venv)을 사용하는 것을 추천합니다.

### Git 설치

> bash shell 명령을 Windows에서 실행하기 위해 필요합니다.

[Git Download](https://git-scm.com/downloads) 클릭하여 다운로드 및 설치합니다.

### Repo 소스코드 다운로드

```
git clone https://github.com/Kor-SVS/Enunu-Training-Kit.git
```

또는 [직접 다운로드](https://github.com/Kor-SVS/Enunu-Training-Kit/archive/refs/heads/main.zip)를 사용할 수 있습니다.

### CUDA 개발 킷 설치 및 PyTorch 설치

TODO...

### 필요 패키지 설치

> 한국어 가사에서 발음 방법에 알맞는 음소 생성 등의 작업을 위해 필요한 패키지들 입니다.

1. 형태소 분석기 설치

    1. [mecab-ko](https://github.com/Kor-SVS/Enunu-Training-Kit/releases/download/other/mecab.zip) 클릭하여 다운로드 합니다.

    2. 압축을 풀고 `C:\`경로에 옮겨줍니다.  
       (작업을 완료하면 `C:\mecab` 위치에서 mecab.exe를 찾을 수 있어야 합니다.)

    3. [mecab-python-msvc](https://github.com/Kor-SVS/Enunu-Training-Kit/releases/download/other/mecab_python-0.996_ko_0.9.2_msvc-cp38-cp38-win_amd64.whl) 클릭하여 다운로드 합니다.

    4. `python -m pip install (다운로드 경로)`를 입력하여 설치합니다.

2. enunu-kor-tool 설치

    1. `python -m pip install git+https://github.com/Kor-SVS/enunu-kor-tool.git`를 입력하여 설치합니다.

3. nnsvs 설치

    1. `python -m pip install nnsvs`를 입력하여 설치합니다.

4. 기타 필요 패키지 설치

    1. `python -m pip install pydub hydra-optuna-sweeper mlflow`를 입력하여 설치합니다.

### 실행 방법

run.bat 또는 run_resf0.bat(권장)으로 실행할 수 있습니다.

보코더 학습은 run_vocoder.bat으로 실행할 수 있습니다.

ex) `run_resf0.bat 0 6` (0 단계에서 ~ 6단계까지 실행)
