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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FCQRKIN%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDvuB5ba8%2F1DLAcw0w3mTIM%2B6jkl0NHtosA3HGFne%2BeXgIhAMV4RXp19SoupQ121WHHCY80KUpupdYoFYGnCN1OGPoJKv8DCAAQABoMNjM3NDIzMTgzODA1IgzuraytksJw7JwFlpEq3AP2RYV3igyf5hyvoplv%2FQnYeZM7n6Mwde05M4hcJzhiOd7uJCajZPBNY1YuIWXUlQ1YhFDZqTab6aZZ3TkIdVg1Pu1XSYKdmVL3PQhSend3QxO9RTfnv8Vn6W2CK6wJYowBgym%2BIZy416%2F16az3V4B66sUn%2BuSmtShXB5uB9jgYBXPXSNI1NzS%2FsXtAKhUhUaTqxI03K6LfhRD90jOJ1nIbokEuDIT8Kgm9%2Ft5L3cjzmZERcI%2F4mTtF5TbPnG493W7j2eZkFXtkzh5H8%2BVWZUsiME4y1Q5I0TGZzNHnE%2FooHk7GI%2FnhxG%2BMxPalXAK%2Fc6wLhaUgYx3LrjiLgViq7x%2BUXbgzKpHc%2BPIgUXmSc7wT4CNmY09cV7sLWc7ONoYoh%2FeroE%2By0Qhdu2xyoZyDyO7HFQcuQqlNNmiqqFPsngnTN98UubMoq1SayIzINCNeEF49CiDL0TOwOT22dyK2zO2L9KwjVfnDz%2FKWQp8GtyeYFq54fEUzjS0IexHYuCIJZ5YQk5Trm%2F%2BcwICj0AuxP4RCrj1CYNExHvqAzxoSqZcuKjMA45Zob23am%2BhGHrwiNYXuaqmcdC%2FpCHtnw%2FJNa5Xbs44G%2BExfJ7rHfUDrram2Rm1MZ%2FA7EnaYPDUkYjDW0pvSBjqkAWLUZLB0SaVOUl5mNc7POXEMgPPX6hx4MOiryIIrmpCJd1HV4YHJ1WJbweqWcwWCQ3NfyXgnstr3t%2FA8k3i1vbPoUoJUmcOYecFQb%2FdmqIaay2ExcrEq7gVEPjMgXDlJ5WpKqPPvfhIhqE9DksrTxcPPWqSK05EA9voYRm4GHzzjvNiPiWDHkT413jRK2i8uqBfWeuEs0AQWnb2taMelJoIYtLyy&X-Amz-Signature=78c4bfa86b6ac06ce392737a5f41c3f7c5710374dab7e52e8a1d169340290967&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FCQRKIN%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDvuB5ba8%2F1DLAcw0w3mTIM%2B6jkl0NHtosA3HGFne%2BeXgIhAMV4RXp19SoupQ121WHHCY80KUpupdYoFYGnCN1OGPoJKv8DCAAQABoMNjM3NDIzMTgzODA1IgzuraytksJw7JwFlpEq3AP2RYV3igyf5hyvoplv%2FQnYeZM7n6Mwde05M4hcJzhiOd7uJCajZPBNY1YuIWXUlQ1YhFDZqTab6aZZ3TkIdVg1Pu1XSYKdmVL3PQhSend3QxO9RTfnv8Vn6W2CK6wJYowBgym%2BIZy416%2F16az3V4B66sUn%2BuSmtShXB5uB9jgYBXPXSNI1NzS%2FsXtAKhUhUaTqxI03K6LfhRD90jOJ1nIbokEuDIT8Kgm9%2Ft5L3cjzmZERcI%2F4mTtF5TbPnG493W7j2eZkFXtkzh5H8%2BVWZUsiME4y1Q5I0TGZzNHnE%2FooHk7GI%2FnhxG%2BMxPalXAK%2Fc6wLhaUgYx3LrjiLgViq7x%2BUXbgzKpHc%2BPIgUXmSc7wT4CNmY09cV7sLWc7ONoYoh%2FeroE%2By0Qhdu2xyoZyDyO7HFQcuQqlNNmiqqFPsngnTN98UubMoq1SayIzINCNeEF49CiDL0TOwOT22dyK2zO2L9KwjVfnDz%2FKWQp8GtyeYFq54fEUzjS0IexHYuCIJZ5YQk5Trm%2F%2BcwICj0AuxP4RCrj1CYNExHvqAzxoSqZcuKjMA45Zob23am%2BhGHrwiNYXuaqmcdC%2FpCHtnw%2FJNa5Xbs44G%2BExfJ7rHfUDrram2Rm1MZ%2FA7EnaYPDUkYjDW0pvSBjqkAWLUZLB0SaVOUl5mNc7POXEMgPPX6hx4MOiryIIrmpCJd1HV4YHJ1WJbweqWcwWCQ3NfyXgnstr3t%2FA8k3i1vbPoUoJUmcOYecFQb%2FdmqIaay2ExcrEq7gVEPjMgXDlJ5WpKqPPvfhIhqE9DksrTxcPPWqSK05EA9voYRm4GHzzjvNiPiWDHkT413jRK2i8uqBfWeuEs0AQWnb2taMelJoIYtLyy&X-Amz-Signature=01621c62de429b40f46acd396588c46dfa5a011f0bec4eb7cfc5cf5811cbb1ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
