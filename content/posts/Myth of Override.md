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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKB3HZEM%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T224651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFsDrtHAITevvpXeZCIqJR1fIzZplPQeLKmAjfPeGc5wIgSFfZjpSW4IDYlZOU2yb3AOO41%2FKszole1h5HUnhot7YqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNM0pI06FZMRc8vBSrcA2ih7Bf3h6qsbhq3q37ZaP9DcyeIndzZJrOM6E8WTa56t9lvzUCFkN7oGBDdVPeOOiC%2BZBwc1F2X%2Fobp%2BEzFK%2BiApHFhW%2F7QALkHCTSUkhoLkkZ6fLkCtKEqff0mrhp3%2BGjP%2B8hI9GbO7pqHcT%2BdQr2vQPv7O9Dtny0iKeO2GxRXJZTv0QLYyheIdqL3X%2Fl9SDNVcr1PduQhldqRty%2FnCeaXgyIAravWDwtTJMOpzSJhp4d9O0TqsK%2BUOd6XXpcqq1bp6sH6NBhRTOzBrqA%2BNpgr5s2u1p7P4haROKAiGC%2FsiPAfWwtIsiAlHu4j3FBlYrsDZawH4628psCwxaWYrMyxHuulRajCK8sMHu4jPmu1%2BKT36shVToECMFvU6G7cEb9CHOL%2BNgI4vZ2T%2B2kUNFxPIe7uxdGX65YN8Flj1mu2idNtjWi6jwMxXrrYOLVYlsbyMUVwFHUQRx3C%2B9stUr%2Bh9PhKHJEY%2B5SoWmmNTDojvkuwmGskt%2B5gWpQrXvmdj9jspFdvFvtC55wYmwQ5yxYI1mXO%2BPSLw43IWEwusIpeBAp5mlRi%2BB5dIaX%2BNG6KKAD%2FOq1rIZ%2FBrlMU0zfUnQK5fU92HpvjKuRHvVvCTF2rR1qSPCzpS7sZPisOMOD8qdMGOqUB1Ljp3WPehW4S5hQRQwS3%2FYZaGeQo8hPTcJKB4dKnBuHNYbE8lMaDh0Tr%2FUvAFM0uemc0tWo0wVD%2BfqHcYyDT68jocEkl7LiNzx2v0vP%2BBEdvP8yfyoAEZ0c662tJRUefb9EPG%2Ba9RyuHAV8zJU%2BRiV3Uk5CORgK8tvInMzSsRUxpCCHpUOLNwKp5MbAFZ05j4PA%2B6XZZYJ1VilWhOO3XsKerN21Z&X-Amz-Signature=3cb279e18d3e506878fa6ab491b94d99c23af932127ae9518eae6c298559d448&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKB3HZEM%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T224651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFsDrtHAITevvpXeZCIqJR1fIzZplPQeLKmAjfPeGc5wIgSFfZjpSW4IDYlZOU2yb3AOO41%2FKszole1h5HUnhot7YqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNM0pI06FZMRc8vBSrcA2ih7Bf3h6qsbhq3q37ZaP9DcyeIndzZJrOM6E8WTa56t9lvzUCFkN7oGBDdVPeOOiC%2BZBwc1F2X%2Fobp%2BEzFK%2BiApHFhW%2F7QALkHCTSUkhoLkkZ6fLkCtKEqff0mrhp3%2BGjP%2B8hI9GbO7pqHcT%2BdQr2vQPv7O9Dtny0iKeO2GxRXJZTv0QLYyheIdqL3X%2Fl9SDNVcr1PduQhldqRty%2FnCeaXgyIAravWDwtTJMOpzSJhp4d9O0TqsK%2BUOd6XXpcqq1bp6sH6NBhRTOzBrqA%2BNpgr5s2u1p7P4haROKAiGC%2FsiPAfWwtIsiAlHu4j3FBlYrsDZawH4628psCwxaWYrMyxHuulRajCK8sMHu4jPmu1%2BKT36shVToECMFvU6G7cEb9CHOL%2BNgI4vZ2T%2B2kUNFxPIe7uxdGX65YN8Flj1mu2idNtjWi6jwMxXrrYOLVYlsbyMUVwFHUQRx3C%2B9stUr%2Bh9PhKHJEY%2B5SoWmmNTDojvkuwmGskt%2B5gWpQrXvmdj9jspFdvFvtC55wYmwQ5yxYI1mXO%2BPSLw43IWEwusIpeBAp5mlRi%2BB5dIaX%2BNG6KKAD%2FOq1rIZ%2FBrlMU0zfUnQK5fU92HpvjKuRHvVvCTF2rR1qSPCzpS7sZPisOMOD8qdMGOqUB1Ljp3WPehW4S5hQRQwS3%2FYZaGeQo8hPTcJKB4dKnBuHNYbE8lMaDh0Tr%2FUvAFM0uemc0tWo0wVD%2BfqHcYyDT68jocEkl7LiNzx2v0vP%2BBEdvP8yfyoAEZ0c662tJRUefb9EPG%2Ba9RyuHAV8zJU%2BRiV3Uk5CORgK8tvInMzSsRUxpCCHpUOLNwKp5MbAFZ05j4PA%2B6XZZYJ1VilWhOO3XsKerN21Z&X-Amz-Signature=5a947beaa307101f35b6daa64017cc94945dffee0603902a77306579a71c4efa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
