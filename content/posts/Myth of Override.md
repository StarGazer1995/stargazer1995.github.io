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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NMP4MM%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T143610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfmBUWmhza7dR7IdX9mexcxFGxPs6vUc8ZpjEmAkVEPAiBCid17dwK%2BbhlY9yKqopFpoZzmv88JxAWPUv4cDUrnwiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjt04IjFeEkKS3xXBKtwDsjbVVwFQbQfg7Xvlw3eFroPcjCX0s8FKx8bE43rY7I8kdTKg%2FniYpIS9F5klRWzwd6Z0k5rpTj47hheHSVX%2BjueRxMzBr2gub44SkrRGG0eIiVL29MuCSQPaJn%2FZZFis3HZ0quwEiSjMF5J4T7enkBbI1fJdZZSqw6FesfcnrO2NQpX8peaXsjx8hQ3yzBn00vYziFRBMXNFOyob1l%2F%2FQ4zcGpeIOQ%2Fd80jGueWqZ167haXq2N%2BPj7y%2FIcHp4%2Bp0qZHU%2Bk38jJLo9zQD10Tpy9Oeud7zGrLSF0jdE%2BtL0kaeI9hsDw8SiTklQjYzZSyNVxdfeRVDv9ghtVmX%2FPIHcQHj%2BpPa6wPd4lq0Y2iROCJKAZh0hcQx71D0X2MjDFWGBvdzGiOmj3OzWqZBlRPo7bYWpMy5fZ%2FFS685WtHzagzieu1sKoZBSD3VagZxMRar7KasDEa5x6OoNPzmD%2BlMG4aggrseEe9wriCkRPEhYFZrdCqQzSHy7Q2JVPvNbfWa20hIEHiWvC%2BoNZzRg%2BH9QqR6L%2F2ZS%2BwkrCo8OUND%2FQkI7U84%2BJRpDBYmdJ%2BnllSoG%2FOhc1%2FRqlj4lo4SnmJs1q%2FlfPdsyA1pXt%2FsCg2jUFdiADY%2BYL4xh3u%2F1CIw0q3m0AY6pgGVVhT9bfn5WKcAcdcY%2FJVuhzk1BaKdsGeC6Uk%2BC82SwwoVxr4IoEcXbaIx8n96ZJfslutq5%2Bofnyvg0AisnJnTIxEX33Z3gWiIpXGDAT8fupjmJwrzWVYgCDkJx5CJ7lZJjhsqldUzhvjo6D2QhV1SfSFOt%2FUz6iQ5vuqT0rESdJ95CgPDKbm8PC1YNkq6oc6Pqjo2xoa1xccYBBjUB1ZM4c1lstVr&X-Amz-Signature=19ea344264db597ba1d116a040a72d8666f0611431bb77b461f165681abd8c59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NMP4MM%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T143610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfmBUWmhza7dR7IdX9mexcxFGxPs6vUc8ZpjEmAkVEPAiBCid17dwK%2BbhlY9yKqopFpoZzmv88JxAWPUv4cDUrnwiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjt04IjFeEkKS3xXBKtwDsjbVVwFQbQfg7Xvlw3eFroPcjCX0s8FKx8bE43rY7I8kdTKg%2FniYpIS9F5klRWzwd6Z0k5rpTj47hheHSVX%2BjueRxMzBr2gub44SkrRGG0eIiVL29MuCSQPaJn%2FZZFis3HZ0quwEiSjMF5J4T7enkBbI1fJdZZSqw6FesfcnrO2NQpX8peaXsjx8hQ3yzBn00vYziFRBMXNFOyob1l%2F%2FQ4zcGpeIOQ%2Fd80jGueWqZ167haXq2N%2BPj7y%2FIcHp4%2Bp0qZHU%2Bk38jJLo9zQD10Tpy9Oeud7zGrLSF0jdE%2BtL0kaeI9hsDw8SiTklQjYzZSyNVxdfeRVDv9ghtVmX%2FPIHcQHj%2BpPa6wPd4lq0Y2iROCJKAZh0hcQx71D0X2MjDFWGBvdzGiOmj3OzWqZBlRPo7bYWpMy5fZ%2FFS685WtHzagzieu1sKoZBSD3VagZxMRar7KasDEa5x6OoNPzmD%2BlMG4aggrseEe9wriCkRPEhYFZrdCqQzSHy7Q2JVPvNbfWa20hIEHiWvC%2BoNZzRg%2BH9QqR6L%2F2ZS%2BwkrCo8OUND%2FQkI7U84%2BJRpDBYmdJ%2BnllSoG%2FOhc1%2FRqlj4lo4SnmJs1q%2FlfPdsyA1pXt%2FsCg2jUFdiADY%2BYL4xh3u%2F1CIw0q3m0AY6pgGVVhT9bfn5WKcAcdcY%2FJVuhzk1BaKdsGeC6Uk%2BC82SwwoVxr4IoEcXbaIx8n96ZJfslutq5%2Bofnyvg0AisnJnTIxEX33Z3gWiIpXGDAT8fupjmJwrzWVYgCDkJx5CJ7lZJjhsqldUzhvjo6D2QhV1SfSFOt%2FUz6iQ5vuqT0rESdJ95CgPDKbm8PC1YNkq6oc6Pqjo2xoa1xccYBBjUB1ZM4c1lstVr&X-Amz-Signature=e03908af87351773c958f80280cbae5f08f9e0c18e78612f4f40b613a5dde8a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
