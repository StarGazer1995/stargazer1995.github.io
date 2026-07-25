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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRHV4UZI%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T074843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQCa2E1ZLEi8gVaV28mR4L%2FhnF%2FHFvy0InnLMDA18TMxWgIgSDfQ%2FrvZayNacXEjKvFiOCOSEYM%2FJjxd%2B%2BvX%2F0QDx8Eq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDKFFJogkDwPajLO1zCrcA2AnhXAgzbp6AfTD%2ByzI8jbX%2BEqJQPljd1SWX1HrdXYldphugMO9SU81dIQgoGY94ukCLk40f3%2FftTex%2Bc6zbAIZHt6Ux2hice65CzKfg6cAgSLVp%2Fqmf6OZq0fnxKZQSg3M%2BIRcu6swojAwtBMJ6zKDkpqTDVBLvRwEkJKT3Hn4V%2Bm2OrGZXJ6QMMk%2BjOqqDWtQ95trfBPMrRW2Zu61le49O1t7YtADT5VyD3puN7%2BVbCte%2BU%2FLhfkbcdvFzO5z6B5Y1I60%2BRPzkl%2FP4Dh51wAqQcYPXbf5VfIsmA9XXwRQMP0yNwvGMoOZiGTcZOrCa1FB7Dq28NbqvSVx98XXzOKVbKT2sAi22KA7fZFYu2OGMJJNPPK68U%2BgsMS1sVg1YvR1GWGDiJK3W0hz9CAfmx0ghDRc67I2Xue6s7U%2FQsiCEw%2FLwmf7awbAJxNvuxaQOirF9S7ak8NftPlBfvYRWMLWwPiZP%2BahP6vDYsJFKFk9VnZY4tpSGT1Njjp9yT3hCUmweT7QSskiBImWeai0OT%2FvDpSYoKjT68uzUx5W33acTZZsKwI9LpHmuWV96ow1YVYhW8KasiMH6z46KJN609gDQipnctkhwb45xPLr9O5WB1kjTa243%2BuUkJiWMP%2FFkdMGOqUBovIv4R2LoriAcRUZCftK7eLbHvsVmIgIqu6gt3RFF%2Fz3S4S7%2BkAyIw6H7ZnNtxq7Ku8MUdQhxxU0V6gxz1jeDO9SUCBLhWid9s6IVj6HwD4SMSW0Y0rh4WHshFcaD9sU97W5ZWfk7Ds5YREPojIzMb7O5Uf8uhH%2B%2BJ42umfexuO7pUVUlFLomTscCOP%2BJmfpw9vUpUHRnhq1xqgriFeCf3pLejFI&X-Amz-Signature=b603a3c614de9edbd157987a37e8eafb10970ee338b05169ddcae00a120b00dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRHV4UZI%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T074843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQCa2E1ZLEi8gVaV28mR4L%2FhnF%2FHFvy0InnLMDA18TMxWgIgSDfQ%2FrvZayNacXEjKvFiOCOSEYM%2FJjxd%2B%2BvX%2F0QDx8Eq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDKFFJogkDwPajLO1zCrcA2AnhXAgzbp6AfTD%2ByzI8jbX%2BEqJQPljd1SWX1HrdXYldphugMO9SU81dIQgoGY94ukCLk40f3%2FftTex%2Bc6zbAIZHt6Ux2hice65CzKfg6cAgSLVp%2Fqmf6OZq0fnxKZQSg3M%2BIRcu6swojAwtBMJ6zKDkpqTDVBLvRwEkJKT3Hn4V%2Bm2OrGZXJ6QMMk%2BjOqqDWtQ95trfBPMrRW2Zu61le49O1t7YtADT5VyD3puN7%2BVbCte%2BU%2FLhfkbcdvFzO5z6B5Y1I60%2BRPzkl%2FP4Dh51wAqQcYPXbf5VfIsmA9XXwRQMP0yNwvGMoOZiGTcZOrCa1FB7Dq28NbqvSVx98XXzOKVbKT2sAi22KA7fZFYu2OGMJJNPPK68U%2BgsMS1sVg1YvR1GWGDiJK3W0hz9CAfmx0ghDRc67I2Xue6s7U%2FQsiCEw%2FLwmf7awbAJxNvuxaQOirF9S7ak8NftPlBfvYRWMLWwPiZP%2BahP6vDYsJFKFk9VnZY4tpSGT1Njjp9yT3hCUmweT7QSskiBImWeai0OT%2FvDpSYoKjT68uzUx5W33acTZZsKwI9LpHmuWV96ow1YVYhW8KasiMH6z46KJN609gDQipnctkhwb45xPLr9O5WB1kjTa243%2BuUkJiWMP%2FFkdMGOqUBovIv4R2LoriAcRUZCftK7eLbHvsVmIgIqu6gt3RFF%2Fz3S4S7%2BkAyIw6H7ZnNtxq7Ku8MUdQhxxU0V6gxz1jeDO9SUCBLhWid9s6IVj6HwD4SMSW0Y0rh4WHshFcaD9sU97W5ZWfk7Ds5YREPojIzMb7O5Uf8uhH%2B%2BJ42umfexuO7pUVUlFLomTscCOP%2BJmfpw9vUpUHRnhq1xqgriFeCf3pLejFI&X-Amz-Signature=444cd6ecd52cc17827b2db97f0820ea689d51e59c59efd30e8615905d40bce43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
