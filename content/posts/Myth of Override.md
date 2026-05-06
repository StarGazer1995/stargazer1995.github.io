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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ4W5MF3%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T132707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8TWdLhR79IouzuhUaoY4h%2Brz02JpMekbRxny6XHXp3AiEAtRd5rtYhdpioq3QYGB5qVhvYAUVuV%2Fx1JI9CONF9eRAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFXrDQZEU6TsavMEyrcA9qA3QMmrjG6zzWkwcJtUpl8uFMfOLhlwctsJIh34tEugjIvvKY%2BGU%2BgiV%2BpV6ICUbt%2B5%2Fz%2BBJmlURpJvEZyGlnTnpsu9LAke%2FEhyuU2W3jC0qwyTj7Xub%2F4mDU%2BLmcVoexLMVF8oggHNvepVILN2r225nTVYEdtlBCU7tC4vXpxLFLDkP4%2FythmZqQpzjlOLNuQ9OonoFnoHJBGFjw5QKXS1Oi7CUAu0BKMkCdCKTb89uC36Xmu%2FUVwDHG3FaTChMG%2BkZL1%2B1PUC7q0eZlBfS9AT2NVgdoHbCUd1hmpC8ZbJO74Dd%2Be6rSbessX2lrleW972%2FW8rlR2baYaILQ2Aq6EzRL9kmtxaddXe0nBZThtElWz0FEOI17AucjnLyFBzgIR0TeJUOomoQ%2F4vdJflLlFjzphIVjKL6a7%2B6%2FtU9mtpbu9JZTxrmLBy8wn%2Fqi43gpH3ThZ0OCs%2Fzu9YpSixzEQFzIfbST0g6%2FfFF%2Bs5%2FYnyHkVGjlhAplcf0JSGElESS9Sl8lGpFQKz3r%2B%2BWZItQD1%2FpatP66EYAr4LfLZJUESl%2BAvAjmLy9HDYMUvHX6Rp6OcP2c55C5JeM%2BnPIuuALaP%2FvclrP63HKt52Co%2BhsvAclV49%2BhCRo5aQCfhMJ7n7M8GOqUBz9VMqbyDXRX6X%2FOzsrByRZCRPg50wJoPZjI1LFPkqC6%2FtUfKRTLnYLkzLj2%2BSPDe%2BNuTBC6Igx%2F5w7caAjkkvnLebzEHZ%2FezZAzwU4aciAMjJd%2BlGCuniblYy6djxP3U4Xgc7HjQ5Cb44EFRLPVwI0QpwL9YpjRyHLAu8YdeeB67fvTCAi5Pe7rgNUY0Si60mjGN0HHOCXnZW7IpgHHxU2vnXLlQ&X-Amz-Signature=bff4162dba039262fc812e6c9d8d792c6d5c5ec32c9d3ef54e2c905c61cd2122&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ4W5MF3%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T132707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8TWdLhR79IouzuhUaoY4h%2Brz02JpMekbRxny6XHXp3AiEAtRd5rtYhdpioq3QYGB5qVhvYAUVuV%2Fx1JI9CONF9eRAqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFXrDQZEU6TsavMEyrcA9qA3QMmrjG6zzWkwcJtUpl8uFMfOLhlwctsJIh34tEugjIvvKY%2BGU%2BgiV%2BpV6ICUbt%2B5%2Fz%2BBJmlURpJvEZyGlnTnpsu9LAke%2FEhyuU2W3jC0qwyTj7Xub%2F4mDU%2BLmcVoexLMVF8oggHNvepVILN2r225nTVYEdtlBCU7tC4vXpxLFLDkP4%2FythmZqQpzjlOLNuQ9OonoFnoHJBGFjw5QKXS1Oi7CUAu0BKMkCdCKTb89uC36Xmu%2FUVwDHG3FaTChMG%2BkZL1%2B1PUC7q0eZlBfS9AT2NVgdoHbCUd1hmpC8ZbJO74Dd%2Be6rSbessX2lrleW972%2FW8rlR2baYaILQ2Aq6EzRL9kmtxaddXe0nBZThtElWz0FEOI17AucjnLyFBzgIR0TeJUOomoQ%2F4vdJflLlFjzphIVjKL6a7%2B6%2FtU9mtpbu9JZTxrmLBy8wn%2Fqi43gpH3ThZ0OCs%2Fzu9YpSixzEQFzIfbST0g6%2FfFF%2Bs5%2FYnyHkVGjlhAplcf0JSGElESS9Sl8lGpFQKz3r%2B%2BWZItQD1%2FpatP66EYAr4LfLZJUESl%2BAvAjmLy9HDYMUvHX6Rp6OcP2c55C5JeM%2BnPIuuALaP%2FvclrP63HKt52Co%2BhsvAclV49%2BhCRo5aQCfhMJ7n7M8GOqUBz9VMqbyDXRX6X%2FOzsrByRZCRPg50wJoPZjI1LFPkqC6%2FtUfKRTLnYLkzLj2%2BSPDe%2BNuTBC6Igx%2F5w7caAjkkvnLebzEHZ%2FezZAzwU4aciAMjJd%2BlGCuniblYy6djxP3U4Xgc7HjQ5Cb44EFRLPVwI0QpwL9YpjRyHLAu8YdeeB67fvTCAi5Pe7rgNUY0Si60mjGN0HHOCXnZW7IpgHHxU2vnXLlQ&X-Amz-Signature=45f3fe90bb3826ffa43dd522452827209feb8b7816ebc95d9c9dc1e30a76856c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
