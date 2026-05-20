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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZL77G3B2%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T180941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCm%2FpPend6vR6cYV3nwYCygTVfouHMsLjZhUEHpC2kaeQIhAKwV%2BKp%2BTVcYFYfG%2BauvA4lZW8cHTXYjF1E2JstOJrVlKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6B5bKF3qu388WO18q3ANACQBo3ZWNqKcKfqPORSWjVaazk3Fzut5YYt6CaL8aGi%2BJnLaodfjMI8RsH0IN5kvT59BotPzWGqkQ3BX3y1vEzrVI1wPYn%2FiHMnElm7gPMkxRREx5J3x0jrJc9SBdv11vG0VRlLawfvcf5ygiOGTGvG9hLFTLt3MEX7phKjxZtV%2FCUnW%2FHEUPt1J2vlyIFCN8zElDbB%2F60p63xZdO9nOBsQsZxDRrEZksH8YIqBWG0NoLD2ElosdTblN%2Ff6U9g9cwZfuBlSwcU1cDEAH0HW0xCpPuDUJJyaXrDQPn0sfnaFrDgzUsAKlHec%2BFSd7%2B8N040yjS9j5qRUwvamypE9n3LEDxP85ZcZ8E4j6til46Vt6pSF0wz8t9MNJC2c681MabX5W3f9nooq6fZeD9NgO9zFJaH8KXlGec6HUkHtioGM2sOVVFS0MU8x72jN1CSkkPhj6x3mNXGkMva9hxgIHMxuzhL9vLkku%2BZ3sJCoSOzysR9dBAyQHKe951Rcy9Ux0aTG%2Fnv1MRX30%2FMEs05WTsdnWMDispXpYRp1JnkUhkPfsTEj9R4RC0L5u2%2BXf%2FMoFZFCuey3yigSRB04F3TLH%2FJZWLxfdyikL7ArqzN6MhDbcjZOhE5AJkhIvedDDI3rfQBjqkAQW4QJySxmJV7cG5OR2xvR%2BQFByFRnBJqoBA2HMJ3bcfHi7ifyP4jkAEgwjJKY2YXjrzTPZxbpiN12H0llaynrOX%2FF%2FEPCvViHPi3CYRWAP1asrRbigL%2BrSNczcze6fNAGbbrfspszP6%2BQUN1LxBxzau13x6rGe7moWQGFc6cPw88Er9ZV5MaBCw0e8A0Gc2r7%2ByFpJ4tqNyTNg6pIq10m7hAb8x&X-Amz-Signature=ec4c68d2e2d255636b2eff5228d498b19aa33ded97026c12cab95cd7ee777856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZL77G3B2%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T180940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCm%2FpPend6vR6cYV3nwYCygTVfouHMsLjZhUEHpC2kaeQIhAKwV%2BKp%2BTVcYFYfG%2BauvA4lZW8cHTXYjF1E2JstOJrVlKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6B5bKF3qu388WO18q3ANACQBo3ZWNqKcKfqPORSWjVaazk3Fzut5YYt6CaL8aGi%2BJnLaodfjMI8RsH0IN5kvT59BotPzWGqkQ3BX3y1vEzrVI1wPYn%2FiHMnElm7gPMkxRREx5J3x0jrJc9SBdv11vG0VRlLawfvcf5ygiOGTGvG9hLFTLt3MEX7phKjxZtV%2FCUnW%2FHEUPt1J2vlyIFCN8zElDbB%2F60p63xZdO9nOBsQsZxDRrEZksH8YIqBWG0NoLD2ElosdTblN%2Ff6U9g9cwZfuBlSwcU1cDEAH0HW0xCpPuDUJJyaXrDQPn0sfnaFrDgzUsAKlHec%2BFSd7%2B8N040yjS9j5qRUwvamypE9n3LEDxP85ZcZ8E4j6til46Vt6pSF0wz8t9MNJC2c681MabX5W3f9nooq6fZeD9NgO9zFJaH8KXlGec6HUkHtioGM2sOVVFS0MU8x72jN1CSkkPhj6x3mNXGkMva9hxgIHMxuzhL9vLkku%2BZ3sJCoSOzysR9dBAyQHKe951Rcy9Ux0aTG%2Fnv1MRX30%2FMEs05WTsdnWMDispXpYRp1JnkUhkPfsTEj9R4RC0L5u2%2BXf%2FMoFZFCuey3yigSRB04F3TLH%2FJZWLxfdyikL7ArqzN6MhDbcjZOhE5AJkhIvedDDI3rfQBjqkAQW4QJySxmJV7cG5OR2xvR%2BQFByFRnBJqoBA2HMJ3bcfHi7ifyP4jkAEgwjJKY2YXjrzTPZxbpiN12H0llaynrOX%2FF%2FEPCvViHPi3CYRWAP1asrRbigL%2BrSNczcze6fNAGbbrfspszP6%2BQUN1LxBxzau13x6rGe7moWQGFc6cPw88Er9ZV5MaBCw0e8A0Gc2r7%2ByFpJ4tqNyTNg6pIq10m7hAb8x&X-Amz-Signature=f60f28d9097e48961ee995046d777cfa18998dc7829432229f612152591514ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
