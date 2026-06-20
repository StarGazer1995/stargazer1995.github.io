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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633HDV3EF%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T102527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIF1XmdKP%2Bqgmt8mCneRCPUUgOChnZdNyhJlmWD%2BlO4khAiEAontEq5vS%2FOhZHdnj5ln7maDwOBWEhhda6lafCX6CvwIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCsktZZSDcNe6isBaircAy9cG4bMDatYIBJSU5USE%2BtCz%2FLww1z6V9YA%2BgDdKH4%2BYIQg1QFXYJ%2BBw3KPAOYDCpapY%2FxZ4sdAuhrPESa%2Bzb6rcIDGu4ZGe9%2FpYCnHrBYub9LJjrhNOHXT58a%2Fng7Ce5hf22XBT9azdg0McO7GokEbrKMJ5gYfdo6Rck2aPAXS%2FoMYIQVW4W0mdl3f9TnHLCcuBCA9hwiXjRk1x%2FhIzY%2FL8g%2F8JTIsA2pBBqZRhS9ZTfmDyrvBl4as41UKET9vLe02AZAhjt4eeBGszGV6pVAW7U%2FVhJuBzHNoCp1mM1xQNDtRFdnRdIEuM7HWHcIiEjTaB%2FLHmtvaP6Q%2BKgt3SH5CpylwGHKdcczkd21uVxZIosDNad%2BbeitUa6KoQHLF3895dbcnLO5t8Zg3Ih1FDoPmIpDlKGhbPdirFEk%2FKtvBDIDq4UEmIBYt6tD%2Fj2MEdlGbeko9Ya6GxeS55%2FeS7TwNgigQUnLjHliZ70TfiRgCA7yO%2Bms%2B3mCwvv6eTVafCpi%2BBDHI033oG98o69FCRR4%2BDzAP24RRFwkgKa%2Fz2qqxuE54HtqLT%2FW3%2Bbf0kreTFICD1NJAGcl6MGzAHMXMvFGPgWrAcBkN0IVmiPwnUSe88i1TvVPENitzZI2OMNfD2dEGOqUBzFoaOAiViy2g5zcgnMpDhXHWNy9y3znZWJKzo8F6EpyqkGUlPzIgVqCBVZs4bz8CvSFgeyqHYZIp5HFEkstej4C7%2B1bBEAud%2Bi0Fl1oxOGMq7dI3ZmHV1B1gJBsUwMg%2BmDeZEH8VL7HEDa7ZftKLw0%2FYsCPppUfDYMI%2Fwi2zUGEPWCbEm2310k9u8qVASBmztNE4RQdLqGzjsTiqunsWxZBAiLAA&X-Amz-Signature=8ea8d4bd0793fb04d254d763a3ddef0beae460053a1bb8227b9d992673913774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633HDV3EF%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T102527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIF1XmdKP%2Bqgmt8mCneRCPUUgOChnZdNyhJlmWD%2BlO4khAiEAontEq5vS%2FOhZHdnj5ln7maDwOBWEhhda6lafCX6CvwIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCsktZZSDcNe6isBaircAy9cG4bMDatYIBJSU5USE%2BtCz%2FLww1z6V9YA%2BgDdKH4%2BYIQg1QFXYJ%2BBw3KPAOYDCpapY%2FxZ4sdAuhrPESa%2Bzb6rcIDGu4ZGe9%2FpYCnHrBYub9LJjrhNOHXT58a%2Fng7Ce5hf22XBT9azdg0McO7GokEbrKMJ5gYfdo6Rck2aPAXS%2FoMYIQVW4W0mdl3f9TnHLCcuBCA9hwiXjRk1x%2FhIzY%2FL8g%2F8JTIsA2pBBqZRhS9ZTfmDyrvBl4as41UKET9vLe02AZAhjt4eeBGszGV6pVAW7U%2FVhJuBzHNoCp1mM1xQNDtRFdnRdIEuM7HWHcIiEjTaB%2FLHmtvaP6Q%2BKgt3SH5CpylwGHKdcczkd21uVxZIosDNad%2BbeitUa6KoQHLF3895dbcnLO5t8Zg3Ih1FDoPmIpDlKGhbPdirFEk%2FKtvBDIDq4UEmIBYt6tD%2Fj2MEdlGbeko9Ya6GxeS55%2FeS7TwNgigQUnLjHliZ70TfiRgCA7yO%2Bms%2B3mCwvv6eTVafCpi%2BBDHI033oG98o69FCRR4%2BDzAP24RRFwkgKa%2Fz2qqxuE54HtqLT%2FW3%2Bbf0kreTFICD1NJAGcl6MGzAHMXMvFGPgWrAcBkN0IVmiPwnUSe88i1TvVPENitzZI2OMNfD2dEGOqUBzFoaOAiViy2g5zcgnMpDhXHWNy9y3znZWJKzo8F6EpyqkGUlPzIgVqCBVZs4bz8CvSFgeyqHYZIp5HFEkstej4C7%2B1bBEAud%2Bi0Fl1oxOGMq7dI3ZmHV1B1gJBsUwMg%2BmDeZEH8VL7HEDa7ZftKLw0%2FYsCPppUfDYMI%2Fwi2zUGEPWCbEm2310k9u8qVASBmztNE4RQdLqGzjsTiqunsWxZBAiLAA&X-Amz-Signature=32ddd4028ef01f3077c24a8b85f9f641e3dc2a46594f23b95d2213bd42508e48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
