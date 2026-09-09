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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYJMK3D%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T015229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtRwr0qGM9LkM5cZ4g99dJAUjn7fEeGX%2FWjE%2FMBN1FogIhAMvWxT5YZ92cP7StI7pr0NS9KHyu%2F29dIW63SegpozWEKv8DCGAQABoMNjM3NDIzMTgzODA1IgwN3gLUOpCNqr1wGUQq3ANVw6q%2F76Fk5zEAsrX5aa08g71MpPBFSIJiM41Fh33hdoUu%2FvTKAiPi9HQsX4sRbc58G0%2BvWJn%2F3fPgg93r2OEGiRNG88yIif64HnAJi%2Bf2jHbgnnu2EUvRMiGOhJaYHmTEE9xwPLAQdbTg1q%2BfY3KGfvNo%2BsnlsjgDiUgrXZ1fC1%2BjVVqESEnS2RvYexhbss8PBcWbXo89BYZO7mXx3wgBaRHB0RwjXJWjDsSc2Wbt36udPgYDaE1mlzRgi%2FYN9KT2mJjLIt4QbdHrif6JTAqzIdgW3ZfIyKocCJwQFXnQCZ7FGkkq4CxZCBlE3IzrDfMrb7SWMGfNna3avtHZVPKPfcXGYGMrjJFTiFVO6SEr%2FpjD0w1rUtwRrGVpBiGErBtsEbANYqszYjO2xtcCSeH7whacOa22cFVulIjBl9fZM9CcMZFhVbgYpfgCvxxYuxQZwOB%2Bo7Gu3mhHCE61X43Yg%2BVhatBnEnlWYmxSDFdzje3iowFzEUNkrgARIB7hQkqcNekoue9hDiQ5S6IgojZpKjTBmooV97Xiv9CLnTB00ZGF%2BSgx%2BiSyuHbVEtWzNfMGlyLuHgrx7%2B5XURjaTeKt8iCxJVUdcZmTwbk8PP66vaAz1Ik%2FsZ3mYqH%2BETDGpILVBjqkAcg4MopUynhe4NTCnC10IFD%2BbF6xg3kTXbd6jeHzYZUx62AXJ%2FvGOm%2BdCvxzQnyTunawxxDiq8dBVhc9JHK1QOA3zAMJ5x5VXDt6UN22z3Ks4j7o9tv5%2B5DD%2FtBLBI7iV8XHrg8fEKFLoqamJGEbzyr1qFHOboNzpUa8j10OqrZnaOAxPrv5IYiSzyCQlqvOGUpzHUWfyAHnZQInnbdtQUi2nPDl&X-Amz-Signature=217e9679b2081d5e139c34a419b6743adfc390f28a69ba29f89a57d7fdb75914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QYJMK3D%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T015229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtRwr0qGM9LkM5cZ4g99dJAUjn7fEeGX%2FWjE%2FMBN1FogIhAMvWxT5YZ92cP7StI7pr0NS9KHyu%2F29dIW63SegpozWEKv8DCGAQABoMNjM3NDIzMTgzODA1IgwN3gLUOpCNqr1wGUQq3ANVw6q%2F76Fk5zEAsrX5aa08g71MpPBFSIJiM41Fh33hdoUu%2FvTKAiPi9HQsX4sRbc58G0%2BvWJn%2F3fPgg93r2OEGiRNG88yIif64HnAJi%2Bf2jHbgnnu2EUvRMiGOhJaYHmTEE9xwPLAQdbTg1q%2BfY3KGfvNo%2BsnlsjgDiUgrXZ1fC1%2BjVVqESEnS2RvYexhbss8PBcWbXo89BYZO7mXx3wgBaRHB0RwjXJWjDsSc2Wbt36udPgYDaE1mlzRgi%2FYN9KT2mJjLIt4QbdHrif6JTAqzIdgW3ZfIyKocCJwQFXnQCZ7FGkkq4CxZCBlE3IzrDfMrb7SWMGfNna3avtHZVPKPfcXGYGMrjJFTiFVO6SEr%2FpjD0w1rUtwRrGVpBiGErBtsEbANYqszYjO2xtcCSeH7whacOa22cFVulIjBl9fZM9CcMZFhVbgYpfgCvxxYuxQZwOB%2Bo7Gu3mhHCE61X43Yg%2BVhatBnEnlWYmxSDFdzje3iowFzEUNkrgARIB7hQkqcNekoue9hDiQ5S6IgojZpKjTBmooV97Xiv9CLnTB00ZGF%2BSgx%2BiSyuHbVEtWzNfMGlyLuHgrx7%2B5XURjaTeKt8iCxJVUdcZmTwbk8PP66vaAz1Ik%2FsZ3mYqH%2BETDGpILVBjqkAcg4MopUynhe4NTCnC10IFD%2BbF6xg3kTXbd6jeHzYZUx62AXJ%2FvGOm%2BdCvxzQnyTunawxxDiq8dBVhc9JHK1QOA3zAMJ5x5VXDt6UN22z3Ks4j7o9tv5%2B5DD%2FtBLBI7iV8XHrg8fEKFLoqamJGEbzyr1qFHOboNzpUa8j10OqrZnaOAxPrv5IYiSzyCQlqvOGUpzHUWfyAHnZQInnbdtQUi2nPDl&X-Amz-Signature=b5f9fdddb5a3d54c5fd08b0d9fed5caa140264b46f8c62eb7f5bbf71004edc27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
