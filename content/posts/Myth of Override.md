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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JVIDJN6%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T215843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAmjIUVuihw56Exr7TbUvaUOoIhuO2J0MCCyNXyjHCzIAiEAwymsALCmfJTKJnKY2%2BlCz%2BX9Qn8FdEvif5gUr6DZ1U4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBEIKmmDXv9xMN74CrcA40VvayvwwqJ4wh0hgJBqPP4jIXvhqghVpUsVqH6yxYTf6MvSaQnVYDFz3qlg%2FpoM4TcN5pZnWT%2FGIRucgcjKPQgiO4nEn%2FQ3fjoKpIM7WJdtbvws6%2BoL%2BgKFhCFmAxRVteFkptBtzDgXez2zGvvnKgIcQBQ%2FKmiEn3WtKrHdB8IuI4NpGbfQjeUnIznYm5uVC5UEgDAKaX1iBYhPvy1yOMzUOYKj5WJyB9YyoZKk534CwYFF%2Bikb1tD35r0sBw7rqy1vwkhZ0M0vWvFWtWBQhRA2uiDUayXbLF8sMITfP%2FXd0l2yeikU3GhRYgwyXE7eTROTe8lnXLS9UW%2FzcyXfbJRdGEStTeKrszb0so7axC4NkUC92FPolD2zYxPvV67LBoGI7illfWeGgFPF4I4z6Uw8bdZtNwLBZmlgGgtCxYPJOeK4BElWj0c9CO8ouS6b6Gnjr6oWIbg1Gmv09Clw9Ib1X5SUxwl8w0LniKTo%2Fcnavr98R2AxDovvCTJziF%2Fx6oRHVDSl0llXqds8WnnTPbVkjt1Hedzz1Ml7eWxzD9s3sJBhisPXkiDR%2B3glEXtCej4vJz3I9jHRkGrFTeFkhKfjfIUn62VL6bgKkreKTrv0byZ53ONp5FO6vDsMObjlNYGOqUBPMliyhIGd5ch6oCTT2wIOrzhctTPLUNre9HnSuUqZ7cD4IuQpon9WPYb4HTVo41ie6OC2kHXBeDu2JUA%2F1%2BEdh5mI2i24IRZjDnEcXN6nO4%2BfsltGUY4jq9b3fG3FlQMl8h%2FiyBWCQcxvq7502HR1pYssAnJZQ%2BolB84cT5WlVxmYj%2FSpTeUR%2FahKkl1HGuhH2Apul3SSXIe1U3g6ggTqpv8tX4o&X-Amz-Signature=fd5f155b067ea36914afc29fdbdfd7df3d427e7b2191d9e07623071cb6765f00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JVIDJN6%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T215843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAmjIUVuihw56Exr7TbUvaUOoIhuO2J0MCCyNXyjHCzIAiEAwymsALCmfJTKJnKY2%2BlCz%2BX9Qn8FdEvif5gUr6DZ1U4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBEIKmmDXv9xMN74CrcA40VvayvwwqJ4wh0hgJBqPP4jIXvhqghVpUsVqH6yxYTf6MvSaQnVYDFz3qlg%2FpoM4TcN5pZnWT%2FGIRucgcjKPQgiO4nEn%2FQ3fjoKpIM7WJdtbvws6%2BoL%2BgKFhCFmAxRVteFkptBtzDgXez2zGvvnKgIcQBQ%2FKmiEn3WtKrHdB8IuI4NpGbfQjeUnIznYm5uVC5UEgDAKaX1iBYhPvy1yOMzUOYKj5WJyB9YyoZKk534CwYFF%2Bikb1tD35r0sBw7rqy1vwkhZ0M0vWvFWtWBQhRA2uiDUayXbLF8sMITfP%2FXd0l2yeikU3GhRYgwyXE7eTROTe8lnXLS9UW%2FzcyXfbJRdGEStTeKrszb0so7axC4NkUC92FPolD2zYxPvV67LBoGI7illfWeGgFPF4I4z6Uw8bdZtNwLBZmlgGgtCxYPJOeK4BElWj0c9CO8ouS6b6Gnjr6oWIbg1Gmv09Clw9Ib1X5SUxwl8w0LniKTo%2Fcnavr98R2AxDovvCTJziF%2Fx6oRHVDSl0llXqds8WnnTPbVkjt1Hedzz1Ml7eWxzD9s3sJBhisPXkiDR%2B3glEXtCej4vJz3I9jHRkGrFTeFkhKfjfIUn62VL6bgKkreKTrv0byZ53ONp5FO6vDsMObjlNYGOqUBPMliyhIGd5ch6oCTT2wIOrzhctTPLUNre9HnSuUqZ7cD4IuQpon9WPYb4HTVo41ie6OC2kHXBeDu2JUA%2F1%2BEdh5mI2i24IRZjDnEcXN6nO4%2BfsltGUY4jq9b3fG3FlQMl8h%2FiyBWCQcxvq7502HR1pYssAnJZQ%2BolB84cT5WlVxmYj%2FSpTeUR%2FahKkl1HGuhH2Apul3SSXIe1U3g6ggTqpv8tX4o&X-Amz-Signature=567bd81a73603b1a59868a4dabd9fc11cc010ff6648c1aa7ff32037a839d2d61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
