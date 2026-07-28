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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622EKJBTC%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T155905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEdX3EABPMGma56grZkg2o29KwPsA5K4JG9zNm3oWTKwIhAKzzoHeAecoMkicqSmDkKgbg85ZesvAgB%2FqihJtPQ%2B%2FOKv8DCGgQABoMNjM3NDIzMTgzODA1Igz%2FAcC%2FRfE4km0FGLEq3APl3mbh%2FO%2BjJgYJ%2BXaMnV%2B7L57wUiUq4UZseXzy5sLIlsaSGlz%2BjsJCd8DvFER5T3KEQviIVqrnCHhbgIOEZ6ky1QjFCl1KqTAg5CM1PrNIiOrADAQJNDrxu37zqHNQ30zZ5fj%2F2fvYaxI6HfhskxOfykheXvGhA4oup24GbLFFbdu4wr%2FK2dqA2tORMlJTcicfcF4i4MhhPslpc3e3d3rsSKFfaUvdSONoz6SWjU4itXlSwcYeII26aiHN2wNdOZioJrl%2FVrgva4qmHHHi8xKpKADDBEQZyRoZKWHlHhUGN4SnH%2BrE9mr5Ak2OJRux9E7zOJ5actYYdqcbs7OijhnrBjaw5uKd%2BmPVTdY73OVz3j%2F0D21Gzmdsd0fCNQN14UBCc1PEPTJY%2FIg1H5YHpPApvM02HcGmLEPxRnZlkE%2Blm3gTECe5lvlwnarWlshc6hFE0dg4nrpFQztom1fkXxaquULey0pyPgLRy9ix2q7kzSAsVQP1HgE5w%2BKLpWm9fQMi9Qn1SsAeL3mZq82etXVL16G4uqxZDXIBXt4PH3QnzyYipqP9Sbkl2%2F%2BkC4fRXLP6WLtFCW%2BukHIjEpT3JhAHrriPrsYl9C6V%2FovM2lBdhWM4iZYcz5BB4WbluTDmkaPTBjqkAfRlnUFquFvPwVvqx8hETsEjLwreZVZqz9mbB%2F1hGt%2BJSrRYfCrXp%2BfoDLZ9Vz5j0ESrQEHbTtNg1kFYCU02hGHYGN01D5WNOWmc0b9wLeg38DC2zHipZOhUwYRN9mMa3CT62tmdwFOLNTi6WDCPZQvpkS8Q4c6y2kSlEyfLzjud09YEWqk3YgXJElAQWM%2B%2FOB%2BVR6LTFoW%2Bh3KwqcOKzO6oc4vc&X-Amz-Signature=d764dff274c6ea0f47b0492b7d8b423f2eb705457b6dd384103c9d77ab1bdcbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622EKJBTC%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T155905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEdX3EABPMGma56grZkg2o29KwPsA5K4JG9zNm3oWTKwIhAKzzoHeAecoMkicqSmDkKgbg85ZesvAgB%2FqihJtPQ%2B%2FOKv8DCGgQABoMNjM3NDIzMTgzODA1Igz%2FAcC%2FRfE4km0FGLEq3APl3mbh%2FO%2BjJgYJ%2BXaMnV%2B7L57wUiUq4UZseXzy5sLIlsaSGlz%2BjsJCd8DvFER5T3KEQviIVqrnCHhbgIOEZ6ky1QjFCl1KqTAg5CM1PrNIiOrADAQJNDrxu37zqHNQ30zZ5fj%2F2fvYaxI6HfhskxOfykheXvGhA4oup24GbLFFbdu4wr%2FK2dqA2tORMlJTcicfcF4i4MhhPslpc3e3d3rsSKFfaUvdSONoz6SWjU4itXlSwcYeII26aiHN2wNdOZioJrl%2FVrgva4qmHHHi8xKpKADDBEQZyRoZKWHlHhUGN4SnH%2BrE9mr5Ak2OJRux9E7zOJ5actYYdqcbs7OijhnrBjaw5uKd%2BmPVTdY73OVz3j%2F0D21Gzmdsd0fCNQN14UBCc1PEPTJY%2FIg1H5YHpPApvM02HcGmLEPxRnZlkE%2Blm3gTECe5lvlwnarWlshc6hFE0dg4nrpFQztom1fkXxaquULey0pyPgLRy9ix2q7kzSAsVQP1HgE5w%2BKLpWm9fQMi9Qn1SsAeL3mZq82etXVL16G4uqxZDXIBXt4PH3QnzyYipqP9Sbkl2%2F%2BkC4fRXLP6WLtFCW%2BukHIjEpT3JhAHrriPrsYl9C6V%2FovM2lBdhWM4iZYcz5BB4WbluTDmkaPTBjqkAfRlnUFquFvPwVvqx8hETsEjLwreZVZqz9mbB%2F1hGt%2BJSrRYfCrXp%2BfoDLZ9Vz5j0ESrQEHbTtNg1kFYCU02hGHYGN01D5WNOWmc0b9wLeg38DC2zHipZOhUwYRN9mMa3CT62tmdwFOLNTi6WDCPZQvpkS8Q4c6y2kSlEyfLzjud09YEWqk3YgXJElAQWM%2B%2FOB%2BVR6LTFoW%2Bh3KwqcOKzO6oc4vc&X-Amz-Signature=2b18a247324ec79f20ac0f9f1fb71bc131169a45a91bebfb0f3e5aedfce2810f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
