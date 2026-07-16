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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6JVJ6K%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T044914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIHELJeneBfC6JJLM%2F1QWk%2FRmwWSKITHGZ39BXFbJx1ZnAiABFRyKRqa34EGJZUv7VzSSF96sdTf0ugVr2nW665VDSCr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMKZ20N%2FEOyAh1XWh9KtwDuKwKhewSskAPuW296%2FbeOuvKvdN47YEUXjhTHAeOZyAVkE2q76b%2B%2BpgNRmopq%2BRs54aQKnopjQLymbU8kO0Mx24DooDwju9WBib266paOzc%2FPwVsFoeR59ajVtZxZuLnWLCsZJbPMJ2lHpxFte6uP6oEtAdiR1%2FSLqhOX5PzfceUjjkb3YWiFdxQY0P%2BTTDO%2BtiQb8zUkejkaugf73FH%2Fc2a8Z6o5H5R79lizjqmHmDPBHrmV4IajVJMguodO%2FzPdv8r694CB5IasYp3WQ5DaOqW87MZKLXS0JX4VcX98GGt79zrJCfReIEgDwe1jJfDmxGbD4vODl4r9Cgk6yPfDEOYITIKZAjRSg7JFOHlMH09rvhYZtb8kSfG1jgw3zmKVPjPN2HqVkziIhX4i5xzyRwW4KxiXxMITwehdL2EknlJehnAMTueeHwwUiqsW1P668jfm95B%2BS6b6WHwMg%2FJqHa3Y7KmLMaGK5p5cD16f5BxqCa0RzU39f2ZefAibaF1xjER5aZ5rjoJKO8Uyg9RjYDEQ8zl%2Bg5jRWHwzbGHNWGxVcV7BpWEQEJ8zy6AGiMaJCIjh1pfFcqdxWtP0WSTo%2BUJXDFyXCCIBGKiEYnSaJyBDYhcPmlhJ9x%2FLjcwzMDh0gY6pgFXOi1U%2F5OBDIa%2FBe8bd6Co9KoGMBPy%2FbekEV43yuzYqC%2FINfAqlj3yJSRTx%2BXj79Z%2BZTwRWd%2BVQU5%2BeDi4%2BzBq7qFTiwUCb%2B8QobMx3r0AKKKGbp8wxzpVY2lIFtkPmqTty%2FTBbazC2R9YuwSYepqJRi0Xuh8rLxQy51c13pbZh%2F6ba2QhB4ZWI9P75mdznkh%2BXyiArgg%2Bbl1FJSQ0U6Ohdyejp%2BDq&X-Amz-Signature=e4fb189f708b72ec29a1a513483eeead8d0b0559eb3bc0b4eadb7da030d730af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6JVJ6K%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T044914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIHELJeneBfC6JJLM%2F1QWk%2FRmwWSKITHGZ39BXFbJx1ZnAiABFRyKRqa34EGJZUv7VzSSF96sdTf0ugVr2nW665VDSCr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMKZ20N%2FEOyAh1XWh9KtwDuKwKhewSskAPuW296%2FbeOuvKvdN47YEUXjhTHAeOZyAVkE2q76b%2B%2BpgNRmopq%2BRs54aQKnopjQLymbU8kO0Mx24DooDwju9WBib266paOzc%2FPwVsFoeR59ajVtZxZuLnWLCsZJbPMJ2lHpxFte6uP6oEtAdiR1%2FSLqhOX5PzfceUjjkb3YWiFdxQY0P%2BTTDO%2BtiQb8zUkejkaugf73FH%2Fc2a8Z6o5H5R79lizjqmHmDPBHrmV4IajVJMguodO%2FzPdv8r694CB5IasYp3WQ5DaOqW87MZKLXS0JX4VcX98GGt79zrJCfReIEgDwe1jJfDmxGbD4vODl4r9Cgk6yPfDEOYITIKZAjRSg7JFOHlMH09rvhYZtb8kSfG1jgw3zmKVPjPN2HqVkziIhX4i5xzyRwW4KxiXxMITwehdL2EknlJehnAMTueeHwwUiqsW1P668jfm95B%2BS6b6WHwMg%2FJqHa3Y7KmLMaGK5p5cD16f5BxqCa0RzU39f2ZefAibaF1xjER5aZ5rjoJKO8Uyg9RjYDEQ8zl%2Bg5jRWHwzbGHNWGxVcV7BpWEQEJ8zy6AGiMaJCIjh1pfFcqdxWtP0WSTo%2BUJXDFyXCCIBGKiEYnSaJyBDYhcPmlhJ9x%2FLjcwzMDh0gY6pgFXOi1U%2F5OBDIa%2FBe8bd6Co9KoGMBPy%2FbekEV43yuzYqC%2FINfAqlj3yJSRTx%2BXj79Z%2BZTwRWd%2BVQU5%2BeDi4%2BzBq7qFTiwUCb%2B8QobMx3r0AKKKGbp8wxzpVY2lIFtkPmqTty%2FTBbazC2R9YuwSYepqJRi0Xuh8rLxQy51c13pbZh%2F6ba2QhB4ZWI9P75mdznkh%2BXyiArgg%2Bbl1FJSQ0U6Ohdyejp%2BDq&X-Amz-Signature=8fd39aef2a4b8445cf2df8f9ee009f37950b6a9313f90d2ae0146f60081efb1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
