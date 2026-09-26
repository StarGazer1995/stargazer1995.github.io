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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKPRCEHF%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T201812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIAms%2BobZT7O5OPXfED3ngs61id7KSt80V3nnacJ04Dg%2FAiEAmnbaSa4YijuCSrZoso4lbsb%2FUqi73%2FZiU30hcfkWmo8q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDEOnkyvrdjF59%2FxmAircAwBpsGp7Vs4DwOKiw9su2VmTIKE3qUKff29HrB%2FTdzQvkhHl2c45ZZUSM8bgjmwFLtYrTl954bMJlCTHVu9bcYWtV6zShQMicrJc1LE7LGtsUaTeP1Arf7IzD8cOiYi%2BE6aRU999mCLV327y6ucMwImEsFkE%2FDDQQqC4akHol2jLNZw1nyf5loMzq%2FgPIq3r7lZyuhshbfo5S3CWZ6I4e7pqYwys4OkV88wkvOo3bI5lvZciSG6nc%2Fm8rT8xkYkQ3vlG%2BNY%2FSJY9e0%2FV3NlX8E3tRGju%2B0UgWjzZOgMuL596iNlTWnjxUfSBYh62e%2BpUvvOmrZ%2F9l4P%2BCFWuo1z2y6uTRoqrYODsCEfms0IDk%2BBX7b7eg0%2BENCYKniCvKkZkQXuqS68ca%2FxKEqnWHw%2FMulHMc9TK0dF0H75Dw3jIYhgL8H%2B4ObmAvu7u%2BlQ1N%2FFc0JvVldfLgwVvOCL%2FYv0Od93P6NOiqPnhtJ6BA2Jk2JGy70%2B60FrKq0h%2BifEHLwr5nCnOo5rJgQTQ6Rzz6ihm%2FHGbl2nl2z5twkzBbMprtBDbD%2Bmw5iNBeMtUi%2BilK3B3P02gtapYgCJhx4U84KJ5KpBN3ZtXYJxOs0VECwhCULpQPdQVNjep4oHlY%2BrVMLau4NUGOqUBdfVnDQBNPTFxnhy8963GjXIonoiaMaoswHu3eAg418%2FNlCltOaRKts6UyqWc%2BGsystbbldYSBxHNRlKIsoMWCkRZn%2FN3b0VFENu%2Fp%2BliO7m2PplVi6CUZxzMTkXWGiM2BT%2B%2BMaq%2BqWNPOyv6z8TPUKAREW46OxYje%2FQBtcCnv%2FW%2BCd7qBe4VKfpp70bQAtzrmtZylWve3bEPncFBgu14olC12%2BA2&X-Amz-Signature=2dd3d4355063504f87864d991300f157e4a258d75f44cad5fe44b4ae272beef6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKPRCEHF%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T201812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIAms%2BobZT7O5OPXfED3ngs61id7KSt80V3nnacJ04Dg%2FAiEAmnbaSa4YijuCSrZoso4lbsb%2FUqi73%2FZiU30hcfkWmo8q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDEOnkyvrdjF59%2FxmAircAwBpsGp7Vs4DwOKiw9su2VmTIKE3qUKff29HrB%2FTdzQvkhHl2c45ZZUSM8bgjmwFLtYrTl954bMJlCTHVu9bcYWtV6zShQMicrJc1LE7LGtsUaTeP1Arf7IzD8cOiYi%2BE6aRU999mCLV327y6ucMwImEsFkE%2FDDQQqC4akHol2jLNZw1nyf5loMzq%2FgPIq3r7lZyuhshbfo5S3CWZ6I4e7pqYwys4OkV88wkvOo3bI5lvZciSG6nc%2Fm8rT8xkYkQ3vlG%2BNY%2FSJY9e0%2FV3NlX8E3tRGju%2B0UgWjzZOgMuL596iNlTWnjxUfSBYh62e%2BpUvvOmrZ%2F9l4P%2BCFWuo1z2y6uTRoqrYODsCEfms0IDk%2BBX7b7eg0%2BENCYKniCvKkZkQXuqS68ca%2FxKEqnWHw%2FMulHMc9TK0dF0H75Dw3jIYhgL8H%2B4ObmAvu7u%2BlQ1N%2FFc0JvVldfLgwVvOCL%2FYv0Od93P6NOiqPnhtJ6BA2Jk2JGy70%2B60FrKq0h%2BifEHLwr5nCnOo5rJgQTQ6Rzz6ihm%2FHGbl2nl2z5twkzBbMprtBDbD%2Bmw5iNBeMtUi%2BilK3B3P02gtapYgCJhx4U84KJ5KpBN3ZtXYJxOs0VECwhCULpQPdQVNjep4oHlY%2BrVMLau4NUGOqUBdfVnDQBNPTFxnhy8963GjXIonoiaMaoswHu3eAg418%2FNlCltOaRKts6UyqWc%2BGsystbbldYSBxHNRlKIsoMWCkRZn%2FN3b0VFENu%2Fp%2BliO7m2PplVi6CUZxzMTkXWGiM2BT%2B%2BMaq%2BqWNPOyv6z8TPUKAREW46OxYje%2FQBtcCnv%2FW%2BCd7qBe4VKfpp70bQAtzrmtZylWve3bEPncFBgu14olC12%2BA2&X-Amz-Signature=35f6a8fdbaa22a6943fa9eec6fb2620e0e41937ce16d0dcf37ee6ab130ba4fc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
