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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INV5B4C%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T065425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIc8BFKcTi3uWPugUWNjhi6j8feQLW3cSlr403cmwcIQIhAOZ6FAO5xWD2h7KCkfeJSzFoEz8evKQwT3Edfx%2F%2Br4%2BkKv8DCFIQABoMNjM3NDIzMTgzODA1Igzj6XFEBNCyZT1Ne0Mq3AOZEjVADFTovwZg1ezQeVoZe4EG36lasrrblcjqV1BNb433WBJjWUgRPpQ7LRvuZixY1GDT3d2CG96k374SC7fSdugB1v3rR%2B4TRp8wHtAM2DroGrEheVdumKubDmSswrsrnJgMa688wlhG0A7U4jbA7kQAyU8XjXd12bbuWk7sCxx7tE%2B%2FcWz0gyXG3yfmcZLu1WK9NqZECeZW4S5oFaLoJgowIyEsEJnfHjewoXFjTjYGIfG%2B5uLTe7PZBAIs9sqlUqYTuE%2FDTLjOaRkQypCZwaqQ1lFXeZLetOhWLvV29JMA5ukDahzDOjClyDAqkn5aTHGHHq%2BwzaLtPG3%2FPM1hcsPqqFFwW1kKv363f9k%2BjFaBvT48YoA7xW0YZSDMbC2O9H1sdxKg6lnhoUV3PF%2BRI7j4nwWAEf3W2ByZrLuEYKZOdFBdaG%2FjSTYdCiELhlmNZ%2BHJW90eT%2FLNkyg%2FMKPfyqFTeSekMfJ%2FECcdX7T4ykUrCYIqaDM%2BwBx2d8Iu6Hm0rynry%2FAPLm3kTrAICEb8T8UxH%2BCFDU8A6jBc4hkmGFYY733qZ4sZHNeKA86N%2BpYA5RfS4gyUbesbniMKAGKxIEC3pQaxyAYnflsF9RvOZtqohnBl481b58A2NjCOzLfVBjqkAb83s33MrZtk9Vvel%2FlqQ1kRq6kye9POg3rAA8HgQE1LhL2stID10HBipZymVmuvQsJg8YMufXkKjEi6aelR8sNWftqokOTgTsJm1ReaU2u4irEgmz7gVMtF%2F1H4zPgy3TFJw24JACCECVAf%2BeD7nYSHMTc%2FJ6SWLyGDY54OtvwLxxx6hxCMLoNG9yEJaZKKnwaOhyS9cQrMiqCSkwsHMzELZ8a7&X-Amz-Signature=097a4d116c69dee485e25636087c6775f0c5611a73b9c99710dc94f4ddbaaa3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INV5B4C%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T065425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIc8BFKcTi3uWPugUWNjhi6j8feQLW3cSlr403cmwcIQIhAOZ6FAO5xWD2h7KCkfeJSzFoEz8evKQwT3Edfx%2F%2Br4%2BkKv8DCFIQABoMNjM3NDIzMTgzODA1Igzj6XFEBNCyZT1Ne0Mq3AOZEjVADFTovwZg1ezQeVoZe4EG36lasrrblcjqV1BNb433WBJjWUgRPpQ7LRvuZixY1GDT3d2CG96k374SC7fSdugB1v3rR%2B4TRp8wHtAM2DroGrEheVdumKubDmSswrsrnJgMa688wlhG0A7U4jbA7kQAyU8XjXd12bbuWk7sCxx7tE%2B%2FcWz0gyXG3yfmcZLu1WK9NqZECeZW4S5oFaLoJgowIyEsEJnfHjewoXFjTjYGIfG%2B5uLTe7PZBAIs9sqlUqYTuE%2FDTLjOaRkQypCZwaqQ1lFXeZLetOhWLvV29JMA5ukDahzDOjClyDAqkn5aTHGHHq%2BwzaLtPG3%2FPM1hcsPqqFFwW1kKv363f9k%2BjFaBvT48YoA7xW0YZSDMbC2O9H1sdxKg6lnhoUV3PF%2BRI7j4nwWAEf3W2ByZrLuEYKZOdFBdaG%2FjSTYdCiELhlmNZ%2BHJW90eT%2FLNkyg%2FMKPfyqFTeSekMfJ%2FECcdX7T4ykUrCYIqaDM%2BwBx2d8Iu6Hm0rynry%2FAPLm3kTrAICEb8T8UxH%2BCFDU8A6jBc4hkmGFYY733qZ4sZHNeKA86N%2BpYA5RfS4gyUbesbniMKAGKxIEC3pQaxyAYnflsF9RvOZtqohnBl481b58A2NjCOzLfVBjqkAb83s33MrZtk9Vvel%2FlqQ1kRq6kye9POg3rAA8HgQE1LhL2stID10HBipZymVmuvQsJg8YMufXkKjEi6aelR8sNWftqokOTgTsJm1ReaU2u4irEgmz7gVMtF%2F1H4zPgy3TFJw24JACCECVAf%2BeD7nYSHMTc%2FJ6SWLyGDY54OtvwLxxx6hxCMLoNG9yEJaZKKnwaOhyS9cQrMiqCSkwsHMzELZ8a7&X-Amz-Signature=0acfd6565c8a083e2581c4297eaba2fa306e8c4d3fab8491a2b2e13ba8629790&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
