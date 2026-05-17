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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBXTMFOC%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T145013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBUdYT7c2qRPs%2FE0O9hhXIr%2BFUiLR%2FKJaMem%2F1AibEMlAiEA5TYk%2BcAKERRxuNY8DdkJzpcUKXMq%2FvgjoWOH25qiAakqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOT90ieLqzfuJfcGVCrcA2Y9VW4Or%2B8zYDdm84c8xDthskjnHOryhHbIlwHx3cTIP3XSR6sHNEisXQB8pVn3QIflBV5pJKd5LE%2F%2BpGHoZgbr6vojIZ6Kco%2BpUdiSsRc%2BBOzCv4035RzD4B%2BvlWPtPhuynbtMqDiTNbaKHYmU%2F7dB8TN2r9rW279LxEUUuFBB4gCdNBG3pTvrdhdFVSwNj4fWW7snraSVw7SJgltncybYtICHO%2FVpuBs5Cyr%2FYJQPNHwgRbmF%2Bl4db8IgtoO4%2BSxd7JR%2Fvlvw8LYruislsvgZpxEP%2Br8PN3R1DFMDl3Bt9CiuESNVgs76pXNPSGw2fsMesOjbKHDTyGbKPgKjYuWWDimuBMjqtT8x7V9CiQ5rs1KdRss2V7%2BhfBMstLTtuMz%2B1FhTZHoH2J%2FONrchXXBTb1qW6H62G3I6x8dSI3aCVVo6nrAWvXquapOYbqD68sgdGJAiQBriHDJ2jrxYrzAIJ%2BEzsfkP8xt0LvUluuFBEow2Oij7qEhV2No%2FIjX7nzI%2F3hkbPZ7tTSgoaUixeYBBjqL40goTIVY79VEWJWaFQ9fGvgsuxBNJEcHPob9aSFEAdmpmlzHsxenFjhDhv7zGFf%2Bdo0LxJ6vacRlJnTw65RIikmyBDyOcKJnEMJaSp9AGOqUBtX9DkH6YqRcbdCbX%2FgFDKkV%2BKHj250OWU%2BB5x4KZ3NIKU5XZYVbgbpXoblppc47mJs67f8GASqZl%2BETJKdaTIFvOCQDX4nZpFn5GHby%2BTnd2uhYC6EfVZ3qouMQsbgYiNcCHfTyXwK8t8LmJQj8RXzkAZS%2Fl2qMc%2BAzeNY1PuwqBsXMwNttAxzGMT0NjxA7FL9i0Ju5kmgGCnMcJnQE6PNMEOfGT&X-Amz-Signature=d8305ffff1fc2754b29d6f8464545bb77d9364f99112109d750135d2ea587945&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBXTMFOC%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T145013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBUdYT7c2qRPs%2FE0O9hhXIr%2BFUiLR%2FKJaMem%2F1AibEMlAiEA5TYk%2BcAKERRxuNY8DdkJzpcUKXMq%2FvgjoWOH25qiAakqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOT90ieLqzfuJfcGVCrcA2Y9VW4Or%2B8zYDdm84c8xDthskjnHOryhHbIlwHx3cTIP3XSR6sHNEisXQB8pVn3QIflBV5pJKd5LE%2F%2BpGHoZgbr6vojIZ6Kco%2BpUdiSsRc%2BBOzCv4035RzD4B%2BvlWPtPhuynbtMqDiTNbaKHYmU%2F7dB8TN2r9rW279LxEUUuFBB4gCdNBG3pTvrdhdFVSwNj4fWW7snraSVw7SJgltncybYtICHO%2FVpuBs5Cyr%2FYJQPNHwgRbmF%2Bl4db8IgtoO4%2BSxd7JR%2Fvlvw8LYruislsvgZpxEP%2Br8PN3R1DFMDl3Bt9CiuESNVgs76pXNPSGw2fsMesOjbKHDTyGbKPgKjYuWWDimuBMjqtT8x7V9CiQ5rs1KdRss2V7%2BhfBMstLTtuMz%2B1FhTZHoH2J%2FONrchXXBTb1qW6H62G3I6x8dSI3aCVVo6nrAWvXquapOYbqD68sgdGJAiQBriHDJ2jrxYrzAIJ%2BEzsfkP8xt0LvUluuFBEow2Oij7qEhV2No%2FIjX7nzI%2F3hkbPZ7tTSgoaUixeYBBjqL40goTIVY79VEWJWaFQ9fGvgsuxBNJEcHPob9aSFEAdmpmlzHsxenFjhDhv7zGFf%2Bdo0LxJ6vacRlJnTw65RIikmyBDyOcKJnEMJaSp9AGOqUBtX9DkH6YqRcbdCbX%2FgFDKkV%2BKHj250OWU%2BB5x4KZ3NIKU5XZYVbgbpXoblppc47mJs67f8GASqZl%2BETJKdaTIFvOCQDX4nZpFn5GHby%2BTnd2uhYC6EfVZ3qouMQsbgYiNcCHfTyXwK8t8LmJQj8RXzkAZS%2Fl2qMc%2BAzeNY1PuwqBsXMwNttAxzGMT0NjxA7FL9i0Ju5kmgGCnMcJnQE6PNMEOfGT&X-Amz-Signature=f0e6c30ddcb6e81e849eb023413596fdcf42227db0de2b4cd66f487f7cda66a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
