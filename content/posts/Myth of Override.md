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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBRN4FI%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T111659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQDz9B67Oqx%2FSnBWz4jAYZCtVESzI7gOZgTIUjmmnP4a6wIhAKjyRWEZ1tiHru4SgjNVXlNEoAFCYtvrNVckotBV5VCSKv8DCCIQABoMNjM3NDIzMTgzODA1IgwTpIbvT7Upcl3YhfAq3AP71CuPLTJcZRmkq79xCIgKigx7DYWfquFSp29ekzrgDyfM9bHya8O9lyPCC08c8EynM%2Ff4ZB8DYXPCpZ3PUOcJB6SrTeI0SxVVjpkQTCrViNE675gK9ujbkaCHlMY6Z8nN7Ro%2F3WfP5cbPacVrztMS8W4zH3kmBRKZ1vOOskcRONnZEweqpb7U5v1Kp4DUXmTBXxyp4e92aJ1tKb83Mf5ohlCps1zsE9Bsaxzd2LuWIZm13kLYlGiJ7ujb6FiPt5BEO7dIjNTaTu6VGGM4uIYFsZz3hvj%2FwptLfKpTIa65rwjJTID9%2FDiUZpbiPotnkZv3vvYRu%2FWbPW5t2g%2F2RmGGhqjFjZ55itfgLAF2Xh0iH%2Bkf9fIs5ci2RMJXsyKLtFCUBO1iq0zBKNatjRm59ZHEdPrCgC2IaNykFWTMlRD5soAYxH4ktFoBeYCZj4uqCaAM5NOojH34XdLwSjVn5QzFQY%2FEB1L8sQ9vT8gbhpchfq%2B%2BrT4wWlROKmnTCMh84tfqCEa14yO2MXjC2uWtEYwbWgT48AnsiDaBnT0ISYgxO%2BU2NCcSHEZ0AAhA86nrjkYjjWE%2BU0XPpa6SUJyDygvedHBijHHu0pnqMD5M0Qe45zlvTYQDBdmd3AXg3TDooqPSBjqkAbruwSYDcsMtCvDIOzSXivjnveL%2BQF5Er6ukwVn%2BmsejT2kp2HM1WjJ%2FSQOA7i0P8uwLmzhQi%2FbUu6X0cPTwTDjY3vvWGpf7osjRkZurvKc%2FHqUGgs0J3h4zBc8S526THi1wUevdVczj%2BI%2FdBthpca%2BVlena6tec3qobcgMt4qIiYSESFU9LSudEMQ4xzQ%2F%2B7IqgigzSPFjI2gEBhMCLLyz6t%2BQr&X-Amz-Signature=5e13b9dcdbdc07e57be69423e12fa6013b6b173f9fe7a03a309549ca9d2a366f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBRN4FI%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T111659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQDz9B67Oqx%2FSnBWz4jAYZCtVESzI7gOZgTIUjmmnP4a6wIhAKjyRWEZ1tiHru4SgjNVXlNEoAFCYtvrNVckotBV5VCSKv8DCCIQABoMNjM3NDIzMTgzODA1IgwTpIbvT7Upcl3YhfAq3AP71CuPLTJcZRmkq79xCIgKigx7DYWfquFSp29ekzrgDyfM9bHya8O9lyPCC08c8EynM%2Ff4ZB8DYXPCpZ3PUOcJB6SrTeI0SxVVjpkQTCrViNE675gK9ujbkaCHlMY6Z8nN7Ro%2F3WfP5cbPacVrztMS8W4zH3kmBRKZ1vOOskcRONnZEweqpb7U5v1Kp4DUXmTBXxyp4e92aJ1tKb83Mf5ohlCps1zsE9Bsaxzd2LuWIZm13kLYlGiJ7ujb6FiPt5BEO7dIjNTaTu6VGGM4uIYFsZz3hvj%2FwptLfKpTIa65rwjJTID9%2FDiUZpbiPotnkZv3vvYRu%2FWbPW5t2g%2F2RmGGhqjFjZ55itfgLAF2Xh0iH%2Bkf9fIs5ci2RMJXsyKLtFCUBO1iq0zBKNatjRm59ZHEdPrCgC2IaNykFWTMlRD5soAYxH4ktFoBeYCZj4uqCaAM5NOojH34XdLwSjVn5QzFQY%2FEB1L8sQ9vT8gbhpchfq%2B%2BrT4wWlROKmnTCMh84tfqCEa14yO2MXjC2uWtEYwbWgT48AnsiDaBnT0ISYgxO%2BU2NCcSHEZ0AAhA86nrjkYjjWE%2BU0XPpa6SUJyDygvedHBijHHu0pnqMD5M0Qe45zlvTYQDBdmd3AXg3TDooqPSBjqkAbruwSYDcsMtCvDIOzSXivjnveL%2BQF5Er6ukwVn%2BmsejT2kp2HM1WjJ%2FSQOA7i0P8uwLmzhQi%2FbUu6X0cPTwTDjY3vvWGpf7osjRkZurvKc%2FHqUGgs0J3h4zBc8S526THi1wUevdVczj%2BI%2FdBthpca%2BVlena6tec3qobcgMt4qIiYSESFU9LSudEMQ4xzQ%2F%2B7IqgigzSPFjI2gEBhMCLLyz6t%2BQr&X-Amz-Signature=04572f7d9ff7a295e398ef1d9a26f9745fbb5bede762b602b947740636c1d659&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
