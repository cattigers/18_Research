

# Video to TFRecord

### 1. video -> frames
* using OpenCV
### 2. frames + labels -> tfrecord
* using plain TF
### 3. tfrecord -> ndarray
* using plain TF, numpy


# 사용법

## 설치

이 git 저장소를 받는다 아래의 방법 중 하나를 선택하여 모든 파일을 받도록 한다.
* Github Desktop 등의 프로그램을 사용하여 이 저장소를 clone 한다
* 명령 프롬프트 혹은 터미널을 이용하여 이 저장소를 clone 한다. 명령어는
` git clone https://github.com/yhunroh/18_Research.git `
이다.
* 그대로 저장소 페이지 우측 상단의 다운로드 버튼을 통해 zip파일로 다운로드 후 압축해제한다.

저장소를 받아온 후, 웹 페이지에서 보이는 파일들이 전부 있는지 확인한다.

이 저장소에서 사용하는 pip 패키지를 전부 설치하기 위해서 `pip3 install -r requirments.txt`를 명령 프롬프트 혹은 터미널에서 실행한다.

## 데이터를 놓는 위치

변환하고자 하는 비디오 파일을 프로젝트의 가장 상위 위치에서 video 폴더를 만든 후, 그 안에 넣는다.  
이 때, `/video/model1/(비디오 파일 이름)` 처럼 되게 놓도록 한다. (즉, video폴더 안에 model1, model2, ... 의 폴더를 넣는다)  
~~후에 그냥 대충 넣어도 트리를 그대로 옮길 수 있도록 할 예정~~

## 실행 방법

프로젝트 최상위 위치에서 `python3 main.py`로 main.py를 실행시킨다.
실행시키고 나면 메시지가 뜨니, 정상 작동하고 있는지 확인할 수 있다.  
~~가능하다면 이후에 tqdm등을 사용하여 진행도를 표현할 수 있도록~~

## 결과물

**현재 1단계만 완성됨.**

비디오에서 추출한 프레임은 `/result/frame/` 아래에 생성된다. 비디오별로 폴더가 다르게 구분되어 있으며, 이미 그 위치에 파일이 있어도 인식하지 않고 덮어쓴다. 비디오를 처리하는 순서는 이름순서대로일 것이다.


`/hdf5/`위치에 h5파일들을 놓고 나서 `python3 hdf5_to_tfrecords.py`를 실행하면 된다.
