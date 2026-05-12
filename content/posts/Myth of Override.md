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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLKCW3OM%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T082138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCUGl97T2vIgQFT%2Fjp2A1ElHGVgl%2Fl8gUTmdDZ9JRJkjQIgLOUcZaPXuighsNG6bzYqgLhVO2I%2BkrjeNxt%2FMfwNf1kq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDPFs0mdcLC0AKQHFJSrcAyTWkStpHwRJBr2Roii36%2BX8fVdCkfWsXgfw%2B82iWwwsDSPnHbrti6lu6VpYMkQ3uO8st2fr%2FWwIdwdZ2Or23oKMJX6Nyr7EEtKhkNveZVH75VYLpUIMKO9xz71jogAaiC9wHRwUPVJETgr8FdDsmsqij9Xy6Tt0OfWlpDCZDzUgaB5g%2BrW7PCrDtsdNsFGEIfLyVN5LQ1%2BUgRy%2BVz6bfcpdc%2Fk9BGHDxp6ZrickfWGI9ksZl1te2aWA3Luauuli0bgh4L8eMgQQrbYCOOiPkhmn%2FtV8w4%2B87HVqPB2UnpyNTPfcC2zUYXlFxA8H%2BvN3u%2BF6QF4wS9ruheS7wC8EmuwYEgjdgsVHbAbBm5HqW0MdDWPOmzxi8uMHBuHfDt3DpyXQ5jPWttfnXf0ZLQfKhsUC6Tri13LGVdn8ykm9I%2B%2BDg8OFAesEuVnjqUN7NOxPh%2FZ6Y%2BYUm5hgWjXwtSRU9wFVkRx1LH1DIP6S67mR5%2BSzzVPpVZI9cUdboyVYCKtaEDwvS9siifxzps88zohPjkJuXC3wGZ1fGsMBvpD4ZCAMjmU%2BRQyXmsWMr5Du1ddjQgYInQwidbMaNAjFmy9STGlAOzUz4GBT0gb7Dh49Mg%2FhC5BUESjSmKvYPPbGMJCei9AGOqUBpMG7qZPAxCEfkRpueQna1HbeLH0Vd%2BBLRxIKUnQmAWS1g%2FuhAb0GK8sAPzYaf7fW8k%2ByiGqDKTeVhCB7avC%2B%2F947hMemswZdbg3pH8uIs7W6uHhIJNEbZ20lqSbI6E%2BDLl%2BueTc4oRK5dmkpMhSSixtuV63mj%2F6hxhkcTDPAjkI35yVQpoUTnk9vOwRJYd6SGTU2qmNT1n%2FRZ8Wzw7Fr3l0VFtYT&X-Amz-Signature=6b74f6134964febcfa8f69ba41b39d4a263181e520c0a2d97f2b5a8ff2117823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLKCW3OM%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T082138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCUGl97T2vIgQFT%2Fjp2A1ElHGVgl%2Fl8gUTmdDZ9JRJkjQIgLOUcZaPXuighsNG6bzYqgLhVO2I%2BkrjeNxt%2FMfwNf1kq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDPFs0mdcLC0AKQHFJSrcAyTWkStpHwRJBr2Roii36%2BX8fVdCkfWsXgfw%2B82iWwwsDSPnHbrti6lu6VpYMkQ3uO8st2fr%2FWwIdwdZ2Or23oKMJX6Nyr7EEtKhkNveZVH75VYLpUIMKO9xz71jogAaiC9wHRwUPVJETgr8FdDsmsqij9Xy6Tt0OfWlpDCZDzUgaB5g%2BrW7PCrDtsdNsFGEIfLyVN5LQ1%2BUgRy%2BVz6bfcpdc%2Fk9BGHDxp6ZrickfWGI9ksZl1te2aWA3Luauuli0bgh4L8eMgQQrbYCOOiPkhmn%2FtV8w4%2B87HVqPB2UnpyNTPfcC2zUYXlFxA8H%2BvN3u%2BF6QF4wS9ruheS7wC8EmuwYEgjdgsVHbAbBm5HqW0MdDWPOmzxi8uMHBuHfDt3DpyXQ5jPWttfnXf0ZLQfKhsUC6Tri13LGVdn8ykm9I%2B%2BDg8OFAesEuVnjqUN7NOxPh%2FZ6Y%2BYUm5hgWjXwtSRU9wFVkRx1LH1DIP6S67mR5%2BSzzVPpVZI9cUdboyVYCKtaEDwvS9siifxzps88zohPjkJuXC3wGZ1fGsMBvpD4ZCAMjmU%2BRQyXmsWMr5Du1ddjQgYInQwidbMaNAjFmy9STGlAOzUz4GBT0gb7Dh49Mg%2FhC5BUESjSmKvYPPbGMJCei9AGOqUBpMG7qZPAxCEfkRpueQna1HbeLH0Vd%2BBLRxIKUnQmAWS1g%2FuhAb0GK8sAPzYaf7fW8k%2ByiGqDKTeVhCB7avC%2B%2F947hMemswZdbg3pH8uIs7W6uHhIJNEbZ20lqSbI6E%2BDLl%2BueTc4oRK5dmkpMhSSixtuV63mj%2F6hxhkcTDPAjkI35yVQpoUTnk9vOwRJYd6SGTU2qmNT1n%2FRZ8Wzw7Fr3l0VFtYT&X-Amz-Signature=b656c5cb3ad67d221907a475bf53826b18d19f850ab313f0125f274e7b1f561a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
