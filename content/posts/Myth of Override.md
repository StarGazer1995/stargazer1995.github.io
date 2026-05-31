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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643PPKT56%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T151035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCID2tpHfv8eP8YdQhiPaejnLQiLcWUpTKJc01mSUx2j%2FtAiEAjE0AYSG%2FUqPqKMav1RD1wAFQxC%2F%2BfRp9L%2BIRWZ4cttwqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOBbHBaBp3VV3nYbircAz6nrAFl1sFYpMjZ9pfl%2BFtfwBowR%2BCGjCkkaBE2tAyECHlNe5tDMe5QQIrI4GcvEYlQYV81n2l%2F5%2BIZT7QOYxK%2F8EbKMx6w%2FILs9iuqsPQTcOARfNDKQ%2BcSyGBtHdBuOOveNF1tKREz26Lwsft0LHu7kxreSiCJ7JZ9vw2dq24%2BvZrqAAj%2FkC%2B1dsoNHTUnCQ4xWRJfACUEFexCv1ZlQmu9ndql1MgI9w6P8gsgKlKZ4orsRNI2SZxyHZBn1f8pa7oISx40q72%2B06AHChXNSKLlnFo1zuVK7AZQ35Oe4yDrOHZRy5GgSa%2BDDRY0xQ1mifsp4yGzzyHNte3pc2G%2B3G00KinXARDThCU8KdhOlkR6Q8n2PJY%2Fv%2BGZdmYECLBtXmFN02pUcYQrx52Eb7ixOPp4WmKNiMHo8Dwmwtt1%2FlRL%2FPnEAtQbBwllTTI7g5EED%2BP1iU27Rf1Qpjk%2F1TRbiYiirRbjaFxkmiZZB5QXivQxID0tYQj2hxKHXKV%2FcWd4er4wPpg6ZmpzuTy1zE5FFpKKEcRASBN1Y1Ma4hruVqzzdagLBQk8%2FqEeI7mEWMafCbcfbz06o1D2nZzYo2YTu8IQqMboJuw%2BfIIMgcNBym0R2WMBRZw93CgbmHbHML%2BL8NAGOqUBkVcL1hZDVQAm4ef75Y5bGW1lAIRYicZItaGnQyFwl%2BYY4Ne%2F%2FDlfcAq46KdH4uQwfbeHZS5LAgghXqZLDLynAuGFyh36InhJ775kKSXitXU9A%2FpyTqWA7V5HiKMItaQ8HsCsi%2Bt8nJLnHTpIeUq7Uh%2BEzZ5kNBqWg2qhdD662pvWKJqm%2BqzOqmTr4fGZNpxckVr77q0cFSPlQotRY87jKB6mC3if&X-Amz-Signature=b5adbbb3e4981ce7ccf64691e947765ee9dc1c05fac807e221e98745580c15a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643PPKT56%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T151035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCID2tpHfv8eP8YdQhiPaejnLQiLcWUpTKJc01mSUx2j%2FtAiEAjE0AYSG%2FUqPqKMav1RD1wAFQxC%2F%2BfRp9L%2BIRWZ4cttwqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOBbHBaBp3VV3nYbircAz6nrAFl1sFYpMjZ9pfl%2BFtfwBowR%2BCGjCkkaBE2tAyECHlNe5tDMe5QQIrI4GcvEYlQYV81n2l%2F5%2BIZT7QOYxK%2F8EbKMx6w%2FILs9iuqsPQTcOARfNDKQ%2BcSyGBtHdBuOOveNF1tKREz26Lwsft0LHu7kxreSiCJ7JZ9vw2dq24%2BvZrqAAj%2FkC%2B1dsoNHTUnCQ4xWRJfACUEFexCv1ZlQmu9ndql1MgI9w6P8gsgKlKZ4orsRNI2SZxyHZBn1f8pa7oISx40q72%2B06AHChXNSKLlnFo1zuVK7AZQ35Oe4yDrOHZRy5GgSa%2BDDRY0xQ1mifsp4yGzzyHNte3pc2G%2B3G00KinXARDThCU8KdhOlkR6Q8n2PJY%2Fv%2BGZdmYECLBtXmFN02pUcYQrx52Eb7ixOPp4WmKNiMHo8Dwmwtt1%2FlRL%2FPnEAtQbBwllTTI7g5EED%2BP1iU27Rf1Qpjk%2F1TRbiYiirRbjaFxkmiZZB5QXivQxID0tYQj2hxKHXKV%2FcWd4er4wPpg6ZmpzuTy1zE5FFpKKEcRASBN1Y1Ma4hruVqzzdagLBQk8%2FqEeI7mEWMafCbcfbz06o1D2nZzYo2YTu8IQqMboJuw%2BfIIMgcNBym0R2WMBRZw93CgbmHbHML%2BL8NAGOqUBkVcL1hZDVQAm4ef75Y5bGW1lAIRYicZItaGnQyFwl%2BYY4Ne%2F%2FDlfcAq46KdH4uQwfbeHZS5LAgghXqZLDLynAuGFyh36InhJ775kKSXitXU9A%2FpyTqWA7V5HiKMItaQ8HsCsi%2Bt8nJLnHTpIeUq7Uh%2BEzZ5kNBqWg2qhdD662pvWKJqm%2BqzOqmTr4fGZNpxckVr77q0cFSPlQotRY87jKB6mC3if&X-Amz-Signature=65442bbdd029db648552a52b0ae46e7c41a4396b56f934d1d8ae411cc48b8cf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
