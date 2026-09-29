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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFGKNQXN%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T073727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIAqYH0Y%2BJLWkKui9MXMVvT1LGYSgVnxfgDLINvxFLET%2BAiA4fb4MI6R9TkoFmVQZ%2BojeB%2FsWIzRXw3m%2FXwr486ST2Cr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMcXkN8P4zS6venSq8KtwDiu5r%2F8gm5h%2Bl2vWhrl04gaPa%2B1f0JvIKA63z9UgFV64fTbcuysnMAIto%2FzwgYVht%2FOoyfoq2fpcspaFfaAtm9Hfg42To7%2FpjQ28piVv0vauaW3rXIQWdwdRGknMoL2jL1e71Coyv4XF7gFSXOnNfEte%2B8SUlpn%2FYt8B%2FsHCsRDg5Tx4VMhiSSqVYAsK6WR7Bt3%2BPNBVRVaU6nB%2FLC%2BaguHaYq0%2FQKFVKH5dpMeztyv0jNHF84T34GB%2Bim3ACIq5yCnME0P2kNtSZwOoHWUUJ4OzqngEe%2BZOXYq8Oa15zsGRa61XABuIbaJ2bSRFG2zxgk7w9LygcFNjkSGQv20wBqaNkqUW%2BEWmqUXwpkwvqE%2Fzr9HZrJzbLZBehXIZYfPGowRQ4NqgtT0Y%2FOLVO0XawzvJJSZOsOi0uGdzHz%2FDTPwMbgYFH2o5ZhNCk81Hojt9Myldnlfjoss7MuOCxDQ15J4b%2Bv9LwsxYXNECfiQXArZoWMWgw%2FXR8qbEKZ68FdA7VNuy%2BIxrKZ5WXW5Yg6svy7Bg%2Fde6sl2g20YAmIlKvIcemQ8rLFJQ2iw2Aqf2JJlx4RIOgAY6oUMli9EDfU8avrnyHOPhlcTQUaPE315AbznWtGJBH1wtJR03dUN4w1srt1QY6pgFtCkHJrzeQMwaRdHuQNttMLQDnE3QOpDUmGsQJ9t7g3Vnfk6JPySqokNhvfuvcsUO1WfEP%2Fe%2FJgV7H%2Fe5ev%2Ff8xlwvoPukvtGKh8733mfTunmMfOkIwF94ktAt0QzDrZ84mhiViBIP5fXgsPG768EZO2KWakdIylwqsxR8vNLPiZE96T%2B%2FzWh%2FGvol44waHsfrJQ4uA6rUJcPkFxfGcrzhhJCXus94&X-Amz-Signature=ca4d0c75fd09344e1caad9c52769bd0cf010dd0c6c0764d8ac3a6e2bfdd8d4b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFGKNQXN%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T073727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIAqYH0Y%2BJLWkKui9MXMVvT1LGYSgVnxfgDLINvxFLET%2BAiA4fb4MI6R9TkoFmVQZ%2BojeB%2FsWIzRXw3m%2FXwr486ST2Cr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMcXkN8P4zS6venSq8KtwDiu5r%2F8gm5h%2Bl2vWhrl04gaPa%2B1f0JvIKA63z9UgFV64fTbcuysnMAIto%2FzwgYVht%2FOoyfoq2fpcspaFfaAtm9Hfg42To7%2FpjQ28piVv0vauaW3rXIQWdwdRGknMoL2jL1e71Coyv4XF7gFSXOnNfEte%2B8SUlpn%2FYt8B%2FsHCsRDg5Tx4VMhiSSqVYAsK6WR7Bt3%2BPNBVRVaU6nB%2FLC%2BaguHaYq0%2FQKFVKH5dpMeztyv0jNHF84T34GB%2Bim3ACIq5yCnME0P2kNtSZwOoHWUUJ4OzqngEe%2BZOXYq8Oa15zsGRa61XABuIbaJ2bSRFG2zxgk7w9LygcFNjkSGQv20wBqaNkqUW%2BEWmqUXwpkwvqE%2Fzr9HZrJzbLZBehXIZYfPGowRQ4NqgtT0Y%2FOLVO0XawzvJJSZOsOi0uGdzHz%2FDTPwMbgYFH2o5ZhNCk81Hojt9Myldnlfjoss7MuOCxDQ15J4b%2Bv9LwsxYXNECfiQXArZoWMWgw%2FXR8qbEKZ68FdA7VNuy%2BIxrKZ5WXW5Yg6svy7Bg%2Fde6sl2g20YAmIlKvIcemQ8rLFJQ2iw2Aqf2JJlx4RIOgAY6oUMli9EDfU8avrnyHOPhlcTQUaPE315AbznWtGJBH1wtJR03dUN4w1srt1QY6pgFtCkHJrzeQMwaRdHuQNttMLQDnE3QOpDUmGsQJ9t7g3Vnfk6JPySqokNhvfuvcsUO1WfEP%2Fe%2FJgV7H%2Fe5ev%2Ff8xlwvoPukvtGKh8733mfTunmMfOkIwF94ktAt0QzDrZ84mhiViBIP5fXgsPG768EZO2KWakdIylwqsxR8vNLPiZE96T%2B%2FzWh%2FGvol44waHsfrJQ4uA6rUJcPkFxfGcrzhhJCXus94&X-Amz-Signature=a66e9925e811ed278c33c6088e1fa1d294aa169e2e86dd4fcbe66fe11d59c1be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
