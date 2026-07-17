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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662MVLCTB%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T204138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYTj46P6UjNuDoEUCd5sJLTC422wusJb2%2Fgor5JoHWfAIhALMZXrvl7VZzHByeNYeHZawyr6G4t58o0mQGjFOX8SVWKv8DCGUQABoMNjM3NDIzMTgzODA1Igwx5wGhJM4ZpBKJiiwq3AMS3agAwHYsYX8cC3lzIOYRGFEUxe7nP4z11BVGbH2a3XaFe5n36vH5ciSK7K0hb6tHj319b9Lg4CsxD%2BS1jBVFMWBzsEImDUm5V9X%2BeAojDUTFtdZe%2F77vb1NLbZ3KavWxgKzRJF7zK2f3TtmfDxi2sZAnq%2Bh%2BPKk2AS%2F7z3ceQAvHWjC7nVshlKECYdREbxL3gjl89b7fDFUF1dTERUTnujpfkZZIsoqQNYTeG8IPCVU4Jsri2pUItVE3cwjXt4EjPQ6cDUCoDdfavt8RpK4WsNNQQ6abTCU8FvmtbBow1OKaDAjxI53B0KjfDFvkb1J1O6h1XpaoXBH7df%2BaomXcQhig1Uu1otI9I7BeXxjyxGhzE5Umc3ymUVx0pTTmuv%2FpHxLzrunfIemfpoZvHus8T%2F6hqaaF2j5hcg%2FxVsICMFlPH0RtDMFbkt%2Fl%2Fi9%2BfWBJ6Utz0I%2FArt8N47lWDduUgnm%2F0ooU5SbYPxS415iRm5PxZl8oOtXeyXWGVEknNoFdk1KTCU36kv4C4%2BmKCUMsC5eHTJ3qSwoLQa%2Bwm33Xo8a2iej2bAvZb0HROrulXlT7OCmJHiB92PbpcfBcDQSNLNaXil5GjPr3mWPkMnpTumTCzGtBCTeBHZzvBTCDhurSBjqkAYYqZz1BGpTtMKsDxCwq23gv95Sqg4cjkGUMyetyTH5kJYooJWR3M83Go0Qj1BGuoOgm1y6Lo8YR5wWfXrA6JwgYebe10h%2BqxkWqAhJIQQjAr6BWJDX7eE1Z%2FYS%2BAmvoeysiCtCN5mXSFzV2VESZPPqajW6sGI6mAMkykEK%2FVkY7q0lgfWI7IIw7AM658IA1bdEC%2BhIgl39vZasds4FpHQcHynZY&X-Amz-Signature=d57c6d449c8dfb810900fd1a7f81273d10f4b5fe7c157ad2f1131be76cfca18d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662MVLCTB%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T204138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYTj46P6UjNuDoEUCd5sJLTC422wusJb2%2Fgor5JoHWfAIhALMZXrvl7VZzHByeNYeHZawyr6G4t58o0mQGjFOX8SVWKv8DCGUQABoMNjM3NDIzMTgzODA1Igwx5wGhJM4ZpBKJiiwq3AMS3agAwHYsYX8cC3lzIOYRGFEUxe7nP4z11BVGbH2a3XaFe5n36vH5ciSK7K0hb6tHj319b9Lg4CsxD%2BS1jBVFMWBzsEImDUm5V9X%2BeAojDUTFtdZe%2F77vb1NLbZ3KavWxgKzRJF7zK2f3TtmfDxi2sZAnq%2Bh%2BPKk2AS%2F7z3ceQAvHWjC7nVshlKECYdREbxL3gjl89b7fDFUF1dTERUTnujpfkZZIsoqQNYTeG8IPCVU4Jsri2pUItVE3cwjXt4EjPQ6cDUCoDdfavt8RpK4WsNNQQ6abTCU8FvmtbBow1OKaDAjxI53B0KjfDFvkb1J1O6h1XpaoXBH7df%2BaomXcQhig1Uu1otI9I7BeXxjyxGhzE5Umc3ymUVx0pTTmuv%2FpHxLzrunfIemfpoZvHus8T%2F6hqaaF2j5hcg%2FxVsICMFlPH0RtDMFbkt%2Fl%2Fi9%2BfWBJ6Utz0I%2FArt8N47lWDduUgnm%2F0ooU5SbYPxS415iRm5PxZl8oOtXeyXWGVEknNoFdk1KTCU36kv4C4%2BmKCUMsC5eHTJ3qSwoLQa%2Bwm33Xo8a2iej2bAvZb0HROrulXlT7OCmJHiB92PbpcfBcDQSNLNaXil5GjPr3mWPkMnpTumTCzGtBCTeBHZzvBTCDhurSBjqkAYYqZz1BGpTtMKsDxCwq23gv95Sqg4cjkGUMyetyTH5kJYooJWR3M83Go0Qj1BGuoOgm1y6Lo8YR5wWfXrA6JwgYebe10h%2BqxkWqAhJIQQjAr6BWJDX7eE1Z%2FYS%2BAmvoeysiCtCN5mXSFzV2VESZPPqajW6sGI6mAMkykEK%2FVkY7q0lgfWI7IIw7AM658IA1bdEC%2BhIgl39vZasds4FpHQcHynZY&X-Amz-Signature=e0fbb9afa36ccfdadd9b303f14e2fad6d30a2d0492ce0dd1125b0a9d59f1b6ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
