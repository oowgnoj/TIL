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

