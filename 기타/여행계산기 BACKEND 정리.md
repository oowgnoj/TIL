## 1. 스택

node.js

express

mysql

sequelize



## 2. 배포



**서버 🐋**



- **EC2 배포 순서**

  

  1. AWS 사이트에서 인스턴스 시작 후 인스턴스 생성 과정에서 다운받은 프라이빗 키(.pem)를 로컬 SSH 로 이동시킵니다.https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

     

  2. 터미널 창에서 ssh 명령을 사용하여 EC2 인스턴스에 접속합니다.

     **.ssh**
     // ssh 로 이동

     **ssh -i "travel-calculator-server.pem" ubuntu@3.15.20.155**
     // ssh -i "{프라이빗키파일명}" ubuntu@{IPv4 퍼블릭 IP}

     

  3. Upstream 레파지토리 (codestates/travelCalculator-server) 를 클론합니다.

     **git clone https://github.com/codestates/travelCalculator-server.git**

     

  4. npm install 을 실행하여 package 설치를 진행 후 node 를 실행하여 서버를 켭니다!!





- **EC2 수정 배포**

  

  1. ssh 명령어로 EC2 인스턴스 접속 후 Upstream 레파지토리를 pull 받습니다.

     **git pull https://github.com/codestates/travelCalculator-server.git dev0**

     *// git pull {깃주소} {브랜치명}*

     

     ** 주의사항! 배포 전 콘솔을 잘 정리하자! (api key 가 콘솔에 잔뜩 찍히지 않도록)





- **각종 이슈**

  

  1. cors

     1차 배포 후 클라이언트와의 테스트에서 cors 이슈가 있었습니다. cors 이슈를 해결하기 위해 npm cors 를 설치한 후 (https://www.npmjs.com/package/cors) 아래의 shortly sprint 에서 사용하였던 코드에 origin 부분을 수정하여 반영하였으나 문제가 해결되지 않았습니다.

  ```
    app.use(cors({
  
    origin:['[<http://localhost:3000>](<http://localhost:3000/>)'],
  
    methods:['GET','POST'],
  
    credentials: true
  
    }));
  ```

  ​	결국 모든 옵션을 지우고 **app.use(cors())** 를 app.use("/", routes) 보다 **앞에! 먼저! 작성**하여 cors 문제를 해결하였	습니다. (다른 팀의 이야기를 들어보니 origin 에 주소를 넣는 과정에서 '<http://localhost:3000>' 이 아닌 
  ​	'<http://localhost:3000/>' 으로 작성해서 문제가 있었다고도 합니다; 우리도 그랬던 것일지도 ...)

  

  결론은 app.use(cors());

  

  ... 인줄 알았으나 발표를 하루 앞두고 cors 문제가 또 터져버렸습니다!!!!! 해결된 내용을 다시 정리하자면,

  

  쿠키를 사용하려면 (즉 쿠키/세션을 이용하는 로그인, 로그아웃 등을 하려면) **cors credentials 옵션 값이 true**여야하고 credentials 옵션을 사용하면 모든 Access 를 허용해서는 안되기에 **origin 을 설정해주어야합니다!**

  

  (이전까지는 쿠키와 무관한 api 만 있었기에 origin 설정을 하지 않은 app.use(cors()) 에서도 잘 작동하였으나 로그인 로그아웃에서부터 쿠키를 쓰기 위해 credentials 설정을 해주어야만 했고, 때문에 뒤늦게 origin 설정 문제가 터진 것입니다..!)

  

  ```
  var whitelist = ['<http://localhost:3000>', '<http://travel-calculator-client.s3-website.ap-northeast-2.amazonaws.com>'];
  app.use(cors({ credentials: true, **origin: whitelist** }));
  
  app.use(function (req, res, next) {
    var allowedOrigins = ['<http://localhost:3000>', '<http://travel-calculator-client.s3-website.ap-northeast-2.amazonaws.com>', '<http://localhost:3000/>', '<http://travel-calculator-client.s3-website.ap-northeast-2.amazonaws.com/>'];
    var origin = req.headers.origin;
    if (allowedOrigins.indexOf(origin) > -1) {
      **res.setHeader('Access-Control-Allow-Origin', origin);**
    }
    //res.header('Access-Control-Allow-Origin', '<http://127.0.0.1:8020>');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.header('Access-Control-Allow-Credentials', true);
    return next();
  });
  ```

  

  위에가 지금 (11/9 오전) 클라이언트 배포 주소는 cors 를 잘 허용해주는 (localhost 는 안되는 것 같습니다) 현 상태의 서버측 코드인데 cors 미들웨어가 잘 적용이 되어서인지, res.setHeader 가 잘 적용되어서인지 현재로서는 파악이 어렵습니다. 심지어 S3 에서 CORS 설정을 추가로 해주었기 때문에 총 3가지 중 어떤 방법이 제대로 먹힌건지 모르겠습니다....!!! S3 의 CORS 설정은 AWS 홈페이지에서 진행합니다.

  

  ![](/Users/kyungjushim/Desktop/Screen Shot 2019-11-09 at 9.53.34 AM.png)

  

  https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/cors.html

  

  CORS 에 대한 공부가 좀 더 필요해보여요! 

  

  참고로 클라이언트측에 credentials 옵션을 반영하는 방법은 아래와 같습니다. (서버 cors 미들웨어에서는 true 클라이언트 fetch api 에서는 include!)

  

  ```
  fetch('<http://3.15.20.155:5000/mypage>', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        **credentials: 'include',**
      }).then(res => console.log(res));
  ```

  

  

  

  2. port

     서버에 재접속을 하려고하면 이미 우리가 쓰려던 5000 포트가 쓰이고있다고 경고가 뜨며 node index.js 실행이 안되는 경우가 몇 번 있었습니다. EOINLISTEN : 5000 인가? 이런식으로!

     그럴 땐 기존에 5000 에서 돌고있는 노드를 죽이고 다시 node index.js 를 해야합니다!
     https://88240.tistory.com/475

     현재 사용중인 포트 확인

     **lsof -i :5000**

     사용중인 포트 조회 결과 예시

     **lsof -i :8000**

     COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME

     node  1234 shaking 15u IPv4 0x1f23462a48d69d65 0t0 TCP localhost:cslistener (LISTEN)
     


     Kill 하기
    
     **kill -9 1234**(1234 대신 PID 번호를 쓰면 됩니다!)


​     

​     

**데이터베이스**🐦



- **RDS 연결하기**

  

  1. github에 올리기 전에 config 파일 변경하기 (ec2 - rds 연결)

     { "development": 

     ​		{"username": "admin",

     ​		"password": "travelflight",

     ​		"database": "travelcalculator",

     ​		"host": "[travel-calculator-db.cxcx72nawcwf.us-east-2.rds.amazonaws.com](http://travel-calculator-db.cxcx72nawcwf.us-east-2.rds.amazonaws.com/)",

     ​		"port": "13306",

     ​		"dialect": "mysql",

     ​		"operatorsAliases": false }

     

  2. ec2 서버를 켜면 싱크맞춰지면서 테이블 생성

     

  3. 데이터 백업하기

     

     1) mysqldump 이용해서 데이터 백업

     **mysqldump -u root -p travelcalculator > backup.sql(백업파일이름아무거나)**

     

     2) rds 에서 퍼블릭 액세스 허용 → 터미널에서 rds 진입

     ​			물론 평소에는 보안을 위해서는 '퍼블릭 엑세스 가능성' 을 '아니오' 로 수정하는 것이 더 좋은 것 같습니다! 퍼블			릭 엑세스 관련 메모 :

     ​			말 그대로 외부에서 우리의 데이터베이스에 접근할 수 없게 프라이빗 서브넷에 데이터베이스를 배포하는 것입니			다. 데이터베이스가 퍼블릭 액세스를 막더라도 동일한 VPC 내에 배포되어있는 서버(EC2) 는 접근이 가능하기 			때문에 현재 같은 VPC 에 배포되어있는 우리 EC2 와 RDS 의 연결에는 문제가 없을 것으로 예상됩니다!

     ​			VPC에 있는 DB 인스턴스를 인터넷에서 숨기기 :

     ​			https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Hiding

     ​			동일한 VPC에 있는 EC2 인스턴스가 VPC 내에 있는 DB 인스턴스에 액세스 :

     ​			https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1

     

     **mysql -u admin --port=13306 --host=travel-calculator-db.cxcx72nawcwf.us-east-2.rds.amazonaws.com -p**

     → 비밀번호 입력

     

     3) rds db 끄지말고 유지한 채로 바깥 터미널에서 아래 진행 (-P 포트번호 써야함!)

     ​	그 전에 truncate!!!!!!!!!!!!!!!!!!!!!!!

     **mysql -h travel-calculator-db.cxcx72nawcwf.us-east-2.rds.amazonaws.com -P 13306 -u admin -p travelcalculator < backup.sql(위에서 생성한 파일)**

     

  4. 데이터 변경하기

     테이블 truncate나 delete 이용해서 삭제 후,

     **INSERT INTO <테이블> (field1, field2) VALUES ('apple','banana')**

     

     **업데이트 왜 안되는지 아직 해결안됨.**

     만약 한 row 를 통째로, 모든 필드 다 채워서 입력한다면 **INSERT INTO <테이블> VALUES ('apple', 'banana')**로 입력 (fields 명시안해줘도 되는듯)

     

     ex) api key **교체할 때**

     INSERT INTO apikeys VALUES(4,'googlekey','바꿀 키');

     

- **데이터 넣을 때 유의사항**

  

  1. 데이터베이스 CHARACTER SET UFT8 로 맞춰주기

     1) db 생성 시 설정 : 

     CREATE DATABASE 데이타베이스_이름 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

     2) db 생성 후 변경 : 

     **ALTER DATABASE 데이타베이스_이름 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;**

     

  2. 한글때문에 워크벤치에서 import 안 될 경우, mysql에서 load data 이용해서 데이터 넣기

     mysql 들어가서!!!!

     **LOAD DATA LOCAL INFILE '/path/your_data.csv' INTO TABLE table_name CHARACTER SET utf8 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'**

     

  3. 워크벤치에 import, 또는 load data 할 때

     csv 파일 맨 윗 줄에 필드명 없고! 바로 데이터 있는 상태여야 함.


     ![](/Users/kyungjushim/Desktop/Screen Shot 2019-11-08 at 1.10.44 PM.png)


​     

  4. 데이터 넣을 때 끝에 **띄어쓰기**들어가 있는지 확인하기! ( \r )

     → 맞게 넣은 것 같은데 안 된다면 이 문제일 가능성이 높다. length 확인하자

  

## 3. API

**체크리스트 🌵**

- [ ] 무료인지
- [ ] 무료 한도는 몇 회인지
- [ ] (여러 API 를 동시에 써야한다면) 서비스 범위가 좁은 API 를 기준으로 공통 분모를 빠르게 확인할 것
- [ ] 대체 API 찾거나 API 응답이 없을 경우 클라이언트에 전달할 fake data 만들어두기





## 4. POSTMAN

Request body 가 포함된 POST 요청을 보내야 할 때 :

![](/Users/kyungjushim/Desktop/Screen Shot 2019-11-08 at 12.53.44 PM.png)

request 옵션을 'Params' 이 아닌 **'Body'**로 선택한 후 데이터 타입을 **'raw'**로 지정하여 body 가 될 object 를 작성합니다.
그리고 raw 인 상태에서 데이터 타입을 JSON 으로도 꼭 바꿉시다!





## 5. 그 외 툴

jsonblob : https://jsonblob.com/

miro : https://miro.com/

구글스프레드시트 : https://www.google.com/intl/ko_kr/sheets/about/





지금까지 해결이 안된것은

- promise all
- \r 어째서???
- google api ...

  