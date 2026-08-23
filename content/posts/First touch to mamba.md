---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NQCGYCA%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T141259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQC2HfVrQ%2BdfW6%2BPrMVIPBtF4kkVeEbkUEQx41aWJ00CpAIhAPU%2F7TtrALnfL%2BEEhmqQEL%2FzepiU4LQ3qJgYpmlms%2FYPKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4qU0PabR%2FARkJ97gq3AP3lcnfIXGZ5Uyf%2BST2pEzOCO%2FBNhznQ8Wu8K7MLDdOe%2FxE5eWgV8%2F2BwHTvBdIWtUzCJfz9pkZ8F0BdZgmsRSSmzQ8rQu%2BamsJOK9S1KbU65O9jfogyWNdtV5gS%2Flrfr1j8LsteN6EyIGCdHlqCHrPBhrZJJlPJmLpvhfRtI418SYc9hpQGkCgPZrElxy1shhBXOq4iNkKZOZEU5%2BsPoJuDHqN%2BA9RWlJ%2B92jA21rEctapB0e5%2FmvOYSw6xEt4dYYK8HGnJrjxiZCNOa1T8zpATJf9kcVJglJWZH%2FMIzprUpqanQFBmJ4%2Fc1lHnmu9TJjvURWGqyTfgPv2GIzLNGxE7qIdz5yOjzBUWc8ExjwNN4umO%2FFnonrXokwVhwizYDFLoGTwWmY8PWVfLVhguSqwpJPtAMI0Nop4qiZ%2Fmc30JDVEVpTj196H8ehUDpRzfZ%2F%2BFgNTCTvKNdB81e1ite3yKNrgQ%2F5UJ%2F4jVzowd6OgfSBW1bnGp3aIKypSnFADETDzaD9WjRDSu6CFUI7am7Ik1ByXEZuLo09ZiLFJvNxyqm5fAQUlqTRJP6JEQxqwWz51HG0NArV5FMUzXc%2Faqr6AwSO9%2ByoTvg7J0yEWSX5Vf9NurJ%2BopLO5im4BBDDk%2BKvUBjqkAb02LAeg8hMHBWgrKvEAXR7DSt4NnENHinAVZGHTEoytXTps3Ibj5GPRU5VFuvNqosfTFeRUF%2BixF6SSsxFqMmCDHxL4zvfz3rTMlfDM7%2Bsu6bCKQ1GvehONTReKQRLiswGtEI2KZdnmQBbKStQNlwvcLt5draXzPLlj0fFhNDtw2tKLSpTCkEWtoZPCKM%2Bvg0y6p9xHHf2EBE%2BDLm5A%2FkJunR2h&X-Amz-Signature=d5febf10f454216a4151022cb956478d7f72a73a15ca8da45c1a442867edf392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
