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





### REDUX 가 필요한 이유



리덕스 스토어 를 통해 상태(state)값을 컴포넌트에 종속시키지 않고, 상태 관리를 컴포넌트의 바깥에서 관리 할 수 있게 된다.



### 개념 미리 정리

액션 (action) : 어떤 액션을 일으킬 것인가에 대한 정보가 담아있는 객체. Type 필드를 필수적으로 가지고 있어야 한다.

````javascript
{
	type : "TOGGLE_VALUE"
}

{
	type : "ADD_TODO",
	data : {
        id:0 ,
        text: 'learn redux'
     		 }
}
````



액션 생성함수(action creator) : 파라미터를 받아와서, action 객체로 만들어주는 함수

````javascript
function addTodo(data) {
  return {
    type: "ADD_TODO",
    data
  };
}

// 화살표 함수로도 만들 수 있습니다.
const changeInput = text => ({ 
  type: "CHANGE_INPUT",
  text
});

````

리듀서 : 변화를 일으키는 함수 . 두가지 파라미터를 받는다. 'reducer : 변형하는 것'

````javascript
function reducer(state, action) {
	return alteredState;
}
````

스토어 : 현재의 앱 상태와, 리듀서, 추가적으로 몇가지 내장함수

디스패치 : action을 발생 시키는 것. 스토어에 있는 추가적인 내장함수 중 하나. 

````javascript
dispatch(action)  //액션을 실행한다		
````

구독(subscribe) : 특정함수를 전달해주면, action이 dispatch(실행) 될 때 마다 전달해준 함수가 호출됨. 
함수 형태의 값을 파라미터로 받는다. 스토어의 추가적인 내장함수 중 하나.



1. module 만들기 (module = 필요한 액션, 액션생성함수, 초깃값, 리듀서함수가 들어있는 파일)

2. 액션 타입 정의하기 

   : 모듈에 카운터쪽에서 사용할 액션들을 작성해준다

3. 액션 생성함수(파라미터를 받아와서, action 객체로 만들어주는 함수) 정의
4. 초기상태(initial)와 리듀서 정의
5. 리듀서 합쳐주기



Provider : 프로젝트 & 스토어

connect : component & store





redux tutorial velopert

1. component 기본세팅

2. Action : 작업에 대한 정보를 가지고있는 객체

   이 경우에는

   1. 값을 1씩 증가 INCREMENT
   2. 값을 1씩 감소 DECREMENT
   3. 새로운 색상 SER_COLOR

3. Actiontypes 만듬

   ````javascript
   export const INCREMENT = "INCREMENT";
   export const DECREMENT = "DECREMENT";
   export const SET_COLOR = "SET_COLOR";
   
   //action의 이름을 만들어줌. action 객체는 이렇게 생김
   ㅡ 
   {type : "INCREMENT"}
   {type : "DECREMENT"}
   {
     type : "SET_COLOR",
     COLOR : [200,200,200]
   }
   
   ````

4. 액션 객체를 그때그때 만들기 귀찮아서 만드는 것 -> 액션 생성자 함수

5. index.js 에 액션생성자 함수 생성

   ````javascript
   import * as types from './ActionTypes'
   
   //액션생성자 함수를 만들고. 기존에 만들었던 types파일에서 types.INCREMENT를 사용해서 불러옴
   export function increment (){
       return {
           type : types.INCREMENT
       }
   }
   export function decrement (){
       return {
           type : types.DECREMENT
       }
   }
   export function setColor (){
       return {
           type : types.SET_COLOR,
           color : color
       }
   }
   
   ````

6. 리듀서 recucer 변화를 일으키는 함수.

   ##### 이전상태와 액션을 받아 다음 상태를 반환한다 : (previousState, action) => newState

   이전상태를 변경하는게 아니라 새로운 상태를 반환한다.

   기존상태를 복사하고, 변화를 준 다음에 반환

   1. 비동기작업 X

   2. 전달받은 인수변경 X

   3. 동일 인수 = 동일 결과

   

   counter, ui 두개의 리듀서 파일 만들고 

    reducers/counter.js , ui.js

   컴바인 comebineReducer

   

7. store

   1. dispatch(action)
   2. 

   

   

   

   

   

   

   