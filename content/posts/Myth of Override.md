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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EXJINIZ%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T234435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMS8Y%2FZopFwjFAHxpRuIvP%2BtevB4vd%2FTwnV8hZ%2FZYUWwIgBaP%2FoOKAfrD6PAtTN6cwoBd5%2BtdMM6u0%2FWYuyuynEw4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFVN15yhO19YTM9sryrcA1X4j%2B2CRg0i%2FYDl5YHGe6CeUxrxXxC0YsArirGJlZQK32aV8V%2Bh%2BlTW%2BpZ9lMejhLUe%2B1MMvM9bKH%2B9F3yA6VgDqiQD97J4HdIP2DOv7QEyTbCjXcgbieTXuNcohjwd0wBttqFb69PQITR1bPfsO%2BEI6u65V8Tl410ZsmXE3Q6C0Z04PFELdGrt5osgFbSo5KZ4Ob1cotuY3hxQIp1EF4NdKZn8Tnafhid0WBFpmmmAMMZxY6WJLTG4Mtbd9kAxHze14pq%2FgArxrqCTKjtCQmlR%2FS%2BLFg%2B5Kx1vA%2BGK53KdrJg%2BNCERpdQN8%2BCy3G1ij0R93gSbGuObzcSaYMWc%2F1k7R%2BS7ant%2FTjDG29xg%2FAvTkJcRVNi5PnSk6ZS9DZgYFctcjDuCarpxHPxR5%2BNN04xI3Hlx%2FMdwixSH88%2BUBpgft2ZtiEe1ugF9Abznw%2BK7A2TNjrNIiIrk%2BxYOey%2F10tR%2BffaZa3HUAfwNSw1beSd6W8uhfj19t8y0Vl8PFhOAxY3ymIArbhV8I0mXk1VnmvCZNjaeOJc%2FFNRo9HlRUsgX6eUib1%2BkztpFwXK72v2c8KeRjrJuOF7vEdVIL%2F7f%2BMZKd2hOhOtshlt8JwFREUvFbFEdlv3jn1DsDLFPMOW1u9UGOqUBZ3kxW5kowmuZzCtXVGeEZocnQUL%2FHODJIrmDqfsECDkKibK0rJ799yAVxrKqViuiUukBa3gioMnC%2Fdcm7WdYSI0MGUQUfcYBlqStYyKrLcR3E7R7%2BB0cRbot%2FtaUqH5sQg8PYBUt%2F6%2BjJSWrDQigJLVABn9k6wRVuiVCHW5NVJW6VGaaHpgo449deGgIUt3vCevNSNR3J6JAcJ%2BLN6PlilCu%2FiFA&X-Amz-Signature=9e2f9ac201ce007c7ed761a6c83f6e2bfa5ce711174660fe80be06ac5a9974c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EXJINIZ%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T234435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMS8Y%2FZopFwjFAHxpRuIvP%2BtevB4vd%2FTwnV8hZ%2FZYUWwIgBaP%2FoOKAfrD6PAtTN6cwoBd5%2BtdMM6u0%2FWYuyuynEw4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFVN15yhO19YTM9sryrcA1X4j%2B2CRg0i%2FYDl5YHGe6CeUxrxXxC0YsArirGJlZQK32aV8V%2Bh%2BlTW%2BpZ9lMejhLUe%2B1MMvM9bKH%2B9F3yA6VgDqiQD97J4HdIP2DOv7QEyTbCjXcgbieTXuNcohjwd0wBttqFb69PQITR1bPfsO%2BEI6u65V8Tl410ZsmXE3Q6C0Z04PFELdGrt5osgFbSo5KZ4Ob1cotuY3hxQIp1EF4NdKZn8Tnafhid0WBFpmmmAMMZxY6WJLTG4Mtbd9kAxHze14pq%2FgArxrqCTKjtCQmlR%2FS%2BLFg%2B5Kx1vA%2BGK53KdrJg%2BNCERpdQN8%2BCy3G1ij0R93gSbGuObzcSaYMWc%2F1k7R%2BS7ant%2FTjDG29xg%2FAvTkJcRVNi5PnSk6ZS9DZgYFctcjDuCarpxHPxR5%2BNN04xI3Hlx%2FMdwixSH88%2BUBpgft2ZtiEe1ugF9Abznw%2BK7A2TNjrNIiIrk%2BxYOey%2F10tR%2BffaZa3HUAfwNSw1beSd6W8uhfj19t8y0Vl8PFhOAxY3ymIArbhV8I0mXk1VnmvCZNjaeOJc%2FFNRo9HlRUsgX6eUib1%2BkztpFwXK72v2c8KeRjrJuOF7vEdVIL%2F7f%2BMZKd2hOhOtshlt8JwFREUvFbFEdlv3jn1DsDLFPMOW1u9UGOqUBZ3kxW5kowmuZzCtXVGeEZocnQUL%2FHODJIrmDqfsECDkKibK0rJ799yAVxrKqViuiUukBa3gioMnC%2Fdcm7WdYSI0MGUQUfcYBlqStYyKrLcR3E7R7%2BB0cRbot%2FtaUqH5sQg8PYBUt%2F6%2BjJSWrDQigJLVABn9k6wRVuiVCHW5NVJW6VGaaHpgo449deGgIUt3vCevNSNR3J6JAcJ%2BLN6PlilCu%2FiFA&X-Amz-Signature=d46481d8046b3bec68bdaebd0b6b2e457bdcf1b82563978027f7616d7131f8f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
