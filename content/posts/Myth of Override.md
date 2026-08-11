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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YH5FGUVD%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T104111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICas%2F9GxtmyN%2FdEqkcgSsr6w7R5djU1vroLjGtmrObC4AiEAh%2BbIeY0wm3o%2FMuYNWaYm46UAhm3aGhEZhg4PtI58frAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETZbl6qeKC7PfGK8CrcA%2BGqJOdJYcxArE%2BBK%2BNpkVlHgjlOp3DAUFLx%2FpCuQL13YVzcqdnwmN6YsOFCrZG%2BR4njzNg36VXDUwdXkqSBSYtNww6fNTIAcoyXt5%2BJg2USZQ%2BL2%2BHH1RIE7u2oud8RfbE2L1QWpvCEqoh8TDyHktIxCaR7AFIYoalQk71bEtt%2Fc3XTD7C3zG4nda0FNLyJ4r%2BggbfSyR1qMZ7XHVD7cW93zJGfkcsVSBK147zNAzgaKDFBVyje%2B%2FU6RCPZNO2bqhQ4Jv6AhenBcFWJqJUssb07dnvGlgWa1MPWWeEj1tl2kmwoCpMSP7%2FGkikllgZcBL%2B1Fm3Zp087e7g6ocvOdUgerOu8NAIP4pRLAuxitCI5ZpJO%2BJrbYmrW7Pbzar0Po5EVxdNxqXtASW56Ay%2Bmq0pYlNAdpL6y2J1NWBltPdqyisa0DhHVsTD06xUCZPyr4SnZTgCDzDl0LvudjqOjN8uFGoU2oGJqEk5a5K2wEzjX02EefMYN99CMyHIuzWYUjTWbA8BKVvkFes5hSqzc6clCSKATceTvWPqwXWD4U%2FezGonf%2F2r%2BRV6%2BjScP2JZaB9oT1ud4r8HFF2vzZhpT2%2FkD1nnSDpJKJFglki7JJ%2BZAnhkH3qrpdVZ4XvMfMLLO69MGOqUBQ9%2B5nMJjdJnR6qPRENY9EGqeibZmMK9hF53Fv9XKrMrm6cD2p3vM1Q6j2QyBa0MUkhTgrXVeEBnZF%2FNm3xlFtuzvtHzhmCPc5Ys926%2BtKdDvfFOxDAmn10rma4%2FVVcXuFU5YSmdu8nLHWkxAWitHb%2FQ2wK6JSMz3OMglg3yptzU4G2OIc6UobuK1aA%2FmFlOMBV6g%2BpHNyAraB4HRBQavhsXLgRXd&X-Amz-Signature=82f17ce125c49f8dcb60689dd9447c69a2b8cfec2cf76dc3dd1ef3bf65a0732c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YH5FGUVD%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T104111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICas%2F9GxtmyN%2FdEqkcgSsr6w7R5djU1vroLjGtmrObC4AiEAh%2BbIeY0wm3o%2FMuYNWaYm46UAhm3aGhEZhg4PtI58frAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETZbl6qeKC7PfGK8CrcA%2BGqJOdJYcxArE%2BBK%2BNpkVlHgjlOp3DAUFLx%2FpCuQL13YVzcqdnwmN6YsOFCrZG%2BR4njzNg36VXDUwdXkqSBSYtNww6fNTIAcoyXt5%2BJg2USZQ%2BL2%2BHH1RIE7u2oud8RfbE2L1QWpvCEqoh8TDyHktIxCaR7AFIYoalQk71bEtt%2Fc3XTD7C3zG4nda0FNLyJ4r%2BggbfSyR1qMZ7XHVD7cW93zJGfkcsVSBK147zNAzgaKDFBVyje%2B%2FU6RCPZNO2bqhQ4Jv6AhenBcFWJqJUssb07dnvGlgWa1MPWWeEj1tl2kmwoCpMSP7%2FGkikllgZcBL%2B1Fm3Zp087e7g6ocvOdUgerOu8NAIP4pRLAuxitCI5ZpJO%2BJrbYmrW7Pbzar0Po5EVxdNxqXtASW56Ay%2Bmq0pYlNAdpL6y2J1NWBltPdqyisa0DhHVsTD06xUCZPyr4SnZTgCDzDl0LvudjqOjN8uFGoU2oGJqEk5a5K2wEzjX02EefMYN99CMyHIuzWYUjTWbA8BKVvkFes5hSqzc6clCSKATceTvWPqwXWD4U%2FezGonf%2F2r%2BRV6%2BjScP2JZaB9oT1ud4r8HFF2vzZhpT2%2FkD1nnSDpJKJFglki7JJ%2BZAnhkH3qrpdVZ4XvMfMLLO69MGOqUBQ9%2B5nMJjdJnR6qPRENY9EGqeibZmMK9hF53Fv9XKrMrm6cD2p3vM1Q6j2QyBa0MUkhTgrXVeEBnZF%2FNm3xlFtuzvtHzhmCPc5Ys926%2BtKdDvfFOxDAmn10rma4%2FVVcXuFU5YSmdu8nLHWkxAWitHb%2FQ2wK6JSMz3OMglg3yptzU4G2OIc6UobuK1aA%2FmFlOMBV6g%2BpHNyAraB4HRBQavhsXLgRXd&X-Amz-Signature=771559759859b816cada130c4737a161c5d191600863fc6e733d33af0a03fbd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
