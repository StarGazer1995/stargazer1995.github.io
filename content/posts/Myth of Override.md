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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMMEPNG5%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T233409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf2PwD8NPKyaS1eWvQOaBUqf3vzhn9CLcyP2Tn2zOuZwIhAPtkpzzyQGPvOOVXfC%2Fujk9eL6iEyZ6IbiJbYMcZtpoiKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyN39L20sUxNkwGaEwq3ANO9amVvPmwCR67NN%2Byf71ayxOB4QwwhVOUgwYdq0wvNXmgY%2FOyZGg%2B9w2IrXGDwBthtkTKqObmPb4KPCKbgWaRgpguyMR29fAGtx231nNMqAodiRt21wyh%2Bm6%2Fc7jvBWhzZe7ZxkTX118ctyO4BdhcItoM1pLN1Hz%2B1Xr9aSMrNi8gXz2qoHWf5IlhLTgTod8enZtlCyLg%2BBv1Sox1dPVROTa222Arv3WIuQrHifTgjlFxqKeOSQQCIfvXX1L8hXk4CyFHCT1D1thipWIAY4A2dFSU81U1ubojtqNDhYg%2FVurA9DUNm1Bt8HL3i4KH6TYxaHoUeOyo1SMkg6fv%2Bn2r0XLe3ASl6QTDvKita7Y0tIb85BA%2BJQi5HQVZqU4HDsCfIjVfGZnE%2B9%2B53J4JXY%2BTNF5xJU2oUYCEdIRTHoeseZj6My4uG8apsAFAYyEdmk%2FtJNWtlb%2BhPpZ3ZB4TU6OET0nQXrlaXE2mwNctcUPxusQdemnirMcpKwDPxMz%2BkshK6olfMQTJE2jqd%2BDMVKf1LB%2FsL7m23L%2Fb1ZQBIua24p3mOVcheGuWsSRazJwKUkKdrrW1moM%2F2kFJr9C%2Fr%2BUKsVLRQPEn9Bj476o7XYn0izAie5GN1HrDKbw5VjDa6OjPBjqkAcKpf6bOWU6bwclTqR6b6GB3LawwoZyEc06bNfD5SVdEecP7ke2hNikFHsfNV3HkHWr1%2FT276VMd2HuSOOxoZ74tfh0gp%2B03qbBmxStBYe%2F%2FQgAXFExBf23heATqFnlJj0czjFHv9la2sRk65%2B5E0c58pOEeRLl30J6D3wgtmclhaR39Tf5thF1FTDB49BBl69EfO22BmBmrbRU901W63ajDYkql&X-Amz-Signature=a5e805483d7003dbee89ab2ab11730ccab56772e2e7a7d90414fbe5f668b543f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMMEPNG5%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T233409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf2PwD8NPKyaS1eWvQOaBUqf3vzhn9CLcyP2Tn2zOuZwIhAPtkpzzyQGPvOOVXfC%2Fujk9eL6iEyZ6IbiJbYMcZtpoiKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyN39L20sUxNkwGaEwq3ANO9amVvPmwCR67NN%2Byf71ayxOB4QwwhVOUgwYdq0wvNXmgY%2FOyZGg%2B9w2IrXGDwBthtkTKqObmPb4KPCKbgWaRgpguyMR29fAGtx231nNMqAodiRt21wyh%2Bm6%2Fc7jvBWhzZe7ZxkTX118ctyO4BdhcItoM1pLN1Hz%2B1Xr9aSMrNi8gXz2qoHWf5IlhLTgTod8enZtlCyLg%2BBv1Sox1dPVROTa222Arv3WIuQrHifTgjlFxqKeOSQQCIfvXX1L8hXk4CyFHCT1D1thipWIAY4A2dFSU81U1ubojtqNDhYg%2FVurA9DUNm1Bt8HL3i4KH6TYxaHoUeOyo1SMkg6fv%2Bn2r0XLe3ASl6QTDvKita7Y0tIb85BA%2BJQi5HQVZqU4HDsCfIjVfGZnE%2B9%2B53J4JXY%2BTNF5xJU2oUYCEdIRTHoeseZj6My4uG8apsAFAYyEdmk%2FtJNWtlb%2BhPpZ3ZB4TU6OET0nQXrlaXE2mwNctcUPxusQdemnirMcpKwDPxMz%2BkshK6olfMQTJE2jqd%2BDMVKf1LB%2FsL7m23L%2Fb1ZQBIua24p3mOVcheGuWsSRazJwKUkKdrrW1moM%2F2kFJr9C%2Fr%2BUKsVLRQPEn9Bj476o7XYn0izAie5GN1HrDKbw5VjDa6OjPBjqkAcKpf6bOWU6bwclTqR6b6GB3LawwoZyEc06bNfD5SVdEecP7ke2hNikFHsfNV3HkHWr1%2FT276VMd2HuSOOxoZ74tfh0gp%2B03qbBmxStBYe%2F%2FQgAXFExBf23heATqFnlJj0czjFHv9la2sRk65%2B5E0c58pOEeRLl30J6D3wgtmclhaR39Tf5thF1FTDB49BBl69EfO22BmBmrbRU901W63ajDYkql&X-Amz-Signature=f2a40f0b0bc8dc5c11e40b087741c98af54756f67cc5c2a04e4a37926df1e4cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
