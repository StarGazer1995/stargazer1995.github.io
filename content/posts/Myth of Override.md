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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SST53TVG%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T082008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIBPtihG0WvKhtJWEGVCU1BRzphhg9oYPuMm%2BlKGd0rAWAiAUl5lIOWZhqPG%2BUfW2abZL9WNHPIrLa9%2FQA6YahNaQ6yr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMzqor2eTWIsDXTU5EKtwD2UmconMbjup28P%2BfqsXDSFf4s1Kc3K6PNwQN21XRf7b99b8r09Ue1x7VFJDI4Shmu4qAmUbISJEAtWdg%2BpMX8Hm2lnJ6Ehrxbj5SsHzrgxHrbTtSfU7jDV%2BNOUpHEW3PrTE%2FLR%2BLR1Qx%2FStfWmyR8xWmhvWkJI76QTQB468%2Bj0f%2BLj5Ei%2Fu8r%2FIgQ7eStiJc51BsYvZBTtFSc8gNrJAPvD9BAnAXYrEhSo9%2FW8q%2FOOTHmgAGW9ePcvc69Dz4FB%2BXU5yNRlrSuMT%2Bf368cnNwykOBOHd0qSfmHSfJtkVDc0N9FP5ThLHz7Ur1NOO49vWM%2FYmLYZThTYrVdm4y0pKWrho30v1Ynfs22Hte1WjVSLMa%2BjHhvPFxyvkhoPsa%2B5qVU5JH33bbLUXqWkIducTflXUJX%2FS8TwQxTb6Db8jKMsE4p1BAuz%2BjmLl7Jn5s2DuzLwdlKNwQQemxZi4cbDrmeckkCWecCjMD8nESzIUa7sBapJUqZRi%2BX3wgowchu1rsbY3mqLcuLlkMmm3i7IsuyWGOZEJ%2FTQ79B1Iq7mYYspjEbFf96IttLWZ04ZDZ9IwdsEIb4NByufqW28xdv9XqRr%2BSDAn0987Meu6U9qAUGxpSLlpivXMvLHZTjvMwpqb50AY6pgEXFl9uGUKC26%2FsZqYF8ADQE%2BNDBOifCsj2Gg4oc40TDJn2jUhKWys0M4oPRYwU55vCHKluVGk2epCba%2Bet%2FKJtqloqQRMTc79mcyvPgUt0EVsFR8KAAf%2B8hRfRgFP5Xfd57MZGSFJDTFCGqD%2BJL4NYEMlhvv5fZbrbiWIqbuQ6hGB7kWd9fDE8OR00WtnA9LQZMJGZVIw3AWIbmADYHodaT9jW17xt&X-Amz-Signature=9692bff76959fa1318e3efc5312b083847cba834450fa3a9e8cba20580cf5650&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SST53TVG%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T082008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIBPtihG0WvKhtJWEGVCU1BRzphhg9oYPuMm%2BlKGd0rAWAiAUl5lIOWZhqPG%2BUfW2abZL9WNHPIrLa9%2FQA6YahNaQ6yr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMzqor2eTWIsDXTU5EKtwD2UmconMbjup28P%2BfqsXDSFf4s1Kc3K6PNwQN21XRf7b99b8r09Ue1x7VFJDI4Shmu4qAmUbISJEAtWdg%2BpMX8Hm2lnJ6Ehrxbj5SsHzrgxHrbTtSfU7jDV%2BNOUpHEW3PrTE%2FLR%2BLR1Qx%2FStfWmyR8xWmhvWkJI76QTQB468%2Bj0f%2BLj5Ei%2Fu8r%2FIgQ7eStiJc51BsYvZBTtFSc8gNrJAPvD9BAnAXYrEhSo9%2FW8q%2FOOTHmgAGW9ePcvc69Dz4FB%2BXU5yNRlrSuMT%2Bf368cnNwykOBOHd0qSfmHSfJtkVDc0N9FP5ThLHz7Ur1NOO49vWM%2FYmLYZThTYrVdm4y0pKWrho30v1Ynfs22Hte1WjVSLMa%2BjHhvPFxyvkhoPsa%2B5qVU5JH33bbLUXqWkIducTflXUJX%2FS8TwQxTb6Db8jKMsE4p1BAuz%2BjmLl7Jn5s2DuzLwdlKNwQQemxZi4cbDrmeckkCWecCjMD8nESzIUa7sBapJUqZRi%2BX3wgowchu1rsbY3mqLcuLlkMmm3i7IsuyWGOZEJ%2FTQ79B1Iq7mYYspjEbFf96IttLWZ04ZDZ9IwdsEIb4NByufqW28xdv9XqRr%2BSDAn0987Meu6U9qAUGxpSLlpivXMvLHZTjvMwpqb50AY6pgEXFl9uGUKC26%2FsZqYF8ADQE%2BNDBOifCsj2Gg4oc40TDJn2jUhKWys0M4oPRYwU55vCHKluVGk2epCba%2Bet%2FKJtqloqQRMTc79mcyvPgUt0EVsFR8KAAf%2B8hRfRgFP5Xfd57MZGSFJDTFCGqD%2BJL4NYEMlhvv5fZbrbiWIqbuQ6hGB7kWd9fDE8OR00WtnA9LQZMJGZVIw3AWIbmADYHodaT9jW17xt&X-Amz-Signature=49e280578d48f064f08a39e423529cd1da6a68414ed00ea9ce0b7b842d38eee0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
