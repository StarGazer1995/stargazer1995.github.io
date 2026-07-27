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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S4RGC7T%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T092413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwf5pDJzIJswxXEmWaw5GzsUz6pXq0gUhW4AfY%2F9VuoAIhAI6TbX%2Bghe1gFARE0AGmoGoNhgTC1JCmQ9%2B371lktoRWKv8DCEoQABoMNjM3NDIzMTgzODA1IgyccUkjqjGCqT3DTN8q3AOUjYzJHBrzr2f3dNddCAngrh%2BFpXlbFCNyAVxuWjezkozkgnTVtBux%2FqwFXv2Xdkq7fnDIvym9am7pkE616yaYAOFWu2pyBpGT%2Byx%2Ftm3m%2BvVD3y99fuJdLR4%2Bus1YgwcvAkUk8%2FYjdKl46GMdxgZj08UudnyO%2FpyxyQP9BeSvL19uV6HPPpkOXl1ucycv1bowlm7SwlI%2BZLjib092Foe18mJjFzL5tKTUhkyHc0klmoRvpnXb08C7lC3VMsml0%2FkM8SnbE4x037EgJktrXA5vyxrWMauwWF9gUIn%2BD%2Fbh%2FpXMq%2BKu9LEnh2MkFTNQ85PRyo3ca7o4pYoHcgBabruUKIZaenN0mB60RI1ylavcjEK%2BBX6rvxgP%2B0aUi%2FTU3v3BVwYrkcTgz7m6i3oP3HQSuAFoK6bYaNf53xWs5DVPqb1aWwZxwz9s6faxGVHSFhI764xpApT4d5VZmNNiU9%2BcmRoDTN5CQ2dcYma2ktDidp2RlcuqeHHwbFrzG4QYZ3T5RS11xkzYeR%2FD1hZ%2FyRQ3vvya5DsxflWXf1mNxwmlZokjQOn3%2Bu18T%2BdDWU2fepoaQK6ndV1gedaI3nr4jjlmvBEYoLy5x3sfqrG7YQh33K9WDM2PPGLiSA2J8DCbtJzTBjqkAWSE1oIbMRw2a53SSPlESEsJISNGGKRt%2FU6UNp8VJaQ6SqgjOmNq6AM%2BtQzhG%2FlB%2BLOQTLSOpgOYYoYokJqz2%2BDQjiEny%2BmOFsU90JlcXTEsBBBzcXnmrTlTEVMyNkW2RKTLFnCuvN4k07XqvJneoi6Z5mHbOxXeP03EtoLDcAB1jq5kDB31knsRL1TPdAjwzWQwI6EtmMpiWukRxq%2FOcN7x%2B7iO&X-Amz-Signature=f55dc70c773fcb1ae7a01d640edfe5a057878a0bdeda2a3fafadfe9b039b0957&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S4RGC7T%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T092413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwf5pDJzIJswxXEmWaw5GzsUz6pXq0gUhW4AfY%2F9VuoAIhAI6TbX%2Bghe1gFARE0AGmoGoNhgTC1JCmQ9%2B371lktoRWKv8DCEoQABoMNjM3NDIzMTgzODA1IgyccUkjqjGCqT3DTN8q3AOUjYzJHBrzr2f3dNddCAngrh%2BFpXlbFCNyAVxuWjezkozkgnTVtBux%2FqwFXv2Xdkq7fnDIvym9am7pkE616yaYAOFWu2pyBpGT%2Byx%2Ftm3m%2BvVD3y99fuJdLR4%2Bus1YgwcvAkUk8%2FYjdKl46GMdxgZj08UudnyO%2FpyxyQP9BeSvL19uV6HPPpkOXl1ucycv1bowlm7SwlI%2BZLjib092Foe18mJjFzL5tKTUhkyHc0klmoRvpnXb08C7lC3VMsml0%2FkM8SnbE4x037EgJktrXA5vyxrWMauwWF9gUIn%2BD%2Fbh%2FpXMq%2BKu9LEnh2MkFTNQ85PRyo3ca7o4pYoHcgBabruUKIZaenN0mB60RI1ylavcjEK%2BBX6rvxgP%2B0aUi%2FTU3v3BVwYrkcTgz7m6i3oP3HQSuAFoK6bYaNf53xWs5DVPqb1aWwZxwz9s6faxGVHSFhI764xpApT4d5VZmNNiU9%2BcmRoDTN5CQ2dcYma2ktDidp2RlcuqeHHwbFrzG4QYZ3T5RS11xkzYeR%2FD1hZ%2FyRQ3vvya5DsxflWXf1mNxwmlZokjQOn3%2Bu18T%2BdDWU2fepoaQK6ndV1gedaI3nr4jjlmvBEYoLy5x3sfqrG7YQh33K9WDM2PPGLiSA2J8DCbtJzTBjqkAWSE1oIbMRw2a53SSPlESEsJISNGGKRt%2FU6UNp8VJaQ6SqgjOmNq6AM%2BtQzhG%2FlB%2BLOQTLSOpgOYYoYokJqz2%2BDQjiEny%2BmOFsU90JlcXTEsBBBzcXnmrTlTEVMyNkW2RKTLFnCuvN4k07XqvJneoi6Z5mHbOxXeP03EtoLDcAB1jq5kDB31knsRL1TPdAjwzWQwI6EtmMpiWukRxq%2FOcN7x%2B7iO&X-Amz-Signature=c72dd3847f630d872ea8c2d07b72f144ad5c3282dc5b6b1d256f841a1eeedcdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
