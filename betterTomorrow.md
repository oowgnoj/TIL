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





### React

리액트는 컴포넌트로 이루어져 있고, 

컴포넌트는 상위 컴포넌트로부터, props를 받는다.

해당 컴포넌트는 props를 input으로 하고, element 를 아웃풋 하며

화면을 구성한다.

그러므로 component 는 a -> componenting -> [a]의 함수이고,

[] ->. 이것만 보면 template 이다.



이 component 는 생성 => 업데이트 => 제거의 단계를 차례로 겪는 생명주기(life cycle )을 가지고 있다.

#### Mounting(생성) 

#####component 가 새롭게 생성되는 시점이다. component 함수가 실행되고, 결과물로 나온 element들이 가상 DOM에 삽입되고 실제 DOM을 업데이트하기까지의 과정이다.

componentDidmount() : componenet의 결과물이 DOM에 마운트 된 직후에 실행되는 methods



###Debounce / throttle 이 필요한 이유

지금 현재 앱에서 검색을 하게 되면

박종우를 검색했을 때 ㅂ -> 바 ->박 이렇게 다 검색이 되는데 위에걸 사용하게 되면 괜찮다.

debounce : 연속된 이벤트가 있을 때 마지막 이벤트만 실행하는 것

##### debounce : 연속된 이벤트가 있을 때 마지막 이벤트만 실행하는 것

##### throttle : enforces a maximum number of times a function can be called overtime. 





#### 리액트 주요개념

##### 리액트 큰 틀

1. 왜 (리액트)를 사용하는가 ? =
    왜 프론트엔드 라이브러리를 사용하는 가..
   DOM에 신경쓰지않고 로직에만 집중할 수 있게
   1. 컴포넌트로 관리해서 재사용성과 유지보수
   2. 수정
   3. 가독성
   4. dom 편리한 접근
2. props, states
3. class component / functional component 
4. lifecycle
5. 최적화 -> virtual dom -> JS (너무 힘들어)->JSX(자바스크립트를 일반 태그처럼 사용할 수 있게끔)

#### props / states

props: 상위 -> 하위 속성값

state : component 가 가지는 상태



Class component : 데이터 유동

functional component : 데이터 고정



setState -> render -> comDiDUpdate

