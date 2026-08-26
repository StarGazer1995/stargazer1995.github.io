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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4AXQMGX%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T143340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIA8ompbA%2BSH7WC71uEsc3uQR%2FXrlnnvSUnu%2BArZVDJmbAiEA0eEgY%2F7Kth%2BWx3YarXxElxIOXGpUJ3%2B738ydD%2FwSYCUq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDIw6QSzazy%2FjCb5b2CrcAzwq7cVughOi4bvZBCtmtRaAYtkCEvmWDSYIY%2B9a2sMUj5c5KCeHWH2A4GFsrfZKYdXopWS5b95QXuYu1e%2Fq2iOnpIXg6hkC4CCFvQ0qZ%2BUZNe5rvga3lfNhz1%2Fpu%2FIPUl%2FoyIEUjVTjWRXWbQPY0U6xqB7RzKZ5rATByD9PUXEiq7qU4Nf3nETLFmswTdS2q5QQ1JM1tQAH48N5J17H4%2BC6iX2rHJAsQ5MSVOte5CsmYPwxdQF%2FOeCwVpTfkhWZ9r58LqllZRhMACJ1sjkfemxpldHJjFbp3u2LhfmtEzH6BwpbSQFbvjSiehDAw1h78iPSm%2BzUWE9NEEeX1dl50N6EDukY4Uv2uQrgxdlFJW6jNeKllMUgVHCCHs2aEe20GMaxazbCRRRmnrTbbwywXI8h7sHOm2EyJ%2BfJb5ulugPx2UpQ%2F2sySVKqBeVbrDMpUl%2BRJ8%2BOdcs0ATGu1jJCztW9FXO%2BBSigN5y4%2FaFVdWLxGz9qbqstfyIbGVE0aj25iO6BHZLDWk%2Bngd1RGgsHo8uFYT9JxyoMIbHxQYi3EVQa5eYyUufiLXpAYWYAChCALJhA2R2aak4tTovjRxygTCLkMdfOdfYI3lu5mX4hm82JM4sARdoMpcKOwAWuMLHhu9QGOqUBiDj18YK98%2FuTXRAT9grbw2KtevMQJNOUSN7eMkspO9i2rpFbrIPau5qSJmSp1BLSjz%2Bcqde4UdradNGAmPDWWpUR%2BbOQrz2QBDBxbOkQBAliusOhOsXRzt8s2%2BsPOw%2BnvXVt%2FmYg5yJmPuMpsvpen29xzvsLoVhwUF7MpfcZgMl47lqj6345m%2FrlrbvGH0av%2FzbXK63uIyVFwQgUarmeFuba%2ByUR&X-Amz-Signature=c925fd9edba3c53730d597a3ea87a0132a736d93f7661952a09968c71f38e951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4AXQMGX%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T143340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIA8ompbA%2BSH7WC71uEsc3uQR%2FXrlnnvSUnu%2BArZVDJmbAiEA0eEgY%2F7Kth%2BWx3YarXxElxIOXGpUJ3%2B738ydD%2FwSYCUq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDIw6QSzazy%2FjCb5b2CrcAzwq7cVughOi4bvZBCtmtRaAYtkCEvmWDSYIY%2B9a2sMUj5c5KCeHWH2A4GFsrfZKYdXopWS5b95QXuYu1e%2Fq2iOnpIXg6hkC4CCFvQ0qZ%2BUZNe5rvga3lfNhz1%2Fpu%2FIPUl%2FoyIEUjVTjWRXWbQPY0U6xqB7RzKZ5rATByD9PUXEiq7qU4Nf3nETLFmswTdS2q5QQ1JM1tQAH48N5J17H4%2BC6iX2rHJAsQ5MSVOte5CsmYPwxdQF%2FOeCwVpTfkhWZ9r58LqllZRhMACJ1sjkfemxpldHJjFbp3u2LhfmtEzH6BwpbSQFbvjSiehDAw1h78iPSm%2BzUWE9NEEeX1dl50N6EDukY4Uv2uQrgxdlFJW6jNeKllMUgVHCCHs2aEe20GMaxazbCRRRmnrTbbwywXI8h7sHOm2EyJ%2BfJb5ulugPx2UpQ%2F2sySVKqBeVbrDMpUl%2BRJ8%2BOdcs0ATGu1jJCztW9FXO%2BBSigN5y4%2FaFVdWLxGz9qbqstfyIbGVE0aj25iO6BHZLDWk%2Bngd1RGgsHo8uFYT9JxyoMIbHxQYi3EVQa5eYyUufiLXpAYWYAChCALJhA2R2aak4tTovjRxygTCLkMdfOdfYI3lu5mX4hm82JM4sARdoMpcKOwAWuMLHhu9QGOqUBiDj18YK98%2FuTXRAT9grbw2KtevMQJNOUSN7eMkspO9i2rpFbrIPau5qSJmSp1BLSjz%2Bcqde4UdradNGAmPDWWpUR%2BbOQrz2QBDBxbOkQBAliusOhOsXRzt8s2%2BsPOw%2BnvXVt%2FmYg5yJmPuMpsvpen29xzvsLoVhwUF7MpfcZgMl47lqj6345m%2FrlrbvGH0av%2FzbXK63uIyVFwQgUarmeFuba%2ByUR&X-Amz-Signature=6786422b79d302950367774c68de684c9970325b03cfe934fd67b0c61cc6c0e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
