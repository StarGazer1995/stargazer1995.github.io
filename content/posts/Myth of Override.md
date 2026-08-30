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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PYWOLSE%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T020300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpfjtemmhf9KNeNjD0BUDDe9PPS2uZXHXC1yMgxYRAeAiEA104kEARBfq6Xbxb8ZKC09DvSZGvF20KyI2CYDuBKtwYq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDGum0hGdwUTFU6UuoircA66mMyHey%2BIT0v%2FrM4Ulf0K%2BUyfAkxKKbKZX42XFmryrUKeUOixELyIMj4Z9RFo5IWdx5P2Tmavj8ref4JLqPewlGqlMubkp3uN0H0kNk0pQkTR4DDN%2BMbbmp%2BuHDTxkff5WDsW%2F4hC%2BZqQ69eEjpRqMVlQVTxKyJzk679Kxx2GIe6TPbc8dCXmfAV1jIfrxAGC2rHg4QnBu7xPhVRQFniAHcZeTGfvbRWa0ioqrdu9uRA8Xgv3RmclLDdDTfWYX6v0rx3lOEtXSGm2lf5cX8klADq1ChLtAkLDr9xY2VoJfc9ldnc%2F0psriYS98pktBqiOvKa%2Be2pAvGk9cmA2Ji8xcz%2FX26YTSXoJDVHo31zp9HrzGMW3ZQcvV0%2FiRpnAc%2F2zeFp%2FB38H8%2BdicJvM7KYljN9DS%2BMhLB23ehNYazTA9aDgiYPlqQMtd8I%2BGVcsEjbu0MbiU%2FZO7fjyXy3HbA%2BotW3DV9wjWpl27xQBGjwKZPymK%2BVmffc0i04QTMVE3zB00H0Ir%2FSoIpCHQUfIObpFY32Ivf3iV7DkjuEgpnfD5jMO57O5tX29pu76pb6C8coIVylb0LbdNpMD6ht0uLSkTViPn74o2LhnnRyYc9Y483jrbN%2F5KH8Vn%2B%2BC%2BMOWYztQGOqUBx7y7sXlhKzKbQ1bFtcZ29RsJaSTRfsaJ6kmmy7UpMUiNR%2BJTXEAlN%2BgotVAIJZ7M3XB436Ps0ILTrZZtleQ%2FqURBmVRL5%2B45xEpGuc%2FF3Dzc%2F983O297s%2BE9lrOwc2YPv%2BlxkPJ4Ea0UgC0MRie4XIc9K8bN3gSb5FNgZ737xNTSnvsWx7qmmUzEH%2FGIRt4Qp5%2BXA72ZIYK%2BknMwEzCaB7WALobn&X-Amz-Signature=193e63f7fd1f0ed2b285258cd46666b04323050dd42bd047c0b4f6dda68019df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PYWOLSE%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T020300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpfjtemmhf9KNeNjD0BUDDe9PPS2uZXHXC1yMgxYRAeAiEA104kEARBfq6Xbxb8ZKC09DvSZGvF20KyI2CYDuBKtwYq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDGum0hGdwUTFU6UuoircA66mMyHey%2BIT0v%2FrM4Ulf0K%2BUyfAkxKKbKZX42XFmryrUKeUOixELyIMj4Z9RFo5IWdx5P2Tmavj8ref4JLqPewlGqlMubkp3uN0H0kNk0pQkTR4DDN%2BMbbmp%2BuHDTxkff5WDsW%2F4hC%2BZqQ69eEjpRqMVlQVTxKyJzk679Kxx2GIe6TPbc8dCXmfAV1jIfrxAGC2rHg4QnBu7xPhVRQFniAHcZeTGfvbRWa0ioqrdu9uRA8Xgv3RmclLDdDTfWYX6v0rx3lOEtXSGm2lf5cX8klADq1ChLtAkLDr9xY2VoJfc9ldnc%2F0psriYS98pktBqiOvKa%2Be2pAvGk9cmA2Ji8xcz%2FX26YTSXoJDVHo31zp9HrzGMW3ZQcvV0%2FiRpnAc%2F2zeFp%2FB38H8%2BdicJvM7KYljN9DS%2BMhLB23ehNYazTA9aDgiYPlqQMtd8I%2BGVcsEjbu0MbiU%2FZO7fjyXy3HbA%2BotW3DV9wjWpl27xQBGjwKZPymK%2BVmffc0i04QTMVE3zB00H0Ir%2FSoIpCHQUfIObpFY32Ivf3iV7DkjuEgpnfD5jMO57O5tX29pu76pb6C8coIVylb0LbdNpMD6ht0uLSkTViPn74o2LhnnRyYc9Y483jrbN%2F5KH8Vn%2B%2BC%2BMOWYztQGOqUBx7y7sXlhKzKbQ1bFtcZ29RsJaSTRfsaJ6kmmy7UpMUiNR%2BJTXEAlN%2BgotVAIJZ7M3XB436Ps0ILTrZZtleQ%2FqURBmVRL5%2B45xEpGuc%2FF3Dzc%2F983O297s%2BE9lrOwc2YPv%2BlxkPJ4Ea0UgC0MRie4XIc9K8bN3gSb5FNgZ737xNTSnvsWx7qmmUzEH%2FGIRt4Qp5%2BXA72ZIYK%2BknMwEzCaB7WALobn&X-Amz-Signature=4bfa09ceb0b012b39bdb45ff959b1dbcf02f20ced3c9f165b86c548746b91600&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
