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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZZRPEOW%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T025627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIFdWA5V5AqyBqQLH9ZJMW8a3zZUJlVZKgiWVOpd%2B5C1JAiEAkBR1qLlLA5J4ycRIprvQ4JxzVk2zHjszlWSsD%2FRvaL0q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDLiQcQ275u4mrG%2BWyircA28Evl8HmssYelQrSrr9%2FGuBaDfFK3n82bnXNBRXPdaRkR%2FAey54%2FaJu%2FeDeUD8URNYeF7s4ErXVzrzKpZn3D9owSh3PBxW%2Bq47zGytXbleQQqcTlIY85OgZ0Vj%2BrBU2FTXWag9%2Bqj1A0qxlrFX3u%2F2EUHE2hjP%2BJ5wJMMlMWip01QqYexVOcljCiXDiVDI8fBke79UzotuVZYWG0AmT6n5uWo7uoG1ZIG8tH1y7NO74OL1FptRDyuYgfhUJpkkh6A835Yh6M%2F8kEg5ZTE3o7bimyytHeDmW4x9L%2FlQ52SqOW08UZxJBDEo5lodJFKyIVnoLklNfHj38RYqu3NeWj1eBFRi1xq31u4LLcF6socFM%2BBuJSs302JzyVc1BQPJ7Ubpu8OFkUWKFTtPTDoa6VUt3d0aHjzhWRyTU27sAoZ29GZ0AwGhq479PwKdVgSKYpU8zJc5bR9t%2FTawIX6pVxXBoUALuYVoP%2B4ZuA9Hr%2Bx2UryK9k3Z8sguRlJ4vboIJ01hLQqL%2BFRNKn7ub0IBliWs7GKWWJQyFT1XMeQi50fMu%2B8xHmxbwCGvrR7ppFAigbnqiCQORzYGOR%2FtHlQB8eH3SgPpWR1Aka%2BPzO7a6r6k7QGLVKgZ4wTvJqLzoMIaUudQGOqUBSGAyh2mr2DQYJh1M2CPqvEsnKU44mmblTw5d4DPL8vDkAxgdMza1pi7O%2BwhwIXrGear74%2FX%2B0AD%2FO33Yv0vujxMpID6S%2FNwm9VU79mwlX4qmMShxjxmNm3kIHf7MSPuLZ%2BW0dOcVqOUHHBPnp0Jw9wxiLo9RFOQ6aTNu%2Fz6%2FnfXM2JyGih6QBY51Y8BQOJe1Zx7kVnEe%2F7Wh6AmkGnnF0uDn2hkJ&X-Amz-Signature=c1483d05835986b6da48dc09cded09c23aa8bd37f7b5beb5198a6b072bd73ea8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZZRPEOW%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T025627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIFdWA5V5AqyBqQLH9ZJMW8a3zZUJlVZKgiWVOpd%2B5C1JAiEAkBR1qLlLA5J4ycRIprvQ4JxzVk2zHjszlWSsD%2FRvaL0q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDLiQcQ275u4mrG%2BWyircA28Evl8HmssYelQrSrr9%2FGuBaDfFK3n82bnXNBRXPdaRkR%2FAey54%2FaJu%2FeDeUD8URNYeF7s4ErXVzrzKpZn3D9owSh3PBxW%2Bq47zGytXbleQQqcTlIY85OgZ0Vj%2BrBU2FTXWag9%2Bqj1A0qxlrFX3u%2F2EUHE2hjP%2BJ5wJMMlMWip01QqYexVOcljCiXDiVDI8fBke79UzotuVZYWG0AmT6n5uWo7uoG1ZIG8tH1y7NO74OL1FptRDyuYgfhUJpkkh6A835Yh6M%2F8kEg5ZTE3o7bimyytHeDmW4x9L%2FlQ52SqOW08UZxJBDEo5lodJFKyIVnoLklNfHj38RYqu3NeWj1eBFRi1xq31u4LLcF6socFM%2BBuJSs302JzyVc1BQPJ7Ubpu8OFkUWKFTtPTDoa6VUt3d0aHjzhWRyTU27sAoZ29GZ0AwGhq479PwKdVgSKYpU8zJc5bR9t%2FTawIX6pVxXBoUALuYVoP%2B4ZuA9Hr%2Bx2UryK9k3Z8sguRlJ4vboIJ01hLQqL%2BFRNKn7ub0IBliWs7GKWWJQyFT1XMeQi50fMu%2B8xHmxbwCGvrR7ppFAigbnqiCQORzYGOR%2FtHlQB8eH3SgPpWR1Aka%2BPzO7a6r6k7QGLVKgZ4wTvJqLzoMIaUudQGOqUBSGAyh2mr2DQYJh1M2CPqvEsnKU44mmblTw5d4DPL8vDkAxgdMza1pi7O%2BwhwIXrGear74%2FX%2B0AD%2FO33Yv0vujxMpID6S%2FNwm9VU79mwlX4qmMShxjxmNm3kIHf7MSPuLZ%2BW0dOcVqOUHHBPnp0Jw9wxiLo9RFOQ6aTNu%2Fz6%2FnfXM2JyGih6QBY51Y8BQOJe1Zx7kVnEe%2F7Wh6AmkGnnF0uDn2hkJ&X-Amz-Signature=b82fd65bc2d3378ca3eebda5716f4856411ceb8b2432190acd92f218e59faf4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
