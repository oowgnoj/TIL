타입스크립트 !
타입을 지정해줘야하는 때는 언제인가?

우선 리액트와의 조화를 생각하지 않고 한다면 그냥
모든 변수에 들어간다고 하면 된다.
string, number 던 function 이던 function 안에 들어가는 parameter 던

````javascript

````



## **Creating a component**
_without component_

```javascript
import * as React from 'react';

export interface Props {
  name:string ; 
  enthusiamLevel?:number;
}

function Hello({name, enthusiamLevel = 1}:Props){
  if (enthusiasmLevel <= ){
    throw new Error('You Could be...')
  }
  return (
    <div>
    Hello {name + getExclamationMarks(enthusiasmLevel)}
    </div>
  )
}

function getExclamationMarks(numChars:number){
  return Array(numChars +1).join('!');
}

```


_w/ state_


````javascript
import * as React from "react";

export interface Props {
  name: string;
  enthusiasmLevel?: number;
}

**interface** State {
  currentEnthusiasm: number;
}

class Hello extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { currentEnthusiasm: props.enthusiasmLevel || 1 };
  }

  onIncrement = () => this.updateEnthusiasm(this.state.currentEnthusiasm + 1);
  onDecrement = () => this.updateEnthusiasm(this.state.currentEnthusiasm - 1);

  render() {
    const { name } = this.props;

    if (this.state.currentEnthusiasm <= 0) {
      throw new Error('You could be a little more enthusiastic. :D');
    }

    return (
      <div className="hello">
        <div className="greeting">
          Hello {name + getExclamationMarks(this.state.currentEnthusiasm)}
        </div>
        <button onClick={this.onDecrement}>-</button>
        <button onClick={this.onIncrement}>+</button>
      </div>
    );
  }

  updateEnthusiasm(currentEnthusiasm: number) {
    this.setState({ currentEnthusiasm });
  }
}

export default Hello;

function getExclamationMarks(numChars: number) {
  return Array(numChars + 1).join('!');
}

````



