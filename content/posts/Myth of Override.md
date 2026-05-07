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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLENSHNP%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T132617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBRQ88f0yD2oLC6%2F3e0XIbWYRq31US12wMo1cVTVGNqKAiEAhhfX5ZcbETvJVo0v3Jt9fkExk%2BNHulmTfYLkPB7R8jgqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7alSRHCrqUkrOMlSrcAxXRNdAVnPyTZoVkRBI7Jmz3iVL3AeehjG4i7Z2R%2BXCVkyhxK2NACVKONGEVcT8xyH1gzRTeNaL3Y3Cca4SmZnECNjVujSwcXInH6c4%2F35pmrE8XZXAa%2BuNtLVx8FsQlu%2FoEX3f8IlOckcAgC8rRnT9R%2BlLgK4iDVEOOqb4HgU5%2BJSdEhKN7zHnfv6Gfkps%2F34Dd0TtEJK8Osn9tiyAjUkWliNNY14krxWxZ%2FbtI%2BY4jT0nZbm0A%2B9Pf%2FoDuQgmnH6iSTMHzJghwnEWrq1V1ljG%2B1SDDG6Tg9r29HgAL4sRlfdQ73JVhabmNwfpmQq8OP%2FzjPUGVXOvuPa6caA1Bkz8frwyXb88u2PBBT1zrf82mQuvgyY6wbzurNspkc37BingoPoTykOo77gPt3PoF9ZUVWp%2FiSPH1w8k3hxc0rkKZ2V3Fo01MI1vuyb%2BK6kBhC3Wn%2F62XwlNhtTFpuUUtSPUBZPWhvTebXnGdadWfh9sRwMTdi7VzeG5k9A4EccHuJl4QLwYnkMcLwThDvNj%2BRbS68lGQc%2Fu%2BDKkJmQG86PZKN1OZAnbpKKlHQLA69dqCbsmbFcEOI9A%2BaGD%2FEMkyrIyFqKKxvlYqaSnz6Kln2glVzw0AePsgvS7ghA21MIKf8s8GOqUBNIr5IYU2HQQ7oUf7QAw%2Beo3TT1g6ytGplP6ZdAH1ZI02EDnnVn9meOe7PnRrBLPs1GcdKBLi4ZKfeGgm%2Fn0ZQQvqjG2mAdCJN7SaKGVCVbGR9NHtueaY3P7lWBPG4Dfy63zgMpJMVYadcVoC%2F2Hg%2FrSHHLMcrAugGqOUmKcaENnOe6ARSaEroiMCYa9duL4nKh3AjZzpf2wgrBsqNyTa%2FUCAG6wq&X-Amz-Signature=739a0f18762316facd6b02fa333eccb28517a2c653aa390e0f8cb75c31a3aaa8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLENSHNP%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T132617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBRQ88f0yD2oLC6%2F3e0XIbWYRq31US12wMo1cVTVGNqKAiEAhhfX5ZcbETvJVo0v3Jt9fkExk%2BNHulmTfYLkPB7R8jgqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7alSRHCrqUkrOMlSrcAxXRNdAVnPyTZoVkRBI7Jmz3iVL3AeehjG4i7Z2R%2BXCVkyhxK2NACVKONGEVcT8xyH1gzRTeNaL3Y3Cca4SmZnECNjVujSwcXInH6c4%2F35pmrE8XZXAa%2BuNtLVx8FsQlu%2FoEX3f8IlOckcAgC8rRnT9R%2BlLgK4iDVEOOqb4HgU5%2BJSdEhKN7zHnfv6Gfkps%2F34Dd0TtEJK8Osn9tiyAjUkWliNNY14krxWxZ%2FbtI%2BY4jT0nZbm0A%2B9Pf%2FoDuQgmnH6iSTMHzJghwnEWrq1V1ljG%2B1SDDG6Tg9r29HgAL4sRlfdQ73JVhabmNwfpmQq8OP%2FzjPUGVXOvuPa6caA1Bkz8frwyXb88u2PBBT1zrf82mQuvgyY6wbzurNspkc37BingoPoTykOo77gPt3PoF9ZUVWp%2FiSPH1w8k3hxc0rkKZ2V3Fo01MI1vuyb%2BK6kBhC3Wn%2F62XwlNhtTFpuUUtSPUBZPWhvTebXnGdadWfh9sRwMTdi7VzeG5k9A4EccHuJl4QLwYnkMcLwThDvNj%2BRbS68lGQc%2Fu%2BDKkJmQG86PZKN1OZAnbpKKlHQLA69dqCbsmbFcEOI9A%2BaGD%2FEMkyrIyFqKKxvlYqaSnz6Kln2glVzw0AePsgvS7ghA21MIKf8s8GOqUBNIr5IYU2HQQ7oUf7QAw%2Beo3TT1g6ytGplP6ZdAH1ZI02EDnnVn9meOe7PnRrBLPs1GcdKBLi4ZKfeGgm%2Fn0ZQQvqjG2mAdCJN7SaKGVCVbGR9NHtueaY3P7lWBPG4Dfy63zgMpJMVYadcVoC%2F2Hg%2FrSHHLMcrAugGqOUmKcaENnOe6ARSaEroiMCYa9duL4nKh3AjZzpf2wgrBsqNyTa%2FUCAG6wq&X-Amz-Signature=b1549ee70a47a8d6af915ca14441f78c1078aa582f06b839ac232e81dca27acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
