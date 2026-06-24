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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EAEWE7T%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T104000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCyHxd5OUFD7GjwJzCSyWxbQSYoyhP3NoFOCcEqgdUYVgIgIbToz5NufhZWHYfpzOaEWa8ouwjy3oNTIi%2Bu4d28vC8q%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLdS1kXT8CdrpkJbkSrcAzQWkAtF2t8w7gesXGZdGEgXe%2BNHOtHQRrTWBbW5XPv5pwIsDc7%2BGz7W0wq0ZNaBCuG8Z165aJHRmK7l%2FKaKldeOGlYylgWGGj%2B4uQCfCFMyqCWGgDe%2Fcdi6Nym6k%2FU31HSL0Kbfp%2Fzq%2BFYtjGjo2N%2FqztNKMI6RpfX2%2F5xFdu5pIrHTBdUxi5w6%2BzFMF12PL5xS7KZFsQY9SKOzSQrlYFC6EmB6iSDNtReOQ8hxnoIn%2FBK8HNC719JcyWhtCcKXyeoTb0EwPfkHhM1jrEdOzo43wZmMhyjO6%2FR1UAnZ8CSubIppQjpvZoxwIIgBytBurNWp2w0OAjbL0OnG%2FTud9efzbQcGL5lYI%2BmESZSeFUEwlZnSaVfZ9828IVvjKI4EpKrNiK9F%2Fc5474vbrPSWLxMBJqO%2BN6Utt3btLiqft1mACLYGP2lE0%2BIzCjb9sMQexkRb0FWWe0f0TMVH3QhLzfrkiwzZC6D4MUyTHQVW0B5drRjPanqd0ux8B3vPNE8n5YTjo0fVKDgFry%2Bwo1X6ToxFupGBD5LEWKSPM6TuiFWqdybZ6uqRhPFJmRp%2FYiTi21yPGALQITNFGG0QjUtWDykiUYSeg%2F0G6%2BUMTBrT%2F4bYUgd1Sam5zn468DtsMMnB7tEGOqUB3Ebbnrypk6hyJa8BEdMXehoH%2FoBkW4GTq%2F0ehQ5CD0Hy6v91T4rF37mf0BQ3b0y9XmwwWbri77waG9ISjCDm%2BLrBU53pzq7qkmHorOLq5U1G4rKownqe7mVPZ8ktSfNXNEx8TCNbjSC2sz109292Owyn5UioT781vTDi6S6y2XjOIjzeZ3pFFu%2BeWFstP0C6y41oRVgvh1rzL%2FVv%2Bk57TR2ok5ZZ&X-Amz-Signature=712722d5678744eea6e565df7a28b8fa4c2b0b5c691ee91eb655ec1c75c502dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EAEWE7T%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T104000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCyHxd5OUFD7GjwJzCSyWxbQSYoyhP3NoFOCcEqgdUYVgIgIbToz5NufhZWHYfpzOaEWa8ouwjy3oNTIi%2Bu4d28vC8q%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLdS1kXT8CdrpkJbkSrcAzQWkAtF2t8w7gesXGZdGEgXe%2BNHOtHQRrTWBbW5XPv5pwIsDc7%2BGz7W0wq0ZNaBCuG8Z165aJHRmK7l%2FKaKldeOGlYylgWGGj%2B4uQCfCFMyqCWGgDe%2Fcdi6Nym6k%2FU31HSL0Kbfp%2Fzq%2BFYtjGjo2N%2FqztNKMI6RpfX2%2F5xFdu5pIrHTBdUxi5w6%2BzFMF12PL5xS7KZFsQY9SKOzSQrlYFC6EmB6iSDNtReOQ8hxnoIn%2FBK8HNC719JcyWhtCcKXyeoTb0EwPfkHhM1jrEdOzo43wZmMhyjO6%2FR1UAnZ8CSubIppQjpvZoxwIIgBytBurNWp2w0OAjbL0OnG%2FTud9efzbQcGL5lYI%2BmESZSeFUEwlZnSaVfZ9828IVvjKI4EpKrNiK9F%2Fc5474vbrPSWLxMBJqO%2BN6Utt3btLiqft1mACLYGP2lE0%2BIzCjb9sMQexkRb0FWWe0f0TMVH3QhLzfrkiwzZC6D4MUyTHQVW0B5drRjPanqd0ux8B3vPNE8n5YTjo0fVKDgFry%2Bwo1X6ToxFupGBD5LEWKSPM6TuiFWqdybZ6uqRhPFJmRp%2FYiTi21yPGALQITNFGG0QjUtWDykiUYSeg%2F0G6%2BUMTBrT%2F4bYUgd1Sam5zn468DtsMMnB7tEGOqUB3Ebbnrypk6hyJa8BEdMXehoH%2FoBkW4GTq%2F0ehQ5CD0Hy6v91T4rF37mf0BQ3b0y9XmwwWbri77waG9ISjCDm%2BLrBU53pzq7qkmHorOLq5U1G4rKownqe7mVPZ8ktSfNXNEx8TCNbjSC2sz109292Owyn5UioT781vTDi6S6y2XjOIjzeZ3pFFu%2BeWFstP0C6y41oRVgvh1rzL%2FVv%2Bk57TR2ok5ZZ&X-Amz-Signature=b412f065a408e1c1fd347b557bbdf6b78a6e732c0737c9b9879aaabdb4e13659&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
