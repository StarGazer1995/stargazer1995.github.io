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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZGIN6SG%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T181218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIBFhuT1WUcE5b%2FgLhwihxPs67RonF7Uy1GINI%2BWyrC%2FiAiA7E6aUKz2nCx5R16Z8pde6LC%2FYIuKQIF3sY%2FHVB5qcGyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMNbQpe4pxlP7uuXcbKtwDfVIz8PvyJ3%2FhzHeAm4hmbsDVb%2ByBJHzXakOrBH2468nko%2Fn55VO%2B%2Bsj5gFebbhmnc6CVhsdqGCUkOVtvQ4YL4CJJ2ymVniS4RGhlrk89ZAc%2BrjjXJd6FRLDl7lM6doqUM%2BcjuD55IS%2FGIASaIoArcHYtWQgyWYColf46bPvke6JiPiryQfiCT2Y7niGgd%2F4vsZBLWcEstoX0u8eIX5TWf4C%2FFzPyExwOO%2FaPdiz2SeJlEwMSoDZdCzMxZLr9YmQq7ycAo%2B0av4f6W2r4UxFQGUwWI%2BeJ%2FGGhGLboI9QMP%2BNuwesXDJCYNi9cf%2BXnanW0ijScTtVcJld%2BxPYHRvs9FdD5ULosZqFWW9insgJ1173aKW8mirknOFIMt7QDYo%2B3HO4rmCmsr2y87te640%2FfiyS4OxCd7%2F8LOY%2FuxIqujuqEuirzFxvZcJWMI66yLtEt5eJiSNQ0VJ7SwFlqqHtZqCSdF9pcxGQ0uWZHwUKtlYAKAzT00Fbk5FDBHca385ewbI6P3OL7afbC%2BkSz2rGFi%2FNPL3t%2FeIr0Eh2QgudzVpqSI6TlBMwCvzzomzqQjr29fHDQrU3pLwseBDYsZF%2FIC8OOlVYwof8VmJJY%2Fa9tvcr%2Bsl1KExs9b%2FgHHRowxcWC1AY6pgF3o9RGFhlANsjKYqEPVoU2Bt4aBVJBS6t%2FrIc1Yi7xYaEcaxNiBcYi%2F6v%2F0zkn%2Bo2DBZlDSnbCJbxZjSMZK7L2LF3tL%2FDwm89BxwJdDYPk8h82Wpl6RU6NyS9Y435kYMxl5Wfa9VgKxr1V7J4mcBLm7G%2FrocGfgFeN4JHtiJcwqvzVlAxVVlj6mym%2FlAvZEufZcbBqzPk%2BEzQ2WgukloyJBso%2BY67e&X-Amz-Signature=c4edd50847e285c06a219fac9a3ec752fb1d2fe9945f369859dbb368c5fdd150&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZGIN6SG%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T181218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIBFhuT1WUcE5b%2FgLhwihxPs67RonF7Uy1GINI%2BWyrC%2FiAiA7E6aUKz2nCx5R16Z8pde6LC%2FYIuKQIF3sY%2FHVB5qcGyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMNbQpe4pxlP7uuXcbKtwDfVIz8PvyJ3%2FhzHeAm4hmbsDVb%2ByBJHzXakOrBH2468nko%2Fn55VO%2B%2Bsj5gFebbhmnc6CVhsdqGCUkOVtvQ4YL4CJJ2ymVniS4RGhlrk89ZAc%2BrjjXJd6FRLDl7lM6doqUM%2BcjuD55IS%2FGIASaIoArcHYtWQgyWYColf46bPvke6JiPiryQfiCT2Y7niGgd%2F4vsZBLWcEstoX0u8eIX5TWf4C%2FFzPyExwOO%2FaPdiz2SeJlEwMSoDZdCzMxZLr9YmQq7ycAo%2B0av4f6W2r4UxFQGUwWI%2BeJ%2FGGhGLboI9QMP%2BNuwesXDJCYNi9cf%2BXnanW0ijScTtVcJld%2BxPYHRvs9FdD5ULosZqFWW9insgJ1173aKW8mirknOFIMt7QDYo%2B3HO4rmCmsr2y87te640%2FfiyS4OxCd7%2F8LOY%2FuxIqujuqEuirzFxvZcJWMI66yLtEt5eJiSNQ0VJ7SwFlqqHtZqCSdF9pcxGQ0uWZHwUKtlYAKAzT00Fbk5FDBHca385ewbI6P3OL7afbC%2BkSz2rGFi%2FNPL3t%2FeIr0Eh2QgudzVpqSI6TlBMwCvzzomzqQjr29fHDQrU3pLwseBDYsZF%2FIC8OOlVYwof8VmJJY%2Fa9tvcr%2Bsl1KExs9b%2FgHHRowxcWC1AY6pgF3o9RGFhlANsjKYqEPVoU2Bt4aBVJBS6t%2FrIc1Yi7xYaEcaxNiBcYi%2F6v%2F0zkn%2Bo2DBZlDSnbCJbxZjSMZK7L2LF3tL%2FDwm89BxwJdDYPk8h82Wpl6RU6NyS9Y435kYMxl5Wfa9VgKxr1V7J4mcBLm7G%2FrocGfgFeN4JHtiJcwqvzVlAxVVlj6mym%2FlAvZEufZcbBqzPk%2BEzQ2WgukloyJBso%2BY67e&X-Amz-Signature=04fda9b512a69aacc137b0e955279268e72b1c6ed4cb9500ce35b4e74bbb59da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
