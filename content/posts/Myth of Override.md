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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BE4T32B%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T184633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuXRHFbg%2Fe%2BjdIFGUD6OyuNPSjjdEMDX3F6b5WCX9cywIgdOY3l2PbwOH3LwyH8hvzhECsgE5xTNoe77xeilHXCWkqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7MyOv%2B2ipxENTgJyrcA%2FDaL6Ni5ebha2S7TWDdevmHZGFD%2BPdLanJOtGL3KHexbmfVsGqSbBQ%2FiHgt%2BcvglyZzMxqorlo0nKP9NY%2BXZFV3OIVnKOeCp%2Fq1JJ76pDkH%2Bspq%2Fz9ty%2BH1eOp5aNM3guKxvgMxD4Gda6s3BuedJNa7x%2BBkUuLU9OZj3TAO016vRB5cWPf902vtukyUh%2F80d%2BLrE3quO1z%2Bd%2BdPmCz3h6v%2BFR%2FB0H0byLhTPkWe1k%2FpkO73zcyUy5dh3eU9gj9iqpAxxqKUSDx38k7qlfNKFblBk2aVlvgbM2FihlIC1aZdZmdiXPb46PeWxLestnEsdjiVsGuDCMHgqz3VzJV9%2BAuBO%2FlN%2F0I9uJu8n5LD1ACHt%2BeFUxF45fB9yxBGkWA6wfeZZZgjOsEETZhUlVIYc1uo8gPyqcfxvl2n%2B2mW7IDm6OrZjdc2nAPSqADl8SaQXuEW7pawjajBxPbTozuypnK6eY1KtFGct%2B3LruqbeHj983YVy0BeQGzsMjE1J7GPlpk8G7qFkJ%2FfxFTvhbbjuqC3oJtsIcs1Z6J%2BQGVSP1IiliOZKMMt2qGVtS5BK8W3fAOkOVhygLx%2FFL8Cp8h5rmeIWdWnZ4trAjPpDMlWdiGc0EsSQNzNrPP855FnMN2G9NIGOqUBGCPS5dW7KBzEPHgKL77%2FnZBKztwzVptEFTJebwyYND93xIq35zjZGnjjkGMr44ZEzPTAN2vkz3NI7TmVrhhbITs2c6w5DK20l1I10kThkrBt1rXWFQig0lBJYemURkEHEuALFynKgyUEu%2FURhtnDwLzD9FfAHh1b2%2FW8bLCA09c9ztxqCRGPj88ojQGhaIIZ%2FTSHGGNQHW4Vc7Tn4Lvil7RY8QcJ&X-Amz-Signature=cf98f9615125af0b6cc166ccb25528a6625df91752f3e460bdd2b29ab705f909&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BE4T32B%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T184633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuXRHFbg%2Fe%2BjdIFGUD6OyuNPSjjdEMDX3F6b5WCX9cywIgdOY3l2PbwOH3LwyH8hvzhECsgE5xTNoe77xeilHXCWkqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7MyOv%2B2ipxENTgJyrcA%2FDaL6Ni5ebha2S7TWDdevmHZGFD%2BPdLanJOtGL3KHexbmfVsGqSbBQ%2FiHgt%2BcvglyZzMxqorlo0nKP9NY%2BXZFV3OIVnKOeCp%2Fq1JJ76pDkH%2Bspq%2Fz9ty%2BH1eOp5aNM3guKxvgMxD4Gda6s3BuedJNa7x%2BBkUuLU9OZj3TAO016vRB5cWPf902vtukyUh%2F80d%2BLrE3quO1z%2Bd%2BdPmCz3h6v%2BFR%2FB0H0byLhTPkWe1k%2FpkO73zcyUy5dh3eU9gj9iqpAxxqKUSDx38k7qlfNKFblBk2aVlvgbM2FihlIC1aZdZmdiXPb46PeWxLestnEsdjiVsGuDCMHgqz3VzJV9%2BAuBO%2FlN%2F0I9uJu8n5LD1ACHt%2BeFUxF45fB9yxBGkWA6wfeZZZgjOsEETZhUlVIYc1uo8gPyqcfxvl2n%2B2mW7IDm6OrZjdc2nAPSqADl8SaQXuEW7pawjajBxPbTozuypnK6eY1KtFGct%2B3LruqbeHj983YVy0BeQGzsMjE1J7GPlpk8G7qFkJ%2FfxFTvhbbjuqC3oJtsIcs1Z6J%2BQGVSP1IiliOZKMMt2qGVtS5BK8W3fAOkOVhygLx%2FFL8Cp8h5rmeIWdWnZ4trAjPpDMlWdiGc0EsSQNzNrPP855FnMN2G9NIGOqUBGCPS5dW7KBzEPHgKL77%2FnZBKztwzVptEFTJebwyYND93xIq35zjZGnjjkGMr44ZEzPTAN2vkz3NI7TmVrhhbITs2c6w5DK20l1I10kThkrBt1rXWFQig0lBJYemURkEHEuALFynKgyUEu%2FURhtnDwLzD9FfAHh1b2%2FW8bLCA09c9ztxqCRGPj88ojQGhaIIZ%2FTSHGGNQHW4Vc7Tn4Lvil7RY8QcJ&X-Amz-Signature=2a75aa8a4688c8140df64368ad2443c11fd9f6417884cb26358fb73a5aadb4a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
