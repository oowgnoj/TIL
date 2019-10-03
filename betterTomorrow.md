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





## 10/4 TIL

####예정사항

1. componentDidMount
2. Callback 함수
3. React 블로깅 준비
4. gitignore

