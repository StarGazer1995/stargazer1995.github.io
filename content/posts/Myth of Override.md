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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622MJ5XGN%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDs2YPP9ev3GDd8eRZwQI9M1Usdg%2B2vQFztuCN2EdZSagIhAMxk1mB9hwCl1T7uB4lDPN5d9ziaJGELjTnKNsVf8o4BKv8DCDQQABoMNjM3NDIzMTgzODA1IgxPhwl9DjqfJWZbplMq3AMlcMIj3WB5pEZRS1jNDzZF8%2BMVLBDtaso%2F03gbEiTtpB%2FhJ6T6x9SSuF3QlTeVp04wWO%2FtD2UqSddWxpY0kJ1RS3xo2s2aJQV9s%2FBSjaV8rLyH1CAt9EIw3pApadADaW7jPHjQ0xmH8UR90F7j1K9fS%2BM0O2sLkxFmLqsePYJ8kFf8UcBnChZBnA6i3sgy%2FKV5RwhvAoG5h%2Bnrrs06f7kSO0PKTfIUDw3NsfNBFPtD0e31zfkONnbFat5b76ICd37LNYf6oUDEsJh%2B7EaHOuNFtyVxTszXohdXGEZO9POIRYYTIMjldCcAMU7PTa9HsQva1KbpflJsB1qu8BIyHRjN%2F20IJRax9Qq3rpEERPXGTRxpJAv4PeSMXAxKTs0bRFTm8fI2RhiwXUQatBJxkScsseLkVkkpTyTcG9tm1jS%2Bs5zb2KpzetfKySc5%2BDtnLYOOcaJ8CYRk%2BBo0EL3KD8wNpIZwM6NMzBHUWOZp7tfxXX0BefyOtbRrozQGoVy21YT08essZ8991h%2B2xgeey3SGMwJpvu2qq3xkH9xIwuu%2FCJwRLgASBgu%2BuiOkTqGi2afhW%2Fv49svdXD15rplNuiv1pn8tC2Ah6d1J6Kteosk3g1Z7WlNo20G0pGSIwjC1ksbQBjqkAfRC1S7vW4Jig7PZmA8cCJl7QF9m919FL0tAfF2DbS53ARVMeBiLe%2F8bVjzTKk7ZYYxbxfChmTbLlqruIKCEHgQ5G7UuTYZ9%2BfZePLVpO0cjqftZtvvYRVftknNYDCdLvUnZoQpUyy%2F%2F0ABNDnqL7AILq11jaBwOI0ysgvrYFecHv3IwG0MJqe6inqL5%2FS7Nhtyy%2Fg1uxt%2FIsRtVAlNB3bhM%2BAYi&X-Amz-Signature=dbaf96278459f0d0c17923830793f24c793c320a3c1011c7344e490f9b84740c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622MJ5XGN%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDs2YPP9ev3GDd8eRZwQI9M1Usdg%2B2vQFztuCN2EdZSagIhAMxk1mB9hwCl1T7uB4lDPN5d9ziaJGELjTnKNsVf8o4BKv8DCDQQABoMNjM3NDIzMTgzODA1IgxPhwl9DjqfJWZbplMq3AMlcMIj3WB5pEZRS1jNDzZF8%2BMVLBDtaso%2F03gbEiTtpB%2FhJ6T6x9SSuF3QlTeVp04wWO%2FtD2UqSddWxpY0kJ1RS3xo2s2aJQV9s%2FBSjaV8rLyH1CAt9EIw3pApadADaW7jPHjQ0xmH8UR90F7j1K9fS%2BM0O2sLkxFmLqsePYJ8kFf8UcBnChZBnA6i3sgy%2FKV5RwhvAoG5h%2Bnrrs06f7kSO0PKTfIUDw3NsfNBFPtD0e31zfkONnbFat5b76ICd37LNYf6oUDEsJh%2B7EaHOuNFtyVxTszXohdXGEZO9POIRYYTIMjldCcAMU7PTa9HsQva1KbpflJsB1qu8BIyHRjN%2F20IJRax9Qq3rpEERPXGTRxpJAv4PeSMXAxKTs0bRFTm8fI2RhiwXUQatBJxkScsseLkVkkpTyTcG9tm1jS%2Bs5zb2KpzetfKySc5%2BDtnLYOOcaJ8CYRk%2BBo0EL3KD8wNpIZwM6NMzBHUWOZp7tfxXX0BefyOtbRrozQGoVy21YT08essZ8991h%2B2xgeey3SGMwJpvu2qq3xkH9xIwuu%2FCJwRLgASBgu%2BuiOkTqGi2afhW%2Fv49svdXD15rplNuiv1pn8tC2Ah6d1J6Kteosk3g1Z7WlNo20G0pGSIwjC1ksbQBjqkAfRC1S7vW4Jig7PZmA8cCJl7QF9m919FL0tAfF2DbS53ARVMeBiLe%2F8bVjzTKk7ZYYxbxfChmTbLlqruIKCEHgQ5G7UuTYZ9%2BfZePLVpO0cjqftZtvvYRVftknNYDCdLvUnZoQpUyy%2F%2F0ABNDnqL7AILq11jaBwOI0ysgvrYFecHv3IwG0MJqe6inqL5%2FS7Nhtyy%2Fg1uxt%2FIsRtVAlNB3bhM%2BAYi&X-Amz-Signature=0569d8177a68f09ff6a1f83cf6fe8fc6fda4979461881c5b7328199f526095e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
