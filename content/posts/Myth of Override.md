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

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">code_examples/cpp_examples/01_myth_of_override/src/main.cpp at main · StarGazer1995/code_examples</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;">Contribute to StarGazer1995/code_examples development by creating an account on GitHub.</div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://github.githubassets.com/favicons/favicon.svg"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div><div style="flex: 1 1 180px; display: block; position: relative;"><div style="position: absolute; inset: 0px;"><div style="width: 100%; height: 100%;"><img src="https://opengraph.githubassets.com/24dae9f0ad65ae788f1f405a6204e98dbfd21a90718b49e4873c8a534314d035/StarGazer1995/code_examples" referrerpolicy="no-referrer" style="display: block; object-fit: cover; border-radius: 3px; width: 100%; height: 100%;"></div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNIBFSBL%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDGDCSADyVRICMyLu5FwKWA5%2FDrp%2B8U%2FSEcv1xzVkSSgIhAN6C8gKHFknVhN8nCL%2FMidoN38QqU4RsmTwn0Zpw8Mj2Kv8DCFYQABoMNjM3NDIzMTgzODA1IgyGyqU%2FoMdQB0Hv3wIq3AMdLeKYETNHB9OaKaChGqtRvjXwPYbw6G7qTlfOh0on1G4cplAa0TJ6XMe2gArLXnVWBB1x%2FoQaMukc1wPkUAJ7rKXtc1kT6oZQT3BQzlQ5xYZAaEKEbJLnBCHYXT14gBNSLEYXIAom7Js1XbnfZnNwPCNKyVAQZkSwbHYZZCr8pN4tNr1BEZ%2FHkNe9Jm4ESlbzqYUFmZHIS1lrjEu9eB1xn5AX5J23jq8xTxxFZDvrpwE2tS%2BF0mR9EJzldBI3saL9%2FICc9uFEe6ystLsxxOX98w7PnIMzO2%2BNI%2BWSMRjwiExNZDXU4RMd9uNbvS3dMUA5tlQUkoQQObX9SKKAQ9%2Fd7jb%2BVcjlESU7LMjuwvH4ZlPb0eIQABJm0HxspspD38QRsBXeOu%2Bmr2IGrG9UWRC%2BS5ScXFtYw6I2wwjju0W99rnBVEdg%2B9Dzz8xLW2hYSUcnAHxf3B88sAkpAq7EWBoII2I1BQMuKfEHtI4%2B1OwyR%2FxCYaW78ql76IULfFp8akH8XMndleAqkbJSj%2Bc8RqZluE%2B5bf5Hale9O%2FzopTwGctFYRoPzGC%2BP9x8QkRMvbODv8RvVPHgYU%2FZU4bo6CXiCeYH9VDp9KQ9lrBn1Tam5cRzCPDun%2F5%2FM7yMGEDCP7bbABjqkAS%2B%2B2B8lZoJ33HLbC1wPyokeuFkCagQ6dQ%2BfS3i0zzU4B19VNzrrGjX53EujYZVllYQo%2BU2UC6ldBEc%2FVOzlBjNb7%2Bk8yJI5c0PdTqilFUowxRT0zW%2Fd1HpiHGzjvS6xiLmWv%2BOvuAwPHph2YLkMs55ZWuhmQ0yAwLDnnZJpUF2MpbkzHRgf7Cah3wxf6qrf5T8ozO8DdURECXbrmFPCNoMbfmdE&X-Amz-Signature=5f588c4604ec15cbe1c49a2629dcebf80a37681cff92f64c7b13e8b5cc151d6f&X-Amz-SignedHeaders=host&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNIBFSBL%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDGDCSADyVRICMyLu5FwKWA5%2FDrp%2B8U%2FSEcv1xzVkSSgIhAN6C8gKHFknVhN8nCL%2FMidoN38QqU4RsmTwn0Zpw8Mj2Kv8DCFYQABoMNjM3NDIzMTgzODA1IgyGyqU%2FoMdQB0Hv3wIq3AMdLeKYETNHB9OaKaChGqtRvjXwPYbw6G7qTlfOh0on1G4cplAa0TJ6XMe2gArLXnVWBB1x%2FoQaMukc1wPkUAJ7rKXtc1kT6oZQT3BQzlQ5xYZAaEKEbJLnBCHYXT14gBNSLEYXIAom7Js1XbnfZnNwPCNKyVAQZkSwbHYZZCr8pN4tNr1BEZ%2FHkNe9Jm4ESlbzqYUFmZHIS1lrjEu9eB1xn5AX5J23jq8xTxxFZDvrpwE2tS%2BF0mR9EJzldBI3saL9%2FICc9uFEe6ystLsxxOX98w7PnIMzO2%2BNI%2BWSMRjwiExNZDXU4RMd9uNbvS3dMUA5tlQUkoQQObX9SKKAQ9%2Fd7jb%2BVcjlESU7LMjuwvH4ZlPb0eIQABJm0HxspspD38QRsBXeOu%2Bmr2IGrG9UWRC%2BS5ScXFtYw6I2wwjju0W99rnBVEdg%2B9Dzz8xLW2hYSUcnAHxf3B88sAkpAq7EWBoII2I1BQMuKfEHtI4%2B1OwyR%2FxCYaW78ql76IULfFp8akH8XMndleAqkbJSj%2Bc8RqZluE%2B5bf5Hale9O%2FzopTwGctFYRoPzGC%2BP9x8QkRMvbODv8RvVPHgYU%2FZU4bo6CXiCeYH9VDp9KQ9lrBn1Tam5cRzCPDun%2F5%2FM7yMGEDCP7bbABjqkAS%2B%2B2B8lZoJ33HLbC1wPyokeuFkCagQ6dQ%2BfS3i0zzU4B19VNzrrGjX53EujYZVllYQo%2BU2UC6ldBEc%2FVOzlBjNb7%2Bk8yJI5c0PdTqilFUowxRT0zW%2Fd1HpiHGzjvS6xiLmWv%2BOvuAwPHph2YLkMs55ZWuhmQ0yAwLDnnZJpUF2MpbkzHRgf7Cah3wxf6qrf5T8ozO8DdURECXbrmFPCNoMbfmdE&X-Amz-Signature=20a382bea1038ac633ead9cc993c31caa330e6017b660435c30371f768f1934b&X-Amz-SignedHeaders=host&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">virtual function specifier - cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://en.cppreference.com/favicon.ico"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
