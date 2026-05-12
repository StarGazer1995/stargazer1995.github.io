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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LUZOSZM%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIHWB2b1pxZJFMWdA2V0V%2FpgsLXx%2BzvrsPxuVYRsPNPxQAiEAoa3Hn2uRA30pjNQRdFkSVvG44%2BHJwPWriGR5kXM7LUwq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDNFsUPMfJig91Mwd3yrcA1LS9SQLlcjp%2BUJ6vdrruVrxYugXJGfBW6sGZkAYOsBtmQucCOQSEEZWlZVU2t6f2DPbxGTZaLp4aHzoL7QS%2FIAbL9Pa3GWPsrgp5O0snzkaGy0Gge4mIzHOIdlJ9alfEEFu81zmE7Zm4GTL6iYz4phOYdJVl7r8d5mpAwOGEx95HT15L3aYit8lCQKaQPhNRzzW2mN2odebANb2DaPGk0%2F6%2FQdkRm01%2FH7jocRaZiGiUXTR7fc8hWQeAXR6DMUwymjtGRjcd%2B%2B%2BXI%2FUW2ZEg81xTOQEGeDjAwAAacHOh21PDOCasYhgzJ6KkLb7EAW6O9IInPgYNQ9KwZzLpnz6jXj36Oa%2BfFwJc%2FafDOk5fdIg%2F1vfIQV1deOPPZoNLt%2FebTHyWFxanY44tALPFsow633LA4yqT%2BN1EdmR4aISuCcexBx8piBk4aLrqDgLYXmObuzkp%2Fwqxog7f9wPsLr4JCKs3LSb3JUb3OJrZyhIJg37%2Bj8Sk0lf7ERAwIr8dEU8AizmYAZmoaEt2e9oV4m1gP%2FSTDMkngYfmddQz%2BEWjnvvaJhEZfsaP2vha6Xh4GpVFb%2B9wUOQpEVFEX2l7Aawn9XoQ4bHtaYLk2QyAfqceL3kdf4on5sQ9hos9tB1MJLUjtAGOqUB39jpKzhISZtcoNCYsCoQW%2F%2FAfNbo%2FnhnXbRucSQaRP826JljK9VpYhnHl1mflWnEyAxX6UkcrE1QQ7aKVq6%2FAZrRFwmdRkZvi9BTsw6fC%2FKP2JWiINJILAU603IV9VL4Yu80NBgiaWFbrsInXHaGgEpzTDbs53s658%2FmkGec0JtR8UtdaWbN1l%2FlurBVrAlWZwBbShgJJdFtBSSKcvolKC%2BG2RPA&X-Amz-Signature=8fe28fb0e43a9508521fd172ca4326ea3c3165a89621b4a56e7e60ca94e64334&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LUZOSZM%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIHWB2b1pxZJFMWdA2V0V%2FpgsLXx%2BzvrsPxuVYRsPNPxQAiEAoa3Hn2uRA30pjNQRdFkSVvG44%2BHJwPWriGR5kXM7LUwq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDNFsUPMfJig91Mwd3yrcA1LS9SQLlcjp%2BUJ6vdrruVrxYugXJGfBW6sGZkAYOsBtmQucCOQSEEZWlZVU2t6f2DPbxGTZaLp4aHzoL7QS%2FIAbL9Pa3GWPsrgp5O0snzkaGy0Gge4mIzHOIdlJ9alfEEFu81zmE7Zm4GTL6iYz4phOYdJVl7r8d5mpAwOGEx95HT15L3aYit8lCQKaQPhNRzzW2mN2odebANb2DaPGk0%2F6%2FQdkRm01%2FH7jocRaZiGiUXTR7fc8hWQeAXR6DMUwymjtGRjcd%2B%2B%2BXI%2FUW2ZEg81xTOQEGeDjAwAAacHOh21PDOCasYhgzJ6KkLb7EAW6O9IInPgYNQ9KwZzLpnz6jXj36Oa%2BfFwJc%2FafDOk5fdIg%2F1vfIQV1deOPPZoNLt%2FebTHyWFxanY44tALPFsow633LA4yqT%2BN1EdmR4aISuCcexBx8piBk4aLrqDgLYXmObuzkp%2Fwqxog7f9wPsLr4JCKs3LSb3JUb3OJrZyhIJg37%2Bj8Sk0lf7ERAwIr8dEU8AizmYAZmoaEt2e9oV4m1gP%2FSTDMkngYfmddQz%2BEWjnvvaJhEZfsaP2vha6Xh4GpVFb%2B9wUOQpEVFEX2l7Aawn9XoQ4bHtaYLk2QyAfqceL3kdf4on5sQ9hos9tB1MJLUjtAGOqUB39jpKzhISZtcoNCYsCoQW%2F%2FAfNbo%2FnhnXbRucSQaRP826JljK9VpYhnHl1mflWnEyAxX6UkcrE1QQ7aKVq6%2FAZrRFwmdRkZvi9BTsw6fC%2FKP2JWiINJILAU603IV9VL4Yu80NBgiaWFbrsInXHaGgEpzTDbs53s658%2FmkGec0JtR8UtdaWbN1l%2FlurBVrAlWZwBbShgJJdFtBSSKcvolKC%2BG2RPA&X-Amz-Signature=4b70232f59fa371cdb1c7f26b811fe3ce0bddcb244bb5939de03cf27443aad22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
