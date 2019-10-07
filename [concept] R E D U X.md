



### REDUX 가 필요한 이유

리덕스 스토어 를 통해 상태(state)값을 컴포넌트에 종속시키지 않고, 상태 관리를 컴포넌트의 바깥에서 관리 할 수 있게 된다.


#### 미리 개념 정리

###### 액션 (action) : 어떤 액션을 일으킬 것인가에 대한 정보가 담아있는 객체. Type 필드를 필수적으로 가지고 있어야 한다.

```javascript
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
```



###### 액션 생성함수(action creator) : 파라미터를 받아와서, action 객체로 만들어주는 함수

```javascript
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

```



###### 리듀서 : 변화를 일으키는 함수 . 두가지 파라미터를 받는다. 'reducer : 변형하는 것'

```javascript
function reducer(state, action) {
	return alteredState;
}
```

###### 스토어 : 현재의 앱 상태와, 리듀서, 추가적으로 몇가지 내장함수

###### 디스패치 : action을 발생 시키는 것. 스토어에 있는 추가적인 내장함수 중 하나. 

```javascript
dispatch(action)  //액션을 실행한다		
```



###### 구독(subscribe) : 특정함수를 전달해주면, action이 dispatch(실행) 될 때 마다 전달해준 함수가 호출됨. 함수 형태의 값을 파라미터로 받는다. 스토어의 추가적인 내장함수 중 하나.![Screenshot 2019-09-18 13.13.35](/Users/jongwoopark/Dropbox/Screenshots/Screenshot 2019-09-18 13.13.35.png



뷰 









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

   ```javascript
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
   
   ```

4. 액션 객체를 그때그때 만들기 귀찮아서 만드는 것 -> 액션 생성자 함수

5. index.js 에 액션생성자 함수 생성

   ```javascript
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
   
   ```

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
   2. getState()
   3. subscribe(listener)

8. 















