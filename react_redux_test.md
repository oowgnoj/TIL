1. 나의 서재 책 CSS





1. 책 날짜 추가 및 통계 기능
2. testing



입력방식 hover 에 달력버튼

나의 서재 끝나는부분 =====

progress bar

goal 입력창



password 수정

: client 노출 안시키고, 

password 변경하기 ()

비밀번호 확인 !!





### end - to - end Test

ux 경로로 testing 

1. 로그인
2. 서평 작성
3. 큐레이션 작성
4. myinfo 조회 및 수정
5. mybooks 옮기기 및 잘 옮겨졌는지



`cypress or puppeteer`

 



## react , redux (thunk) error testing

https://redux.js.org/recipes/writing-tests



1. 액션, 리듀서 등

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



2. 