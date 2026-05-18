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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KU5NB7%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T224720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICudfVg%2BLKJq5Vdjafw4cX4OtkovG%2F10BKW88tWx7ndRAiAnIozrw%2BTlMRuzxH7NaPkdQtz0eUmF%2Bt9tu83Immr5VSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7PfOu2jnFCPHvVVNKtwDA39rayRhYq1M9U5sRtItGiXDb63nrHqHm1Vt%2Bbs4FfgdkM5UVerIdkjlJzMrXbCX74Wv2vke4hvykLjnYEYQdUnAA0m6QzqNhMI1%2BhJqiMZBMgkRz6fBT5WYGT6R42tp8xLNgep2Q%2FRfiuM689BZ%2FYwOsWUQpFuGoOKqSnrmQapExEWq8dkmA9HVISgqK5nQVnpKLhrWDkjfo%2Bhn57ZPWzUflBZOeTyZvjGPVXgWYaYCdMV%2FgruehupiIUC1uhuOJopcc%2BRJ8Z757NOlSa9LBIh%2FQFU2%2BwtFvakftJoSCgp4jgOuDk7JuOvKdEwZdpgeBsvcHvgCbm%2BB1FX%2Btby5aPi7tBa8OtDTXQW4wXVM4ycFtJjGRS0ykLA8UaBq4%2FOUo6fnpoR3DeNcSnN5%2BUJ4WWZz95SVGkHar%2B64Lose2CNt5k1%2F93tmsYUrL3SZJY3e894H3weaE1az8SUVH0%2F1NcbwPpUERVctm0%2FQcYgZFRSieo4APQt7T%2BOlNJJrJijUpV03IJQTiDF1OkQ0aNmf24PEYOCMRoFpNAXp2GuaRpfQ7OIGmWQB6RtvfmEl72y4mTNFotD1JddcL8hVdm74iKGGecOMVjEmrQgDmQ%2BkW682y7wbvTq6weXQDfUw64Ou0AY6pgFJi%2F1qnF7QS0sa%2F2Gp7rq179yUxBUuxWMnWTMXU6KegaS8FqkRMxOQaSp%2BFqdpU6ftg8s6PilGOse%2FyJWqtdGjeTBM1Jbh3AnvpMlInxexs8kbg9uszS4OZHKFY03jPK3eWPCRI5X0w5AF9W%2BUSut57PvsDudDTSbXbp4SLikWNj8AgNRkio9Drya%2BwkwNKnai5WbP%2BcePgVMXpznue6YK%2FblOTBFe&X-Amz-Signature=bdc59d2d1471d4fe93b0d29361b72e64fe058cba85c0a18f4de9b34457ba6720&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KU5NB7%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T224720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICudfVg%2BLKJq5Vdjafw4cX4OtkovG%2F10BKW88tWx7ndRAiAnIozrw%2BTlMRuzxH7NaPkdQtz0eUmF%2Bt9tu83Immr5VSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7PfOu2jnFCPHvVVNKtwDA39rayRhYq1M9U5sRtItGiXDb63nrHqHm1Vt%2Bbs4FfgdkM5UVerIdkjlJzMrXbCX74Wv2vke4hvykLjnYEYQdUnAA0m6QzqNhMI1%2BhJqiMZBMgkRz6fBT5WYGT6R42tp8xLNgep2Q%2FRfiuM689BZ%2FYwOsWUQpFuGoOKqSnrmQapExEWq8dkmA9HVISgqK5nQVnpKLhrWDkjfo%2Bhn57ZPWzUflBZOeTyZvjGPVXgWYaYCdMV%2FgruehupiIUC1uhuOJopcc%2BRJ8Z757NOlSa9LBIh%2FQFU2%2BwtFvakftJoSCgp4jgOuDk7JuOvKdEwZdpgeBsvcHvgCbm%2BB1FX%2Btby5aPi7tBa8OtDTXQW4wXVM4ycFtJjGRS0ykLA8UaBq4%2FOUo6fnpoR3DeNcSnN5%2BUJ4WWZz95SVGkHar%2B64Lose2CNt5k1%2F93tmsYUrL3SZJY3e894H3weaE1az8SUVH0%2F1NcbwPpUERVctm0%2FQcYgZFRSieo4APQt7T%2BOlNJJrJijUpV03IJQTiDF1OkQ0aNmf24PEYOCMRoFpNAXp2GuaRpfQ7OIGmWQB6RtvfmEl72y4mTNFotD1JddcL8hVdm74iKGGecOMVjEmrQgDmQ%2BkW682y7wbvTq6weXQDfUw64Ou0AY6pgFJi%2F1qnF7QS0sa%2F2Gp7rq179yUxBUuxWMnWTMXU6KegaS8FqkRMxOQaSp%2BFqdpU6ftg8s6PilGOse%2FyJWqtdGjeTBM1Jbh3AnvpMlInxexs8kbg9uszS4OZHKFY03jPK3eWPCRI5X0w5AF9W%2BUSut57PvsDudDTSbXbp4SLikWNj8AgNRkio9Drya%2BwkwNKnai5WbP%2BcePgVMXpznue6YK%2FblOTBFe&X-Amz-Signature=c1a209884f48ff7dd0c58936f79be7e02f0c36f2b95ecbf21ad5e468fa883068&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
