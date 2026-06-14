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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLNQO7V%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T170750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQD%2BJsM5MSvoseddN8kH7PtqRMk8Rl40zaDjYEAxPT7TXAIhAMM5wnOI3DKQBqH3GnW5DKnck18ZfZbE4cQxDwsQOnbHKv8DCEcQABoMNjM3NDIzMTgzODA1IgyLgKp6UtgPGJJAIcYq3APi1k3R51xPbXRbdfkJLwMl7EAoG5Y4e741oLu%2F5YbgsCnr59OWM1zrZ491WjXmev57iDJz5tyg2vQtWGOtHiY8KyePdOqk%2FlbqCRJNOtrfczlMRpeRqkpj5biB8mWh7%2B3rMnLxqwaEIGnrxSOqpKbsE3ganao6TU8pSOeLK8xpw81q5ZNsDcTn32iAfrfLXimfPzix%2Bh6YijB7UeXAS68kG5QaLZ%2BymWJnGnXvWXKQDUIjmQhc1NuAHpGg7X9w2O5msqt%2FUT2dRLt7Q7z7ycOCqZg6nvw6ZpTJKmRBbPwfxcHi86tdCqquqxvkvmurGf%2BywiYBkB85ORqucylofw0qF3oKQGwm5mhpI8xjbuU29nsexhwkWiv5tDsQKHBly15UwULeLRDWu7%2FMe3S6%2FkquR%2BY3WTi4AcnziqOSAMHJVjQlo%2BJvZiIRthtzfDU3g4U17Qvt8jI56Owq57Gyb59zYf63LMTj6sLxf8h2GUT%2Bsg8oEyOwGORD5aLufiaOG6tP2HTGupXhN0hLEiiuN1IxaroRjZagFXqstR1c2myIMZnQ1z8PFd%2FJs1e9jmyp%2B%2FdajoiIPiIgKICaQpLYq1Q1wafSA58kS3gIWWl2MOtDRen%2F0%2BQbJkpzRDjYuDDJ5brRBjqkAbx%2Bm6rRSOLTAW0zHUFv6PRKuAs%2FUXv64BQFfAdbyITZxVFbbrJioFgMcwb4bFWGpqyCQja2l3Fa1e5%2BPiu7kVq8vekCJ%2BkrhPbboKVGQie8hQ6%2B5pxCosW4xgAmJHBN%2FShnNCG68zIOP95Ey2uB2xjl8wUGXOkq1cID6dt%2FmnYGMrEe8uCobyMjOy95Hwh6SCusryYBka%2Bdz8TTlHQrxPdCfBZA&X-Amz-Signature=a2e806878d53dee7fd499d7781103824b43de046b902562c5bd0c0c953a3394f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLNQO7V%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T170750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQD%2BJsM5MSvoseddN8kH7PtqRMk8Rl40zaDjYEAxPT7TXAIhAMM5wnOI3DKQBqH3GnW5DKnck18ZfZbE4cQxDwsQOnbHKv8DCEcQABoMNjM3NDIzMTgzODA1IgyLgKp6UtgPGJJAIcYq3APi1k3R51xPbXRbdfkJLwMl7EAoG5Y4e741oLu%2F5YbgsCnr59OWM1zrZ491WjXmev57iDJz5tyg2vQtWGOtHiY8KyePdOqk%2FlbqCRJNOtrfczlMRpeRqkpj5biB8mWh7%2B3rMnLxqwaEIGnrxSOqpKbsE3ganao6TU8pSOeLK8xpw81q5ZNsDcTn32iAfrfLXimfPzix%2Bh6YijB7UeXAS68kG5QaLZ%2BymWJnGnXvWXKQDUIjmQhc1NuAHpGg7X9w2O5msqt%2FUT2dRLt7Q7z7ycOCqZg6nvw6ZpTJKmRBbPwfxcHi86tdCqquqxvkvmurGf%2BywiYBkB85ORqucylofw0qF3oKQGwm5mhpI8xjbuU29nsexhwkWiv5tDsQKHBly15UwULeLRDWu7%2FMe3S6%2FkquR%2BY3WTi4AcnziqOSAMHJVjQlo%2BJvZiIRthtzfDU3g4U17Qvt8jI56Owq57Gyb59zYf63LMTj6sLxf8h2GUT%2Bsg8oEyOwGORD5aLufiaOG6tP2HTGupXhN0hLEiiuN1IxaroRjZagFXqstR1c2myIMZnQ1z8PFd%2FJs1e9jmyp%2B%2FdajoiIPiIgKICaQpLYq1Q1wafSA58kS3gIWWl2MOtDRen%2F0%2BQbJkpzRDjYuDDJ5brRBjqkAbx%2Bm6rRSOLTAW0zHUFv6PRKuAs%2FUXv64BQFfAdbyITZxVFbbrJioFgMcwb4bFWGpqyCQja2l3Fa1e5%2BPiu7kVq8vekCJ%2BkrhPbboKVGQie8hQ6%2B5pxCosW4xgAmJHBN%2FShnNCG68zIOP95Ey2uB2xjl8wUGXOkq1cID6dt%2FmnYGMrEe8uCobyMjOy95Hwh6SCusryYBka%2Bdz8TTlHQrxPdCfBZA&X-Amz-Signature=60afdb2ccc90250dcff4337abe3778e6c9bd5c695750206c1172c777b93f7d3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
