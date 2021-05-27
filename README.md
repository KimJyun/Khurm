
# 🌷 quick start 🌷

  #### 1️⃣ git clone & pip install -r requirements.txt<br>
   ###### - clone을 해온 뒤 가상환경을 활성화 하고 requirements를 설치합니다.<br><br>

  #### 2️⃣ secret.json DB 설정
   ###### - secret.json에 mysqlDB user, password 정보를 채워줍니다.
     
  #### 3️⃣ S3 버킷 생성
   ###### - aws에서 S3버킷을 생성합니다. 다른 옵션은 모두 default 값으로 해도 되지만,
   ###### - 아래 이미지의 퍼블릭 액세스는 모두 체크 해제해주셔야 제대로 작동합니다.
![image](https://user-images.githubusercontent.com/39080868/119846239-ec6a4180-bf44-11eb-936e-7cbde2bc6d0b.png)

  #### 4️⃣ IAM 액세스 키 설정
   ###### - 다음처럼 IAM콘솔에서 사용자를 추가합니다. 특히 프로그래밍방식 액세스를 체크해주세요
![image](https://user-images.githubusercontent.com/39080868/119849468-9ea30880-bf47-11eb-897e-21d7125f9aaa.png)
 <br>
   ###### - 다음으로 기존정책 연결에서 AmazonS3FullAccess를 체크해줍니다.
![image](https://user-images.githubusercontent.com/39080868/119849790-e32ea400-bf47-11eb-8ddd-3242e464256f.png)

   ###### - 그럼 .csv로 된 credential 파일을 얻을 수 있습니다. 소중하게 보관해주세요!

  #### 5️⃣ secret.json S3 설정
   ###### - secret.json의 S3 필드를 채워줍니다.


## 💥 push전 해야 할 일 💥
#### 👉 pip freeze > requirements.txt
      부가적으로 install 한 게 있다면 해당 명령어로 꼭 requirements를 업데이트 해주세요
#### 👉 AWS 키를 업로드 하지 않도록 조심하세요 !
