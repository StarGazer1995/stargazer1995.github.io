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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQK2JX7%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQC31j4OyQOHiQ3aG9RUR0OrrM4CGMdLfYNFRLmXRHn3vQIhAOZTwI1YZ2jAkvCVkRH%2FD7H9Sgdan8XrtvuSz%2BR2mp6vKv8DCA8QABoMNjM3NDIzMTgzODA1Igya7m71Nx7CAxGoQJsq3AMP693brGScB5V05y7E3qctkubD3wR609uXNRE%2BXOhhlOE9C1eZNS0B3k0lfyavgmbXJYit%2BIagjqrgQtZ%2FpFo8gjAoPZzYCXQ7ohBiZWn%2FVL7etO8qXePFriXHTAwBpDnFbA8%2B5Rg%2BhTXTtv6g2%2BobNoWeJ1llNcoq2j7bP3RCESvQHBDnWgob%2FPPSYykPZ%2B%2FRivEYUcDRCz5VfYuacV68qpniqLuGng5McEcC3nDySfwEtMxcg0twS3oyg3R5obWpUj%2Bj5Xh8Yi2Dp6HPjKrv6ljn%2BIJKkUC6rya8sLvHGPOcTsktInRlbJbhU21tKwVtNJLwikjyCZGo9AV670Ey2kgB9QpGdpZXeXFMN26ojYo4Q8Clup1KrbK%2ByGwC67rc6ow7nI3LvFNvNFCLtz12ePo6xxrLdjcFdclf5fRXmjiUu3uRsh8hHuXvXpKCC%2FLYaNm5HlShja%2FTwwsd5t2iWTRs60ajmKP%2FL8CO0lFgrtdlJ9gtlrppWFv0UqsLnFaRYALDUbTAxZr6wyzT5Ccy0DU8VdJR41ruMgCESjS0niG5gQXCpXGvkonZJGtwc0kudDls5r4hdPVgTbwwFTLZ3jJnxh%2FU%2FIsnh4tSVPOmwaJy8CBabVD%2BdBOhhjCggL7QBjqkAZBlgMq%2B%2BbF%2BsjBQ7XbZOvhQRRgUJ0q6ncNo1iT74%2Bg3lsp1wCBJXNKuQq5ml07BwScVjSChuz7RJnckFS2hZTmCHZTsEYCvybxOnsuKvD24Hioadx3LEOUuL99goE%2Fm73Jlh70On2wS6Hv9kwOsdKhmnC%2BkGQ8G1%2BeEsTKz2w72X3y1t4SadHS6LjRUC1tJEJwwPN9DjLqMEmfhhEofGHjW02B7&X-Amz-Signature=679dd22bc26ccedb6a80bba1e63ff19a86299d6ce73b5330c521fcc0d8d16678&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQK2JX7%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQC31j4OyQOHiQ3aG9RUR0OrrM4CGMdLfYNFRLmXRHn3vQIhAOZTwI1YZ2jAkvCVkRH%2FD7H9Sgdan8XrtvuSz%2BR2mp6vKv8DCA8QABoMNjM3NDIzMTgzODA1Igya7m71Nx7CAxGoQJsq3AMP693brGScB5V05y7E3qctkubD3wR609uXNRE%2BXOhhlOE9C1eZNS0B3k0lfyavgmbXJYit%2BIagjqrgQtZ%2FpFo8gjAoPZzYCXQ7ohBiZWn%2FVL7etO8qXePFriXHTAwBpDnFbA8%2B5Rg%2BhTXTtv6g2%2BobNoWeJ1llNcoq2j7bP3RCESvQHBDnWgob%2FPPSYykPZ%2B%2FRivEYUcDRCz5VfYuacV68qpniqLuGng5McEcC3nDySfwEtMxcg0twS3oyg3R5obWpUj%2Bj5Xh8Yi2Dp6HPjKrv6ljn%2BIJKkUC6rya8sLvHGPOcTsktInRlbJbhU21tKwVtNJLwikjyCZGo9AV670Ey2kgB9QpGdpZXeXFMN26ojYo4Q8Clup1KrbK%2ByGwC67rc6ow7nI3LvFNvNFCLtz12ePo6xxrLdjcFdclf5fRXmjiUu3uRsh8hHuXvXpKCC%2FLYaNm5HlShja%2FTwwsd5t2iWTRs60ajmKP%2FL8CO0lFgrtdlJ9gtlrppWFv0UqsLnFaRYALDUbTAxZr6wyzT5Ccy0DU8VdJR41ruMgCESjS0niG5gQXCpXGvkonZJGtwc0kudDls5r4hdPVgTbwwFTLZ3jJnxh%2FU%2FIsnh4tSVPOmwaJy8CBabVD%2BdBOhhjCggL7QBjqkAZBlgMq%2B%2BbF%2BsjBQ7XbZOvhQRRgUJ0q6ncNo1iT74%2Bg3lsp1wCBJXNKuQq5ml07BwScVjSChuz7RJnckFS2hZTmCHZTsEYCvybxOnsuKvD24Hioadx3LEOUuL99goE%2Fm73Jlh70On2wS6Hv9kwOsdKhmnC%2BkGQ8G1%2BeEsTKz2w72X3y1t4SadHS6LjRUC1tJEJwwPN9DjLqMEmfhhEofGHjW02B7&X-Amz-Signature=f88b5a6f952874b10a2b38aad006385d0ffee80aa0819f4114bc1bfd85289670&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
