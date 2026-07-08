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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORUJZIQ%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T155733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnKwKv1dXUffOXgDiin2ErKH7DVO8UMRIrvZd%2Fu7N%2BngIhAInbdxHnWb6z9diD8ORh9qL04QgE2mOlsoyMbZcLQLbmKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7mLLDo5k7%2Fflw%2BEoq3APo4WR2JDwAgi0QisWwZWanuUBTn4Ji4TrfW0gvnSAJLyrfsfadAwdNFCQErPsw9b5AfraM%2FbZklgv%2FqJR6ERED%2F3lzSmdAipbS67UGdptGlpGJg%2B29h2Mv%2B8xal%2FJ7smiDaXLhNl4sG%2Bb74AoQHTB8DbmWxJtrr5oXjPadcLxrYg7gkX5yjreexkeFHTGXSxUVhDOMw1ua%2FqfcEIaGKKnQDIe4TLYpQ%2BGwwK3zH6QqErIR70OpNa%2BXE9HNlNGYCEn564xRnbr4roIeCK3Zlm%2B8vhDQgyYC4bGejArSG7uWKEp%2FQj7vqsisa6%2BOABm43ilkoSrn0Qb3oXciIcVFBSTk8dI9IHth5lY40X5qWHFJW4z8GjyMzhaIWzeqapW8GciuR91Icn5tw0%2BQp1G5piBmfOEfkds6Rcbk9XNz01CK07Zeb%2BLnsuEX7T%2BfKJ959VTpWoRqvYkHSm2WDrZ8frqZ3PXvpld2r%2B1GN9zOsuLSKyJSJ49erdvzjbKcHK8EurhC9YR2ZEhpSFUh%2FuhG807Srsu4YhstoJ6B1jDt9S0ho5bldHS%2FW1eZcWH8ed37mPaitInhVIYKZQo%2F4%2BTtaVbUOcBcx2ZVXr%2F%2Fd2oEhcA21ZgDurUDYcOn1diZdTDI3LnSBjqkAQEJ3UswMoMODsyt%2F%2FetPkuLaaZoloP3sKMzZ7JoFRSGt7MBIqh8EqNiV5uNqiDmcp439KVK1kpmQEmbRw7kxFeiSE67bUx03oyNgE%2B%2Bh8zOJUFpJdN5W0HtdJN%2FE%2BtfBp5WYlC1%2Fw%2BV7t7BfpQHfKi8lmBQlGwwTE2bhf8i1X7rEWlpM86A%2BvBgokmHy%2F6b%2FILkuYx3oawHtbrsVqzq6Gnx5Gi2&X-Amz-Signature=60d6d70bc1359b622887ac0ad899d5dde3b47c15578b0b8247330705c3fd8976&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORUJZIQ%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T155733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnKwKv1dXUffOXgDiin2ErKH7DVO8UMRIrvZd%2Fu7N%2BngIhAInbdxHnWb6z9diD8ORh9qL04QgE2mOlsoyMbZcLQLbmKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7mLLDo5k7%2Fflw%2BEoq3APo4WR2JDwAgi0QisWwZWanuUBTn4Ji4TrfW0gvnSAJLyrfsfadAwdNFCQErPsw9b5AfraM%2FbZklgv%2FqJR6ERED%2F3lzSmdAipbS67UGdptGlpGJg%2B29h2Mv%2B8xal%2FJ7smiDaXLhNl4sG%2Bb74AoQHTB8DbmWxJtrr5oXjPadcLxrYg7gkX5yjreexkeFHTGXSxUVhDOMw1ua%2FqfcEIaGKKnQDIe4TLYpQ%2BGwwK3zH6QqErIR70OpNa%2BXE9HNlNGYCEn564xRnbr4roIeCK3Zlm%2B8vhDQgyYC4bGejArSG7uWKEp%2FQj7vqsisa6%2BOABm43ilkoSrn0Qb3oXciIcVFBSTk8dI9IHth5lY40X5qWHFJW4z8GjyMzhaIWzeqapW8GciuR91Icn5tw0%2BQp1G5piBmfOEfkds6Rcbk9XNz01CK07Zeb%2BLnsuEX7T%2BfKJ959VTpWoRqvYkHSm2WDrZ8frqZ3PXvpld2r%2B1GN9zOsuLSKyJSJ49erdvzjbKcHK8EurhC9YR2ZEhpSFUh%2FuhG807Srsu4YhstoJ6B1jDt9S0ho5bldHS%2FW1eZcWH8ed37mPaitInhVIYKZQo%2F4%2BTtaVbUOcBcx2ZVXr%2F%2Fd2oEhcA21ZgDurUDYcOn1diZdTDI3LnSBjqkAQEJ3UswMoMODsyt%2F%2FetPkuLaaZoloP3sKMzZ7JoFRSGt7MBIqh8EqNiV5uNqiDmcp439KVK1kpmQEmbRw7kxFeiSE67bUx03oyNgE%2B%2Bh8zOJUFpJdN5W0HtdJN%2FE%2BtfBp5WYlC1%2Fw%2BV7t7BfpQHfKi8lmBQlGwwTE2bhf8i1X7rEWlpM86A%2BvBgokmHy%2F6b%2FILkuYx3oawHtbrsVqzq6Gnx5Gi2&X-Amz-Signature=42efc4bb15d75c0ca8093f546351cac1a1f79f6308d322d0794a8cae0210663b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
