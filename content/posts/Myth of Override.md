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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOYV7AS5%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T110414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCCkg2PksjqwmPuxVo30lXfPOOaB5fr6f1WMXPvJlJdBAIgPIrB5yyRzxKgdvGQxYFgc4dU0S9%2BzQS0VQCanGJPRy0qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYtU6HNZ43sb18z7ircA%2FRmj%2BVTB3Iii2Lir%2B%2BwKu4Es5ZuwsBXmUxEQddKS6Swyk%2BzpyCy%2Fxv9%2BPydmfLw63X3rksufoflSdNe9BdEkMWoNiq44wgZ1sSMimShLgUa9PGZtdB64kKV%2BqQ%2B7ASMmKNARh%2FH1VndZ5knoXYBDAh1nrZCu0DarcV%2FKvsplf9QMYkrzyZdwBpOq%2BD2zuLvGEkrr5W79YfkvOMpG8kTuWEjJdGy7WgieCc3tdzMs9C6dkrfJJi37AervFS1a9V0kQnYfeHtfrO0K8ukEgpt47uix%2B%2BtI37YOFCZ5PNbJ%2F3EaIwQJ5C41WRU5kigg0EmrI3GOXN6dOldAiRwRD%2BCIi0r%2FTg1AouDs55Wei6sNfqCiFnDGf9HiY3zT%2BzlQxO1v5y%2BbcWIrPCOVxbb1t0qP6rSy8MHvI3%2BA%2FwKEu71LOFC7pyyZjjH8DI7TPfY98%2FN9%2BRNk2ALvRKqdX8Hv%2FxyvRhhg%2F4cHWti80P89cv2TxDg4YwLsWwME2UxTlH5A0ZiemYNKpzbSxZpt4tLykcuUjrCqyckKtwJ1gAjvKfg71FdN7g%2FpltSoPcyTiyWvxa0AHESYK3PSiQ2wY4nb29Jz3JhOt62dnlPGv0GyKh5wxTwwCKSqDHOHL%2FZqsmpMJ6LzdIGOqUBQB17gOyabeD7%2B6xKqq%2BEyEzmw8oCYMM8141hdIi%2BNbmjQUhzTB273bFC4uwz2TA8ly%2FDtMhNSpkQxVMSws9%2Fz5TlWqk9ZLnczhGe9SzDzr%2Fk%2FbOBpWWY%2BHz5LJHtMd5phNLA6Yq47dyZj8AAhXybuAiT%2BT1jS9t%2BLAiclnczyy19gGLH41Q21L5phUo0Sfi9a578l302mi0iN5mnAgZuFpjm5i8l&X-Amz-Signature=563d16496c173ec7c5180dc9c263e77d2c91cfa62b528fe9b837be021e77450e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOYV7AS5%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T110414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCCkg2PksjqwmPuxVo30lXfPOOaB5fr6f1WMXPvJlJdBAIgPIrB5yyRzxKgdvGQxYFgc4dU0S9%2BzQS0VQCanGJPRy0qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYtU6HNZ43sb18z7ircA%2FRmj%2BVTB3Iii2Lir%2B%2BwKu4Es5ZuwsBXmUxEQddKS6Swyk%2BzpyCy%2Fxv9%2BPydmfLw63X3rksufoflSdNe9BdEkMWoNiq44wgZ1sSMimShLgUa9PGZtdB64kKV%2BqQ%2B7ASMmKNARh%2FH1VndZ5knoXYBDAh1nrZCu0DarcV%2FKvsplf9QMYkrzyZdwBpOq%2BD2zuLvGEkrr5W79YfkvOMpG8kTuWEjJdGy7WgieCc3tdzMs9C6dkrfJJi37AervFS1a9V0kQnYfeHtfrO0K8ukEgpt47uix%2B%2BtI37YOFCZ5PNbJ%2F3EaIwQJ5C41WRU5kigg0EmrI3GOXN6dOldAiRwRD%2BCIi0r%2FTg1AouDs55Wei6sNfqCiFnDGf9HiY3zT%2BzlQxO1v5y%2BbcWIrPCOVxbb1t0qP6rSy8MHvI3%2BA%2FwKEu71LOFC7pyyZjjH8DI7TPfY98%2FN9%2BRNk2ALvRKqdX8Hv%2FxyvRhhg%2F4cHWti80P89cv2TxDg4YwLsWwME2UxTlH5A0ZiemYNKpzbSxZpt4tLykcuUjrCqyckKtwJ1gAjvKfg71FdN7g%2FpltSoPcyTiyWvxa0AHESYK3PSiQ2wY4nb29Jz3JhOt62dnlPGv0GyKh5wxTwwCKSqDHOHL%2FZqsmpMJ6LzdIGOqUBQB17gOyabeD7%2B6xKqq%2BEyEzmw8oCYMM8141hdIi%2BNbmjQUhzTB273bFC4uwz2TA8ly%2FDtMhNSpkQxVMSws9%2Fz5TlWqk9ZLnczhGe9SzDzr%2Fk%2FbOBpWWY%2BHz5LJHtMd5phNLA6Yq47dyZj8AAhXybuAiT%2BT1jS9t%2BLAiclnczyy19gGLH41Q21L5phUo0Sfi9a578l302mi0iN5mnAgZuFpjm5i8l&X-Amz-Signature=d099be50ebc13c2ef8fd9c0830a4b6602284cd3ef2c948c9127715be73070d58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
