



### REDUX 가 필요한 이유

리덕스 스토어 를 통해 상태(state)값을 컴포넌트에 종속시키지 않고, 상태 관리를 컴포넌트의 바깥에서 관리 할 수 있게 된다.

#### ![Screenshot 2019-10-25 10.46.55](/Users/jongwoopark/Dropbox/Screenshots/Screenshot 2019-10-25 10.46.55.png)

The whole state of your app is stored in an object tree inside a single *store*.

### 리덕스가 왜 필요할까요.

1. 개발자 입장에서 편한 state 관리

2. facebook message 사건

   

MVC 패턴과 FLUX의 차이

MVC

V -> C -> M <-> db

![1200px-MVC-Process.svg](/Users/jongwoopark/Desktop/1200px-MVC-Process.svg.png)

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

   1. Action : 작업에 대한 정보를 가지고있는 객체

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

   

6. store 하는일

   1. dispatch(action) 액션을 reducer에 보냄.
      1. reducer에게 현재 **자신의 상태와, 전달받은 액션**
      2. (리듀서가 변화해서 새로운 상태 준다.)
      3. 현 상태에 **바꿔치기**
   2. getState()
      1. 현재 상태를 반환하는 함수
   3. subscribe(listener)
      1. 상태가 바뀔 때 마다 **실행할 함수** 등록
      2. listener -> 콜백 함수
   4. replaceReducer(생 략)

   










REDUX OFFICIAL GUIDE

1. 액션 type 정의

   ````javascript
   export const INCREMENT = "INCREMENT";
   export const DECREMENT = "DECREMENT";
   
   ````

2. 액션 생성자 만들기 

   1. 액션을 받아와서 return {Type:action 종류} 
   2. 매번 만들어주기 귀찬
   3. 아마도 리듀서가 action 객체를 받아서 그럼

   ````javascript
   import * as types from "actiontypes.js";
   
   export function increment() {
     return {
       type: types.INCREMENT
     };
   }
   
   export function decrement() {
     return {
       type: types.DECREMENT
     };
   }
   
   ````

   

3. 리듀서 만들기

   1. 실질적으로 (state(previous), action) 을 받아서

   2. 함수 적용 후

   3. 새로운 state를 반환해주는 중요한 녀석

      ````javascript
      import * as types from "../action/actiontypes";
      
      const initialState = {
        count: -1
      };
      
      export const countReducer = (previousState = initialState, action) => {
        switch (action) {
          case types.INCREMENT:
            return {
              ...previousState,
              count: previousState.count + 1
            };
      
          case types.DECREMENT:
            return {
              ...previousState,
              count: previousState.count + -1
            };
      
          default:
            return previousState;
        }
      };
      
      ````

   4. 각자 리듀서를 만들고

   5. main reducer에서 combinedReduce

4. 스토어 만들기

   1. index.js 에서 createStore(**reducer**)
   2. console.log(store) 해보기
      1. dispatch(), getState()등 등

5. State 를 각 component 와 연결하기 (view-layer binding)

   1. React-redux

      1. Provider : 컴포넌트에서 리덕스 사용하도록 도와줌. 하나의 컴포넌트임

         index file에서 App Component 를 provider로 감싸줌

         Props 로 store = {store}

         1. ````javascript
            <Provider store = {store}>
              <App/>
            </Provider>
            ````

      2. Connect([..options]) => 컴포넌트를 REDUX에 연결하는 또 다른 **함수** 반환

         `connect()(Counter)`: 카운터가 리덕스에 연결됨. 함수의 반환값으로 새로운 컴포넌트 클래스 반환 => 리덕스에 연결되어있음

         this.props.Store로 접근 가능

         

         근데 options? 넣으면 깔끔해짐

         connect([option])

         [mapStateToProps]

         [mapDispatchToProps]

         [options] =>{[pure:true], [withRef = false]} 

         

      3. 컴포넌트 연결

         1. import {connect} from 'react-redux'

         2. ````javascript
            const mapStateToProps =(state) =>{
              return {
                number : state.counter.number,
            }
            
            //action dispatch 해주는 함수를 props 로 전달
            //action creator 불러와야함
            const mapDispatchToProps = (dispatch) =>{
              return {
                handleIncrement : ()=>{dispatch(actions.increment())},
                handleDecrement : ()=>{dispatch(actions.Decrement())}
              }
            }
            
            //참조사항
            const mapDispatchToProps = (dispatch) =>{
              return bindActionCreator(actions, dispatch)
            }
            
            export default connect()(Counter) //connect() 로 반환된 함수에 (Counter) 컴포넌트 인자로 넣어주는 과정
              
            export default connect(mapStateToProps, mapDispatchToProps)(Counter) //connect() 로 반환된 함수에 (Counter) 컴포넌트 인자로 넣어주는 과정
              
              
            ````




REDUX 를 사용해 Todo만들고 느낀 점.

- state 변경 할 때, Immutable data를 다루는 점이 어렵게 느껴졌음. 아직 rest parameter 에 대한 이해와

  map, reduce 를 더 공부해봐야 할 것 같다.

- action, action 생성함수, 리듀서에 대한 역할은 어느정도 개념이 정리가 된 것 같다.

  클라이언트에서 발생하는 순서대로 설명 해 보자면

  container 를 만들 때 mapPropsToDispatch 를 함으로서 addTodo button 이 생기는 것이다. 그러니까 가장 먼저 일어나는 것은

  1. Dispatch (디스패치) : action을 발생 시키는 것. 스토어에 있는 추가적인 내장함수 중 하나. 

  action이 발생하게 되면, (state, action)을 인자로 받는 녀석이 생각 날 것이다.

  2. REDUCER (리듀서) : action과 이전 상태를 받아서 **기존데이터를 수정하지 않고** **수정된 새로운 데이터를 store엗게 전달해준다** .

  3. 그러면 store는 리듀서에게 전달받은 state값을 바꿔준다.

     

     -  코드 짜는 것 말고, 개념적으로는 이렇게 이해를 했다.

     - 그럼 내가 처음에 쓴 state변경건은 그냥 기존 reference type adress를 조심해서 모든 state 의 nested array 를 신경 써 가면서, 하면 된다.

       

  









