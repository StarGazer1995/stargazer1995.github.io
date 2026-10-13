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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623HN3IUQ%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T014332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9HDjZxlZZ1JYZrw9jBKC5Mvu1ug5fKIuJl5ubF%2FY0bgIhAMfzbAoAfeYaeERdehAaAM0g%2FXYcf910bXCMEvlDrXrFKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMoe84NucMqbc9kRgq3ANzokBO%2FxwthPnT2o7MkyeRFvEEB4miRYvVOy2gDc95AK0BvUorZK0eTgB9y0QkCbL3tgDMJf%2B6y%2Fss790l5RXamydmvGS62AZsrZ8rT8jv5p7BEp4pTklpMRfXD98Wj4WOQYB1Xoh%2B5KHNUQiVFN7uwEXkVjEQNkfkbwOKMVXo%2FfuCTtGicc2MohnrgARxBlrTWG0gQ%2B7ntiHo%2F6lv6yEbJoRIiXR62sTw12AXajFGWE84Z6fcit03g4G7Uy287iBnDzUH7CbPVYR%2BPTAOzZ9h0MVK9gR%2BBhmKtvlvc9JsZYK4esof%2BdtxDMSRiYbuQmBqIUxSQpQvdPAlqJGSPaJ4ANm1o0lN1Fi131QQXoQr59Ms6P9hOl38lVsnH7GspS5emgY42ERQXvr6frCJmj%2FHuqfFbLDtqkmrqiRPkZ2RKmvPKMg7h2JsL%2FSlTpKyr%2FAEcrFnNyKCUMoYop53mW5ElMtJ0uAtIikLKRexmmVIzpFZLkg%2BnqLJ3%2FalstHy2qQsIYzZ7hUR2SnHR1p2PadckgvryUBMBcQORwUl9nrZIZB6hdVdvU9hqenB%2BS2lm4PBHOlG2oYk38PXX%2BsnsrgwncPaCSz3SGt8pZKAO9KL19pEKm1L9IxFwks2aDCR5rXWBjqkAQ%2Bd1uPUvF9hIXb6waX%2Bjve2tstjuuM1pnRblSRJbxnc%2Bevy5kE3pkyQTvaD13DmJUF9p0Axoi5QPFCopZXz3HQUtT74Msb0Se4IaGumXi%2FAK9Oxk0nFP8IOm7IEkzJp%2BAjQruimyWj76VtqaM590nniEjSMd3j5zJ%2BytMkeCnXYWhCaufUWc83xdXhw2Om6aSgbcvC9Euf%2B9cCvEIVn3JJCJTjE&X-Amz-Signature=0febdd668bc318c6caae7b451682f59ec5e3b0aed42b87643b3318687d206fa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623HN3IUQ%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T014332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9HDjZxlZZ1JYZrw9jBKC5Mvu1ug5fKIuJl5ubF%2FY0bgIhAMfzbAoAfeYaeERdehAaAM0g%2FXYcf910bXCMEvlDrXrFKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMoe84NucMqbc9kRgq3ANzokBO%2FxwthPnT2o7MkyeRFvEEB4miRYvVOy2gDc95AK0BvUorZK0eTgB9y0QkCbL3tgDMJf%2B6y%2Fss790l5RXamydmvGS62AZsrZ8rT8jv5p7BEp4pTklpMRfXD98Wj4WOQYB1Xoh%2B5KHNUQiVFN7uwEXkVjEQNkfkbwOKMVXo%2FfuCTtGicc2MohnrgARxBlrTWG0gQ%2B7ntiHo%2F6lv6yEbJoRIiXR62sTw12AXajFGWE84Z6fcit03g4G7Uy287iBnDzUH7CbPVYR%2BPTAOzZ9h0MVK9gR%2BBhmKtvlvc9JsZYK4esof%2BdtxDMSRiYbuQmBqIUxSQpQvdPAlqJGSPaJ4ANm1o0lN1Fi131QQXoQr59Ms6P9hOl38lVsnH7GspS5emgY42ERQXvr6frCJmj%2FHuqfFbLDtqkmrqiRPkZ2RKmvPKMg7h2JsL%2FSlTpKyr%2FAEcrFnNyKCUMoYop53mW5ElMtJ0uAtIikLKRexmmVIzpFZLkg%2BnqLJ3%2FalstHy2qQsIYzZ7hUR2SnHR1p2PadckgvryUBMBcQORwUl9nrZIZB6hdVdvU9hqenB%2BS2lm4PBHOlG2oYk38PXX%2BsnsrgwncPaCSz3SGt8pZKAO9KL19pEKm1L9IxFwks2aDCR5rXWBjqkAQ%2Bd1uPUvF9hIXb6waX%2Bjve2tstjuuM1pnRblSRJbxnc%2Bevy5kE3pkyQTvaD13DmJUF9p0Axoi5QPFCopZXz3HQUtT74Msb0Se4IaGumXi%2FAK9Oxk0nFP8IOm7IEkzJp%2BAjQruimyWj76VtqaM590nniEjSMd3j5zJ%2BytMkeCnXYWhCaufUWc83xdXhw2Om6aSgbcvC9Euf%2B9cCvEIVn3JJCJTjE&X-Amz-Signature=33e1d0c877078431e08c71bc07aab5ff20fe1d255818af3c76f5c1224da7182c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
