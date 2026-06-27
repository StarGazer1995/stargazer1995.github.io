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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH7Y4OMV%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T055112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCogXPdyEobk1ScjPJgV2vl4bs1vf6NFnKGkOFIhMHpeAIgZqn0SBC5b1TofQSZVy%2Fynbt7sQBRpy%2Bz%2BWqe1cYwkYgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHR1Ejm%2Fk0LtywTe9yrcA%2B6Zn5WnW%2BvjZJniGxpmPLVEIcQi8cc9fVbzhfvPUAi4O76yAxfQY3MGkIfkWlJXZwYwvv88ADMtkoZLwwH8Ji3iJZkwrUv2xsdu7Cx3OD%2BDSFgO5SkAjshxdkhY9qn3wUWCUdG9lyW%2FtdxKr0bIs2KXDlFW0byBBumMx6LcPJQamx%2FW5vDOTlXyXSET9KVK2Zu2VIANbjlnD2EpWYRUmKylvQ6H8NC1UpPl45B68z5%2Fsj3W%2BA5ztD3PXF8Z%2BOmGMtkFdr6zuHZyywojz8E9BhOKGx9U%2FAl9ZcSsDOnRivRFdVlYPxiY7Pgz92dsf%2F8RyAHHQHQGDHLwkG%2F%2ByLvi2aRv%2F6542ohyca4uY4JUw6%2BVpwE2KjDfkAVXT0vj9aZGtGD9uH5Y59QfD%2BXAAj4baEkbF%2BM%2BgxCg3eK4bxy37o7PkAXb6Ru6X4%2FjIBGhqU9%2FccrWtIW2iHbzniUuxq4xHsx6WUTQXwZMCwgM0tFX9gXCROFVgFC8QBwhHeSYCKabmCRQs4889K4Sv3%2FHe3hZl8ltZSVkmeXW33WXENXvmiTF3ns3vjYDSp9JQaT9M%2FTxVpVnofR7TM%2BaFwfrDGGjCGr%2Fyb8PVO9F9%2FchZWpdgRQfhKeNbsKSvLsncnQmMKGz%2FdEGOqUB5evWH2rOs4cvCkLq1qFDWqU%2FgdyhrVmkn%2ByRCDBYX9LQp1tQCdC3qEwBDvHKOKr2H3QUuPlDjCIJVChjJ5b5hBsA3zsSl73dG%2F8Sn%2B1Zl%2B6HObdjyJ6NEJRTVs1t6K5STcRdnr2riwB9HRz74HWNX%2B5sZbvher2eL%2BtCvdq3zoQqQwi6URRoOKYwmhZiiKetUODP%2FxeWkk8C4w5fIK3j57PDo%2Fp%2F&X-Amz-Signature=ee8ca07cc3cc28096f06226395831e8dbdf896d33549e999ffbb015b7d795634&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH7Y4OMV%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T055112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCogXPdyEobk1ScjPJgV2vl4bs1vf6NFnKGkOFIhMHpeAIgZqn0SBC5b1TofQSZVy%2Fynbt7sQBRpy%2Bz%2BWqe1cYwkYgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHR1Ejm%2Fk0LtywTe9yrcA%2B6Zn5WnW%2BvjZJniGxpmPLVEIcQi8cc9fVbzhfvPUAi4O76yAxfQY3MGkIfkWlJXZwYwvv88ADMtkoZLwwH8Ji3iJZkwrUv2xsdu7Cx3OD%2BDSFgO5SkAjshxdkhY9qn3wUWCUdG9lyW%2FtdxKr0bIs2KXDlFW0byBBumMx6LcPJQamx%2FW5vDOTlXyXSET9KVK2Zu2VIANbjlnD2EpWYRUmKylvQ6H8NC1UpPl45B68z5%2Fsj3W%2BA5ztD3PXF8Z%2BOmGMtkFdr6zuHZyywojz8E9BhOKGx9U%2FAl9ZcSsDOnRivRFdVlYPxiY7Pgz92dsf%2F8RyAHHQHQGDHLwkG%2F%2ByLvi2aRv%2F6542ohyca4uY4JUw6%2BVpwE2KjDfkAVXT0vj9aZGtGD9uH5Y59QfD%2BXAAj4baEkbF%2BM%2BgxCg3eK4bxy37o7PkAXb6Ru6X4%2FjIBGhqU9%2FccrWtIW2iHbzniUuxq4xHsx6WUTQXwZMCwgM0tFX9gXCROFVgFC8QBwhHeSYCKabmCRQs4889K4Sv3%2FHe3hZl8ltZSVkmeXW33WXENXvmiTF3ns3vjYDSp9JQaT9M%2FTxVpVnofR7TM%2BaFwfrDGGjCGr%2Fyb8PVO9F9%2FchZWpdgRQfhKeNbsKSvLsncnQmMKGz%2FdEGOqUB5evWH2rOs4cvCkLq1qFDWqU%2FgdyhrVmkn%2ByRCDBYX9LQp1tQCdC3qEwBDvHKOKr2H3QUuPlDjCIJVChjJ5b5hBsA3zsSl73dG%2F8Sn%2B1Zl%2B6HObdjyJ6NEJRTVs1t6K5STcRdnr2riwB9HRz74HWNX%2B5sZbvher2eL%2BtCvdq3zoQqQwi6URRoOKYwmhZiiKetUODP%2FxeWkk8C4w5fIK3j57PDo%2Fp%2F&X-Amz-Signature=a66f96bbbba6827ef2393d61b67972932496c4901a79be3b30a83fa81fc4f1b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
