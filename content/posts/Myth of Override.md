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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FQSEWPP%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIBALQldegR5KKK5%2FJ4pmWBaSzCG6doNCu2OHIxRkMmJyAiAL%2F6paBuBkAhBz7xq1WDxTfF%2BAqxMWA7VJD4LFwrKiAir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM4pjPfmT66tDXcA90KtwD9g%2F9xzbOSf5YVnseu84pV1s9LeZYSglwNY0ndZOlkYu2Xq85GHhB7993B0B6IXsMyyhsDQnxonVXRIjTyfpbBxE9Je2Fv3FdYRBFgc6yBJI3Xk%2B8DpBmNj1ZUpZ1HqHexQj%2BItqCqeZJjSpkPAWMkKAfHyLcnWvnKr31lEco4LI3uCq3wJ2k4L2KTOIFj%2BX%2Flrfe7wVJ%2BZ3QE3lpreMCMu%2FZgYq64IphyDY681%2FOz1VB5pfIvL2TrKhrvNYG5TGChJEB8uNBvby9iV4B9hACGkjha8x91Ta4pxVnr5Zju1%2BiR4KwoaQbjEHMKNfOgJR4LvT3JLHt2VGTn4eBCbgMuyZbVmK%2BWzr0K%2B%2FI3C%2FqsG7IG9NbF3eeNXWDDHHU8ntF2013IcndSyw9B%2FfEpRR1y1U0cAc5l4KmIOEt4YVHTqAWiH1%2BMhW2aClN6Pe%2B8z8ZIBrtlnCoTgdqVZw%2Fc919kG3cGkYf9DgaFPRi0dQvFOEGXhHYxEvpkE84VgfxyiETixocK6l9vP0bS4VhkDXy6bfGPy%2BXQMIkO2J8VyXNowXg7W1avTBDUfqt5lDWejaiGoM%2Fj4vPgVctr1vXzB0rma3owDJZexnn1sgP2xAGwJ%2Ba%2BBOSX5F42HlDEkAw%2B7vx0QY6pgGzaNm0gr9nSNTRAqahFY3BgbobSshayXIizqY3qf6l9lU4CS222al24hTURjWF7Q7LfsaSUY%2B3Q5I28cFTIcz5bkfLt7evYhcCfCDAnYMkxJ9ei%2FTtU9cvrNsqvQBZkXWTL%2Fb5CuJi8QBVQY%2FZutttUuHRTbodMfGBic3wSu25uAOSqGercc6MGCsSOFWhTFUNc9vLvE6hCUNPqxcA1ZSHFfYqbItV&X-Amz-Signature=d754d5ac3b1c513d5c8b6d87121a2ad676c222e001bec9ea6c27a5f7d47a4d7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FQSEWPP%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIBALQldegR5KKK5%2FJ4pmWBaSzCG6doNCu2OHIxRkMmJyAiAL%2F6paBuBkAhBz7xq1WDxTfF%2BAqxMWA7VJD4LFwrKiAir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM4pjPfmT66tDXcA90KtwD9g%2F9xzbOSf5YVnseu84pV1s9LeZYSglwNY0ndZOlkYu2Xq85GHhB7993B0B6IXsMyyhsDQnxonVXRIjTyfpbBxE9Je2Fv3FdYRBFgc6yBJI3Xk%2B8DpBmNj1ZUpZ1HqHexQj%2BItqCqeZJjSpkPAWMkKAfHyLcnWvnKr31lEco4LI3uCq3wJ2k4L2KTOIFj%2BX%2Flrfe7wVJ%2BZ3QE3lpreMCMu%2FZgYq64IphyDY681%2FOz1VB5pfIvL2TrKhrvNYG5TGChJEB8uNBvby9iV4B9hACGkjha8x91Ta4pxVnr5Zju1%2BiR4KwoaQbjEHMKNfOgJR4LvT3JLHt2VGTn4eBCbgMuyZbVmK%2BWzr0K%2B%2FI3C%2FqsG7IG9NbF3eeNXWDDHHU8ntF2013IcndSyw9B%2FfEpRR1y1U0cAc5l4KmIOEt4YVHTqAWiH1%2BMhW2aClN6Pe%2B8z8ZIBrtlnCoTgdqVZw%2Fc919kG3cGkYf9DgaFPRi0dQvFOEGXhHYxEvpkE84VgfxyiETixocK6l9vP0bS4VhkDXy6bfGPy%2BXQMIkO2J8VyXNowXg7W1avTBDUfqt5lDWejaiGoM%2Fj4vPgVctr1vXzB0rma3owDJZexnn1sgP2xAGwJ%2Ba%2BBOSX5F42HlDEkAw%2B7vx0QY6pgGzaNm0gr9nSNTRAqahFY3BgbobSshayXIizqY3qf6l9lU4CS222al24hTURjWF7Q7LfsaSUY%2B3Q5I28cFTIcz5bkfLt7evYhcCfCDAnYMkxJ9ei%2FTtU9cvrNsqvQBZkXWTL%2Fb5CuJi8QBVQY%2FZutttUuHRTbodMfGBic3wSu25uAOSqGercc6MGCsSOFWhTFUNc9vLvE6hCUNPqxcA1ZSHFfYqbItV&X-Amz-Signature=5ae358aa66c1cbb069dc7933316f788bdd01d791dda7244cca04b8536323b09c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
