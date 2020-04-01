

typscript and redux boilerplate

https://velog.io/@velopert/use-typescript-and-redux-like-a-pro


````

$ npx create-react-app ts-react-redux-tutorial --typescript
$ cd ts-react-redux-tutorial
$ yarn add redux react-redux @types/react-redux
```



https://huns.me/development/1953

## 리듀서

제일 먼저 리듀서(reducer)가 눈에 들어왔다. 이름부터 난해하다. 리듀서라니. 리덕스를 이해하려면 리듀서를 이해해야 할 것 같다. 그래서 설계의 시작도 리듀서다.

**'단일 스토어, 다수의 리듀서**’ 정책이다.

커지는 코드 베이스에 맞춰 스토어 역시 쉽게 비대해진다. 이런 상황이 오면 하나였던 스토어를 다수의 스토어로 분리한다.









https://www.freecodecamp.org/news/the-best-way-to-architect-your-redux-app-ad9bd16c8e2d/



## 4 stages to build a redux application

1. ### visualise the state tree

   : state tree 를 visualize 한다

   ![Screen Shot 2019-11-12 at 10.46.15 PM](/Users/jongwoopark/Desktop/Screen Shot 2019-11-12 at 10.46.15 PM.png)

2. ### design your reducers

   ##### reducer(기존상태, action) 을 받아 새로운 상태값을 return 해주는 reducer 설계

   ##### 리듀서도 많아지니까 트리구조로 작성

   ````javascript
   const rootReducer = combineReducer ({
     header : headerReducer
   })
   
   
   const headerReducer = combineReducer({
       menu: menuReducer,  
       search: searchReducer,  
       location: locationReducer
   });
   ````

   

   #### 

   #### 위의 searchReducer를 예로 들어서 action 별로 어떤 함수를 수행할지 만들어보자

   

   1. action type에 따라 switch 로 분기 처리를 해준다.

      

   ````javascript
   
   const initialState = {  payload: [],  isLoading: false,  error: {}};
   
   export function searchReducer( state=initialState, action ) { 	 
       switch(action.type) {    
           case FETCH_SEARCH_DATA:      
               return {        
                   	...state,        
                       isLoading: true    
               };        
   
           case FETCH_SEARCH_SUCCESS:      
               return {        
   	                ...state,        
                       payload: action.payload,        
                       isLoading: false      
                      };        
   
           case FETCH_SEARCH_FAILURE:      
               return {        
   	                ...state,        
                       error: action.error,        
                       isLoading: false            
               };
   
           case RESET_SEARCH_DATA:      
               return { ...state, ...initialState }        
   		default:      return state;
       }
   }
   ````

   
   

### 3. implement actions 액션 시행

:모든 action that has API calls usually goes through three stages in an app

1. search 실행하고

2. success or

3. failure

   

````javascript
export function fetchSearchData(args) {  
	return async (dispatch) => {    
        // Initiate loading state    
        dispatch({      
            type: FETCH_SEARCH_DATA    
        });
        try {      
            // Call the API      
            const result = await fetchSearchData(
                args.pageCount, 
                args.itemsPerPage
            );           
            // Update payload in reducer on success     
            dispatch({        
                type: FETCH_SEARCH_SUCCESS,        
                payload: result,        
                currentPage: args.pageCount      
            });    
        } catch (err) {     
            // Update error in reducer on failure           
            dispatch({        
                type: FETCH_SEARCH_FAILURE,        
                error: err      
            });    
        }  
    };
}

````



### 4. implement presentation



````javascript
import React, { Component } from 'react';
import { connect } from 'react-redux';;

import fetchSearchData from './action/fetchSearchData';
import SearchData from './SearchData';

const Search = (props) => (  
    <SearchData     
    	search={props.search}    
		fetchSearchData={props.fetchSearchData}   
	/>
);

const mapStateToProps = (state) => ({  
    search: state.header.search.payload
});

const mapDispatchToProps = {  fetchSearchData};

export default connect(mapStateToProps, mapDispatchToProps)(Search)
````







https://medium.com/@stanleyfok/designing-a-scalable-redux-architecture-f75fc4077b8



# how to design redux application 

### with real e-commerce example



file directory

````
└ redux
  ├─ actions
  │  ├─ categoryActions.js
  │  ├─ productActions.js
  │  ├─ profileActions.js
  │  ├─ sessionActions.js
  │  ├─ watchlistActions.js
  │  ├─ uiActions.js
  ├─ reducers
  │  ├─ data
  │  │  ├─ categoryReducer.js
  │  │  ├─ productReducer.js
  │  │  ├─ profileReducer.js
  │  │  ├─ watchlistReducer.js
  │  │  ├─ sessionReducer.js
  │  ├─ ui
  │  │  ├─ homeContainerReducer
  │  │  ├─ searchContainerReducer.js
  │  │  ├─ productContainerReducer.js
  │  │  ├─ loginContainerReducer.js
  │  ├─ index.js
  ├─ store
  │  ├─ configureStore.js
  ├─ constants.js
  
````





### 

## 1. Map actions to your API resources : Action

ACTION 과 API resource의 동사를 일치시키자.



### Write

````
POST /api/write
GET /api/review/{reviewID} //2번에서 3개의 actions 를 처리해 줘야함
````



## 2. Entity actions should handle begin, success and failure



**any API calls, it must have these 3 states : begin, success, failure**

````
GET_PRODUCT_BEGIN 
GET_PRODUCT_SUCCESS
GET_PRODUCT_FAILURE
````



````javascript

import APIClient from '~lib/apiClient';
import { actionTypes } from '../constants';

const apiClient = new APIClient();

export const getProduct = productId => async (dispatch) => {
  dispatch({
    type: actionTypes.GET_PRODUCT_BEGIN,
  });

  try {
    const product = await apiClient.getProduct(productId);

    dispatch({
      type: actionTypes.GET_PRODUCT_SUCCESS,
      payload: {
        product,
      },
    });
  } catch (error) {
    dispatch({
      type: actionTypes.GET_PRODUCT_FAILURE,
      payload: {
        error,
      },
    });
  }
};

export const getProducts = (keyword, categoryId, page, size) => async (dispatch) => {
  // similar to getProduct illustrated above
};


````

### 



## 3. Separate your Reducers by entities and container component 



**entities 와 container components 로 나누자 **






REDUX 공식

https://lunit.gitbook.io/redux-in-korean/



당신의 앱이 커지면 스토어를 추가하는 대신 루트 리듀서를 쪼개서 상태 트리의 각기 다른 부분을 독립적으로 다루는 리듀서들을 만들면 됩니다. 마치 React 앱에는 하나의 루트 컴포넌트가 있고 이 루트 컴포넌트가 여러개의 작은 컴포넌트로 이루어진 것처럼요.

액션에 의해 상태 트리가 어떻게 변화하는 지를 지정하기 위해 프로그래머는 순수 리듀서를 작성해야합니다.
리듀서는 그저 이전 상태와 액션을 받아 다음 상태를 반환하는 순수 함수입니다. 이전 상태를 변경하는 대신 새로운 상태 객체를 생성해서 반환해야한다는 사실을 기억해야 합니다. 처음에는 하나의 리듀서만으로 충분하지만, 애플리케이션이 성장해나가면 상태 트리의 특정한 부분들을 조작하는 더 작은 리듀서들로 나누는 것도 가능합니다. 리듀서는 그저 함수이기 때문에 호출되는 순서를 정하거나 추가적인 데이터를 넘길 수도 있습니다. **심지어 페이지네이션과 같이 일반적인 재사용 가능한 리듀서를 작성하는 것도 가능합니다.**


REDUX 앱의 데이터 생명주기

1. store.dispatch(action) 호출합니다.
  이때 action은 앱 내의 어디서나 호출할 수 있다 - 이 말은  앱의 어떠한 장소에서도 액션을 실행할 수 있고, state를 변경할 수 있다.
  
2. redux store가 내가 지정한 리듀서 함수를 호출한다
  switch (action type ===A){
    console.log(A)} 이러한 것 들
    
3. root reducer가 각 리듀서의 출력을 합쳐서 하나의 상태트리를 만든다.

  1. 이게  가능한 이유는 reducer는 기본적으로 복사하기 때문에 
하나만 바뀌더라도 새로운 상태를 그냥 통채로 갈아낀다
```javascript
const initialTodoState = { arr: [] };

export const Todo = (state = initialTodoState, action) => {
  switch (action.type) {
    case types.ADDTODO:
      return {
        ...state,
        arr: state.arr.concat(action.todo)
      };
```

4. Redux 스토어가 루트 리듀서에 의해 반환된 상태 트리를 저장합니다.

    

REDUX 에서 스토어의 역할
1. 애플리케이션의 상태 저장
2. getState()를 통해 상태에 **접근**
3. dispatch(action)을 통해 상태를 수정할 수 있음
4. subscribe(listener)를 통해 리스너를 등록 한다.



https://lunit.gitbook.io/redux-in-korean/basics/usagewithreact
**REDUX 프로젝트 순서**

**환경 
npm install --save react-redux


1. Presentational 컴포넌트와 Container 컴포넌트 구분

presentational component 의 특징
- 목적 : 어떻게 보여질 지(마크업, 스타일)
- 리덕스와 연관 : NO
- 데이터를 읽기 위해 : props
- 데이터를 바꾸기 위해 : props 에서 콜백 호출 (methods)
    -> props 를 통해 함수를 내려서 callback 으로 실행
  
Contatiner component
- 목적 : 어떻게 동작할 지 (데이터 / 상태 변경)
- REDUX 와 연관 : YES
- 데이터를 읽기 위해 : REDUX 구독
- 데이터를 바꾸기 위해 : redux 에 액션을 보냄
    - 1. dispatch(action)
    - 2. store는 리듀서에게 state, action 보냄
    - 3. 리듀서는 모든 상태값을 복사하고 일부 바뀐 부분이 있을 경우에 적용해서 상태 트리를 다시 store에 주고
    - 4. store 는 바뀐 상태트리를 새로 저장한다




중첩된 개체를 가지고 있거나, 사용자들이 개체를 편집할 수 있게 하고 싶다면 이들을 데이터베이스에 넣뜻이 상태에 분리해서 보관해야 합니다. 페이지 정보에는 이들의 ID만을 참조하게 하면 됩니다. 이를 통해 개체들을 항상 최신으로 유지할 수 있습니다.
real world example 에서는 normalizr(npm package)를 통해 중첩된 API응답을 정규화하는 방법을 접근법을 보여줍니다.
**Component 계층 설계**



REDUX 도입 이유  
「좀 더 예측 가능한 형태로 코드를 구조화하는 것」 : 단방향 data flow

Model과 view 사이에 데이터를 양방향으로 흐르게 할 가능성
따라서 이해하고  디버깅하기 어렵다.

MVC 란?
user -> controller <-> model

