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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV5TSDUC%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T195936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLGFMjKuNRtcMRVH6tmWE7kt3m23Gdvon60HdxfjF4jAiEAkEjL7Lun6u3qtMESy0%2BnFL2rp1BtcWcsFQgytT85J6gqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEm5YtTnyD9gLNFRxSrcAy3jNDScDTSM2tPMBaGUI131b35lN5x7AhB71LjVqBo%2BTgGif8Dw%2FEg20HU0j8iV5Z2Q7t5yOMxEmWBXC5LsgK1h40NDWfW9Ys7hQBBGiOrOL9VNp5e%2BQXj03MHTA4dqf1UgQrBbCChjGkN1Bc6ksGPOUjhUSJVgbdekTVOZgYJAk4BIHbinjWv7XOFoANbacWLOjAjo3E1DCPJZcDNiyF7uzOm6munuMzhR1gMv8R9ME8C4zCLugGaxA396fuBsY%2BCRIcaqxNwxkYx2jlIJ9eNFByfCBKpt2gwjvRtgPA5UcUmPuR5pt%2Fw9TtpIqp6uHWxfQTKi8pZpfp5d9Anr56SgcK1HWyEa3DiTpuXokLW32KPrhEokKdczd871yj2ohOeMYer54qSAWkHCyIwUp0naswJAodGBt9c5nSV92oVYiS70SuDt73W1RvTZr42IEOEope8%2BSK605ibTsvDfuPBpAFQsirErxVLNREAjVpXbXWQ6BSaNnL0B9ryVm2QEDdijFuUQMyF7p7zlmPyy7D9vK640%2Bwn6zn2L75datB9dNDM8OzsOt%2ByNeDd4b%2F01XiTy7Z1zpY2iAzNgrM9RwDqd50JQjQnHQB77j31x3c2M4trl%2B8LzffbFv0ICMI36m9EGOqUBW4E1DDrAsqDisiE%2FeTY4m98PpMm1TrSLpnPeOzjG5tLI61cqTNNeX36bCoFwUqA8lIwKBvm%2F7LkaRG8e7TQOBUqC6AgTzjdsAAdQWZCBGl0JDSR9QDBMJaTsFE%2BxiERYRRyiaphbSxmt3qU3UWv4GFuJXt94diWjrSkGi%2BiVHW9JLjSA8zsIyvJ1C%2BRpKc1S5yPiI3W7HeyTtx2pG6vvmVUYMD57&X-Amz-Signature=800214df162736e17e7b74ec192dba9c91d41581cbb44b27666f95f3e64cd1cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV5TSDUC%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T195936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLGFMjKuNRtcMRVH6tmWE7kt3m23Gdvon60HdxfjF4jAiEAkEjL7Lun6u3qtMESy0%2BnFL2rp1BtcWcsFQgytT85J6gqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEm5YtTnyD9gLNFRxSrcAy3jNDScDTSM2tPMBaGUI131b35lN5x7AhB71LjVqBo%2BTgGif8Dw%2FEg20HU0j8iV5Z2Q7t5yOMxEmWBXC5LsgK1h40NDWfW9Ys7hQBBGiOrOL9VNp5e%2BQXj03MHTA4dqf1UgQrBbCChjGkN1Bc6ksGPOUjhUSJVgbdekTVOZgYJAk4BIHbinjWv7XOFoANbacWLOjAjo3E1DCPJZcDNiyF7uzOm6munuMzhR1gMv8R9ME8C4zCLugGaxA396fuBsY%2BCRIcaqxNwxkYx2jlIJ9eNFByfCBKpt2gwjvRtgPA5UcUmPuR5pt%2Fw9TtpIqp6uHWxfQTKi8pZpfp5d9Anr56SgcK1HWyEa3DiTpuXokLW32KPrhEokKdczd871yj2ohOeMYer54qSAWkHCyIwUp0naswJAodGBt9c5nSV92oVYiS70SuDt73W1RvTZr42IEOEope8%2BSK605ibTsvDfuPBpAFQsirErxVLNREAjVpXbXWQ6BSaNnL0B9ryVm2QEDdijFuUQMyF7p7zlmPyy7D9vK640%2Bwn6zn2L75datB9dNDM8OzsOt%2ByNeDd4b%2F01XiTy7Z1zpY2iAzNgrM9RwDqd50JQjQnHQB77j31x3c2M4trl%2B8LzffbFv0ICMI36m9EGOqUBW4E1DDrAsqDisiE%2FeTY4m98PpMm1TrSLpnPeOzjG5tLI61cqTNNeX36bCoFwUqA8lIwKBvm%2F7LkaRG8e7TQOBUqC6AgTzjdsAAdQWZCBGl0JDSR9QDBMJaTsFE%2BxiERYRRyiaphbSxmt3qU3UWv4GFuJXt94diWjrSkGi%2BiVHW9JLjSA8zsIyvJ1C%2BRpKc1S5yPiI3W7HeyTtx2pG6vvmVUYMD57&X-Amz-Signature=4ab8dc41665df69ca9bdfb6998b13809cc599b226407790e3a6d7bc8c4ae4331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
