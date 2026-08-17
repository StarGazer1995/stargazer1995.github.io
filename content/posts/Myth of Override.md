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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZHYXSO%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T003309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQD0oRKSFQDmFdlrCLk2fRMo6MMkFGym7v1Q72w%2FDDVjCgIgePTg9hr%2BSdk5oK6rPdIlnom%2BGPKjlDF2zXNjf%2Fk51JMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIixdUuuUJGtlyGNuCrcAxeN9EgoSZKOjKIt4S5R9Cmd%2BcIblKxEJ7eVEtmVna%2BLvDRb7kaYbdpw31MJxuUmdCRYi8dA3jDZ3JXLqx0cFdKKEEyBrHkuSaCACpD%2B%2F5wqrFBhI6KwpMXO0YoxIMBM5q1oFxp7W47XFWxCY1mZdDzAoAtBkzPxPydq6jIoZwN%2BYRZyP%2BB3cNQfgaowRHo%2FH6nhJ1e1GB9Zeojn7qpGu0rn%2FFC4yekHhI1lQYWToko%2FakntPNam%2Bt05nXWGfvC5YFRxDmMAQBNWD4yb%2F2AkM2XRXVBgabeRt%2Bs9hnAS%2BWD8ao%2B49Sk1Y%2Fgp12oiXOBga%2FTW5kGl7hVE6DBEI%2FH6DFEhzdFhBFNcNBD%2FMX5J69ei97Bs8f5UupbQW9b9DHu%2BF16Gseg3hFZCgdxMW9marE1rbfuyDk%2Bj7EzxZhkm0doRTCc9SVeUKv9fE8OsXpthMZbksDGhds6RyC9ssoTAmzopnMUZURVS3MsLbw0Tv%2BMai4WlU7uuXLUdVJig7PFyADmoYW76aH769b%2BZzbPpi2uj1%2BF4o9C0sTgIU02kzsinj4RrpJbaqzJ78JnEVans7lWTaA1USmWttBef5eipSaJ63%2BXgNPC7n7uauLH9u%2B7tt9L9ZgA9Xiq5tI20MJKridQGOqUBG6E0TuMXtAMT662pV01zM3uiO%2FNi2Itk9tY8Z%2FWao3QNhPp16jsL6ETn6r5wuqbRpteImp9jzk1UhTHADKXuKG2BwwRRFtPaU50cRhoH3M0Mnr69LRmpoPs%2Bd8vmY8sNsfuOyk0Sx3iy86bCCnMTyzvWFex2vrPtUpQmVpHRxesWTzL40yEaJAYpI9%2FLDtuTJ%2BfU%2FFGvmKVhPusFDGE2345glKOn&X-Amz-Signature=65c02d44d4419ecbe863bf4942e7bcd7b3f0d9e4f35586f00bf785503aebd5e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZHYXSO%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T003309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQD0oRKSFQDmFdlrCLk2fRMo6MMkFGym7v1Q72w%2FDDVjCgIgePTg9hr%2BSdk5oK6rPdIlnom%2BGPKjlDF2zXNjf%2Fk51JMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIixdUuuUJGtlyGNuCrcAxeN9EgoSZKOjKIt4S5R9Cmd%2BcIblKxEJ7eVEtmVna%2BLvDRb7kaYbdpw31MJxuUmdCRYi8dA3jDZ3JXLqx0cFdKKEEyBrHkuSaCACpD%2B%2F5wqrFBhI6KwpMXO0YoxIMBM5q1oFxp7W47XFWxCY1mZdDzAoAtBkzPxPydq6jIoZwN%2BYRZyP%2BB3cNQfgaowRHo%2FH6nhJ1e1GB9Zeojn7qpGu0rn%2FFC4yekHhI1lQYWToko%2FakntPNam%2Bt05nXWGfvC5YFRxDmMAQBNWD4yb%2F2AkM2XRXVBgabeRt%2Bs9hnAS%2BWD8ao%2B49Sk1Y%2Fgp12oiXOBga%2FTW5kGl7hVE6DBEI%2FH6DFEhzdFhBFNcNBD%2FMX5J69ei97Bs8f5UupbQW9b9DHu%2BF16Gseg3hFZCgdxMW9marE1rbfuyDk%2Bj7EzxZhkm0doRTCc9SVeUKv9fE8OsXpthMZbksDGhds6RyC9ssoTAmzopnMUZURVS3MsLbw0Tv%2BMai4WlU7uuXLUdVJig7PFyADmoYW76aH769b%2BZzbPpi2uj1%2BF4o9C0sTgIU02kzsinj4RrpJbaqzJ78JnEVans7lWTaA1USmWttBef5eipSaJ63%2BXgNPC7n7uauLH9u%2B7tt9L9ZgA9Xiq5tI20MJKridQGOqUBG6E0TuMXtAMT662pV01zM3uiO%2FNi2Itk9tY8Z%2FWao3QNhPp16jsL6ETn6r5wuqbRpteImp9jzk1UhTHADKXuKG2BwwRRFtPaU50cRhoH3M0Mnr69LRmpoPs%2Bd8vmY8sNsfuOyk0Sx3iy86bCCnMTyzvWFex2vrPtUpQmVpHRxesWTzL40yEaJAYpI9%2FLDtuTJ%2BfU%2FFGvmKVhPusFDGE2345glKOn&X-Amz-Signature=34348fe59b3df29cac921353b211119ce44aa71b6c76cc2e14598b15e5bf3db1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
