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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676GO72TF%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T114534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIA2k2AQOCUagUrS%2BKvLXBWwtJ1YY51nl%2F6rAJNcBjz47AiEA8h3iJvzktnK5BSHqHqo46ifvuUZbru50DiW4SHMhpLQqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlEsrqocwbuL2upKircA2g%2BgKiRMSxisTFbZ492W8tXbjjKMkVA5jMq%2B%2BEqu56HTRFOOWlWAhjkjC%2BD2k04iLXwIfwIFB7U47C5vg5c1DItzQjJ2RaXkunxmcD3z962Sq3IrpJeyUr6vyWCuBXnrLgNUNKIOSLjRSJvhxdY3rXKBWE1o1ygBaJP1C5xD4vgHt7qu8C7zx1IPvDY7xun9xY264uNBdN8EfNLERtudXxDsVVaYiUiYoWwCv6yE1SnMGIfIlJhEgAEKugxJMeNHyPeyThdsoC5xrhwmqc%2Flz3S9URd8KNsQJtYkKi37AFpR8HmRkYzFKClGXTTK2EQCViMaXOnL7c2MJzgyqAYEkDGk%2Beo6CJqG1FqIAl2ya7GvOe3I%2BRgdp9%2FxvVDALRHUYVbN2VoBAILzF2bwPeyKF3YLPzE%2FznTU29I5S0eg1CA8J0kzvtpMHvmfa%2F2YAcqsNR7Tb5tbxiXMbViiCpKkLezSJPaBydFKfisVfFO%2BcrkYAOIzan1bq%2BYaK3wE9BaBFg8%2BB6WztQe7fyhbnkly7caidtYJrbpWWX2lkesYGscXYyDvdfqQ2LYQ26NoKv8uD2FmrdGPcJha%2FwG0HFYx2VLO9sMnxDajYLIjVjcX2z9WNU03Fr1z0KRmIKlMOD3h9MGOqUBbqZ2mhW%2B7hhYH3gVn%2FQ4pBflTIcUtwgjXe%2BAxBj5GPC%2FHGpCdNzRiuFXH3tJcDZ%2BQ0iZa5y9RZGQzmp2%2FcJc6OX0vbhs7odgTnAohNpRxOm%2Bsz1NdzpWo8%2Fz4axVQlYTecmNIQ0LIRTZePjcxoISiAGSjOoHX7Xi%2FISLLdyG%2Bx5lmmfJHjg9WMalgKDoAck78Vs%2FyCB4L7P60J4Rk3EVhxTO%2FFwP&X-Amz-Signature=ed282bd4b3931369a92c3851a3a7b814853693627c6d830a72c8a6dd5209f08e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676GO72TF%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T114534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIA2k2AQOCUagUrS%2BKvLXBWwtJ1YY51nl%2F6rAJNcBjz47AiEA8h3iJvzktnK5BSHqHqo46ifvuUZbru50DiW4SHMhpLQqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlEsrqocwbuL2upKircA2g%2BgKiRMSxisTFbZ492W8tXbjjKMkVA5jMq%2B%2BEqu56HTRFOOWlWAhjkjC%2BD2k04iLXwIfwIFB7U47C5vg5c1DItzQjJ2RaXkunxmcD3z962Sq3IrpJeyUr6vyWCuBXnrLgNUNKIOSLjRSJvhxdY3rXKBWE1o1ygBaJP1C5xD4vgHt7qu8C7zx1IPvDY7xun9xY264uNBdN8EfNLERtudXxDsVVaYiUiYoWwCv6yE1SnMGIfIlJhEgAEKugxJMeNHyPeyThdsoC5xrhwmqc%2Flz3S9URd8KNsQJtYkKi37AFpR8HmRkYzFKClGXTTK2EQCViMaXOnL7c2MJzgyqAYEkDGk%2Beo6CJqG1FqIAl2ya7GvOe3I%2BRgdp9%2FxvVDALRHUYVbN2VoBAILzF2bwPeyKF3YLPzE%2FznTU29I5S0eg1CA8J0kzvtpMHvmfa%2F2YAcqsNR7Tb5tbxiXMbViiCpKkLezSJPaBydFKfisVfFO%2BcrkYAOIzan1bq%2BYaK3wE9BaBFg8%2BB6WztQe7fyhbnkly7caidtYJrbpWWX2lkesYGscXYyDvdfqQ2LYQ26NoKv8uD2FmrdGPcJha%2FwG0HFYx2VLO9sMnxDajYLIjVjcX2z9WNU03Fr1z0KRmIKlMOD3h9MGOqUBbqZ2mhW%2B7hhYH3gVn%2FQ4pBflTIcUtwgjXe%2BAxBj5GPC%2FHGpCdNzRiuFXH3tJcDZ%2BQ0iZa5y9RZGQzmp2%2FcJc6OX0vbhs7odgTnAohNpRxOm%2Bsz1NdzpWo8%2Fz4axVQlYTecmNIQ0LIRTZePjcxoISiAGSjOoHX7Xi%2FISLLdyG%2Bx5lmmfJHjg9WMalgKDoAck78Vs%2FyCB4L7P60J4Rk3EVhxTO%2FFwP&X-Amz-Signature=e15c98674924b77def50c2e0cf2b67528ae683da8150e505c7736f7f7956b4ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
