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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XLY4U6T%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T020130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQC9WDtJPW1%2BTJayLr8V4woztUOd8F5GpP5ErXhD5H5yBgIhAIkEpQqT4nGLk5hezNtDSMjwu1bX255B6XVvQJm6fDDRKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXeG7BQNmutOyolEYq3AMCwFtJt%2FIl0YbXvtOzash3JY2spEmrN%2BwAIaQTukaUUe7okXoiFkTZh5d6qxU0NAVCSY8gPCH%2Fwi2YlEcsuz%2F%2F1nirzbNwET%2B0CU7g0tiXczHRCiF2%2FxPrxcWcg3HnA6nn5RrEadRwIwdTd4gAbg343SbMxIWkqT2tVCBoo59LOTSPqWI3Vw%2FIR2HqzT9qaBwNX8ByWtMFucqfaONkjR%2BcBzHxAy6lg6c1AZByO9EqVgMqjYLzgoU6w9JDoywB4aac8mC%2BXN15GjAEgtLmM2iPZnKnr1pckuSxRmcVw%2FXp9ETRtg7LC4Lvjiw6JVJ5Woj4oS06bx%2FJhuzptmvP1Y61Obmdyaq7nHUfgwAUs9o%2BNZXQ7ExlfBLYUu1v7PbWDVSx%2FGhC8%2BseqndFcE9AxhMgZkddSdptiHLfYXitQAFO5v98uRZ7CIi79TLD81Tco28jwqXNflv1ykM6Kw9W4FXBS1Mic008dbvPVsg1kG52sHjHD1BoKbMpBMtkp8fkXrJNKttxlwzvhSa2WEnYjzgr9bNjF1YktM8ibs%2BTdt18taSRalCzHbN%2F3aayJqNwZ%2B7jYTcEcwqTJEMiFwRbQWOqB%2FU5to1UPIXhr5hBqbzwU6Dyl0LHslFckpHFmjDvvLnQBjqkAdWgphFhbu9ejHoNN4ICLtx3Hh5Yd3%2BDbRpLbD8z9NS4jNXeQ9EcVdV8OHRujQ8qV%2BCtmjbKqfxFj%2FUM7jIide7PogmXoeIzsDbpE3eH9C7jWuXSTzw6wJHCabRv33kN9hEk8WngDEMMZHYNJqbA3DsusUogJVQNVTmn%2BOgnyjJX69BNrfCMrVhi70jigS6IMy6NVUCEsqLlrmQhXxT62tf5GetL&X-Amz-Signature=d75ed8dd50f99b847ba19b1ee965bbdd4d026091f363cee0cffb01f62461c380&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XLY4U6T%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T020130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQC9WDtJPW1%2BTJayLr8V4woztUOd8F5GpP5ErXhD5H5yBgIhAIkEpQqT4nGLk5hezNtDSMjwu1bX255B6XVvQJm6fDDRKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXeG7BQNmutOyolEYq3AMCwFtJt%2FIl0YbXvtOzash3JY2spEmrN%2BwAIaQTukaUUe7okXoiFkTZh5d6qxU0NAVCSY8gPCH%2Fwi2YlEcsuz%2F%2F1nirzbNwET%2B0CU7g0tiXczHRCiF2%2FxPrxcWcg3HnA6nn5RrEadRwIwdTd4gAbg343SbMxIWkqT2tVCBoo59LOTSPqWI3Vw%2FIR2HqzT9qaBwNX8ByWtMFucqfaONkjR%2BcBzHxAy6lg6c1AZByO9EqVgMqjYLzgoU6w9JDoywB4aac8mC%2BXN15GjAEgtLmM2iPZnKnr1pckuSxRmcVw%2FXp9ETRtg7LC4Lvjiw6JVJ5Woj4oS06bx%2FJhuzptmvP1Y61Obmdyaq7nHUfgwAUs9o%2BNZXQ7ExlfBLYUu1v7PbWDVSx%2FGhC8%2BseqndFcE9AxhMgZkddSdptiHLfYXitQAFO5v98uRZ7CIi79TLD81Tco28jwqXNflv1ykM6Kw9W4FXBS1Mic008dbvPVsg1kG52sHjHD1BoKbMpBMtkp8fkXrJNKttxlwzvhSa2WEnYjzgr9bNjF1YktM8ibs%2BTdt18taSRalCzHbN%2F3aayJqNwZ%2B7jYTcEcwqTJEMiFwRbQWOqB%2FU5to1UPIXhr5hBqbzwU6Dyl0LHslFckpHFmjDvvLnQBjqkAdWgphFhbu9ejHoNN4ICLtx3Hh5Yd3%2BDbRpLbD8z9NS4jNXeQ9EcVdV8OHRujQ8qV%2BCtmjbKqfxFj%2FUM7jIide7PogmXoeIzsDbpE3eH9C7jWuXSTzw6wJHCabRv33kN9hEk8WngDEMMZHYNJqbA3DsusUogJVQNVTmn%2BOgnyjJX69BNrfCMrVhi70jigS6IMy6NVUCEsqLlrmQhXxT62tf5GetL&X-Amz-Signature=592239ff83f5c8e53e3ea426b3a1580d47ba475a772e2e6e260ab10625444cec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
