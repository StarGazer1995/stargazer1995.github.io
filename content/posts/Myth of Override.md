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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKRTMDJC%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2FHJow5aqxqoYzBNvbvOqDSybYq2gZEWNjKRon7J5KTAiEAynKFKVQRCzOfUq2b5WF50QNr1Dvm%2F41oZyWQ%2FlHAIu0q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDPIHZ8vI7Vn07ITgeCrcA%2Bq31qwXd%2FHc%2FE1eQkdOZCBEE9a2%2BSQ89xfOUEe7v8mJ9GF52ep8jnvLJxDyXNC75Ow75pdb9ryqrwgsWZLUl%2FKiV4sQGdw5H1FWf%2FdKKixAsIHBlwTLIPqeTUXKuUCRsPjJ4QA6NfF2eJQd%2BLH8xQdLVBgiJ%2FxpXfitqcgXRzBPXvkUynsY3qdatdmUtKEED4H5TFS6BBOtP8bT0KzVl3jo2kwWU7rQ4FMiW%2F5UwA7BdJWP%2BmqBbIPZ3KQASZysl2zTHYUFYvkcAE6gZr9l3Zcoc%2F86MG%2FzCO2SE8CRiIhqQ%2BXPkEXUHyka2VfvK0IVCprZ9dxWlMyxQ8RIq4xTvAPnBQB3MPQZfb8qC2YTw5yqmd7bxP9RWrC6Bf%2FRpUe1JhAfNlSnfDqmboz%2BdM9nRwc7uzX%2B7olonAgpo6NP9dSThtggAz4iyhySR7gy2kU3F8AyQj2ANLOBk6Jmp5unERGbk%2FFuxD5m%2B3RRsMRG60PFlONl39an1FQXGV6kexDM2%2B%2Fpg986RmsgZptTWsAXe1UvsMR5vPDAPSeFCNhb3RbkXEo3xb1raUSI4Oz6hngUjWTcJAV3KUd%2FDXyVMNFmwEWcJi5TySoF%2FB2yQbNPzk3S%2BhhXH3m3ummfILxBMN39j9QGOqUBc%2Fac7TXpEo8O5nOfcWlgNXbXM756cS4GaCTXuyeQ9Q2c8kYejSMXDhBDAqEL3ZGcSk4xqDe6%2F8LWVah95Mj2f59KdA%2BF2UCGbp7a8HpUGW52hfoPmm0u3DX5gYDH%2BPe8As2tjPfgkbBK041kbWNgZCCRSn0wEec1b1PEAxc381gkHPdHGbnwJJ4655vORRRagcR7urGgYZELfm3lEu5Go25FVLdK&X-Amz-Signature=c9cda56723a97c2e1cb5c745ea11ea698af89e5ec9498c4775fd26f8f27c3a59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKRTMDJC%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2FHJow5aqxqoYzBNvbvOqDSybYq2gZEWNjKRon7J5KTAiEAynKFKVQRCzOfUq2b5WF50QNr1Dvm%2F41oZyWQ%2FlHAIu0q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDPIHZ8vI7Vn07ITgeCrcA%2Bq31qwXd%2FHc%2FE1eQkdOZCBEE9a2%2BSQ89xfOUEe7v8mJ9GF52ep8jnvLJxDyXNC75Ow75pdb9ryqrwgsWZLUl%2FKiV4sQGdw5H1FWf%2FdKKixAsIHBlwTLIPqeTUXKuUCRsPjJ4QA6NfF2eJQd%2BLH8xQdLVBgiJ%2FxpXfitqcgXRzBPXvkUynsY3qdatdmUtKEED4H5TFS6BBOtP8bT0KzVl3jo2kwWU7rQ4FMiW%2F5UwA7BdJWP%2BmqBbIPZ3KQASZysl2zTHYUFYvkcAE6gZr9l3Zcoc%2F86MG%2FzCO2SE8CRiIhqQ%2BXPkEXUHyka2VfvK0IVCprZ9dxWlMyxQ8RIq4xTvAPnBQB3MPQZfb8qC2YTw5yqmd7bxP9RWrC6Bf%2FRpUe1JhAfNlSnfDqmboz%2BdM9nRwc7uzX%2B7olonAgpo6NP9dSThtggAz4iyhySR7gy2kU3F8AyQj2ANLOBk6Jmp5unERGbk%2FFuxD5m%2B3RRsMRG60PFlONl39an1FQXGV6kexDM2%2B%2Fpg986RmsgZptTWsAXe1UvsMR5vPDAPSeFCNhb3RbkXEo3xb1raUSI4Oz6hngUjWTcJAV3KUd%2FDXyVMNFmwEWcJi5TySoF%2FB2yQbNPzk3S%2BhhXH3m3ummfILxBMN39j9QGOqUBc%2Fac7TXpEo8O5nOfcWlgNXbXM756cS4GaCTXuyeQ9Q2c8kYejSMXDhBDAqEL3ZGcSk4xqDe6%2F8LWVah95Mj2f59KdA%2BF2UCGbp7a8HpUGW52hfoPmm0u3DX5gYDH%2BPe8As2tjPfgkbBK041kbWNgZCCRSn0wEec1b1PEAxc381gkHPdHGbnwJJ4655vORRRagcR7urGgYZELfm3lEu5Go25FVLdK&X-Amz-Signature=a64f77fc2fafe178988314a875592173e90225c28fd7c49b49f7e341b66cbdb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
