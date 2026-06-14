---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Problems
  - Blog
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: Myth of Override
cover: https://app.notion.com/images/page-cover/webb1.jpg
id: 6e79f44c-5df9-46d3-bbec-45dc2f724d70
---

# Introduction:

Recently, while acquainting myself with the new company, I encountered a piece of unusual code.

It seems quite straightforward. We start by declaring a base class with a private virtual function, which is then called by a public member function. Next, we derive a class from the base class and override the virtual function. This pattern is known as the Template Pattern. It defines the skeleton of an algorithm but allows subclasses to override specific steps without altering its structure. The code appears sound until we scrutinize the derived class.

```c++
#include<iostream>
#include<memory>

class base {
public:
    base() = default;
    void callPrivateFunction(){
        privateFunction();
    }
private:
    virtual void privateFunction(){
        std::cout<<"The call comes from a private function"<<std::endl;
    }
};

class derived : public base {
public:
    void privateFunction() override {
        std::cout<<"The cal comes from the overrided function"<<std::endl;
    }
};

int main(){
    base *ptr = new derived();
    ptr->callPrivateFunction();

    derived *ptr_derived = new derived();
    ptr_derived->privateFunction();
    return 0;
}
```

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">github.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBCEIPV%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T205843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID31XcylC4ZB0dpk7xSF4Ay45Nd9wOi309aNnWvWoUiuAiEAgtPEHnfu1xtt%2BgmRF2twrQSs41QaJ09trkCwP9iSkaEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDHGkckKgZFkpk8aSSSrcA4xX4jIzTZ%2B%2FyiUbeWOovrJhl%2FzVM88Y%2FWbPvrQ0wDGhxzm6VIJ6YJpG7mtcuZfYVAUa69c5R3VhZBhQgNMxBzyI7%2BayqM8UfRAlZDoU0Orc2yGrV81uEgllTFwOvLKwj6SPfynmcjnudhywEIBqgebljNRc9YX6z4KiAa1rJQCudD%2FyOUA5oDkZPxOAOuFvIRKsaX6sgFk5HUXi9gu3sLWrQw0ujL6LqQRjT4n0OuLp8odelP3reAFS5ZGCWJXzS%2BuJlPtsIYHP701qa7glIQNdu0VQqErABQ%2Bqv0BMkX4E8aUs07HVrES6iGSHSy8q%2F%2F%2F17eSfxXpVSIBC%2BXbJOYyzLIGohfv2rK9ogfJRz9C6QjTVtQ4w7%2BewKZQDZLXSRBWi7og04AwjiKG9Pf4cMzKTdWZ100ay%2Brhz4woYD80PMj1d4puF%2BnkO74BMu61OeEWmrR33%2BbDLI9xQdPpBCeFSwAvc4Fqtt%2FhmhA62MrBFGEVElkz8XSMW6WGP1Er7GVbHH5joFg%2BHzQZS5D6CNhC0khgIhFW2e4ujdbcpEUZlaQuzIN2XblDsQjI4MEAAa3mRWJ7u%2FS2u49W1LKtSNHrBWtrbuuxXPj%2FgA4dUCsqVbLu%2BFSl0tDU5%2BLlBMNuUvNEGOqUBdxYepEKCakaI8DSsINuq0O%2B%2F7u4qk78aP41G7bg%2BSMYHmh3t40rMmPiOaA8INbsodyqPX59fFOuX3suxNFcXxFPSbA0HBhxlsvvS7iO3H1epsI5TloDkrQc8CkY7hqoUaAWAF4U6oDWdI3yIu0cBn9xZzarinudWaz85hekXOAaGO0o5oUhDGWmZ%2BCwGxQ6SIssdXz6xT7xsrQqPc3ruyeZRVDOa&X-Amz-Signature=eb456e2d969134191c1abe7c8f7a71006309979a80c85b2a545c64dfee2c447d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBCEIPV%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T205843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID31XcylC4ZB0dpk7xSF4Ay45Nd9wOi309aNnWvWoUiuAiEAgtPEHnfu1xtt%2BgmRF2twrQSs41QaJ09trkCwP9iSkaEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDHGkckKgZFkpk8aSSSrcA4xX4jIzTZ%2B%2FyiUbeWOovrJhl%2FzVM88Y%2FWbPvrQ0wDGhxzm6VIJ6YJpG7mtcuZfYVAUa69c5R3VhZBhQgNMxBzyI7%2BayqM8UfRAlZDoU0Orc2yGrV81uEgllTFwOvLKwj6SPfynmcjnudhywEIBqgebljNRc9YX6z4KiAa1rJQCudD%2FyOUA5oDkZPxOAOuFvIRKsaX6sgFk5HUXi9gu3sLWrQw0ujL6LqQRjT4n0OuLp8odelP3reAFS5ZGCWJXzS%2BuJlPtsIYHP701qa7glIQNdu0VQqErABQ%2Bqv0BMkX4E8aUs07HVrES6iGSHSy8q%2F%2F%2F17eSfxXpVSIBC%2BXbJOYyzLIGohfv2rK9ogfJRz9C6QjTVtQ4w7%2BewKZQDZLXSRBWi7og04AwjiKG9Pf4cMzKTdWZ100ay%2Brhz4woYD80PMj1d4puF%2BnkO74BMu61OeEWmrR33%2BbDLI9xQdPpBCeFSwAvc4Fqtt%2FhmhA62MrBFGEVElkz8XSMW6WGP1Er7GVbHH5joFg%2BHzQZS5D6CNhC0khgIhFW2e4ujdbcpEUZlaQuzIN2XblDsQjI4MEAAa3mRWJ7u%2FS2u49W1LKtSNHrBWtrbuuxXPj%2FgA4dUCsqVbLu%2BFSl0tDU5%2BLlBMNuUvNEGOqUBdxYepEKCakaI8DSsINuq0O%2B%2F7u4qk78aP41G7bg%2BSMYHmh3t40rMmPiOaA8INbsodyqPX59fFOuX3suxNFcXxFPSbA0HBhxlsvvS7iO3H1epsI5TloDkrQc8CkY7hqoUaAWAF4U6oDWdI3yIu0cBn9xZzarinudWaz85hekXOAaGO0o5oUhDGWmZ%2BCwGxQ6SIssdXz6xT7xsrQqPc3ruyeZRVDOa&X-Amz-Signature=6fe9f4170edb33c9d3a4111d2af1377c746db374f8a67833ddf8438bb889575c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
