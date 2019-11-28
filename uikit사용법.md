## create-react-app 기준



node-module이 src 폴더 바깥에 있으므로

react-rewired-app package 를 설치해서 해당 설정을 지워줘야한다



https://stackoverflow.com/questions/44114436/the-create-react-app-imports-restriction-outside-of-src-directory







https://stackoverflow.com/questions/44114436/the-create-react-app-imports-restriction-outside-of-src-directory#answer-44115058

`config-overrides.js` file similar to this one:

```js
const ModuleScopePlugin = require('react-dev-utils/ModuleScopePlugin');

module.exports = function override(config, env) {
    config.resolve.plugins = config.resolve.plugins.filter(plugin => !(plugin instanceof ModuleScopePlugin));

    return config;
};
```