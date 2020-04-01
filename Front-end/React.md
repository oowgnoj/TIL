### REACT 처럼 사고하기



JSON 데이터가 다음의 데이터를 반환한다고 생각해 볼게요.

````javascript
[
  {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
  {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
  {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
  {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
  {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
  {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
];
````



복잡한 데이터가 아니니까, 가장 효율적인 visualization은 큰 이견이 없을 것 같아요. 

1. 먼저 category ('sporting goods',  'electronics' )로 나누고, 해당되는 상품(name)대로 분류하고.
2. Category 별로 제품의 name, price, 재고상태를 보여주는 table을 만들면 되겠죠


리액트를 사용해 웹사이트를 구현 할 때에도, UI를 쪼개서 관리해요. 이걸 컴포넌트 (component) 라고 하죠. 컴포넌트 하나에 모든 웹사이트의 기능과 데이터를 다 포함시켜도 되지만, 그러면 리액트를 사용 할 이유가 없죠. 

#### 어떻게 컴포넌트 쪼갤것인가?

이 질문이 리액트로 처음 개발하시는 분들이 처음 대답해야할 문제라고 생각해요. 컴포넌트 구성은 재사용성과 유지보수 뿐만아니라 컴포넌트의 state관리, 즉, data flow와도 깊은 연관이 있기 때문이에요.

https://ko.reactjs.org/docs/thinking-in-react.html

에서 제시하는 한가지 방법은 '단일 책임 원칙' 이에요. single responsibility principle이라는 개념을 살펴보면. 객체 지향 프로그래밍 패러다임에서, 모든 클래스는 하나의 책임만 가지며, 클래스는 그 책임을 완전히 캡슐화 해야함을 일컫는다.

[https://ko.wikipedia.org/wiki/%EB%8B%A8%EC%9D%BC_%EC%B1%85%EC%9E%84_%EC%9B%90%EC%B9%99](https://ko.wikipedia.org/wiki/단일_책임_원칙)

객체지향과 캡슐화에 대해 제가 이해하는걸 바탕으로 간단하게 말씀드리면, 어플리케이션 = 객체1 + 객체2 + 객체3 + 객체 4 의 형태로서. 모든 데이터를 객체로 나눠 분리하고 각 객체가 필요한 계산은 내부에서 해결하는 방법이라고 생각합니다.

리액트에서는 컴포넌트가 하나의 객체라고 생각하면 되겠어요.
예로 간단한 TodoList application 에서는 입력창, 할 일 목록이 컴포넌트로 구성되고 있고, 할 일 목록은 각 할 일이 또 컴포넌트로 구성되겠죠.

#### Todolist 컴포넌트 구성

- App
  - 입력창
  - Todo List
    - Todo 1
    - Todo 2



#### REACT의 동적인 데이터 흐름 : state관리

앞서 말씀드렸지만, component의 구성은 리액트에서 '변하는 데이터'를 뜻하는 state와 큰 관련이 있어요. REACT에서의 데이터는 props와 state로 구분하는데, 

#####props는 상위 컴포넌트가 가지고 있는 property를 자식 컴포넌트에게 '변화할 수 없는' 데이터 형식으로 보내고,

##### state는 property가 가지고있는 '상태'에요. 변경될 수 있고, 자식 객체에는 props의 형태로 보내줄 수 있어요.



App

- 입력창
- Todo List
  - Todo 1
  - Todo 2



위에서 본 Todolist의 컴포넌트 구성에서 입력창에서 받은 입력값은, 한번에 형제컴포넌트인 todoList에게 전달이 안되고, state lifting up을 통해 App으로 올라가서, Todolist - Todo에 props로 내려줘야해요.

##### [입력창] input입력 -> [App] props로 변경 -> [TodoList] -> [Todo3]



이 때 우리는 애플리케이션에서 필요로 하는 변경 가능한 state의 최소 집합을 생각해봐야 하는데, 핵심은 중복배제원칙 이라고 합니다.

- 애플리케이션이 필요로 하는 가장 최소한의 state를 찾는다
- 이를 통해 나머지 모든 것들이 필요에 따라 그때그때 계산되도록 한다.



최소한의 state를 찾는 방법은 친절하게 설명이 되어있습니다. 세가지 질문을 통해 props와 state를 구분한다고 해요.

1. 부모로부터 props를 통해 전달 
2. 시간이 지나도 변하지 않는다
3. 컴포넌트 안의 다른 state나 props를 가지고 계산이 가능한 건지.


12 main concepts of R E A C T from official
about 7, 12 조건부 렌더링 features

#### 7. 조건부 렌더링

React에서 조건부 렌더링은 Javascript 에서의 조건 처리와 같이 동작합니다. if / 조건부 연산자 등을 사용해**조건을 포함한 현재 상태를 나타내는 엘리먼트**를 만드는 데에 사용해요.

```
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}
// login vs Guest User 에 따른 상태 메세지
```

사용자의 **로그인 상태**에 맞게 위 컴포넌트 중 하나를 보여주는 Greeting Component 를 만듭니다.

```
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

ReactDOM.render(
  // Try changing to isLoggedIn={true}:
  <Greeting isLoggedIn={false} />,
  document.getElementById('root')
);
```

엘리먼트 변수 : 엘리먼트를 저장하기 위해 변수를 사용할 때 출력의 다른 부분은 변하지 않은 채로 컴포넌트의 일부를 조건부로 렌더링 할 수 있습니다.

```
function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}
```

조건부 렌더링, login / out 의 상태에 따라 다른 button을 보여주는 예제입니다.

```
Class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    //handleLoginClick에 this를 bind 해주는 이유는 : this.setState 값 변경을 위해
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogOutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }
  handleLoginClick() {
    this.setState({isLoggedIn : true});
}
  handleLogoutClick() {
    this.setState({isLoggedIn : false});
}
  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }
    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn}/>
        {button}
      </div>
    );
  }
}


ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);
```

