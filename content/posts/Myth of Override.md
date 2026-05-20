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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NMKDJLU%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T020209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIFKcn31Fb6uyAKbHVBpZh6TwVZrR3ik9LfxVO4ZbUFN2AiATlcRDh7DD18RrFJjASiikDC1u0fdLdP3iBupRSYqTmyqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCJYORFCuCfFN3CK%2FKtwDGQfd3Xzk2cs2tJUP0skGnkCSidSwdZT11EyfUGy2M0GTydDKaVCq3dyxVCgR0k3%2FSekVdurF1S2ZtqYjsJBtm%2Fmxptg7CA7hqw8gyLVC7Tmk%2B0lzFK5NZkIA5SOEc5Tf6qjE%2FppxhJb030MzASYQb%2BgBq%2BLYmI5M4nj9eNzZox4Lvo5byXB3SGD67q%2BVC7W0qogFpmyy4BiLkQTTU71n7No3WNR0788UHLTZ7%2ByuR%2FK4jFRFa88z%2Fe98tEJXZBwhL7JfZFkIH0iIXZXBm8xw0Is4Wuth9qDtryW7Cr1ikkEEEUrgfjhzR6Q37ZeCRzUC%2FInHZsAcWmk%2B1OjlzrDvnD3m4kx5ol70jT2L5MeERsZeMAvPE%2BiTZDOPvXXy6d6UmEuUE3m1kEOKhoLyrfQHVQ62KvhMdhRpA0vuMudD12F8PnQVi7UEzLABhovq3bMFeUBU0nDipPCUjHtr7aBI962viw0jhavW%2FSDx2%2BmerpGxL9lBwwQdFz3Vfwyw5V2WW7zhMpGeiLYfHLKcZMdG7njBk6LFv3BuyZuI41DcWY44lKNNvXxCtU4%2BKzsiYuFxy7Cq3S6AWuyGvGeP2Dmuq3n7Emt%2FirEJs0cuZrZ9dHWu3KRfTfFDJxMjSmYw04u00AY6pgGPeIkr%2FhBvl5Xhuopu4qRKE5sfiAUuYH%2BokMgAIgRpWew0jEgOj9TtWHyexTRBPwvbj3ZkqXU30fqrpjQMUhK9YNk3avu7CIJhL1a%2Bb2oqrj2cnbuq%2BKv9TxnZxZjsS1DGs6Vv78IHHTDSiBNdpvIXcAwN%2BKAhuhywoOfWwBw%2Bjd%2FB3nCjLITj4kDK4nu7zqzGEhW6ES%2BD04Q%2FrGR6EFVbldT9kcsD&X-Amz-Signature=b922f2269f302c41e8f5a4ce084b30506543d0221851c946e7878d8eae1e50d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NMKDJLU%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T020209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIFKcn31Fb6uyAKbHVBpZh6TwVZrR3ik9LfxVO4ZbUFN2AiATlcRDh7DD18RrFJjASiikDC1u0fdLdP3iBupRSYqTmyqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCJYORFCuCfFN3CK%2FKtwDGQfd3Xzk2cs2tJUP0skGnkCSidSwdZT11EyfUGy2M0GTydDKaVCq3dyxVCgR0k3%2FSekVdurF1S2ZtqYjsJBtm%2Fmxptg7CA7hqw8gyLVC7Tmk%2B0lzFK5NZkIA5SOEc5Tf6qjE%2FppxhJb030MzASYQb%2BgBq%2BLYmI5M4nj9eNzZox4Lvo5byXB3SGD67q%2BVC7W0qogFpmyy4BiLkQTTU71n7No3WNR0788UHLTZ7%2ByuR%2FK4jFRFa88z%2Fe98tEJXZBwhL7JfZFkIH0iIXZXBm8xw0Is4Wuth9qDtryW7Cr1ikkEEEUrgfjhzR6Q37ZeCRzUC%2FInHZsAcWmk%2B1OjlzrDvnD3m4kx5ol70jT2L5MeERsZeMAvPE%2BiTZDOPvXXy6d6UmEuUE3m1kEOKhoLyrfQHVQ62KvhMdhRpA0vuMudD12F8PnQVi7UEzLABhovq3bMFeUBU0nDipPCUjHtr7aBI962viw0jhavW%2FSDx2%2BmerpGxL9lBwwQdFz3Vfwyw5V2WW7zhMpGeiLYfHLKcZMdG7njBk6LFv3BuyZuI41DcWY44lKNNvXxCtU4%2BKzsiYuFxy7Cq3S6AWuyGvGeP2Dmuq3n7Emt%2FirEJs0cuZrZ9dHWu3KRfTfFDJxMjSmYw04u00AY6pgGPeIkr%2FhBvl5Xhuopu4qRKE5sfiAUuYH%2BokMgAIgRpWew0jEgOj9TtWHyexTRBPwvbj3ZkqXU30fqrpjQMUhK9YNk3avu7CIJhL1a%2Bb2oqrj2cnbuq%2BKv9TxnZxZjsS1DGs6Vv78IHHTDSiBNdpvIXcAwN%2BKAhuhywoOfWwBw%2Bjd%2FB3nCjLITj4kDK4nu7zqzGEhW6ES%2BD04Q%2FrGR6EFVbldT9kcsD&X-Amz-Signature=87b50eff9f7294a7cb144a4d5cbc76150b16064eaed6dee6446594f435a9c43f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
