# ZhihuZse86
知乎 js 逆向 zse-86 参数


```
// encrypt 
b = function (e) {
        return __g._encrypt(encodeURIComponent(e));
    };
```
 
1. paramsJoin 为不同参数拼接，接口不同参数不同
2. paramsJoin 拼接后根据不同情况 f(e, t, n) 生成 e
3. __g._encrypt 生成 zse-86

PS: 局部 js 加密，不同接口不同处理方法
