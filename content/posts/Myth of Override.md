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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J5N5RDI%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T171822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT%2Bxq4TMqsVUh9FF%2FhogHqT8QYqfoW9MoUIpASrBMK4wIgaNHjFDBm7CRrjFq2b%2Fx7%2BXCzgrSXeXTE6GsUR1tt6YcqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2WbxsL7%2Fc14WZNUSrcA7u4RgNo4nwl6%2F3VvRJEPbZA%2FAVY9Tp5oEjlCAiXMvINglnY9W3vkRXSyeEFlHuublWTBBzpT1g%2FmCkWVW33hswRfdda36PXuFDqt4W0VcSrA8MSevCQ9JDQmKm580h%2BBqp3mMVYcIaYoOeuRfxzA2PgQQ7z7pB6MHGpAJ2owIhjpiwBuyQob2Jb21kYGU9xP1e8tdZeH3ZV2g6PTxKhjPEg7SVi2l%2F%2FLIhcyxqP9trCkT5Cz7YaDR9C3jS641ZWpqm8IvpgriMXGDHn9UB%2FKJNLHkCct7Y4SFEaYN1q2P7kqSxI%2B7iGQknn3vj3BgUmzambbQYiKgRFHCu599ilQtqV0rL%2FKUXlkY05ZS3ke8ptJxJiXNwDnheJyHMXZR8itHUTN18tWsyBqLaJdybG4UO8QzHinglb1UDUiSvn1czgD%2FXuZKmbAF2zJTSsANkoBFKsg082wCBfZiPisAOJWQkiZPbuiDkmu2VCFsgmZI3D9zBTdBokfynDMl36YJNo84HE3vxBGyQ%2F8mkFM52ZvHBIk%2BLx3k1VuSEPSrtymarZw1KpKLWxPX6Ea8jpzxDSQOe44kVPMFDdiyQD81peWpDszgceTbMsyOkDJWfCjJpOyeQwAnOECUdk9sv%2FMIeZs9MGOqUBhfxGbvmk12x4A40fkno6%2BJKHarRk1%2FTTh0987LO238aebhi9Ep9aCCxmGCie7S44lrBM8dT7S6Jbx6RfY6GAekHIQex%2F%2FrepPXqRSwzJAPfIs8SnZONMgzqzPXOb%2Bd4IZMk1ncuTFQrNrE783pUBHQb9lE1zXU7VZIwy%2BdWG5Z%2FyeEgzlrPF2lbLdbtRZ8r9wuHmbR%2Foz8FoamjIlKk8gbrvhGBC&X-Amz-Signature=dabf2445815a47d18efda807dfbe991d661d68772629078eeb54ca7a328af7e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J5N5RDI%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T171822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT%2Bxq4TMqsVUh9FF%2FhogHqT8QYqfoW9MoUIpASrBMK4wIgaNHjFDBm7CRrjFq2b%2Fx7%2BXCzgrSXeXTE6GsUR1tt6YcqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2WbxsL7%2Fc14WZNUSrcA7u4RgNo4nwl6%2F3VvRJEPbZA%2FAVY9Tp5oEjlCAiXMvINglnY9W3vkRXSyeEFlHuublWTBBzpT1g%2FmCkWVW33hswRfdda36PXuFDqt4W0VcSrA8MSevCQ9JDQmKm580h%2BBqp3mMVYcIaYoOeuRfxzA2PgQQ7z7pB6MHGpAJ2owIhjpiwBuyQob2Jb21kYGU9xP1e8tdZeH3ZV2g6PTxKhjPEg7SVi2l%2F%2FLIhcyxqP9trCkT5Cz7YaDR9C3jS641ZWpqm8IvpgriMXGDHn9UB%2FKJNLHkCct7Y4SFEaYN1q2P7kqSxI%2B7iGQknn3vj3BgUmzambbQYiKgRFHCu599ilQtqV0rL%2FKUXlkY05ZS3ke8ptJxJiXNwDnheJyHMXZR8itHUTN18tWsyBqLaJdybG4UO8QzHinglb1UDUiSvn1czgD%2FXuZKmbAF2zJTSsANkoBFKsg082wCBfZiPisAOJWQkiZPbuiDkmu2VCFsgmZI3D9zBTdBokfynDMl36YJNo84HE3vxBGyQ%2F8mkFM52ZvHBIk%2BLx3k1VuSEPSrtymarZw1KpKLWxPX6Ea8jpzxDSQOe44kVPMFDdiyQD81peWpDszgceTbMsyOkDJWfCjJpOyeQwAnOECUdk9sv%2FMIeZs9MGOqUBhfxGbvmk12x4A40fkno6%2BJKHarRk1%2FTTh0987LO238aebhi9Ep9aCCxmGCie7S44lrBM8dT7S6Jbx6RfY6GAekHIQex%2F%2FrepPXqRSwzJAPfIs8SnZONMgzqzPXOb%2Bd4IZMk1ncuTFQrNrE783pUBHQb9lE1zXU7VZIwy%2BdWG5Z%2FyeEgzlrPF2lbLdbtRZ8r9wuHmbR%2Foz8FoamjIlKk8gbrvhGBC&X-Amz-Signature=7c3b08224825f48006d61f5e02e38b1b729c6e1646e60f112dcae816b723734d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
