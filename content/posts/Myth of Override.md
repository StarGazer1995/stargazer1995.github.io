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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD4EPBJB%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T031627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnhskw6ABGoUilQZSY0N0Fx2ac6l9j39x2SPytfbDxqAiEA4USStv4c9UGLJ7FY2YMa4fJZFO6NRb0Qkl5eNiYtBYUq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDAIGUqR8JyLE2qihoCrcA4qRmFK2PZWW1%2FwJacDC59%2B4xb6xtH7UAPYegEaFe9QIcCJY3dlha9%2Fk6pJjWASCdc9Oyp6zGj%2BnseUslfjOjGaxOxSFFRNFlDnNagCPyRMGUwxity4Jf1YGlpg7hQJsy6ndXW%2FqAh2C0xSpRgv37p33zq6mPc1EL9d3ohETFcciVdR%2FgG1OHf3196uzzbAiiK9ksKJn20qqhYQIN9ZhSy7JFlrnjTbU%2FdrUvApLyQhEt4Rngd2doNqcn%2Bh%2BD59sBHtq3pyqpJzENklNRbVsswx8ZPjPGH93fEnxtkAw4XxEqA9OrhjuSPNNea9g4JLosz%2BdRu48KH2FpuqMDEj%2BQJf%2BblQI3bNEIAZa0Cl5ytbR9zUhflGXT2HE3jeYCQoSbKYGoshqvUwujVWFEIXjLGVTEc0O%2F2MacTqLhDX0gNGZjbV0BhF%2F%2FBINc1PYs91zMH9WQfZ6dPrxBxgOxYeo4fxX9fdxJ0yzik2TP6pC19FOQSLqvUDx7GWDUrwa6sOubwdPHnwVx5RKOiMN0C0PLlCNrQrLQO0sgnr1o2M2FzNXN1o%2Fb4h%2BVDN251gcdDZdyZzz%2FR12OSHyRiUwdTT6qIK2JKsSIF13gzBpyBYSCCYlgDQygPsn%2FSJrOEPXMI2t2tMGOqUBf6LwZSzJw%2BSK7h64FhM0n3fB4ohU5UEMDBrFlnoulDP88IceVSD9RGqJdo3%2FlkVI%2BWW7Tg40US8LFD8mBxXwOXe08kKP4AVRJfeY8lftLpwqBncIUpFzKPEoptm6NrwCn2U1uMtUC4K6OSbzKpvczn6wn%2BnObc%2Fc9QWqdIy7NFdWyhS6PLAA4Tmrw3N6cfIvD2TxeKS1i5qEhcJSK59dRthHhQFZ&X-Amz-Signature=0dcc9d391fd8f85beb750d2b7e6c549345fbc4cb396c6f792386cff69ad8fcd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD4EPBJB%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T031627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBnhskw6ABGoUilQZSY0N0Fx2ac6l9j39x2SPytfbDxqAiEA4USStv4c9UGLJ7FY2YMa4fJZFO6NRb0Qkl5eNiYtBYUq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDAIGUqR8JyLE2qihoCrcA4qRmFK2PZWW1%2FwJacDC59%2B4xb6xtH7UAPYegEaFe9QIcCJY3dlha9%2Fk6pJjWASCdc9Oyp6zGj%2BnseUslfjOjGaxOxSFFRNFlDnNagCPyRMGUwxity4Jf1YGlpg7hQJsy6ndXW%2FqAh2C0xSpRgv37p33zq6mPc1EL9d3ohETFcciVdR%2FgG1OHf3196uzzbAiiK9ksKJn20qqhYQIN9ZhSy7JFlrnjTbU%2FdrUvApLyQhEt4Rngd2doNqcn%2Bh%2BD59sBHtq3pyqpJzENklNRbVsswx8ZPjPGH93fEnxtkAw4XxEqA9OrhjuSPNNea9g4JLosz%2BdRu48KH2FpuqMDEj%2BQJf%2BblQI3bNEIAZa0Cl5ytbR9zUhflGXT2HE3jeYCQoSbKYGoshqvUwujVWFEIXjLGVTEc0O%2F2MacTqLhDX0gNGZjbV0BhF%2F%2FBINc1PYs91zMH9WQfZ6dPrxBxgOxYeo4fxX9fdxJ0yzik2TP6pC19FOQSLqvUDx7GWDUrwa6sOubwdPHnwVx5RKOiMN0C0PLlCNrQrLQO0sgnr1o2M2FzNXN1o%2Fb4h%2BVDN251gcdDZdyZzz%2FR12OSHyRiUwdTT6qIK2JKsSIF13gzBpyBYSCCYlgDQygPsn%2FSJrOEPXMI2t2tMGOqUBf6LwZSzJw%2BSK7h64FhM0n3fB4ohU5UEMDBrFlnoulDP88IceVSD9RGqJdo3%2FlkVI%2BWW7Tg40US8LFD8mBxXwOXe08kKP4AVRJfeY8lftLpwqBncIUpFzKPEoptm6NrwCn2U1uMtUC4K6OSbzKpvczn6wn%2BnObc%2Fc9QWqdIy7NFdWyhS6PLAA4Tmrw3N6cfIvD2TxeKS1i5qEhcJSK59dRthHhQFZ&X-Amz-Signature=527079043367c0f423d8746be04ea8757fcad742a6b473add2504b77b8a40d81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
