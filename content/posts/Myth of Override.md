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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YCEQGFA%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T064030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDImBFaAl8FkxEVy0ExuWAjVg1ORE6y0gDOIBDeZx199AIhAM7dZKTgmmyZFyAHHZKbhrq%2BOqO0vPAC9888DdU%2F6tvrKv8DCE8QABoMNjM3NDIzMTgzODA1Igw9nIRToDM3hKFFIyYq3APstAIwNlqOvAwoJEbVKNt6zj%2FMO%2F7coYwCKMCUenxTwEJAPBQSrpq8D5wtXVPcOzgrDu36ZqkBWG0QhIB2LytsAqSrfgj9zufdqM3muK7G6UdsRNOh9t3UOSnnW7T3E9xXekKx%2F2H0BcVgjlvzvUNlq9JsJByTRUC5Fgsdg4eM4UoSzDYZg2zrgXaSgKMf6GG2bvNDHUFDWJBb3zN5%2BsHo7Upf1q2HdWRLb4Q8rZ2V7QpKmri4uPYiKp7F2TyHe4GKFpK3m4xex%2FKHlw%2BE1gGbVbCNl%2FNgf3dYlgMf0A4LB2eoa1zy%2FPdKacrgUVh802gY7RKlISxgQbaywV4%2BuoxJ2lDI7L5YyzyyJUU7jl0OlVaH7l8iLOhKNnACHhGVenZobRVus1d3ceTN9zaeiIIF1sPxYYTRtX6ZLnMnnwzOw%2BLbn%2BllB1UEtRuZhnWuK6fddNsO0PKTZ%2FoK3Bu24FwRIme1N53kRwx5HOCHY1xgeaFEecVDzRYNN%2B4mlm2AMWoDKmFW2bfN0y5VrE5YP3fz9xE7mLUDrm0EY0hWqYnVIIaRWLIVBBZbEYjJxrOryoG3%2B66MkTCHD2LqMYa11f8qKc%2FPbH1qrVRXVxG4ymbkGUQtBY2mtklEXEQtcDCG0f7UBjqkAdwjuoWzqmSr7nX50FaWBUSR9bUR%2Fyn3OJCWjHLyLIvTcUw7Z5PomLbdX44appNjRhVpXe95xI1UjmYEfOjoSUQ1aJuJLexNvTO%2FnFgIeDuOOE%2FWHFyTKSn0El8sPfYV3GfTJlNkQBTLQBDXOsLO662DMMVqis22clbA3FYHiREcAxX3CTL7waxY0gwcmEZZZKUvN8IDua5EFwjely8huTcyR23a&X-Amz-Signature=4322293693ca490f65b9ca75ac020e94632079eee7016e98558fcef247c30e9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YCEQGFA%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T064030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDImBFaAl8FkxEVy0ExuWAjVg1ORE6y0gDOIBDeZx199AIhAM7dZKTgmmyZFyAHHZKbhrq%2BOqO0vPAC9888DdU%2F6tvrKv8DCE8QABoMNjM3NDIzMTgzODA1Igw9nIRToDM3hKFFIyYq3APstAIwNlqOvAwoJEbVKNt6zj%2FMO%2F7coYwCKMCUenxTwEJAPBQSrpq8D5wtXVPcOzgrDu36ZqkBWG0QhIB2LytsAqSrfgj9zufdqM3muK7G6UdsRNOh9t3UOSnnW7T3E9xXekKx%2F2H0BcVgjlvzvUNlq9JsJByTRUC5Fgsdg4eM4UoSzDYZg2zrgXaSgKMf6GG2bvNDHUFDWJBb3zN5%2BsHo7Upf1q2HdWRLb4Q8rZ2V7QpKmri4uPYiKp7F2TyHe4GKFpK3m4xex%2FKHlw%2BE1gGbVbCNl%2FNgf3dYlgMf0A4LB2eoa1zy%2FPdKacrgUVh802gY7RKlISxgQbaywV4%2BuoxJ2lDI7L5YyzyyJUU7jl0OlVaH7l8iLOhKNnACHhGVenZobRVus1d3ceTN9zaeiIIF1sPxYYTRtX6ZLnMnnwzOw%2BLbn%2BllB1UEtRuZhnWuK6fddNsO0PKTZ%2FoK3Bu24FwRIme1N53kRwx5HOCHY1xgeaFEecVDzRYNN%2B4mlm2AMWoDKmFW2bfN0y5VrE5YP3fz9xE7mLUDrm0EY0hWqYnVIIaRWLIVBBZbEYjJxrOryoG3%2B66MkTCHD2LqMYa11f8qKc%2FPbH1qrVRXVxG4ymbkGUQtBY2mtklEXEQtcDCG0f7UBjqkAdwjuoWzqmSr7nX50FaWBUSR9bUR%2Fyn3OJCWjHLyLIvTcUw7Z5PomLbdX44appNjRhVpXe95xI1UjmYEfOjoSUQ1aJuJLexNvTO%2FnFgIeDuOOE%2FWHFyTKSn0El8sPfYV3GfTJlNkQBTLQBDXOsLO662DMMVqis22clbA3FYHiREcAxX3CTL7waxY0gwcmEZZZKUvN8IDua5EFwjely8huTcyR23a&X-Amz-Signature=f76d152ba93321a508f1fc24e8c8faf04a314e5c3bdb661b7031d42ea1b91fa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
