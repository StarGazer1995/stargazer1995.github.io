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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U46UJ3KZ%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T193309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIG%2F6ZXATQY4%2F0CWlkL11r0HV3WrOnVWdK3q3AzAPADM%2FAiEAhwsYYMeQWXan%2FRFeHHCVlihWZVoKhJKbGW9VuTGRbyoqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfxeMre0G9gdY%2Bc9ircA1cWEu%2Bxi6J7Xhb%2FyFsTYdLGVCj2H%2Funnah0Y%2FCHHtPDp5J%2FK7H8W3rdI2MBX0z%2BWp4YfWeAvN1LI2FsmowK%2BIABYSjZhNnXFJrYspxq0D8wOFU4YjFFNHhrAvwKjiCBhmLiE%2FKYfjxKG9vKyKIJl8DHJVw4XvYKo7R50%2BebRm8KChsQdGSGwaWBchFWv7ltf%2FbIPfCW6YQeWcdsF3o%2FrhPSgsXOG%2FxrJH1bfYAcJdkDIe%2F1B3ymnPqit3qlsrGX3BU9Z0SsgZRxiT1CZ%2FtujZtY2%2FY6fVO4Ux293GhNomkOjFiWb8Er4cyeNZ0rJ2qqVru4yy2POkfcTI%2FDRq6i%2BbB%2B1%2BAwpQRYXh6W%2F80NlAg0uBDXIgQB6Au4NQCufWeD7R%2BW3LVHQO%2FY5gtop%2F01dLygvTh%2F69fXqwayn38J0He4arsbmyiSNXpjHLy2bZ7mBq3d5sY0T4aeR6JN3L5rOoiOWe3acjN6RqF5DIT2FZ58xI0j3Zte%2FZIs0oyRVfRxPp8VDf3%2F7ofQiQtK6Vj9wFSiSnZTWl8PPyD5QObvp0x4uuiCxtaMOCrOvSQjnqWIMwVHDtz5RsebVATAU6v9KSZ0ksqazjdnKCmP4wNaosr3S5p%2FCJJArYoGWSg2MOqVxNYGOqUBHG4Rs2xGq19Rvp8hsdeLiOWqLLsLIv9VcrvbxiAl59DZHo3RcLrUwqceSRSojtvutbtziroHzAzWhhOgwh4lfT5e880GO8pZF%2F9osltvdziGMj%2FDekkv6rUHgfmx2dW1HVwzIJSy62Sfc28mNxKScaMKfgcxaJZu9obhhAL6GOy%2BlVYiptFffopxUzBw8E4ohQykVhEVtUv%2BD1D2U9F5YA5ZxSWa&X-Amz-Signature=182da234a6d2b500d085c638af951b639d38ca0a3e83dc010a7788a0568f9a18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U46UJ3KZ%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T193309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIG%2F6ZXATQY4%2F0CWlkL11r0HV3WrOnVWdK3q3AzAPADM%2FAiEAhwsYYMeQWXan%2FRFeHHCVlihWZVoKhJKbGW9VuTGRbyoqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfxeMre0G9gdY%2Bc9ircA1cWEu%2Bxi6J7Xhb%2FyFsTYdLGVCj2H%2Funnah0Y%2FCHHtPDp5J%2FK7H8W3rdI2MBX0z%2BWp4YfWeAvN1LI2FsmowK%2BIABYSjZhNnXFJrYspxq0D8wOFU4YjFFNHhrAvwKjiCBhmLiE%2FKYfjxKG9vKyKIJl8DHJVw4XvYKo7R50%2BebRm8KChsQdGSGwaWBchFWv7ltf%2FbIPfCW6YQeWcdsF3o%2FrhPSgsXOG%2FxrJH1bfYAcJdkDIe%2F1B3ymnPqit3qlsrGX3BU9Z0SsgZRxiT1CZ%2FtujZtY2%2FY6fVO4Ux293GhNomkOjFiWb8Er4cyeNZ0rJ2qqVru4yy2POkfcTI%2FDRq6i%2BbB%2B1%2BAwpQRYXh6W%2F80NlAg0uBDXIgQB6Au4NQCufWeD7R%2BW3LVHQO%2FY5gtop%2F01dLygvTh%2F69fXqwayn38J0He4arsbmyiSNXpjHLy2bZ7mBq3d5sY0T4aeR6JN3L5rOoiOWe3acjN6RqF5DIT2FZ58xI0j3Zte%2FZIs0oyRVfRxPp8VDf3%2F7ofQiQtK6Vj9wFSiSnZTWl8PPyD5QObvp0x4uuiCxtaMOCrOvSQjnqWIMwVHDtz5RsebVATAU6v9KSZ0ksqazjdnKCmP4wNaosr3S5p%2FCJJArYoGWSg2MOqVxNYGOqUBHG4Rs2xGq19Rvp8hsdeLiOWqLLsLIv9VcrvbxiAl59DZHo3RcLrUwqceSRSojtvutbtziroHzAzWhhOgwh4lfT5e880GO8pZF%2F9osltvdziGMj%2FDekkv6rUHgfmx2dW1HVwzIJSy62Sfc28mNxKScaMKfgcxaJZu9obhhAL6GOy%2BlVYiptFffopxUzBw8E4ohQykVhEVtUv%2BD1D2U9F5YA5ZxSWa&X-Amz-Signature=e2d46c5fd7912bf8006c272ed254443d3570cda8edeac40aee4584e30face394&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
