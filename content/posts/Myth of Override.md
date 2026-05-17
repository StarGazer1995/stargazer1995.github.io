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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQSZSOH%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T185220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL%2FLDLq0VzA1YztyCSxH0w%2B5Dka0RQvjifOmpNWuPxqAiEAtOwLVFozHg%2FOc7gEfEWsyqt0zgN277Y3iaH4S1f0AtoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGQkHoXfuIDFXuQaircAwwEMxWxFW%2ByygttUCIgl%2F9fMkzduy61DqAE7GLI6Ma293Q8pQ9LG2QUqvHwz7XTrb%2Fg9cMnI0zO4tMKpQYhx7z6NYDH%2BQKan51dnMKVGEv%2BWmWvUqDxXcSlmvWO%2FDnrRR0vRZl9xuHKosVv9Cb1RAN3PC9Et%2Bd3DU2jSniCABU4vUVpoDlmUgMiFkljGpzlze1U1nEs8Ls8w4SkDJyzyEkuH3ZH8GMGFrjMoeCWBWwl7UrflwIbmvFGsn%2BFo%2BoYlYbdZDoWHqruqulNBhOO10XiSc6kPjofakXFntT9B7Y%2BgwAnia2BsY%2FCROhpjPDv4BYQFSrbapoLirUHrvW7WMMDEJ%2BqeowqxPQy9niL1%2BuQFT9S7OmyMET6cttkdJAqRrJQeSSxFQ7nBZNfGNN6Tb8Nbu33DIi04XJjmyc9COlvAotocyRPRLaq1LC%2BD%2FlTKo7qnPYDI8NQPLclZiTRXxl96GXqGTKDl6KGKz2DHE2aE7jlyLK8ArRRgw93ybVvkE9Qr0tsY5tOR1bV9%2BEnIZS8qFnQcsSnlGzRP4yFBgbakBHNAKurR3p1U4NbieD%2BGL0WVjrR9hPHzONUiCyh7PGgg4Piz80P9ZmRUS4%2F0x%2BhvmZu31fI0i6btCL4MNGSqNAGOqUBiT%2FUMtkhVdL9INuy2lxv3vmFHHam3SSK1AO5SbL4nYcejeeM20slnzQSP2qNTVfbkAwip7pd%2F2W%2FLDBdqT%2Bqo7gS6WWcqeIbd1kCZnQ5iEBBdk73y8cC5t%2FJe0tiiB%2FhZx9lCX1rkZgtlHo7lbc2%2BxzAp0YuqYwhquyV2tjp8ilgbYenODt2t%2FOgj5p6XWZJm3NylnXjKzaTFS6MkKuPJZdQZdNE&X-Amz-Signature=6dd1c62c9ef79e0813c58b021f6c408340df83b8f8c9e32d8fdfc82f82f0d452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQSZSOH%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T185220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL%2FLDLq0VzA1YztyCSxH0w%2B5Dka0RQvjifOmpNWuPxqAiEAtOwLVFozHg%2FOc7gEfEWsyqt0zgN277Y3iaH4S1f0AtoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGQkHoXfuIDFXuQaircAwwEMxWxFW%2ByygttUCIgl%2F9fMkzduy61DqAE7GLI6Ma293Q8pQ9LG2QUqvHwz7XTrb%2Fg9cMnI0zO4tMKpQYhx7z6NYDH%2BQKan51dnMKVGEv%2BWmWvUqDxXcSlmvWO%2FDnrRR0vRZl9xuHKosVv9Cb1RAN3PC9Et%2Bd3DU2jSniCABU4vUVpoDlmUgMiFkljGpzlze1U1nEs8Ls8w4SkDJyzyEkuH3ZH8GMGFrjMoeCWBWwl7UrflwIbmvFGsn%2BFo%2BoYlYbdZDoWHqruqulNBhOO10XiSc6kPjofakXFntT9B7Y%2BgwAnia2BsY%2FCROhpjPDv4BYQFSrbapoLirUHrvW7WMMDEJ%2BqeowqxPQy9niL1%2BuQFT9S7OmyMET6cttkdJAqRrJQeSSxFQ7nBZNfGNN6Tb8Nbu33DIi04XJjmyc9COlvAotocyRPRLaq1LC%2BD%2FlTKo7qnPYDI8NQPLclZiTRXxl96GXqGTKDl6KGKz2DHE2aE7jlyLK8ArRRgw93ybVvkE9Qr0tsY5tOR1bV9%2BEnIZS8qFnQcsSnlGzRP4yFBgbakBHNAKurR3p1U4NbieD%2BGL0WVjrR9hPHzONUiCyh7PGgg4Piz80P9ZmRUS4%2F0x%2BhvmZu31fI0i6btCL4MNGSqNAGOqUBiT%2FUMtkhVdL9INuy2lxv3vmFHHam3SSK1AO5SbL4nYcejeeM20slnzQSP2qNTVfbkAwip7pd%2F2W%2FLDBdqT%2Bqo7gS6WWcqeIbd1kCZnQ5iEBBdk73y8cC5t%2FJe0tiiB%2FhZx9lCX1rkZgtlHo7lbc2%2BxzAp0YuqYwhquyV2tjp8ilgbYenODt2t%2FOgj5p6XWZJm3NylnXjKzaTFS6MkKuPJZdQZdNE&X-Amz-Signature=9ecea7e48393f5fc358b8db4ee48e37edfaca583443fd85a4909d59affacf03c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
