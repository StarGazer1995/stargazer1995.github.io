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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673AVBHVA%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T155601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOp0ABID7QfQhMuk%2BrUckZJ%2FvoUIfXI%2BrgKK8Y1TMPZAiAu23rlIfrXcm5B9jwIj6Tx5jx5INZh2hh4BMbH4%2BBD%2Fyr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMSbWYttI39sTeY%2FcXKtwD5gFwTD4%2BITyXCs20Qfr1b74FqTAOsKnLxqjvUrff%2B2aSjflQQ1xv69ePrrOSCUrZhJwnIvZRHRWHHUKZCXAD6uHGWoAZxag6RvZZKu0XMvXsjNZO0fxtof7scOxPkiXUjWgUPyuwuv%2BZqb%2B%2Fn%2Ff2FJ25onZbQBSNuYGS6uhD%2BGNeLduCW3yg0FUPVRt8N%2Fp940oB%2BTr2c5hV6pDgWZRjQ4ult3TDkcR5nnrwa02Vcdpnrp35t7Yz96MW0FLrGawl7tMWslx57GvFKmPQzLec1MZ5k%2BgBfAjJ%2FTmUU76cw6UoIEYefu%2FmYe1sC2idzPnetoSL4%2FkjmKxBazUwlkuf7gUIRiW%2FYrGWINfyhBW1Mjt48zeEmdR4sgvXKbogzEM4efL5f3mKpmZvXGyyCEG6lmAVB9bhh13ll4NeQ1CkA46eEg9WjmXCSREMxKQPSm1dC7NCYFKtsKnT51FrnI8%2BtqseabpqvIFXEqRDIIE1wkNrs3kfZCQwLPVTjXgUQ3sOe%2BQzYetmvo999OcJ3xSnHiU1jd3iHPgNSYmt55ayTUzd75vjRybrquIEUBKaXNz6T2cm9b8R%2Byc5v4OgUynLtQG4kFKfPRYA3AbbdGPbXOuY%2FJkC6l83%2BsHPiVww9Pmc0AY6pgEiskq47KiHBYsYC16IhA8FSV6cPseRv582MsFB5l59X7k%2B45NnjdGElWb1sua%2FAqN%2B3XJNcMknQ%2B4%2B2z35fZk1gw9zhU4E9N5S%2FIYJ5zh3S2GAggGKN7%2FmPLIiH9nI3Oo7xVs32z5%2FiCsryaHZ6M3Cx67RCC449tk%2FbSdwRRRWA6OT%2BWENv4wNezErU8fzpJutyUQGj13BaEwo5jTbfC%2Feg3%2FwV%2BNd&X-Amz-Signature=b3c29c036e76db1f80c99999be6fb528e6d909b9936aea6764b35f022c9d14bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673AVBHVA%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T155601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOp0ABID7QfQhMuk%2BrUckZJ%2FvoUIfXI%2BrgKK8Y1TMPZAiAu23rlIfrXcm5B9jwIj6Tx5jx5INZh2hh4BMbH4%2BBD%2Fyr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMSbWYttI39sTeY%2FcXKtwD5gFwTD4%2BITyXCs20Qfr1b74FqTAOsKnLxqjvUrff%2B2aSjflQQ1xv69ePrrOSCUrZhJwnIvZRHRWHHUKZCXAD6uHGWoAZxag6RvZZKu0XMvXsjNZO0fxtof7scOxPkiXUjWgUPyuwuv%2BZqb%2B%2Fn%2Ff2FJ25onZbQBSNuYGS6uhD%2BGNeLduCW3yg0FUPVRt8N%2Fp940oB%2BTr2c5hV6pDgWZRjQ4ult3TDkcR5nnrwa02Vcdpnrp35t7Yz96MW0FLrGawl7tMWslx57GvFKmPQzLec1MZ5k%2BgBfAjJ%2FTmUU76cw6UoIEYefu%2FmYe1sC2idzPnetoSL4%2FkjmKxBazUwlkuf7gUIRiW%2FYrGWINfyhBW1Mjt48zeEmdR4sgvXKbogzEM4efL5f3mKpmZvXGyyCEG6lmAVB9bhh13ll4NeQ1CkA46eEg9WjmXCSREMxKQPSm1dC7NCYFKtsKnT51FrnI8%2BtqseabpqvIFXEqRDIIE1wkNrs3kfZCQwLPVTjXgUQ3sOe%2BQzYetmvo999OcJ3xSnHiU1jd3iHPgNSYmt55ayTUzd75vjRybrquIEUBKaXNz6T2cm9b8R%2Byc5v4OgUynLtQG4kFKfPRYA3AbbdGPbXOuY%2FJkC6l83%2BsHPiVww9Pmc0AY6pgEiskq47KiHBYsYC16IhA8FSV6cPseRv582MsFB5l59X7k%2B45NnjdGElWb1sua%2FAqN%2B3XJNcMknQ%2B4%2B2z35fZk1gw9zhU4E9N5S%2FIYJ5zh3S2GAggGKN7%2FmPLIiH9nI3Oo7xVs32z5%2FiCsryaHZ6M3Cx67RCC449tk%2FbSdwRRRWA6OT%2BWENv4wNezErU8fzpJutyUQGj13BaEwo5jTbfC%2Feg3%2FwV%2BNd&X-Amz-Signature=9aab84df1e0cf3e381f84ab49f3de73e124d982537c7f547fb094d54a9c9a55f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
