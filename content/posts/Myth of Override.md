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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJD6ZW2G%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T130933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDbEfGAoSZHfoFCd5YxwKc9%2F%2Bmc3sl1i31kNpwgCTMnWgIhAPjJaE6petaKSkoNlHZNszDCY6QRsfSYoHAeO9usIfUmKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyefSVytozk3fRMtMcq3ANq7grv9cYiotUay0C7OOK7KnAiE4hQBFDtigowtHONW%2F8ySs5p%2FjEAxy5m6NRG7QibzBFbrTuqWhCGrrkjFrNl6%2B0Wz1%2BtxQ93hBzYENqaUaOoVdhrwwcZLMTeWnQSxM9TT18QEUy7Y5mnMkU%2FDL4vq%2BtdvmsDT8eG5Djxtpi0Oo54%2BF56iEIrN8ElFE033%2Bl2xEm6rb%2FTjyL9nUb4LNtE2sn3efozNLzlw5BUYy5GJXNf0B624aQ7ioTySW5%2BH78R8UCTWlM%2BBz8c4IM7tEpVrRkO%2BgSb6W0difYo0M9YCFZDOExl03JrJDSHTr4TrCxuuty17%2FqcyS5K3gZShnVnEAvx42HyszwkOET5inKpP2gSEBPhQJ5kxnz6kIsNk0gk9HyOkIxgulMQ%2F5Tdx1iyXfo4lFtswbER9W6mK%2F8O6v78%2Fj8lDGTyf3OFm4YqcK8D7wrRZzAEh%2Fs5C4CGezWasMyIU6GSB%2BTIGTv4z6M5Mxq%2BksUYe2PYLUwRxF6BngDycdnC7AJ9YfOafgKwSeOwm7yDmApleKzMG8A%2BKf120cS%2BXzTOUp9LWtQeyAGhq4ZLN64QFZqmDFA6npc%2F512v1LPUoe8ubBZGF94lT6AX%2FeWUCnNG35TuvAsOvzD%2Bi%2FDQBjqkAYYKCSvVQiBB77tLBuGNXyS98Tj9rE8COs6Riu4G7T%2FLufgu6JE2ae%2BF60C4%2B%2BmD5V4wOThfAp7GvVx49nhR7AN1iYTuPL6GG%2BC0KIMyT4Abz2rU3%2BY8Jv9xh%2BE3yBIuD41MBkU1wO62yyjLWVOCE%2BqPwg1vBCErU3U6e5cyxW%2FIMRr%2BMXE9UALAuxPL9CT1MFi1lvdCVXlUaUWGkbBBuIfPI0VG&X-Amz-Signature=fb33f746399387fd05a06c8541ebf3e38523f7a1b839ef85076fe963bfbe76da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJD6ZW2G%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T130933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDbEfGAoSZHfoFCd5YxwKc9%2F%2Bmc3sl1i31kNpwgCTMnWgIhAPjJaE6petaKSkoNlHZNszDCY6QRsfSYoHAeO9usIfUmKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyefSVytozk3fRMtMcq3ANq7grv9cYiotUay0C7OOK7KnAiE4hQBFDtigowtHONW%2F8ySs5p%2FjEAxy5m6NRG7QibzBFbrTuqWhCGrrkjFrNl6%2B0Wz1%2BtxQ93hBzYENqaUaOoVdhrwwcZLMTeWnQSxM9TT18QEUy7Y5mnMkU%2FDL4vq%2BtdvmsDT8eG5Djxtpi0Oo54%2BF56iEIrN8ElFE033%2Bl2xEm6rb%2FTjyL9nUb4LNtE2sn3efozNLzlw5BUYy5GJXNf0B624aQ7ioTySW5%2BH78R8UCTWlM%2BBz8c4IM7tEpVrRkO%2BgSb6W0difYo0M9YCFZDOExl03JrJDSHTr4TrCxuuty17%2FqcyS5K3gZShnVnEAvx42HyszwkOET5inKpP2gSEBPhQJ5kxnz6kIsNk0gk9HyOkIxgulMQ%2F5Tdx1iyXfo4lFtswbER9W6mK%2F8O6v78%2Fj8lDGTyf3OFm4YqcK8D7wrRZzAEh%2Fs5C4CGezWasMyIU6GSB%2BTIGTv4z6M5Mxq%2BksUYe2PYLUwRxF6BngDycdnC7AJ9YfOafgKwSeOwm7yDmApleKzMG8A%2BKf120cS%2BXzTOUp9LWtQeyAGhq4ZLN64QFZqmDFA6npc%2F512v1LPUoe8ubBZGF94lT6AX%2FeWUCnNG35TuvAsOvzD%2Bi%2FDQBjqkAYYKCSvVQiBB77tLBuGNXyS98Tj9rE8COs6Riu4G7T%2FLufgu6JE2ae%2BF60C4%2B%2BmD5V4wOThfAp7GvVx49nhR7AN1iYTuPL6GG%2BC0KIMyT4Abz2rU3%2BY8Jv9xh%2BE3yBIuD41MBkU1wO62yyjLWVOCE%2BqPwg1vBCErU3U6e5cyxW%2FIMRr%2BMXE9UALAuxPL9CT1MFi1lvdCVXlUaUWGkbBBuIfPI0VG&X-Amz-Signature=98ea8a9799123e2a2672b5b540ade44a8116e0a79a3ee97a116b96b0815557e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
