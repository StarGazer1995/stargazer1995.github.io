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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I2TXU6N%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T191113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICfaMapyFPPqkS3ebOJkGbU2bAH1NpfcmyxObsS30OKWAiEAqZuyGqjBk7tl92vxjReaT4yS6fBBWuSud38PqH2ldaIq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLTDlBR3zmNMu48G1ircAwieZ6qo3AAZESFUdqbvNIPSf85dTbhexCYaSz3Xw1JLWcfJ9AkevHhRThnT4UpANRYl4QAscgoEWGqtQCVwOwBWO5BbyTzK6Hpd%2Fgvn3SEuKu1E5tCTHJ9rXihckRQ%2B9tlp2jut7A1Orzglyu%2FE330cRtLwfthaFl4Abqe1JL%2BYH%2BlOHjE7efIs0MGl7D86Vd2cJSEcOre%2BD4h0ClCqWdGOJUXFtADseSRue2hMr2UeEXVvBIl2AIynJ33R9xUefgMGGHSTpSd7b%2BJfIi4hy1VLv8ysAKZ01A8Pkkc7r7YL9ye1ETOgu00qW0craBsfL8dBD4%2FdusxmMsV2CXo8gX0dMickJvn8uIgjW%2By0%2BWQqF8iTfMhg6EYbp%2BhNfeY5pRQCHbwirYzAw2JRZt1l4k5LSCzTPiovqLmhus5%2Btc3xqHuU0UYBtIdtiuj37%2BpfUuehZNtOsNk9dZQwM86AXLp1c5raQGgCnDs8FonazWZVGNKzsZfzTtUPIknTbwD0KD6jIY6XyLy5kLZuIPWpiJKGqr8Ti7flaRu13AcS1AWn8mnwGfR4l7DfiFF1c8FxVZK3eH6wijGRrArndVEoaNm5enkDWnGvibKg1TBAxqCKyKgBexHCVqM2AO%2FZMNaAztMGOqUB0WJxlC%2B9HhUJvxXkkOCTaYJ4n1CwB5ZxpBWeCgeQJsaTYdUziHJsJxIMmKSamGdHwNh7rEO3RAdVvMPdQHpketvu%2FkMQ5L5Qoib166oj33Lc1tbxBbBUyKT%2Bz%2BeofRgP6iJVKe2piZQ96FiieTUgvUZU4HZMqHW4WhWEYh10Lwjy8jSd6Y%2B%2FrAle05d2XQ2k8JNKHWqcPCCCN%2BLrbbz0gCWGYpYd&X-Amz-Signature=217fd7d842c7ff07a3f5e3ebabfba93d3f720504e5e237d33b18ce52105e6dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I2TXU6N%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T191113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICfaMapyFPPqkS3ebOJkGbU2bAH1NpfcmyxObsS30OKWAiEAqZuyGqjBk7tl92vxjReaT4yS6fBBWuSud38PqH2ldaIq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLTDlBR3zmNMu48G1ircAwieZ6qo3AAZESFUdqbvNIPSf85dTbhexCYaSz3Xw1JLWcfJ9AkevHhRThnT4UpANRYl4QAscgoEWGqtQCVwOwBWO5BbyTzK6Hpd%2Fgvn3SEuKu1E5tCTHJ9rXihckRQ%2B9tlp2jut7A1Orzglyu%2FE330cRtLwfthaFl4Abqe1JL%2BYH%2BlOHjE7efIs0MGl7D86Vd2cJSEcOre%2BD4h0ClCqWdGOJUXFtADseSRue2hMr2UeEXVvBIl2AIynJ33R9xUefgMGGHSTpSd7b%2BJfIi4hy1VLv8ysAKZ01A8Pkkc7r7YL9ye1ETOgu00qW0craBsfL8dBD4%2FdusxmMsV2CXo8gX0dMickJvn8uIgjW%2By0%2BWQqF8iTfMhg6EYbp%2BhNfeY5pRQCHbwirYzAw2JRZt1l4k5LSCzTPiovqLmhus5%2Btc3xqHuU0UYBtIdtiuj37%2BpfUuehZNtOsNk9dZQwM86AXLp1c5raQGgCnDs8FonazWZVGNKzsZfzTtUPIknTbwD0KD6jIY6XyLy5kLZuIPWpiJKGqr8Ti7flaRu13AcS1AWn8mnwGfR4l7DfiFF1c8FxVZK3eH6wijGRrArndVEoaNm5enkDWnGvibKg1TBAxqCKyKgBexHCVqM2AO%2FZMNaAztMGOqUB0WJxlC%2B9HhUJvxXkkOCTaYJ4n1CwB5ZxpBWeCgeQJsaTYdUziHJsJxIMmKSamGdHwNh7rEO3RAdVvMPdQHpketvu%2FkMQ5L5Qoib166oj33Lc1tbxBbBUyKT%2Bz%2BeofRgP6iJVKe2piZQ96FiieTUgvUZU4HZMqHW4WhWEYh10Lwjy8jSd6Y%2B%2FrAle05d2XQ2k8JNKHWqcPCCCN%2BLrbbz0gCWGYpYd&X-Amz-Signature=f0c0b11f518bf98c5a182ecb1cad26451cb0162ba7942cb72acc0521925c3229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
