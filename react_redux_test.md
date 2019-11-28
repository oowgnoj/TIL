use jest



Typress

https://redux.js.org/recipes/writing-tests





ux 경로로 testing 

1. 서평 작성
2. 큐레이션 작성
3. myinfo 조회 및 수정
4. mybooks 옮기기 및 잘 옮겨졌는지







들어왔을 때 책이 먼저 보이면 좋겠다

bar 말고 숫자 2/ 10



읽은책 / 읽는중/ 다읽은 책 의 정보를 한번에 보여줄 수 있는 stat

**서평 목표가 좀 애매하다, 필요한가**



mypage email click # alink



#### puppeteer

headless chrome : chrome without UI , how this is useful for us

--headless 

--debugging tool





no URL chrome





## redux thunk error testing

https://redux.js.org/recipes/writing-tests



1. action testing

   ````javascript
   import * as actions from '../../actions/TodoActions'
   import * as types from '../../constants/ActionTypes'
   
   describe('actions', () => {
     it('should create an action to add a todo', () => {
       const text = 'Finish docs'
       const expectedAction = {
         type: types.ADD_TODO,
         text
       }
       expect(actions.addTodo(text)).toEqual(expectedAction)
     })
   })
   ````

   

2. 