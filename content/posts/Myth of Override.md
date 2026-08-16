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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BSBHYQ%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T141239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIBGuvQifmEuN29zKQobDDgUhnrJLJggV7LCLkezIpMhyAiAnkCxxrpKmNgMM2mxeYyTiQNWPGfSXgrU4WosPOjPSnyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMzdcOKLI8btbA%2B%2BDdKtwDKmsS9cj7dJEaqYJ0ERGshdbQ9LDH%2F8Rti%2FXLDCB2jCz4ZappmXRIlh21oCdL%2BXk6nElgBcJNulRcCWd8KQIPgDQAVBUwla01xDB1q980h7X41%2FCtmzghi6b2fno%2BhWuI3xVDUfSsvfqX9Il%2Btf7A8QCjwKDIFzZ2rt9kIi7rAkL18fmrEaCEtnr7TRpUs6mBYi6cIsF8XHAPWgtX5qymgiL4Ex3EgVH6%2BCQSdIX9vobqicIq5vEf0FPB%2BhvbtgPTcoxJHVBvcSeRlMFjAWkFVK8XqVSOpP4ioNyA6FrE3Bu0x3DEBci%2FgD23U5Ap4EraokQBaVyje6hx3sTMF2b9qq%2FCS5Y6bIFS5AjF3h45YXLa2m1IZmPd4vLhUaLWOu4TwsnUzrsT0k38EvRW0iwKdhosMqR55l%2FqfnmLQ18wEnnH9TSoS7jNS%2FFpfqB%2BlOB6f8qkpO%2Fjv9boDA%2Bwt%2B4qIs9t8ptHaN%2Fd5LQI7CNRU39s8IoVscKuZRsU5qG7qhklQbN1I1mTBeaeG9vk%2B69AdpCuoYPlQpRqTLutILhdkYJQmMn7kKkAJ61OZcdwq%2BYKlqkQbDMlQ4qAD1dZ3QI3p88wq09IcddsqPk%2FIZb0UvF5Cqqqt2AhZrSfFzQw86aG1AY6pgGmji9TuxcGNatMYBgFN4osA6LFATl257VUZCnkqP%2BgW8IfMpY16EPbA6jVF8vsBXCH%2Bt3tDhrL55wwgHwHerL4Qprz2PObTxpc%2BZw542XOZwhb6Ec%2BxF%2BqF%2FkNlLeYgXWhN5XCN%2FbLE3y2OHnzAcuPyhNha8bRAy9ZY9%2FDRQJ5JDFAis6BlV7h7TMau7bJp%2Fk27Imop0hh%2FU1oQW3G3d6YLLxgVOAI&X-Amz-Signature=347c90a1cb417aedd36506fc83259a5a7be24b14abf201d8e41b15f6673dd802&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632BSBHYQ%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T141239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIBGuvQifmEuN29zKQobDDgUhnrJLJggV7LCLkezIpMhyAiAnkCxxrpKmNgMM2mxeYyTiQNWPGfSXgrU4WosPOjPSnyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMzdcOKLI8btbA%2B%2BDdKtwDKmsS9cj7dJEaqYJ0ERGshdbQ9LDH%2F8Rti%2FXLDCB2jCz4ZappmXRIlh21oCdL%2BXk6nElgBcJNulRcCWd8KQIPgDQAVBUwla01xDB1q980h7X41%2FCtmzghi6b2fno%2BhWuI3xVDUfSsvfqX9Il%2Btf7A8QCjwKDIFzZ2rt9kIi7rAkL18fmrEaCEtnr7TRpUs6mBYi6cIsF8XHAPWgtX5qymgiL4Ex3EgVH6%2BCQSdIX9vobqicIq5vEf0FPB%2BhvbtgPTcoxJHVBvcSeRlMFjAWkFVK8XqVSOpP4ioNyA6FrE3Bu0x3DEBci%2FgD23U5Ap4EraokQBaVyje6hx3sTMF2b9qq%2FCS5Y6bIFS5AjF3h45YXLa2m1IZmPd4vLhUaLWOu4TwsnUzrsT0k38EvRW0iwKdhosMqR55l%2FqfnmLQ18wEnnH9TSoS7jNS%2FFpfqB%2BlOB6f8qkpO%2Fjv9boDA%2Bwt%2B4qIs9t8ptHaN%2Fd5LQI7CNRU39s8IoVscKuZRsU5qG7qhklQbN1I1mTBeaeG9vk%2B69AdpCuoYPlQpRqTLutILhdkYJQmMn7kKkAJ61OZcdwq%2BYKlqkQbDMlQ4qAD1dZ3QI3p88wq09IcddsqPk%2FIZb0UvF5Cqqqt2AhZrSfFzQw86aG1AY6pgGmji9TuxcGNatMYBgFN4osA6LFATl257VUZCnkqP%2BgW8IfMpY16EPbA6jVF8vsBXCH%2Bt3tDhrL55wwgHwHerL4Qprz2PObTxpc%2BZw542XOZwhb6Ec%2BxF%2BqF%2FkNlLeYgXWhN5XCN%2FbLE3y2OHnzAcuPyhNha8bRAy9ZY9%2FDRQJ5JDFAis6BlV7h7TMau7bJp%2Fk27Imop0hh%2FU1oQW3G3d6YLLxgVOAI&X-Amz-Signature=cba73f9b10a81716cc91a5b0ff56f2e471ac92838d17c9f3d6c6c6a0aefc5c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
