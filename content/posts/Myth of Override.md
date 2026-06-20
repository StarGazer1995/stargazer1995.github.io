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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPGJGBSM%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T152853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIE8xtKhWZZvUo8JE2O6H5W5ca2D%2FhFKMNO15ZdPy%2FAgFAiEA6jr4ka%2FKc6r3YdgJ0E5CfoUAso0jc%2BR%2BHp7im5wzq64qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDPEVG8ZwawSFvJN4ircA7GxmUJ0jLrLIEYcUBjpECamrW6Vj1E5QlYktRRPS7QfMA11OnWKRkB3U8LQZ%2Fq48Sx60AXS451fF897E3uNa1RPhklMG38WiC1MHArAL6juW5gdMLMyJJ16iSOU05Fo7Q6eqkOwOiLHH6ToOxruIiBQAinmfmuGNQfk3iHtFqGSUPSHcEDRPpFm76NlGpS2DUh0%2FtTbhGBFCC0yQusEB9aDNxeLwUkN4vdvnjYrNcmiX8xPFIx8sdBkCIVXyq3o2Uy9M9vv7zD4aY8PrqpZ2EBr5t9xwHUqKPjQB2NSy5L%2FKaO8a4LWQzkve0MKLUWeYukIp4pnq9ay8ZtovY6oHVjSuSMlGz1kD63U3OlDBz1PNrTPkPGfxO6CDoHPQtB1O8iBNMpDju6FWPOQwW6z%2BIeFIzyLyht%2Bg1fEp5cRHXSQz2YewSQCm%2B5SIRy4LuT2OfpPZZZpJXRCyB9SIt0n4lLoZN2qxDdgdd%2Ft28oEa%2FH%2BsI3yZLb6NrAmMzOMkMd3bgeFUvRa6XtpNTbabrjM4kLy4yG77Sg0RzMr4fFna8Ew3r4KxpJF6SZAy%2FI8vXNrSLmXwh1bKkXPGOMji%2BSCYGEq4iE7Ip2VLW4TXEk20Ct0N7D%2BwNyuQ7m%2B4CVxMOTp2dEGOqUBUumjWKENOkwH9DuhhTEmwCr73rfAjiHXKEsRVu%2BaeCAfdOtbdOl4L5KhGicGfmFTHwq66N1mG5El8g7zghttS4kQyCunYKpuDinXnFtdHWorxcVlHkuNt1QDu3b7QhavlI3mB2nKmDzt7lwe5gH8FpWKqnjqiGWGKeZ%2B4BqXwiSHeeaW2RdXkJtONry7JWGKG5%2B4N2hEwGJXViTb53C4YggxAQo7&X-Amz-Signature=3a7b0c2273d099308c73faecffd8fb5a4a868631822740dfee9cfcff5b8a426a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPGJGBSM%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T152853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIE8xtKhWZZvUo8JE2O6H5W5ca2D%2FhFKMNO15ZdPy%2FAgFAiEA6jr4ka%2FKc6r3YdgJ0E5CfoUAso0jc%2BR%2BHp7im5wzq64qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDPEVG8ZwawSFvJN4ircA7GxmUJ0jLrLIEYcUBjpECamrW6Vj1E5QlYktRRPS7QfMA11OnWKRkB3U8LQZ%2Fq48Sx60AXS451fF897E3uNa1RPhklMG38WiC1MHArAL6juW5gdMLMyJJ16iSOU05Fo7Q6eqkOwOiLHH6ToOxruIiBQAinmfmuGNQfk3iHtFqGSUPSHcEDRPpFm76NlGpS2DUh0%2FtTbhGBFCC0yQusEB9aDNxeLwUkN4vdvnjYrNcmiX8xPFIx8sdBkCIVXyq3o2Uy9M9vv7zD4aY8PrqpZ2EBr5t9xwHUqKPjQB2NSy5L%2FKaO8a4LWQzkve0MKLUWeYukIp4pnq9ay8ZtovY6oHVjSuSMlGz1kD63U3OlDBz1PNrTPkPGfxO6CDoHPQtB1O8iBNMpDju6FWPOQwW6z%2BIeFIzyLyht%2Bg1fEp5cRHXSQz2YewSQCm%2B5SIRy4LuT2OfpPZZZpJXRCyB9SIt0n4lLoZN2qxDdgdd%2Ft28oEa%2FH%2BsI3yZLb6NrAmMzOMkMd3bgeFUvRa6XtpNTbabrjM4kLy4yG77Sg0RzMr4fFna8Ew3r4KxpJF6SZAy%2FI8vXNrSLmXwh1bKkXPGOMji%2BSCYGEq4iE7Ip2VLW4TXEk20Ct0N7D%2BwNyuQ7m%2B4CVxMOTp2dEGOqUBUumjWKENOkwH9DuhhTEmwCr73rfAjiHXKEsRVu%2BaeCAfdOtbdOl4L5KhGicGfmFTHwq66N1mG5El8g7zghttS4kQyCunYKpuDinXnFtdHWorxcVlHkuNt1QDu3b7QhavlI3mB2nKmDzt7lwe5gH8FpWKqnjqiGWGKeZ%2B4BqXwiSHeeaW2RdXkJtONry7JWGKG5%2B4N2hEwGJXViTb53C4YggxAQo7&X-Amz-Signature=9e31c6d8f0cb88d27c2549d4c792f0799156c6c270b70494029b7d7ddf3eb514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
