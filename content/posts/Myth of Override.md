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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PQEVQM%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T222426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ2qrkSUuvF0AmLbs5R93UF8mUOsjafQhN0tG%2BtMHjawIgKkO7zAYLEXl3rHYzLzWnPqRZAdA5tehuwiSBDyYrR48q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDGYGndHitMi5TYH6qCrcAwDvQ9n4ngrwm4H1bBPfA7tS%2BQjwUFsTmqdmiJFg8g%2BIZdBOik0hO1tQCQxGTznHTYCU4lt12UPg9r6OSgGPb%2BwYlgsVItKKU%2BN2tnueckx1JC9BSYxj4cKVKC%2BB%2FPzMVNZu7nxR3BXhgJC2oUE8DpjkQKcysM1Y0WyPDZR94oTnoQ21Sz3Qgr%2F8IZHA81EcblyPlPsYFEznSfvoHRoR%2BeSLSdH8NgSbSVcjG5fT%2FD2W%2FrsCpVML%2BhXo1EPJmpnDV%2FT7rSQn%2FR4AJMJRPiv5FJA70zFaY76YUoOSCdeBczrSLxuZ%2Fmb%2Brek7liqjXmLdDeck1c9YXOAN7DmEuU62%2B0kbRKevDXmSnYXjH3VXDXzTiYU3MJUTNiNIz30hKKW9q6Uu5DGbLcfrWOLNN99a3Uk8b5DmzLXhzk91veo8lt5v9GslFjRdxLXEma%2FZI7CXJVO4bndO84OUb2g9M4J3xRlafUcyem%2Baqbw2DCXUrcZpYTy%2Fb5pUQwiZZIKoj5%2BOcbJJd7AuV28pq486WuKHYIwfy513s0oT7IlDwvkyszRVci0ACO%2FHmbXzYzB55osjEo0uB3tdCkWGF%2BhU5EBwS4vlA2J2h4ryfHgL1ZsrZMwAO0PIK4w%2B0Nku5NfFMMiy2dMGOqUBjbndqrrrHx8KzFasfmXgAjBdxccGZBME7ZA7rPP2s1kiO6dTwQSl2HQhwIVypE%2BdzVUfmgwezn%2FwdwmSjla0Ro2KQ7b87oiWQcIIs8Ur5aN7QH8tsboUqlYdjo7gaQ%2B3G%2BfPJKukm%2FPMi2z9FIVfReeu6Nf9kbr7adLesxSIix%2B0NZVgnKNv2ZVRBdjhRP7T5gmmCbUjTHB32huleIBrmftlO9as&X-Amz-Signature=de7d368d468121b543484d16af50703850909ae894631bd287dc4040eda96832&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PQEVQM%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T222426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ2qrkSUuvF0AmLbs5R93UF8mUOsjafQhN0tG%2BtMHjawIgKkO7zAYLEXl3rHYzLzWnPqRZAdA5tehuwiSBDyYrR48q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDGYGndHitMi5TYH6qCrcAwDvQ9n4ngrwm4H1bBPfA7tS%2BQjwUFsTmqdmiJFg8g%2BIZdBOik0hO1tQCQxGTznHTYCU4lt12UPg9r6OSgGPb%2BwYlgsVItKKU%2BN2tnueckx1JC9BSYxj4cKVKC%2BB%2FPzMVNZu7nxR3BXhgJC2oUE8DpjkQKcysM1Y0WyPDZR94oTnoQ21Sz3Qgr%2F8IZHA81EcblyPlPsYFEznSfvoHRoR%2BeSLSdH8NgSbSVcjG5fT%2FD2W%2FrsCpVML%2BhXo1EPJmpnDV%2FT7rSQn%2FR4AJMJRPiv5FJA70zFaY76YUoOSCdeBczrSLxuZ%2Fmb%2Brek7liqjXmLdDeck1c9YXOAN7DmEuU62%2B0kbRKevDXmSnYXjH3VXDXzTiYU3MJUTNiNIz30hKKW9q6Uu5DGbLcfrWOLNN99a3Uk8b5DmzLXhzk91veo8lt5v9GslFjRdxLXEma%2FZI7CXJVO4bndO84OUb2g9M4J3xRlafUcyem%2Baqbw2DCXUrcZpYTy%2Fb5pUQwiZZIKoj5%2BOcbJJd7AuV28pq486WuKHYIwfy513s0oT7IlDwvkyszRVci0ACO%2FHmbXzYzB55osjEo0uB3tdCkWGF%2BhU5EBwS4vlA2J2h4ryfHgL1ZsrZMwAO0PIK4w%2B0Nku5NfFMMiy2dMGOqUBjbndqrrrHx8KzFasfmXgAjBdxccGZBME7ZA7rPP2s1kiO6dTwQSl2HQhwIVypE%2BdzVUfmgwezn%2FwdwmSjla0Ro2KQ7b87oiWQcIIs8Ur5aN7QH8tsboUqlYdjo7gaQ%2B3G%2BfPJKukm%2FPMi2z9FIVfReeu6Nf9kbr7adLesxSIix%2B0NZVgnKNv2ZVRBdjhRP7T5gmmCbUjTHB32huleIBrmftlO9as&X-Amz-Signature=b5aa14ca5b891bb9009db2830ea384b9f0bfa2668b3bd633fdcc8d6f2a53423d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
