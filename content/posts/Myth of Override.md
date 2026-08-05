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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ6MFYGA%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T115550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDXmugQqaKvvsWZWwETlkQYdvLvzgYVdVmRiNGD5D94JwIgC4FAQ7DKSeKZ%2FEiux14l6qglQxV1ZBt2eutsqFGKxZUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDKqK9VYcTEaNJJCuFyrcA4u%2FN8A7XS2gs9qcOm3LwC7QQPGvyDWMZZP8Rv1QxKtn14E6SlIMLTYazlQXvnircx2mP0hAY35%2FaH%2FETmPpXmm%2B8zpFA%2F9gf%2FATp4ukZJoHD%2Fzk068dqOiKCh7JDw%2FpN7zfTEe73UVwns2RmdQIeX3wOuDorblcwggzplWLbc9Tp1%2F9wdZmv2Pr4AGzB0LoiVERPyh4%2BSVde7nfPwtvw%2FTsx4phiGqWWgKgOGBCQS4NdPeMyRM1R1eLSdMF%2BVW%2F6TpK4kmJHBGlIyXyRiL%2B%2F5X0oNDfjCJHkBE%2BbPkeiW6XoZZiB%2FjPBty6WfhiBSFWWWN3y%2FjC9ukPOUVUEexsPLtWc9pN8QxODsoqwOROIzzdjGYD88zvbGAC1SXrKeHx18hbtI%2FkUL6ve0oZe5U5o5CHTYlroxoEDJ3jPlKBCg5tGsYeyVCJJyhfX%2F4hkZxlsKp8jI8v%2FQZwMj%2Bj%2BDwbAO7iOCRO%2BYxPog8jPtQ7o9p7HlO6ga%2BYkuT2MWW1mJxnUTOw%2FI8uhrmIsLJRxOe540dOhI4hX5awl8ZNgm3DeL8Kxwgjm5nxC9G%2BNyIV2CmyjE3D1t7Ln10IVrl1AO9cDTv51t1a07%2BBTfQsDSHrLDE9R7GuW%2Bow%2BVTD%2FumlMNm5zNMGOqUBP4PW2lq%2Be3gfznY1eay9d8g5ZZf%2BlAc5wsreThNOkU3T1aYEdHnM9fNbV8sB0%2BPqoNtOuDzNww24rOsiL6ufT6h0tJ60C2r%2FYfGzYYlxMgsg8jDgAyma91QSS1HfhvX52WS%2B4ykz2%2BLFFruwZ6neMAI6Jzgl1zSzTeWIMYo5DFf0Zl3oXj7lo6A%2BX9CL6QHEa5xAqgcDTy0QrCyImCbWLeCDz5S0&X-Amz-Signature=c2e037d289391166bfd5154a11766f3757261135f1c47c5099d0541bd73eb1d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ6MFYGA%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T115550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDXmugQqaKvvsWZWwETlkQYdvLvzgYVdVmRiNGD5D94JwIgC4FAQ7DKSeKZ%2FEiux14l6qglQxV1ZBt2eutsqFGKxZUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDKqK9VYcTEaNJJCuFyrcA4u%2FN8A7XS2gs9qcOm3LwC7QQPGvyDWMZZP8Rv1QxKtn14E6SlIMLTYazlQXvnircx2mP0hAY35%2FaH%2FETmPpXmm%2B8zpFA%2F9gf%2FATp4ukZJoHD%2Fzk068dqOiKCh7JDw%2FpN7zfTEe73UVwns2RmdQIeX3wOuDorblcwggzplWLbc9Tp1%2F9wdZmv2Pr4AGzB0LoiVERPyh4%2BSVde7nfPwtvw%2FTsx4phiGqWWgKgOGBCQS4NdPeMyRM1R1eLSdMF%2BVW%2F6TpK4kmJHBGlIyXyRiL%2B%2F5X0oNDfjCJHkBE%2BbPkeiW6XoZZiB%2FjPBty6WfhiBSFWWWN3y%2FjC9ukPOUVUEexsPLtWc9pN8QxODsoqwOROIzzdjGYD88zvbGAC1SXrKeHx18hbtI%2FkUL6ve0oZe5U5o5CHTYlroxoEDJ3jPlKBCg5tGsYeyVCJJyhfX%2F4hkZxlsKp8jI8v%2FQZwMj%2Bj%2BDwbAO7iOCRO%2BYxPog8jPtQ7o9p7HlO6ga%2BYkuT2MWW1mJxnUTOw%2FI8uhrmIsLJRxOe540dOhI4hX5awl8ZNgm3DeL8Kxwgjm5nxC9G%2BNyIV2CmyjE3D1t7Ln10IVrl1AO9cDTv51t1a07%2BBTfQsDSHrLDE9R7GuW%2Bow%2BVTD%2FumlMNm5zNMGOqUBP4PW2lq%2Be3gfznY1eay9d8g5ZZf%2BlAc5wsreThNOkU3T1aYEdHnM9fNbV8sB0%2BPqoNtOuDzNww24rOsiL6ufT6h0tJ60C2r%2FYfGzYYlxMgsg8jDgAyma91QSS1HfhvX52WS%2B4ykz2%2BLFFruwZ6neMAI6Jzgl1zSzTeWIMYo5DFf0Zl3oXj7lo6A%2BX9CL6QHEa5xAqgcDTy0QrCyImCbWLeCDz5S0&X-Amz-Signature=cddd7a5e4fbb92c831d411179d66439adf08ed24af0ba6a8b118215eb0d02a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
