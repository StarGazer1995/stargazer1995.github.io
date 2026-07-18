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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD63RYEX%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T223733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeHO%2FWil8cyhjdHyFYMzcAYU4HgUvfEkoNSJC17vC80QIgTHAhA7N9XOl02UC5VSHskIUt6E7OGhryp7FmfSJbwFAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJoBx2ZGEr1sJjS8TCrcA3RB4EkKLTABmV8YIZVsVqp7jAGrzZh7AVlRKJVwJnPXXTKjaaEBSmbgJacBgoE61LtvxqqjKXIY%2Fz4UHfOYf1pC4CIZB%2BYwmz4y7qwmcLKLlkn9Q1KJSMpj1psH2D%2FBv3nzsas3mG9OiHwkFv1Qsuh5wRGcXERq3eJnMYch92cZSphDynP38cwyPM403Etyqm2%2BBAszz%2Fx7THK7jLvwR3vUCLvOSiTGa636X9o3YIcooN5N4WJU9GMdZQbtHtQUVGLoa0pxfGN7GuUfp1EVKREmJPkRrtQgLrxCq8taYU9ESPYA7fbggHpcmmS7U1q3L5rJac9z3ntEL%2B%2BtWXeydWKReru%2F0aFgCB4VKWWzuVjsPZ9Q9dQ9YzxSRaEFnymrImLIN6le5VCveqWxS%2FOkJ8cNPurwfW8zx8FEsZobmSCyBVer5TgYgn%2F2YYyCQvmjvNOegKqKD20ukK8eViYb2KLE2V6YxEsv5QCK3sWgD1gJuFIMMHu6RBci2G5AzF1cQ06m3LrHP%2BG1ld80Iq8Jv5GaveT7vUYQjApCFqPbDe%2Fzk1PFsQw38Kg62u8F9lOFYk97C8JC81zXgcEVGVSC4c%2BrSoHltiG9GgFHzs2Tpo2PYjSQxgHjZdxrHDw9MKr579IGOqUB4AahCzvLDct33zWPXUmjnMVZ%2Bx%2FpeCl6s7Qwq5uv99lPjrhB7BCB1wvuQ3KtMuFL2rT5LGLMSayH4PkW8iTKiiTtELJkm7GSsL87dIUr6znKn1yiHyUeiHLHL3%2FB04Rn7xu8Yn2ooKP47s5SgTDiKUMPSzwFnxZa%2FgLiy%2FlkS%2Fa%2B5ktb5%2FidEV7FFEEO1O6CmMSDzczN7ABrEXAqywSUZ1ftMrkj&X-Amz-Signature=10b24b08e290cbcf883df93f578b6ec1896f811ae6e035cea25cc8cf6b29e0ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD63RYEX%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T223733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeHO%2FWil8cyhjdHyFYMzcAYU4HgUvfEkoNSJC17vC80QIgTHAhA7N9XOl02UC5VSHskIUt6E7OGhryp7FmfSJbwFAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJoBx2ZGEr1sJjS8TCrcA3RB4EkKLTABmV8YIZVsVqp7jAGrzZh7AVlRKJVwJnPXXTKjaaEBSmbgJacBgoE61LtvxqqjKXIY%2Fz4UHfOYf1pC4CIZB%2BYwmz4y7qwmcLKLlkn9Q1KJSMpj1psH2D%2FBv3nzsas3mG9OiHwkFv1Qsuh5wRGcXERq3eJnMYch92cZSphDynP38cwyPM403Etyqm2%2BBAszz%2Fx7THK7jLvwR3vUCLvOSiTGa636X9o3YIcooN5N4WJU9GMdZQbtHtQUVGLoa0pxfGN7GuUfp1EVKREmJPkRrtQgLrxCq8taYU9ESPYA7fbggHpcmmS7U1q3L5rJac9z3ntEL%2B%2BtWXeydWKReru%2F0aFgCB4VKWWzuVjsPZ9Q9dQ9YzxSRaEFnymrImLIN6le5VCveqWxS%2FOkJ8cNPurwfW8zx8FEsZobmSCyBVer5TgYgn%2F2YYyCQvmjvNOegKqKD20ukK8eViYb2KLE2V6YxEsv5QCK3sWgD1gJuFIMMHu6RBci2G5AzF1cQ06m3LrHP%2BG1ld80Iq8Jv5GaveT7vUYQjApCFqPbDe%2Fzk1PFsQw38Kg62u8F9lOFYk97C8JC81zXgcEVGVSC4c%2BrSoHltiG9GgFHzs2Tpo2PYjSQxgHjZdxrHDw9MKr579IGOqUB4AahCzvLDct33zWPXUmjnMVZ%2Bx%2FpeCl6s7Qwq5uv99lPjrhB7BCB1wvuQ3KtMuFL2rT5LGLMSayH4PkW8iTKiiTtELJkm7GSsL87dIUr6znKn1yiHyUeiHLHL3%2FB04Rn7xu8Yn2ooKP47s5SgTDiKUMPSzwFnxZa%2FgLiy%2FlkS%2Fa%2B5ktb5%2FidEV7FFEEO1O6CmMSDzczN7ABrEXAqywSUZ1ftMrkj&X-Amz-Signature=9e8966a8f6bd6fb7b9b1636bcad1623e2d37e9e1942ac88cfdca203d1e569fbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
