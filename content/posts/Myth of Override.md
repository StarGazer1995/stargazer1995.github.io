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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IGOFYT%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T230744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGolKb0h6RCwHVPmWhmR67mImNQZd5dPh8Hajn8MjNagIgdqYwZG5NAc2BnjjurGo438B2YlsfGpTojr%2FRwNP%2FnBsqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoGVwhqpZkWHdkFXCrcA%2Fp4c%2B2LUoElpW3R6GZ%2FeggWAuA1Ge3rE%2FMkojA5H%2F1DGtyFWK3RUZN2s8TRSbv7WwQIZ7Pxh%2FiqBzHQj1%2FOKH5yJe1ZEa6B7DgVShWhf7DA5ldqGPX1uv2VeQ5SkFd2iTpP3lblnPPSPr7489DIEuNv1pZwRvl3pMQ1Vab0BvsB%2BjczdzTd0ImrEV0iFgoNwjbBN4GcnQ9BULsONcX6xSml0KHazM5Dm4k2kFsI6qDQEstVx82WYGMTkNka505RXFEaiYSsKEdPxo1RrO6C%2BHBaX%2FeKLa%2FvXhul9QVJHqatyaRd6QR8NejDQOYxjcVICRgxNrPqzTNtOLrWIu2xV7ObTXldh3uHME8jyavyeBdgvMIQe2P6F2Gq6MX9a6n5bwmusZtr5TGp0zrkuBSCAw1%2BG35ooXnmTOQU%2BOq7c%2FpfHXOrlceWEhIq8RdTVIElhEnfaNFcUL0d2Ob8EWVe%2Bjoimd81O9424atSlA%2FDYC9om1FDtBkhvLbtCWpc8U4ZtgNeZgBCT%2F0DIuWH0mIUMLW61yvrmlvZWuan28YUgCFhpASqq2EJAz25wcwawd9FncLsmuWre1nA6Q75SQCATr6i93lOh8YQLoHWKIEIwgr2rp1qCjSfngaCuiMYMIvf4tAGOqUB1Ahg4OhenxsWcVhz5o24gHiBqEl%2Fxj23059O9qX9TWs2Sj3RjAUPPdL7FpQZK1tiuw68TClDNg%2FZQfoDtKktu3q5f0%2FFaI0WjzO3we2cHo1M2O2%2F3HUjPgTeGH%2FZpjJ25MYxDybQ9SIguTHMnA2LtyqVCxNgyJdKSoU2yjTCHD1RTfPyO3fRJaAHs%2Bxp9qFv2NV99C6I4L%2B8sY94TTQMs2iGV856&X-Amz-Signature=cfe4eade94629a6d0e500a3eaae76fe4440e51d31bb77d5232be65e822551a7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IGOFYT%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T230744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGolKb0h6RCwHVPmWhmR67mImNQZd5dPh8Hajn8MjNagIgdqYwZG5NAc2BnjjurGo438B2YlsfGpTojr%2FRwNP%2FnBsqiAQItv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoGVwhqpZkWHdkFXCrcA%2Fp4c%2B2LUoElpW3R6GZ%2FeggWAuA1Ge3rE%2FMkojA5H%2F1DGtyFWK3RUZN2s8TRSbv7WwQIZ7Pxh%2FiqBzHQj1%2FOKH5yJe1ZEa6B7DgVShWhf7DA5ldqGPX1uv2VeQ5SkFd2iTpP3lblnPPSPr7489DIEuNv1pZwRvl3pMQ1Vab0BvsB%2BjczdzTd0ImrEV0iFgoNwjbBN4GcnQ9BULsONcX6xSml0KHazM5Dm4k2kFsI6qDQEstVx82WYGMTkNka505RXFEaiYSsKEdPxo1RrO6C%2BHBaX%2FeKLa%2FvXhul9QVJHqatyaRd6QR8NejDQOYxjcVICRgxNrPqzTNtOLrWIu2xV7ObTXldh3uHME8jyavyeBdgvMIQe2P6F2Gq6MX9a6n5bwmusZtr5TGp0zrkuBSCAw1%2BG35ooXnmTOQU%2BOq7c%2FpfHXOrlceWEhIq8RdTVIElhEnfaNFcUL0d2Ob8EWVe%2Bjoimd81O9424atSlA%2FDYC9om1FDtBkhvLbtCWpc8U4ZtgNeZgBCT%2F0DIuWH0mIUMLW61yvrmlvZWuan28YUgCFhpASqq2EJAz25wcwawd9FncLsmuWre1nA6Q75SQCATr6i93lOh8YQLoHWKIEIwgr2rp1qCjSfngaCuiMYMIvf4tAGOqUB1Ahg4OhenxsWcVhz5o24gHiBqEl%2Fxj23059O9qX9TWs2Sj3RjAUPPdL7FpQZK1tiuw68TClDNg%2FZQfoDtKktu3q5f0%2FFaI0WjzO3we2cHo1M2O2%2F3HUjPgTeGH%2FZpjJ25MYxDybQ9SIguTHMnA2LtyqVCxNgyJdKSoU2yjTCHD1RTfPyO3fRJaAHs%2Bxp9qFv2NV99C6I4L%2B8sY94TTQMs2iGV856&X-Amz-Signature=a2d1b0f81c585e941bc78243de1a6439184d81bd3e24d5bef0e9c38ed015d117&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
