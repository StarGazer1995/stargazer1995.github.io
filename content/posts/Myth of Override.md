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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4UBEY7J%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T194825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQC4ARj9w2Usrp%2BF175TcVQge5xVitHsYRS%2FVUu97kMz3AIhAJmK1rmxZicOPpM79SiXL%2BVyZvyfKN7fVxBbV0n4wx0BKv8DCCQQABoMNjM3NDIzMTgzODA1IgxY4ycLJ55sW8bv8sQq3AMZvHIVEF9VsJzToyJ%2Fq0%2BzfCsXpYRM6LXizRucCnRJ6Yjm2Hvq719FIJGT5xx%2F2mDCaUd2%2BDLBi2QsIO5CdaFoEHx42g96DoS4vyVGJecLeP5SZwcbriUFFSM9w91Qsykbc0KvNenbwnGMmYR0TdKLeo1sxQ4MhH0ayqauYNuAov8TaJp8SVcMsU64ajTVT6boxeL6e%2FLSZm308EFuOdedpOn%2FRkdl9iViWIFy7bYFCgzPNVrq2EJ5My0TlBBWuOT2WcYujhPZ1WI0JerkLbTv%2FkkKkjckcoBsdRq%2BVb%2BZle574iIRPNmqmBXIzN5GbcEKz7rTsJ3JBorY598du4s%2FiQpYNdhcpaA3bC3rVgnN5NBDXnfGTFljH6HV%2F4Ma%2BVbojhyIDUkuWU2Gi9LaVjnKRcDGmcs5MTHhdvRC%2FCjlTtRJqBka1nt1TM1stI1%2FgNFSEq9jdcD99wYJngnZo9ZJuiCiBV6h5gnQ1E20zTTjCAcOLWI38Vp8gA7TTOgeLjS8DeY12X%2Ba7tyMXSFoctANpTwpJG1XA0R2uOyMx8Ottjg%2BH6epGBi%2B1cQyRMoN65Fur9SrTt%2BENIaKEMsXgRGrEHfSsbosI%2FfcthuNM1RzTD9mX6Chkea0B0CSnzDGtevRBjqkAbmONNE7i6uzQgqn21PNfOFt0rk%2Blkn5c5J929vE1uXY9Umx0H%2FGkvgtfR0w4SS1aBFUFf6ttWMTd%2Bcm8j2UNQUsUOm%2Fjy%2Bnw6eFevSkdIv3ursbCQSkdsa2yUVB2CoL%2BI8%2BOkZTQM8mIqaN6gbu3%2FKQ%2BANPpxREoj8LJfmg2iWeisB%2BtXhkVqnQ7U65gCwWG8QijKxl2YEJGYcfbWgJNluDYXi6&X-Amz-Signature=4cbf27e374339a4e7799e542fb4c0113d2a488a898eea2cfcd603f626d70ad95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4UBEY7J%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T194825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQC4ARj9w2Usrp%2BF175TcVQge5xVitHsYRS%2FVUu97kMz3AIhAJmK1rmxZicOPpM79SiXL%2BVyZvyfKN7fVxBbV0n4wx0BKv8DCCQQABoMNjM3NDIzMTgzODA1IgxY4ycLJ55sW8bv8sQq3AMZvHIVEF9VsJzToyJ%2Fq0%2BzfCsXpYRM6LXizRucCnRJ6Yjm2Hvq719FIJGT5xx%2F2mDCaUd2%2BDLBi2QsIO5CdaFoEHx42g96DoS4vyVGJecLeP5SZwcbriUFFSM9w91Qsykbc0KvNenbwnGMmYR0TdKLeo1sxQ4MhH0ayqauYNuAov8TaJp8SVcMsU64ajTVT6boxeL6e%2FLSZm308EFuOdedpOn%2FRkdl9iViWIFy7bYFCgzPNVrq2EJ5My0TlBBWuOT2WcYujhPZ1WI0JerkLbTv%2FkkKkjckcoBsdRq%2BVb%2BZle574iIRPNmqmBXIzN5GbcEKz7rTsJ3JBorY598du4s%2FiQpYNdhcpaA3bC3rVgnN5NBDXnfGTFljH6HV%2F4Ma%2BVbojhyIDUkuWU2Gi9LaVjnKRcDGmcs5MTHhdvRC%2FCjlTtRJqBka1nt1TM1stI1%2FgNFSEq9jdcD99wYJngnZo9ZJuiCiBV6h5gnQ1E20zTTjCAcOLWI38Vp8gA7TTOgeLjS8DeY12X%2Ba7tyMXSFoctANpTwpJG1XA0R2uOyMx8Ottjg%2BH6epGBi%2B1cQyRMoN65Fur9SrTt%2BENIaKEMsXgRGrEHfSsbosI%2FfcthuNM1RzTD9mX6Chkea0B0CSnzDGtevRBjqkAbmONNE7i6uzQgqn21PNfOFt0rk%2Blkn5c5J929vE1uXY9Umx0H%2FGkvgtfR0w4SS1aBFUFf6ttWMTd%2Bcm8j2UNQUsUOm%2Fjy%2Bnw6eFevSkdIv3ursbCQSkdsa2yUVB2CoL%2BI8%2BOkZTQM8mIqaN6gbu3%2FKQ%2BANPpxREoj8LJfmg2iWeisB%2BtXhkVqnQ7U65gCwWG8QijKxl2YEJGYcfbWgJNluDYXi6&X-Amz-Signature=f9358a816098cd3800773517a3f752cf23d317812619b5d428611b7ee163c068&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
