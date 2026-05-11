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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLH4U6SX%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T224532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQClritqAagEEmfUhxg%2FCzaiMiHeNDOB7qztDPTCJ%2BGMcwIhAKfVHLM%2BloPLJH8rpPpgZCwQEEyX3%2FIhIeGtzZz%2BdCqkKv8DCB8QABoMNjM3NDIzMTgzODA1IgwyFfyqrSAlPAWUlA8q3AOuA4JEHgUn9zZG0dRUmU%2BuSesLUc645gWrUMGPQcJfOxAiEzhinH8L%2Bq0Mw%2FG5uaukCyqcSChiw0MYqIudRSsXfC%2BRbbTo0Kip%2BQ3SKDj8m41t5fZuGmmZ4%2FSeW7%2FSdrzdDsxiPZHGtMOEs%2B0dcVKX%2FZfjoYdTqWNBPLCcDCd%2BefFt6eyCd%2FSkuvvnW0EVoyRiMeAa6FOfVj9S2aNkPfT5xndP4xkwndC9IxmD%2BtRJV0S5o7ap7L9thquitXmXq7y0Esm55EGgvV3c4RMDWFMVWzAi5WB3bFgvgXZlZxDV1LwWxnY3GsPZMh7ZMZlwYIoxllRTPRvcD5CdVn1RSqGad%2BjOSaRYRS3Yc0gzfGsDmswF%2BF9xwoV1yDSw%2Br7RB4sc5rRI3j4IOLYOZmDjfrgMtfD3z7DefHcHIqL%2FJXbnBuALW4c40cPk68Qd1C%2Ba8ZXjeoyARD%2FfMpqL%2BirVMZh94cirf26CzRZJ%2BcCrkxCxnX7nwxi4D%2F%2FvTa5WICCtlYv5kWkZWfcjm7vQ2HCvlXtrjb5F5pDjmlZ4X%2F9yi8ilLSa%2BzJeDS96bnN1WG9ECzQ3Kcm78hB4ZbfumuAFpHVasyjDxxXlX%2FV7XnoLzaZOWhTYnNggqv91usXDqBTDNq4nQBjqkAa3tF%2B18yVQFDsd1yP0PGwMBL4AU6A9JSrpzbQy084oeD1enUmC79zog7LZsgQEQwyoJD7QsXacBORVQJn5EY78UuQ29KMiy0cn4gKKPoHMj%2F4hnNqLp9c%2Bj9mb3rQf9QetdPcgs5hSs4xxKV8VmfymYnfIQO0ixxICm%2FfH5E5asiLwpGCCjS4PPYDpr9zFBqOVh89tmhWp9x8qP6Vv4Lndr3HPx&X-Amz-Signature=73c8b029a7b281c85c31b5019e02e1d92b177d79dc11ad26a73bdcaf9f326779&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLH4U6SX%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T224532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQClritqAagEEmfUhxg%2FCzaiMiHeNDOB7qztDPTCJ%2BGMcwIhAKfVHLM%2BloPLJH8rpPpgZCwQEEyX3%2FIhIeGtzZz%2BdCqkKv8DCB8QABoMNjM3NDIzMTgzODA1IgwyFfyqrSAlPAWUlA8q3AOuA4JEHgUn9zZG0dRUmU%2BuSesLUc645gWrUMGPQcJfOxAiEzhinH8L%2Bq0Mw%2FG5uaukCyqcSChiw0MYqIudRSsXfC%2BRbbTo0Kip%2BQ3SKDj8m41t5fZuGmmZ4%2FSeW7%2FSdrzdDsxiPZHGtMOEs%2B0dcVKX%2FZfjoYdTqWNBPLCcDCd%2BefFt6eyCd%2FSkuvvnW0EVoyRiMeAa6FOfVj9S2aNkPfT5xndP4xkwndC9IxmD%2BtRJV0S5o7ap7L9thquitXmXq7y0Esm55EGgvV3c4RMDWFMVWzAi5WB3bFgvgXZlZxDV1LwWxnY3GsPZMh7ZMZlwYIoxllRTPRvcD5CdVn1RSqGad%2BjOSaRYRS3Yc0gzfGsDmswF%2BF9xwoV1yDSw%2Br7RB4sc5rRI3j4IOLYOZmDjfrgMtfD3z7DefHcHIqL%2FJXbnBuALW4c40cPk68Qd1C%2Ba8ZXjeoyARD%2FfMpqL%2BirVMZh94cirf26CzRZJ%2BcCrkxCxnX7nwxi4D%2F%2FvTa5WICCtlYv5kWkZWfcjm7vQ2HCvlXtrjb5F5pDjmlZ4X%2F9yi8ilLSa%2BzJeDS96bnN1WG9ECzQ3Kcm78hB4ZbfumuAFpHVasyjDxxXlX%2FV7XnoLzaZOWhTYnNggqv91usXDqBTDNq4nQBjqkAa3tF%2B18yVQFDsd1yP0PGwMBL4AU6A9JSrpzbQy084oeD1enUmC79zog7LZsgQEQwyoJD7QsXacBORVQJn5EY78UuQ29KMiy0cn4gKKPoHMj%2F4hnNqLp9c%2Bj9mb3rQf9QetdPcgs5hSs4xxKV8VmfymYnfIQO0ixxICm%2FfH5E5asiLwpGCCjS4PPYDpr9zFBqOVh89tmhWp9x8qP6Vv4Lndr3HPx&X-Amz-Signature=e5ad595bf193e9c76c1a887c426e8093f798ceb0f323fe51e9ffde4a69d1eb0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
