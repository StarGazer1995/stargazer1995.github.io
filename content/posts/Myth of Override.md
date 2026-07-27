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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EJDPK6K%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T053750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIByxpieCxjWdbKWG5stCtd%2B4VL6TNIub%2BQE6CeNiY6gHAiEA4qTtDZnHsQZdYCsFd6aD%2BwLY4Jw3YftczTaqcP%2Ft8k4q%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDAAQmDlGXJ9gcHndVCrcAwEPsLxuot7Tc85j8oqLiTWtx%2BymUt9sg5zXFg14qWvxzij6dFFmsT3qMa%2FKlBhx2YT07nx%2B9hbSAoYp9tHacrH%2BHZ4pI0uhfnXPMDV%2BlvZPmB2C18GNcjABFlKH7N3FHz%2BxVQmaxKhGU4nlesuf3QSLfJO6a05WGoAw0FOOGsaiLAKqBr3Bbh2yIvx7N3jxPrpfd7GRqaPcqPmNBTQdDyUnBnOLTOdNcK8e3yD26urMuaIkZ9MxTtC4uGjnzDa51k3H9XoXyXr5cWz%2Fru3rI7VhmcMu9pvKpaQYRUrRBn1RnHCZ8rzY7cWZUQzGQYmvEgrlyECVSN%2Bh%2BBEAZfxIs9ir3tpi7veRjlOGl03Ct3UekrRlpEjjLpD68B8JybYWC8NuLNhd4wjGwQKeBjEkcTfu2mMDe0cIj%2FQU4Lwk4%2FzejXZAR1aUDdEj6xFnCtdQs7nuTJPh9rvu0jEKdEaQiH9LMTSqPHQr79Gi%2BjNGi%2BuLY2IxcpNmYFE0LbzXXIoybVcVpEi4svYTrWiZBRq9SZZjeIZyg4QDRdK73PLd01NBjM0vF7lV%2FzJ7XPBBXEWEYdWHXE7S0mYeMwtLNd%2FmwqDSKMKs6kt4goRiD98JDuI1KN56Lnu1Lj7BBtn7MLrLm9MGOqUBeCBpDf71hA61uJ7WPg54Tz8yfrnZJnGQ4bMFK9KLNgoY%2F2ZpPOLwH450sqoUEh1Z%2FyIpJCf41z%2Fze4%2BLVgLtPpc70cGHfGriyZfoTzOhTEDrxOrz7409OaeuBdLxG5e0%2FGZDS1tiZnAdQpFMRBJoRqWpF6xV8WMHa%2FTWBfOCIzJ7A9AIPgBuW1AzRRveZjlLZqFazC1%2FDkJ4GZK5BQ5wkF%2FgKmvD&X-Amz-Signature=27a6c1e98cc487fe76c1e0540eae9266a2e206279b9be7c25762c2b7444242b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EJDPK6K%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T053750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIByxpieCxjWdbKWG5stCtd%2B4VL6TNIub%2BQE6CeNiY6gHAiEA4qTtDZnHsQZdYCsFd6aD%2BwLY4Jw3YftczTaqcP%2Ft8k4q%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDAAQmDlGXJ9gcHndVCrcAwEPsLxuot7Tc85j8oqLiTWtx%2BymUt9sg5zXFg14qWvxzij6dFFmsT3qMa%2FKlBhx2YT07nx%2B9hbSAoYp9tHacrH%2BHZ4pI0uhfnXPMDV%2BlvZPmB2C18GNcjABFlKH7N3FHz%2BxVQmaxKhGU4nlesuf3QSLfJO6a05WGoAw0FOOGsaiLAKqBr3Bbh2yIvx7N3jxPrpfd7GRqaPcqPmNBTQdDyUnBnOLTOdNcK8e3yD26urMuaIkZ9MxTtC4uGjnzDa51k3H9XoXyXr5cWz%2Fru3rI7VhmcMu9pvKpaQYRUrRBn1RnHCZ8rzY7cWZUQzGQYmvEgrlyECVSN%2Bh%2BBEAZfxIs9ir3tpi7veRjlOGl03Ct3UekrRlpEjjLpD68B8JybYWC8NuLNhd4wjGwQKeBjEkcTfu2mMDe0cIj%2FQU4Lwk4%2FzejXZAR1aUDdEj6xFnCtdQs7nuTJPh9rvu0jEKdEaQiH9LMTSqPHQr79Gi%2BjNGi%2BuLY2IxcpNmYFE0LbzXXIoybVcVpEi4svYTrWiZBRq9SZZjeIZyg4QDRdK73PLd01NBjM0vF7lV%2FzJ7XPBBXEWEYdWHXE7S0mYeMwtLNd%2FmwqDSKMKs6kt4goRiD98JDuI1KN56Lnu1Lj7BBtn7MLrLm9MGOqUBeCBpDf71hA61uJ7WPg54Tz8yfrnZJnGQ4bMFK9KLNgoY%2F2ZpPOLwH450sqoUEh1Z%2FyIpJCf41z%2Fze4%2BLVgLtPpc70cGHfGriyZfoTzOhTEDrxOrz7409OaeuBdLxG5e0%2FGZDS1tiZnAdQpFMRBJoRqWpF6xV8WMHa%2FTWBfOCIzJ7A9AIPgBuW1AzRRveZjlLZqFazC1%2FDkJ4GZK5BQ5wkF%2FgKmvD&X-Amz-Signature=c1fe09b4871eea0c6be04f4a2e80e043de8fb15fbf86b03ce6151a7102c154a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
