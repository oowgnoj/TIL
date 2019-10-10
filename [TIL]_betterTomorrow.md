# 10/3 개천절 

오늘은 개천절인데도 나와서 열심히 공부했다 무엇보다 오늘은 어제에 이어서 REACT로 youtube clone 앱 만들기를 진행했다. 진행하며 내가 배운 것은 

- react 사용시 props를 내려주는 방법

- 맨 아래 props 에서 onClick(function) 사용 시 기존에 알고있던 함수의 범위를 벗어나는 방식때문에 힘들었다. 

  `onClick = {() =>props.fromApi(document.querySelector('.form-control').value)`

  이렇게 해결하니 간단한 문제였다.

- async 비동기에 대한 간접적인 경험

- 그리고 fetch 함수를 사용하며, helper function에 대한 이해가 부족했다. callback도 그렇고. 지금도 callback 은 잘 모르겠지만 이번 주말에 간단한 예제로 callback을 진행해보려고 한다.

```javascript
export const searchYouTube = {

fetch : (query, callback) => 
  fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&type=video&maxResults=5&key=AIzaSyCUSH2M2vxrFsjA1Q-b6joc0PEGj-VKirI`)
  .then(res => res.json())
  .then(res => res.items)
  .then((res) => {return res}),

  init : () =>
  alert("hello")
}
```





#10/4 TIL

####예정사항

1. ~~componentDidMount~~
2. Callback 함수
3. React 블로깅 준비
4. ~~gitignore~~

5. ~~Prettier~~

6. advanced chagllege

   1. 로그인/로그아웃 기능
   2. 리액트 라우터를 이용한 페이지 이동
   3. 비디오 저장하기 기능 ( 저장된 비디오 리스트를 확인/ 재생할 수 있어야합니다. )
   4. 조회수, 좋아요수를 fetch해와서 보여주세요.

7. ...?

8. export default

   

   

   

   ToyProblem

배열 largest product of three but should consider negative value.

##### 1차시도

(1) 절대값 정렬

(2) array[0] * array[1] *array[2] => Math.abs() => positive : return, negative : recursion..

​	(2-1) negative : array[0 -2 ]에서 negative value 기록한다음에 빼고, 

````javascript

/* Write a function that finds the largest possible product of any three numbers
 * from an array.
 * 
 * Example:
 * largestProductOfThree([2, 1, 3, 7]) === 42
 *
 * Extra credit: Make your function handle negative numbers.
 */


````

##### 2차시도



### recastly.ly

이슈사항 : 
기존 : onclick -> searchYoutube 함수 -> setStates

변경 : input박스의 단어가 바뀔 때 마다 => searchYoutube 실행 => setState

*해결방법

1. 깃 이그노어
2. 일단 푸쉬

3. onchange evnet 실행, 일단 해결



[Advanced challenge]

Our advanced content is intended to throw you in over your head, requiring you to solve problems with very little support or oversight, much like you would as a mid or senior level engineer. The following problem is no exception, and you may have to do a fair amount of work to get enough context to get started on the problem itself.

- Create a `VideoDetails` component that makes another request to the YouTube API and renders more complete video information to the page

  ````
  another request?
  renders more complete video information to the page
  
  API한번 더 보내서, page에 비디오 더 가져오는 것
  ````

  

- Create an auto-play toggle button that will automatically start playing the video selected from 

````
api 마지막에 autoplay = 1 줘야할 듯.
fetch 에 변수를 추가해서..
````



- Give each video it's own unique url with the help of [React Router](https://github.com/reactjs/react-router)





- Refactor your application to use flux. [Redux](https://redux.js.org/) is a popular implementation of flux you might consider



# 10/6

### [설계의 중요성]에 대해 느낀 하루

리액트로 TodoList를 만들었다. 엔지니어 분이 꼭 설계를 하고, 만들라고 말씀 해 주셨고 나도 나름대로 설계를 진행 한 후에 구현을 시작했다. 근데 나는 설계를 위한 설계를 했다. 애플리케이션의 최종 레이아웃 구성을 하고, component, props, state, function을 하기는 했는데 계획도 여러번 수정되고.

'이럴 바에는 시간 낭비 하지말고 일단 만들어 보자. ' 라는 마음에서 만들었다.

지금 나의 TodoList는

- App
  - Todolist
    - TodolistEntry
  - inputbox
    

이렇게 구성이 되어있고, App에서 TodoList에 대한 state관리를 하고 있다. 근데 여기서 문제는 다른 TodoList를 추가 할 수가 없다. 왜냐하면 최상단 component 인 App에서 모든 Todolist의 state 관리하고 있고, 할 수 야 있겠지만 naming부터 다시 손을 봐야한다.

만일 이게 front만 구현하는 프로젝트가 아니라, 서버, db, API까지 이어진 프로젝트였다면, 근데 내가 한참 진행 한 후에 알아차렸다면, 더 큰 교훈이 되었겠지만 그런 경험을 하고싶진 않다...:(

내일 수정할 todolist에서는 

1. 아침 / 점심 / 저녁에 따라 렌더링을 달리했던 entry를 group component 를 추가해 관리
2. TodoList 컴포넌트 상단에 users로 나누던지, theme으로 나눠서 여러 todolist를 쉽게 관리할 수 있도록 해야겠다.

- App
  - Users / Theme
    - TodoList
      - group
        - Todo entry



# 10/7

1. ~~프로그래밍 설계 관련 블로깅 계획~~~
2. ~~React Todolist 완성 ~~



#### 오늘의 느낀점 : 설계. 설계. 또 설계

처음 리액트로 Todolist를 만들어 봤다. 시작하자마자 기존에 했던 설계와는 다른 방향으로 흘러갔다. 그럼에도 재차 설계를 하지않고, 그때 그때 기능을 추가하고, 구조를 바꾸는 방향으로 진행했다.

이번에 앱을 만들기 전에 철저하게 설계를 하고 만들었으면 어땠을까 하는 궁금증이 든다.
사실 이번에는 설계의 중요성을 느낄만한 경험은 아니였다. 하지만  state의 구조나, 변수, 최상위 component에 부모 컴포넌트를 추가할 때 '이러면 안되겠다 하는 생각이 들었다'. 간단하게 생각해보면 이번 todolist를 서버와 db까지 연결하고 배포까지 한다면, 내가 코딩을 하며 짰던 자료구조는 db schema 구조에 전혀 적합하지 않을 수도 있고 정말 뒤엎어야하는 상황이 올 수도 있다. 

이번 기회로 설계에 대한 나만의 matrix를 구축해보자 자료조사와 블로깅을 시작하려고 한다. 애초에 무엇을 할 때 부딫혀보고 수정을 통해서 (agile..?) 하는 방식으로 배워왔기 때문에 나만의 matrix가 필요하다.



#### 5분 개념

1. React virtual DOM  : 실제 DOM 에서 랜더링 하기 전에, 변경된 부분을 javascript tree객체처럼 먼저 비교한 후에 바뀐부분만 rendering 에 적용

   virtual dom 최적화 ? 부모 컴포넌트가 리렌더링 되면, 자식 컴포넌트들 또한 리 렌더링 됩니다.

   

2. destructuring

   mdn definition : unpack values from arrays, properties from object into distinct variables

````
//Object destructuring
var o = {p:42, q: true}
var {p, q} = 0
console.log(p) //45
console.log(q) //true
````



<img src="/Users/jongwoopark/Dropbox/Screenshots/Screenshot 2019-10-07 15.12.51.png" alt="Screenshot 2019-10-07 15.12.51" style="zoom:50%;" />





# 10/8

1. 앤트디자인?
2. react 달력?





### event loop

https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=youtu.be



Single thread 



blocking : things that are slow

$1 --- $2 ... slow

the solution : asynchronous callbacks

event

https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=youtu.be





## 복습: 클라이언트 요청 GET / POST

#### GET 요청

1.  주소값을 이용해 요청을 하는 방식

2. 서버측 주소 끝에 ? 붙이고, `key1=value1&key2=value2`...

   Query String : 실제 주소값 뒤에 붙여가는 값

#### POST 요청

##### POST는 주소만 요청하고 변수와 값을 주소가 아닌 BODY에 담아 서버측에 요청

Header : 요청에 대한 설정정보가 담김

Body : 실제 데이터가 담김







## 서버 : 제공을 하는 주체

http protocol을 통해 통신해서 API를 제공하는 주체

routing(라우팅)? 조건에 따라 분기를 하는 역할.

저장

1. javascript object에 저장 할 수 있다.

2. POST(fs.wrtieFIle 모듈 활용) , GET(fs.readFile)

   (1). object / array -> filesyste,



API 문서 작성하기

API를 만들고 문서화까지 하는 것이 API 제작이다. 

1. API 사용법(method, router, etc)
2. 기대되는 return data 형식 및 예제



#### node js 에서 event 사용

Node js 는 이벤트 기반 비동기 방식의 서버 프레임워크

- EventEmitter : 모든 이벤트처리가 정의된 기본 객체. 

- on() : 이벤트를 연결하는 함수

  ```javascript
    // 2. request객체에 on( ) 함수로 'data' 이벤트를 연결
    request.on('data', function (data) {
      // 3. data 이벤트가 발생할 때마다 callback을 통해 postdata 변수에 값을 저장
      postdata = postdata + data;
    });
  ```

   'data'라는 이벤트를 캐치해서 사용했었는데 모든 이벤트처리는 이런 동일한 루틴



# 10/09

1. functional programming 관련 영상

2. javascript runtime 관련 영상 

   JS conf youtube

3. Chatter-box -server 진행사항 혹은 보충사항

   