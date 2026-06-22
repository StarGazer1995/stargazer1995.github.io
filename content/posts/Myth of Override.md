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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZPYEM64%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T215512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD0s0EkSFgnjAXFLKHv5%2Bc4hOEPMit%2BR2NzqFP0YHVYEgIhAP%2B7Py1DiFdI7GHjPDKpy33dqmIDyZhIi7DRdQwrp2%2FNKv8DCAwQABoMNjM3NDIzMTgzODA1IgyPNh2LHhUnT%2FwIUecq3APAMkCant0K76a2HUZpkaTQy1uVCJIk6XVl78nkUFalt36JEWdLGBkWoAccRAXgJR3UvVqoBjvI0SV3FT2DjRW4RrkW4qU9FuWHbbNLeKMe1%2BSGWCGQT6ByN7uXC2DYN8nZ4fdNo5P1VJqoSm9ObIUF5gKciHQKA4%2FKN9yenjaiRvg3joFUNBHl3YJRhbSS2vR9g0nezo%2FhTW3ZW4%2BjKko3evz6sss8HWyakKWrODsVB8Dkg3Hs0esdqU4HsLwHKmUm8tULWPW5lJlWIkJILeQMEHNtDqTZdbYzy17FNtL%2BFf9n61Om0YU2YCRupnx5ro95zOMKXWushk8o6p4Tuns2kp%2FXiTVSF%2FR0zH3WcxfgSztL13kmY7HtjoevNGAqy9UslwOf4osjTHqJn1fZS8f%2BB7xxiyYD6CZrOm5L%2BEPqP3xl%2B2GRLFAQGwvqPQ3vWbGEtXfqobhthT2JIdhH5vmO1uMCPQZOekb33nNlpv5FD6o1j9YxeJdcBDAyDggY4bPyji3RK6aSP3Xe4d%2B5RuAZTsRSG4lsFoWeGgmcTXgX39Jz68aVPeDwzF59isbMJAL4Ka51LUFO9y1UylS94Jl8075ILU8CWncZJs%2FSl95Kq7xpWEpQ4j7e7JVgwjCojebRBjqkAeEIm%2Bgjv4FMbHpx0bwcZZfPAp21n9cor6ovQM2ZyJMbLR6iAj4LO1zRTFUFYAwQVM9KnP2kNqdI1k%2Bn4No4XOXXDPLKgftuZBCWoj4NPaMR0kVzFWjDn8ZWGOzMZ2xMRPs7%2BH0F5XhaE9KMp3UWtOJ71oRQ2fjEicsqSBsSCQzfj%2Bwlctez26vSCzbt%2F58Oko9aw5dRMilDUZtfYkgaV5j7HaGa&X-Amz-Signature=13ec100b644c7c72c191d7bb6279ad13c12e318222556411822a8427bfd1108d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZPYEM64%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T215512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD0s0EkSFgnjAXFLKHv5%2Bc4hOEPMit%2BR2NzqFP0YHVYEgIhAP%2B7Py1DiFdI7GHjPDKpy33dqmIDyZhIi7DRdQwrp2%2FNKv8DCAwQABoMNjM3NDIzMTgzODA1IgyPNh2LHhUnT%2FwIUecq3APAMkCant0K76a2HUZpkaTQy1uVCJIk6XVl78nkUFalt36JEWdLGBkWoAccRAXgJR3UvVqoBjvI0SV3FT2DjRW4RrkW4qU9FuWHbbNLeKMe1%2BSGWCGQT6ByN7uXC2DYN8nZ4fdNo5P1VJqoSm9ObIUF5gKciHQKA4%2FKN9yenjaiRvg3joFUNBHl3YJRhbSS2vR9g0nezo%2FhTW3ZW4%2BjKko3evz6sss8HWyakKWrODsVB8Dkg3Hs0esdqU4HsLwHKmUm8tULWPW5lJlWIkJILeQMEHNtDqTZdbYzy17FNtL%2BFf9n61Om0YU2YCRupnx5ro95zOMKXWushk8o6p4Tuns2kp%2FXiTVSF%2FR0zH3WcxfgSztL13kmY7HtjoevNGAqy9UslwOf4osjTHqJn1fZS8f%2BB7xxiyYD6CZrOm5L%2BEPqP3xl%2B2GRLFAQGwvqPQ3vWbGEtXfqobhthT2JIdhH5vmO1uMCPQZOekb33nNlpv5FD6o1j9YxeJdcBDAyDggY4bPyji3RK6aSP3Xe4d%2B5RuAZTsRSG4lsFoWeGgmcTXgX39Jz68aVPeDwzF59isbMJAL4Ka51LUFO9y1UylS94Jl8075ILU8CWncZJs%2FSl95Kq7xpWEpQ4j7e7JVgwjCojebRBjqkAeEIm%2Bgjv4FMbHpx0bwcZZfPAp21n9cor6ovQM2ZyJMbLR6iAj4LO1zRTFUFYAwQVM9KnP2kNqdI1k%2Bn4No4XOXXDPLKgftuZBCWoj4NPaMR0kVzFWjDn8ZWGOzMZ2xMRPs7%2BH0F5XhaE9KMp3UWtOJ71oRQ2fjEicsqSBsSCQzfj%2Bwlctez26vSCzbt%2F58Oko9aw5dRMilDUZtfYkgaV5j7HaGa&X-Amz-Signature=fe39ebe7bda1aa380123a8ff833a4f507609e44259bb262e7574b7d95a108526&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
