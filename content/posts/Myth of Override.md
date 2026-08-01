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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XK2FJHY4%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T013007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcGdGUJxuSI3Mj6PpjpnKhMYHXonTO%2BmGnQ%2FIkm6Z7BAIhAJzfqL%2B89JVzldFyDO2Sbp%2FynXVW7gLpor%2Fl6ezUwEryKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyDeohvwklFBqTUTQq3AOH%2F1PjQ8pyzcYpN8TH8RHFRMoY8H0P8oMeakkBtxs0%2FSYF5vQOfUNjQ8%2FBYXSeMqqf6SWvr8PJ63M1hyGYSKxNSq2y5qJAAbFe9OG6Se%2B0hoew6EeXj7fIyJltg9jzd1Db9b1KcSEq88Kffb%2FbCzLBGrkqfabvuZYHadUi%2F3S%2F7JyEaoQ%2FmmNBPhHXcnnEk5HTdgeJbRwIL%2Bz1rBHNxNKgtUuiaOT31o36%2F0d%2FcEHK5F6b728tIfil1hbm%2FMOc9thRjRB5MkMi%2F1qH30inaktNAt4v6PfDGVSeHtv9fe%2BT1sbuzzJnC8GJ73LZnjZzcSiBXNxBKDWSW6tRzElGi%2BKrRGu05Oi%2FcNebcoB9IF7bY13PkbKHNV1Uig2tSTSRDj8QSe9kW%2FnsB9A63kClxgDVjDpAXTNyhbCSu7t3FL2Dd6ZeQCIpAKBwf2ZzC%2FagFsoOMl6q8M7aYxWZebvVTtKU%2Bel7ZEj4DFoptSGRDPTYVhch8ecgYArnEINv1MdyluYc382GwPymg3H6v6ASYeYN8c4vDgCac2GiifKxNUOq3fFgwNFK9DemhbsGqDH1JPIwO77Xi60YIqNOeZhdPEL75edXRtG%2Bx3xJOEyJVHSJ3KNk1T%2B6BZRCfe53HzCSi7XTBjqkAbJ70iyrHLBYVtxnygi5%2FMeSI94g6gLCDQUhBayUjqWW%2F79Jmc8iAaPKjKH3TgyaywF70El0VZpnD%2FmQEcilY0z1Pey0UVCDCIRM%2BfwORfwb%2F%2Bjzz7h9PP4a009u1rMyBLSm9mFQtECwtIVRl9tAXxgN1ExtiqTUQ0s57mOSpnUvt94MRRR7EWeh7JLYt25db94FBv79%2BaWfi64cGocHGgEzBQ%2Bk&X-Amz-Signature=225b417f3dfef56dffa7d73e4324267e8204fd82a1601f94efa9a477a75f34e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XK2FJHY4%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T013007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcGdGUJxuSI3Mj6PpjpnKhMYHXonTO%2BmGnQ%2FIkm6Z7BAIhAJzfqL%2B89JVzldFyDO2Sbp%2FynXVW7gLpor%2Fl6ezUwEryKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyDeohvwklFBqTUTQq3AOH%2F1PjQ8pyzcYpN8TH8RHFRMoY8H0P8oMeakkBtxs0%2FSYF5vQOfUNjQ8%2FBYXSeMqqf6SWvr8PJ63M1hyGYSKxNSq2y5qJAAbFe9OG6Se%2B0hoew6EeXj7fIyJltg9jzd1Db9b1KcSEq88Kffb%2FbCzLBGrkqfabvuZYHadUi%2F3S%2F7JyEaoQ%2FmmNBPhHXcnnEk5HTdgeJbRwIL%2Bz1rBHNxNKgtUuiaOT31o36%2F0d%2FcEHK5F6b728tIfil1hbm%2FMOc9thRjRB5MkMi%2F1qH30inaktNAt4v6PfDGVSeHtv9fe%2BT1sbuzzJnC8GJ73LZnjZzcSiBXNxBKDWSW6tRzElGi%2BKrRGu05Oi%2FcNebcoB9IF7bY13PkbKHNV1Uig2tSTSRDj8QSe9kW%2FnsB9A63kClxgDVjDpAXTNyhbCSu7t3FL2Dd6ZeQCIpAKBwf2ZzC%2FagFsoOMl6q8M7aYxWZebvVTtKU%2Bel7ZEj4DFoptSGRDPTYVhch8ecgYArnEINv1MdyluYc382GwPymg3H6v6ASYeYN8c4vDgCac2GiifKxNUOq3fFgwNFK9DemhbsGqDH1JPIwO77Xi60YIqNOeZhdPEL75edXRtG%2Bx3xJOEyJVHSJ3KNk1T%2B6BZRCfe53HzCSi7XTBjqkAbJ70iyrHLBYVtxnygi5%2FMeSI94g6gLCDQUhBayUjqWW%2F79Jmc8iAaPKjKH3TgyaywF70El0VZpnD%2FmQEcilY0z1Pey0UVCDCIRM%2BfwORfwb%2F%2Bjzz7h9PP4a009u1rMyBLSm9mFQtECwtIVRl9tAXxgN1ExtiqTUQ0s57mOSpnUvt94MRRR7EWeh7JLYt25db94FBv79%2BaWfi64cGocHGgEzBQ%2Bk&X-Amz-Signature=e43fa6030da02f37aa2af96c350add71551d2ed88aa8b51faafcedeb9c255c55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
