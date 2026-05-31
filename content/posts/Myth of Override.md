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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QR6KLCU%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T020951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCICCgyYcVUQKJF43uLty4Qskvv9D2BzzQ%2Bux4cNFeF2rNAiEAwHBB02ylV0BxAO%2BEVmlPHjNkWvlrPgDr%2FSEm%2FT28GqwqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbOiDk1bcqphhVW3CrcA6bshzOwcbJEzcYdBrhAV9xG2SPeIycFcBZcejr7QCSS4fAQgIuScWOdtMPEC3mSaAs7NB2V41HTMdku8DAmv63JrqpcSucBSMVlKXyr4FXXPv10GXqMGMz4IrtpIt8KvqaHZmGCwGTCa0X4NlHZ6Yz9YbL0VaujK%2FQsdcH6JI6FeN6d%2BIgFbvs9108pYr8Py%2BXv6wDsJhghUwoiCZQ3WMPHOTOZCVicRXg8QWvB7l7bU3TRmyJZaXlXNzycjryp1Ey%2BLKRTAC1TB4RoHyFCdKRgH%2Fxa%2FNsli%2BU3b2LsFchnLYHkx4AfA4URDESaOk3B0gMtrpeUtlULU%2BwDHHLxTFXY%2FU74Enp5fMnWU4pa9buzftUrQgMUMDh51MxYN6fKAjKO%2FC9lje1Z7L6wQ8b43sh0rkdBKL0HI0kv3%2FIBC5eZf3rSoAnZi8PvkHUR2dsamSKKlQctEsqgy3eN4D9eCPPm0VxB7VVnE7%2FMf1%2FL1kxLipcvfVQYW1RG0JaZfg8LFsYlfTpOaey8TbzvXQlzot2mTDbUV2K9nQCL9m6baCtx0HmZPP8MXetXNBxYrmJI3yUt7hm7y8Vwbdj%2BG%2BYl3j8VpyuJLbhzJYEBDVdFPHMCnrGqq6%2BTYUMY5ZLlMJyD7tAGOqUB7ioTAtUvkKsQYtCvlDo2ym%2FJYSBvITfIkwM5GBcdwN7WYCLtRWAbbBiUSKdRDWAFzJc6G3PubQ5O9nEkVuBXKnj9GWCZwfgXYOi%2FG9cyOcRVQFxyqTefraTH2IhQ%2FfpR62qLNb2V1Nzuq8rIymejVAba5ZVX2cI5J%2Fww4TiCXa39GYG0MhaAyIK91%2FFW6CRdXqqY2G4mY6QZo484PIBgPok7yx8d&X-Amz-Signature=1e3b25f9fe43a5190d365deed6a330c37595696adfae7e4302009e36ae4bf73c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QR6KLCU%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T020951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCICCgyYcVUQKJF43uLty4Qskvv9D2BzzQ%2Bux4cNFeF2rNAiEAwHBB02ylV0BxAO%2BEVmlPHjNkWvlrPgDr%2FSEm%2FT28GqwqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPbOiDk1bcqphhVW3CrcA6bshzOwcbJEzcYdBrhAV9xG2SPeIycFcBZcejr7QCSS4fAQgIuScWOdtMPEC3mSaAs7NB2V41HTMdku8DAmv63JrqpcSucBSMVlKXyr4FXXPv10GXqMGMz4IrtpIt8KvqaHZmGCwGTCa0X4NlHZ6Yz9YbL0VaujK%2FQsdcH6JI6FeN6d%2BIgFbvs9108pYr8Py%2BXv6wDsJhghUwoiCZQ3WMPHOTOZCVicRXg8QWvB7l7bU3TRmyJZaXlXNzycjryp1Ey%2BLKRTAC1TB4RoHyFCdKRgH%2Fxa%2FNsli%2BU3b2LsFchnLYHkx4AfA4URDESaOk3B0gMtrpeUtlULU%2BwDHHLxTFXY%2FU74Enp5fMnWU4pa9buzftUrQgMUMDh51MxYN6fKAjKO%2FC9lje1Z7L6wQ8b43sh0rkdBKL0HI0kv3%2FIBC5eZf3rSoAnZi8PvkHUR2dsamSKKlQctEsqgy3eN4D9eCPPm0VxB7VVnE7%2FMf1%2FL1kxLipcvfVQYW1RG0JaZfg8LFsYlfTpOaey8TbzvXQlzot2mTDbUV2K9nQCL9m6baCtx0HmZPP8MXetXNBxYrmJI3yUt7hm7y8Vwbdj%2BG%2BYl3j8VpyuJLbhzJYEBDVdFPHMCnrGqq6%2BTYUMY5ZLlMJyD7tAGOqUB7ioTAtUvkKsQYtCvlDo2ym%2FJYSBvITfIkwM5GBcdwN7WYCLtRWAbbBiUSKdRDWAFzJc6G3PubQ5O9nEkVuBXKnj9GWCZwfgXYOi%2FG9cyOcRVQFxyqTefraTH2IhQ%2FfpR62qLNb2V1Nzuq8rIymejVAba5ZVX2cI5J%2Fww4TiCXa39GYG0MhaAyIK91%2FFW6CRdXqqY2G4mY6QZo484PIBgPok7yx8d&X-Amz-Signature=aabab3b401f16c6538990c18ef1a2cb1a930f3e2bb0906a7b26022e6c6c2d26f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
