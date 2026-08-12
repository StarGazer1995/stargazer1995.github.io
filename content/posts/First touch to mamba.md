---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHIZW7B%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T145022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDVxSkcVnBgAFCTgh2oAMmn7tUCpxJ7VNvsfJ2uiiP5bAIgBAnK7l13Bi8mrhbUfdIBt6ZrZqtrk4Qi9rfPx%2BeOvOIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHxo9%2FrO2eurQIuRvyrcA4Uzchsy700lG%2B3VtqaKCMJnfNwSfXwXBlrsOGyefideKbZsV5NPA4hJ7Iu4ou11lp2M8HYBMMVhHKBT4UNnZRO%2BPwsIMZgtsICXBMMEmlYmGWI13qH9e%2BU6ezG5osuX802r%2BNR%2FaEKsyhXriALp8kWGffDEoZ%2FMNOdBcRhQb8u44U4CnE8COXZuRJSyH9XqvLynjlJ1gItVWB%2FQsQgq%2BmstqT34Mu7Z18c%2FPGarmF1tX7wXsYIr2jNXxrjgtI%2B7SHxk9iGi%2Be3UfwKylVeYTiWjgm0CW9yYiHtTdoeSX5VceiEM3Q0wE2%2BfQWeJY90Bsr7jJ%2FuIharSW6nFZcSzCLzcnHfux8%2BH2lc4Zgogk2OO%2B0p7%2BJsG%2FclZV8sfe%2FNTa%2BLfLOy4%2BYqkmnEiaxvl%2Fnxdxt0F72KZ%2BnWDKndJNymeshxnvduxGjt7APkQ%2BCZUS0X27Yjppg2ewq%2BAvNSr14HAFc7zxe%2FBwCTWdz5uUmVmpLMGuvfjGd6QdUc6Tbene2QWHuB0o9DSEPxB8eEwoFsobi4X6%2F5dZAAUwqHWqkmAHAXghvi5e6f7x94KTSJpTPrce6dTBU6STZMxW6x5N01LazFFZ6p8bqUUujXs3t%2B%2FNUQ70cl111T2mr%2F0MMDt8dMGOqUBN%2FAjCtsagl5otpEKfalHnHdOFC03Meh%2BHOsHq63AkYUnGvLd%2FP%2BA%2F0w%2BVsB7Zb7Ul8qiRDL82Kr2RzUGCT77GDSMY3A%2F3O7Sp66C8jMdRD2X0%2F6LO2tSH%2BtBtUbFLhCILMtsOYA%2B6YQf6QFVq%2FLLVYMaXUj0zrBlKASdUsbgzw1BZrZQvULakZH62J8%2BminBH5y6HZi%2BYjQb8lS16Kamfh7pcpUP&X-Amz-Signature=3c9e071e7f036d8e292310826bcf12906354d4737422b777681abe0fe294a26f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
