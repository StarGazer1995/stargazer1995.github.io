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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPBLA4OH%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T152035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIEuC4L7hrIsNod2I6eoS1Pk0bVZIaVoKlFNyce4EH5vKAiEAt4LH4wsAvk0zen%2BqgmFjEIyRH%2BLw9kbSg3%2FVZHLbTloq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDP6PqR%2FebhDhc8wtCyrcA%2Bs%2FYr6T2OPcXNlBAPmBpdApGWzVJk2PQ7DzYILSt7lRxJ4pEfeF89EFqKyg7HatXLRFdfdCdbcOeVofM1vxV6cH84LwYEhJGT5ExcAAfvQZttsV%2BceRmt%2BpnNLxO3Fx6T6SPILOdo7N172wvtVCpVdA%2BPGTJH4qL7TfznRtxGFJsRFJwLGl6l8ZfN4PDJ%2FzNsPQQQHPx3K2zPC632msA3NgTzIvYy%2FIlrSjLi%2FWJ5nUukBOAQjB%2B5JpZKvUG%2By%2B7Qpb8mBimzW5FZ0Y2%2B9P%2FlsTg1ef0a4YW70yae2baC7X3HL0c1jnpPglEn5KqyH3IYW3JnvlWsIGlChMLvzmg8Q3YpItib71f0VCo%2FbSI%2F%2FEDGXr%2BNFcgZOePqMTTJnYItrasT%2BfG%2FFZyKpTzYU7VipcqccKLuSrmCjqmmVDxrv3XNHQTvxdxPIAl4Fgmuy6nWdhuFtXlg7UZAVFkPjW4Y6xqLotLXGSg80FCEN06dl9%2FH3T5NA87m5wxQOv9Gisf1CCnSh82AW3g8GWfYwIof70OoucIQ2UYk2Qq%2Fi7tmml6kiVaRBHAeUvN8q0BXU92RBX9y6wSzvTBb3EaPhLc%2B%2FYZYwPcncTXQxifEzsJyBpHzA9vaDUTfr3HpOOMI3%2FjdMGOqUBog8ePM2GKgBtITRN3UkV%2F4aGzEignJ7or0luvm9gwgWFOWzhLmYIJMImvmQsx8B7mOko7%2ByTBqXNcNwgifmoda5A9XRzeerxDxDRWIej%2B9J0%2FeNUyf6qsHpZU0rrAsdCSku3mrRr2LLBrVBPv2QtNCRVG23xFtmJ%2Fjb8CcPru5PKOeQfnWtMDwq6QnJ6NZXXEF2tsbdt63GuD3lqHYeV3jofYOsQ&X-Amz-Signature=fbd55d75bad285961c99ccdc3c49c353d68af54caa517bf18e51a9ecb3d565f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPBLA4OH%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T152036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIEuC4L7hrIsNod2I6eoS1Pk0bVZIaVoKlFNyce4EH5vKAiEAt4LH4wsAvk0zen%2BqgmFjEIyRH%2BLw9kbSg3%2FVZHLbTloq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDP6PqR%2FebhDhc8wtCyrcA%2Bs%2FYr6T2OPcXNlBAPmBpdApGWzVJk2PQ7DzYILSt7lRxJ4pEfeF89EFqKyg7HatXLRFdfdCdbcOeVofM1vxV6cH84LwYEhJGT5ExcAAfvQZttsV%2BceRmt%2BpnNLxO3Fx6T6SPILOdo7N172wvtVCpVdA%2BPGTJH4qL7TfznRtxGFJsRFJwLGl6l8ZfN4PDJ%2FzNsPQQQHPx3K2zPC632msA3NgTzIvYy%2FIlrSjLi%2FWJ5nUukBOAQjB%2B5JpZKvUG%2By%2B7Qpb8mBimzW5FZ0Y2%2B9P%2FlsTg1ef0a4YW70yae2baC7X3HL0c1jnpPglEn5KqyH3IYW3JnvlWsIGlChMLvzmg8Q3YpItib71f0VCo%2FbSI%2F%2FEDGXr%2BNFcgZOePqMTTJnYItrasT%2BfG%2FFZyKpTzYU7VipcqccKLuSrmCjqmmVDxrv3XNHQTvxdxPIAl4Fgmuy6nWdhuFtXlg7UZAVFkPjW4Y6xqLotLXGSg80FCEN06dl9%2FH3T5NA87m5wxQOv9Gisf1CCnSh82AW3g8GWfYwIof70OoucIQ2UYk2Qq%2Fi7tmml6kiVaRBHAeUvN8q0BXU92RBX9y6wSzvTBb3EaPhLc%2B%2FYZYwPcncTXQxifEzsJyBpHzA9vaDUTfr3HpOOMI3%2FjdMGOqUBog8ePM2GKgBtITRN3UkV%2F4aGzEignJ7or0luvm9gwgWFOWzhLmYIJMImvmQsx8B7mOko7%2ByTBqXNcNwgifmoda5A9XRzeerxDxDRWIej%2B9J0%2FeNUyf6qsHpZU0rrAsdCSku3mrRr2LLBrVBPv2QtNCRVG23xFtmJ%2Fjb8CcPru5PKOeQfnWtMDwq6QnJ6NZXXEF2tsbdt63GuD3lqHYeV3jofYOsQ&X-Amz-Signature=33265da2534807acfacdf03f0736a08ab89551475e0abaa62d915bf237676dee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
