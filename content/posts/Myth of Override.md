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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XBZLOOM%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T005225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhz05URRajppOcrL0pVyIBYONgr8iRPWWMbodl5ikS9QIhAPt5O33iVBEeCVjKIztWh%2BC%2FHT96%2BhLDMNKMpKAufOqKKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxfPSaZLFUIYTDvh0q3APCOKRyenAVl%2Fzp9ZEJxTLS27C%2B9dn1uW6QshL9tzrE%2FWXELqQY0F56pYgRKYZiwmg387dCCX%2BT5OtKPZgilOyyD2wbZJl8pHZdhCSqv9JIVxMDHZcX5Cu9ofmOny%2FDix6O7ISYmnMfrtDb7hObzahw1k6dGhRCVvbdBnZ9NgBzxW%2FWEQmIz7Lysh0KRrm%2FJM5%2BRzO%2F4vmprlG4KuFIyLTSvctZ4at9qHrtCugqctBXibDyUjX%2Bxw9VjVYfLKPsrExnXfQKU1Mp15uKhOqAyFcuWgoACueT3H8q%2B2n3aDPH9a%2B5lX8%2FjCaDgRCXNhLhDBzDBRFR2xACOuhThg0t7Fo%2FvibqiGvg0UD0zMcCRRP9Sun%2BPe8e1R9P6bJyEN6MG6sVXSi3u4R%2Fe86eS5tLm2nKDRP6I1nKXHIoT8dWe3nl9UQrWOMCYwiqa79TSjD%2FIFQVnwnDvcqHhgu1KHLSXYySd7UO54HEPmIjcn81MVv3MuLfB7ewKau65shb9R0YpzoPNIQWQOA5GZp84CLH4%2F%2BFYAoFBu3cm1iGOBiHdvkQE5HWWP80abyzS3uKueZ6oNn6Br4Nmog7HsaLPUqjWk9syhIZggUoWnI%2FjlcmtU7UNP1GCTbhb77pbLtVuTDxidjUBjqkAUU%2FEbKfYLoAPClXfCTRPd%2BS%2FdiEcOj9u38TIR2uLpg6DU9%2FYyFHM3Aj1Ysi28wnsSxHPUPGDkerekSDRoWFCYG7d2%2FpkPVRmSsAlaK327beXVQPA5eWJ3xF6%2BSBzjL1Q9vDd7y%2FJ6KW7Y5DFzwz6luhqI73FL1E8QToI79KZgr%2FQftRxs0MrZmK73cV64ZxRFvaotqarSa1towQpUKabkkONIFP&X-Amz-Signature=4169382add265f7defebd8b7183eaa9475b4e4daed860ad340e8962b86c7e4f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XBZLOOM%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T005225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhz05URRajppOcrL0pVyIBYONgr8iRPWWMbodl5ikS9QIhAPt5O33iVBEeCVjKIztWh%2BC%2FHT96%2BhLDMNKMpKAufOqKKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxfPSaZLFUIYTDvh0q3APCOKRyenAVl%2Fzp9ZEJxTLS27C%2B9dn1uW6QshL9tzrE%2FWXELqQY0F56pYgRKYZiwmg387dCCX%2BT5OtKPZgilOyyD2wbZJl8pHZdhCSqv9JIVxMDHZcX5Cu9ofmOny%2FDix6O7ISYmnMfrtDb7hObzahw1k6dGhRCVvbdBnZ9NgBzxW%2FWEQmIz7Lysh0KRrm%2FJM5%2BRzO%2F4vmprlG4KuFIyLTSvctZ4at9qHrtCugqctBXibDyUjX%2Bxw9VjVYfLKPsrExnXfQKU1Mp15uKhOqAyFcuWgoACueT3H8q%2B2n3aDPH9a%2B5lX8%2FjCaDgRCXNhLhDBzDBRFR2xACOuhThg0t7Fo%2FvibqiGvg0UD0zMcCRRP9Sun%2BPe8e1R9P6bJyEN6MG6sVXSi3u4R%2Fe86eS5tLm2nKDRP6I1nKXHIoT8dWe3nl9UQrWOMCYwiqa79TSjD%2FIFQVnwnDvcqHhgu1KHLSXYySd7UO54HEPmIjcn81MVv3MuLfB7ewKau65shb9R0YpzoPNIQWQOA5GZp84CLH4%2F%2BFYAoFBu3cm1iGOBiHdvkQE5HWWP80abyzS3uKueZ6oNn6Br4Nmog7HsaLPUqjWk9syhIZggUoWnI%2FjlcmtU7UNP1GCTbhb77pbLtVuTDxidjUBjqkAUU%2FEbKfYLoAPClXfCTRPd%2BS%2FdiEcOj9u38TIR2uLpg6DU9%2FYyFHM3Aj1Ysi28wnsSxHPUPGDkerekSDRoWFCYG7d2%2FpkPVRmSsAlaK327beXVQPA5eWJ3xF6%2BSBzjL1Q9vDd7y%2FJ6KW7Y5DFzwz6luhqI73FL1E8QToI79KZgr%2FQftRxs0MrZmK73cV64ZxRFvaotqarSa1towQpUKabkkONIFP&X-Amz-Signature=b9aea5372d43f1f4383d1f269aa4a97639af54e97db435bb3c71d7ba8420158b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
